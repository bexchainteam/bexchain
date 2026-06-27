import hashlib
import json
import time
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import uuid
import uuid
from Crypto.Hash import keccak
from eth_account import Account
from eth_account.hdaccount import mnemonic

# Enable unaudited HD wallet features for BIP-39/BIP-44 support
Account.enable_unaudited_hdwallet_features()

def _to_checksum_address(addr_hex):
    addr = addr_hex.lower().replace('0x', '')
    k = keccak.new(digest_bits=256)
    k.update(addr.encode())
    hash_hex = k.hexdigest()
    out = ''
    for i, c in enumerate(addr):
        if c in 'abcdef':
            out += c.upper() if int(hash_hex[i], 16) >= 8 else c
        else:
            out += c
    return '0x' + out

# BIP-44 / SLIP-0044 Constants for BEXChain
BEX_CHAIN_ID = 140586
BEX_COIN_TYPE = 140586  # SLIP-0044 registered coin type
BIP44_PATH_BEX = f"m/44'/{BEX_COIN_TYPE}'/0'/0/0"  # BIP-44 derivation path for BEXChain

def generate_wallet():
    """Generate a new wallet with private and public keys"""
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    private_key_hex = private_key.to_string().hex()
    public_key_bytes = public_key.to_string()
    k = keccak.new(digest_bits=256)
    k.update(public_key_bytes)
    address_hex = k.digest()[-20:].hex()
    address = _to_checksum_address('0x' + address_hex)
    return {
        'private_key': '0x' + private_key_hex,
        'public_key': public_key_bytes.hex(),
        'address': address
    }

def generate_wallet_from_mnemonic(mnemonic_phrase, account_index=0):
    """Generate wallet from BIP-39 mnemonic phrase with BIP-44 derivation for BEXChain"""
    try:
        # Use eth_account with custom derivation path
        # BIP-44: m/44'/coin_type'/account'/change/address_index
        derivation_path = f"m/44'/{BEX_COIN_TYPE}'/{account_index}'/0/0"
        
        # Create account from mnemonic
        account = Account.from_mnemonic(
            mnemonic_phrase,
            account_path=derivation_path
        )
        
        # Get the wallet address and private key
        address = account.address
        private_key = account.key.hex()
        
        # Derive public key from private key
        private_key_bytes = bytes.fromhex(private_key[2:] if private_key.startswith('0x') else private_key)
        signing_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
        public_key = signing_key.get_verifying_key().to_string().hex()
        
        return {
            'mnemonic': mnemonic_phrase,
            'address': address,
            'private_key': private_key,
            'public_key': public_key,
            'path': derivation_path,
            'coin_type': BEX_COIN_TYPE,
            'chain_id': BEX_CHAIN_ID
        }
    except Exception as e:
        print(f"Error generating wallet from mnemonic: {e}")
        return None

def generate_mnemonic():
    """Generate a new BIP-39 compatible mnemonic phrase"""
    try:
        # Use eth_account's Account.create_with_mnemonic after enabling unaudited features
        account, mnemonic_phrase = Account.create_with_mnemonic()
        return mnemonic_phrase
    except Exception as e:
        print(f"Error generating mnemonic with eth_account: {e}")
        # Fallback: use the mnemonic module directly
        try:
            return mnemonic.generate_mnemonic()
        except Exception as e2:
            print(f"Error with fallback mnemonic generation: {e2}")
            return None

def generate_wallet_with_mnemonic():
    """Generate a new wallet with BIP-39 mnemonic phrase (BIP-44 compliant)"""
    try:
        # Generate mnemonic
        mnemonic_phrase = generate_mnemonic()
        if not mnemonic_phrase:
            raise ValueError("Failed to generate mnemonic")
        
        # Generate wallet from mnemonic
        wallet = generate_wallet_from_mnemonic(mnemonic_phrase)
        if not wallet:
            raise ValueError("Failed to generate wallet from mnemonic")
        
        return wallet
    except Exception as e:
        print(f"Error generating wallet with mnemonic: {e}")
        return None

def generate_multiple_accounts_from_mnemonic(mnemonic_phrase, num_accounts=5):
    """Generate multiple accounts from a single mnemonic phrase"""
    try:
        accounts = []
        for i in range(num_accounts):
            wallet = generate_wallet_from_mnemonic(mnemonic_phrase, account_index=i)
            if wallet:
                accounts.append(wallet)
        return accounts
    except Exception as e:
        print(f"Error generating multiple accounts: {e}")
        return None

def display_wallet_for_copying(wallet):
    """Display wallet information in a format that's easy to copy"""
    print("=" * 50)
    print("WALLET INFORMATION - READY TO COPY")
    print("=" * 50)
    print(f"ADDRESS: {wallet['address']}")
    print("-" * 50)
    print("PRIVATE KEY:")
    print(wallet['private_key'])
    print("-" * 50)
    print("PUBLIC KEY:")
    print(wallet['public_key'])
    print("=" * 50)
    print("IMPORTANT: Save your private key in a secure location!")
    print("Do not share your private key with anyone!")
    print("=" * 50)

def encrypt_private_key(private_key, password):
    """Encrypt private key with password"""
    # Derive key from password
    salt = b'blockchain_wallet_salt'  # In production, use a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    # Encrypt private key
    f = Fernet(key)
    encrypted_key = f.encrypt(private_key.encode())
    return base64.urlsafe_b64encode(encrypted_key).decode()

def decrypt_private_key(encrypted_private_key, password):
    """Decrypt private key with password"""
    # Derive key from password
    salt = b'blockchain_wallet_salt'  # In production, use a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    # Decrypt private key
    f = Fernet(key)
    encrypted_data = base64.urlsafe_b64decode(encrypted_private_key.encode())
    decrypted_key = f.decrypt(encrypted_data)
    return decrypted_key.decode()

def create_transaction(sender, recipient, amount, private_key):
    """Create and sign a transaction"""
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount,
        'timestamp': time.time()
    }
    
    # Add transaction hash/ID
    tx_data = f"{sender}{recipient}{amount}{transaction['timestamp']}"
    transaction['hash'] = hashlib.sha256(tx_data.encode()).hexdigest()
    
    # Sign the transaction
    return sign_transaction(transaction, private_key)

def sign_transaction(transaction, private_key):
    """Sign a transaction with a private key"""
    # Create transaction data string (excluding signature if present)
    tx_data = f"{transaction['sender']}{transaction['recipient']}{transaction['amount']}{transaction['timestamp']}"
    tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()
    
    # Decode private key and sign
    try:
        if isinstance(private_key, str) and private_key.startswith("0x") and len(private_key) == 66:
            pk_bytes = bytes.fromhex(private_key[2:])
        elif isinstance(private_key, str) and all(c in "0123456789abcdefABCDEF" for c in private_key) and len(private_key) == 64:
            pk_bytes = bytes.fromhex(private_key)
        else:
            pk_bytes = base64.b64decode(private_key)
    except Exception:
        pk_bytes = base64.b64decode(private_key)
    signing_key = SigningKey.from_string(pk_bytes, curve=SECP256k1)
    signature = signing_key.sign(tx_hash.encode())
    
    # Add signature to transaction
    transaction['signature'] = base64.b64encode(signature).decode()
    return transaction

def get_public_key_from_private(private_key):
    """Extract public key from private key"""
    try:
        # Decode private key
        if isinstance(private_key, str) and private_key.startswith("0x") and len(private_key) == 66:
            pk_bytes = bytes.fromhex(private_key[2:])
        elif isinstance(private_key, str) and all(c in "0123456789abcdefABCDEF" for c in private_key) and len(private_key) == 64:
            pk_bytes = bytes.fromhex(private_key)
        else:
            pk_bytes = base64.b64decode(private_key)
        
        # Create signing key and get public key
        signing_key = SigningKey.from_string(pk_bytes, curve=SECP256k1)
        public_key = signing_key.get_verifying_key()
        return public_key
    except Exception as e:
        print(f"Error extracting public key: {e}")
        return None

def get_address_from_public_key(public_key):
    """Generate address from public key"""
    try:
        # Get public key bytes
        pub_bytes = public_key.to_string()
        
        # Hash with keccak256
        k = keccak.new(digest_bits=256)
        k.update(pub_bytes)
        hash_hex = k.hexdigest()
        
        # Take last 20 bytes (40 hex chars) as address
        address = '0x' + hash_hex[-40:]
        return _to_checksum_address(address)
    except Exception as e:
        print(f"Error generating address: {e}")
        return None

def verify_private_key_matches_address(private_key, address):
    """Verify that private key corresponds to the given address"""
    try:
        public_key = get_public_key_from_private(private_key)
        if not public_key:
            return False
        
        derived_address = get_address_from_public_key(public_key)
        if not derived_address:
            return False
        
        return derived_address.lower() == address.lower()
    except Exception as e:
        print(f"Error verifying private key matches address: {e}")
        return False

def verify_transaction(transaction):
    """Verify a transaction signature"""
    try:
        # Check if signature exists
        if 'signature' not in transaction:
            return False
            
        # Recreate transaction data string
        tx_data = f"{transaction['sender']}{transaction['recipient']}{transaction['amount']}{transaction['timestamp']}"
        tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()
        
        # Decode signature
        signature = base64.b64decode(transaction['signature'])
        
        # For now, implement basic signature format validation
        # In production, we need to store and retrieve public keys for addresses
        if len(signature) < 64:
            return False
        
        # Basic ECDSA signature format check
        # This is still simplified - proper implementation needs public key recovery
        try:
            # Try to verify signature format
            # We can't fully verify without the public key, but we can check format
            r = int.from_bytes(signature[:32], 'big')
            s = int.from_bytes(signature[32:64], 'big')
            
            # Check if r and s are in valid range
            n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141  # SECP256k1 order
            if r >= n or s >= n or r == 0 or s == 0:
                return False
            
            return True  # Format is valid, but we still need proper public key verification
        except Exception:
            return False
        
    except Exception as e:
        print(f"Signature verification error: {e}")
        return False

def get_wallet_balance(address, blockchain):
    """Get wallet balance from blockchain"""
    return blockchain.get_balance(address)

def save_wallet(wallet, filename, password=None):
    """Save wallet to a file with optional encryption"""
    wallet_data = wallet.copy()
    
    # Encrypt private key if password is provided
    if password and 'private_key' in wallet_data:
        wallet_data['private_key'] = encrypt_private_key(wallet_data['private_key'], password)
        wallet_data['encrypted'] = True
    else:
        wallet_data['encrypted'] = False
    
    with open(filename, 'w') as f:
        json.dump(wallet_data, f)
        
def load_wallet(filename, password=None):
    """Load wallet from a file with optional decryption"""
    with open(filename, 'r') as f:
        wallet_data = json.load(f)
    
    # Decrypt private key if it's encrypted and password is provided
    if wallet_data.get('encrypted') and password and 'private_key' in wallet_data:
        try:
            wallet_data['private_key'] = decrypt_private_key(wallet_data['private_key'], password)
            wallet_data['encrypted'] = False
        except Exception as e:
            raise ValueError("Failed to decrypt private key. Invalid password or corrupted data.")
    
    return wallet_data
