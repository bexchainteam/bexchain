#!/usr/bin/env python3
"""
Test BIP-44 wallet generation for BEXChain (SLIP-0044 compliant)
"""

import sys
import os

# Add the project directory to Python path
sys.path.append('/home/bexchain/bex_blockchain')

# Import the wallet generation functions
from wallet_api import (
    generate_wallet,
    generate_mnemonic,
    generate_wallet_with_mnemonic,
    generate_wallet_from_mnemonic,
    generate_multiple_accounts_from_mnemonic,
    BEX_CHAIN_ID,
    BEX_COIN_TYPE,
    BIP44_PATH_BEX
)

def test_simple_wallet():
    """Test simple wallet generation (original method)"""
    print("=" * 60)
    print("TEST 1: Simple Wallet Generation (Original Method)")
    print("=" * 60)
    
    wallet = generate_wallet()
    print(f"Address: {wallet['address']}")
    print(f"Private Key: {wallet['private_key']}")
    print(f"Public Key: {wallet['public_key']}")
    print()

def test_mnemonic_generation():
    """Test BIP-39 mnemonic generation"""
    print("=" * 60)
    print("TEST 2: BIP-39 Mnemonic Generation")
    print("=" * 60)
    
    mnemonic_phrase = generate_mnemonic()
    print(f"Generated Mnemonic: {mnemonic_phrase}")
    print(f"Word Count: {len(mnemonic_phrase.split())}")
    print()

def test_wallet_from_mnemonic():
    """Test wallet generation from mnemonic with BIP-44 derivation"""
    print("=" * 60)
    print("TEST 3: Wallet from Mnemonic (BIP-44 Derivation)")
    print("=" * 60)
    
    # Generate mnemonic
    mnemonic_phrase = generate_mnemonic()
    print(f"Mnemonic: {mnemonic_phrase}")
    
    # Generate wallet
    wallet = generate_wallet_from_mnemonic(mnemonic_phrase)
    if wallet:
        print(f"Address: {wallet['address']}")
        print(f"Private Key: {wallet['private_key']}")
        print(f"Public Key: {wallet['public_key']}")
        print(f"Derivation Path: {wallet['path']}")
        print(f"Coin Type: {wallet['coin_type']} (SLIP-0044)")
        print(f"Chain ID: {wallet['chain_id']}")
    else:
        print("Failed to generate wallet from mnemonic")
    print()

def test_complete_wallet_generation():
    """Test complete wallet generation with mnemonic"""
    print("=" * 60)
    print("TEST 4: Complete Wallet Generation (BIP-39 + BIP-44)")
    print("=" * 60)
    
    wallet = generate_wallet_with_mnemonic()
    if wallet:
        print(f"Mnemonic: {wallet['mnemonic']}")
        print(f"Address: {wallet['address']}")
        print(f"Private Key: {wallet['private_key']}")
        print(f"Derivation Path: {wallet['path']}")
        print(f"Coin Type: {wallet['coin_type']} (SLIP-0044: BEXChain)")
        print(f"Chain ID: {wallet['chain_id']}")
        
        # Display SLIP-0044 compliance info
        print()
        print("SLIP-0044 Compliance:")
        print(f"  Coin Type: {BEX_COIN_TYPE} (0x{BEX_COIN_TYPE:08x})")
        print(f"  Chain ID: {BEX_CHAIN_ID}")
        print(f"  Derivation Path: {BIP44_PATH_BEX}")
        print(f"  Official SLIP-0044 Entry: BEXChain (140586)")
    else:
        print("Failed to generate complete wallet")
    print()

def test_multiple_accounts():
    """Test generating multiple accounts from single mnemonic"""
    print("=" * 60)
    print("TEST 5: Multiple Accounts from Single Mnemonic")
    print("=" * 60)
    
    mnemonic_phrase = generate_mnemonic()
    print(f"Mnemonic: {mnemonic_phrase}")
    print()
    
    accounts = generate_multiple_accounts_from_mnemonic(mnemonic_phrase, num_accounts=3)
    if accounts:
        for i, account in enumerate(accounts):
            print(f"Account {i}:")
            print(f"  Address: {account['address']}")
            print(f"  Path: {account['path']}")
            print()
    else:
        print("Failed to generate multiple accounts")

def main():
    """Run all tests"""
    print()
    print("BEX BLOCKCHAIN - BIP-44 WALLET GENERATION TESTS")
    print("SLIP-0044 Compliant (Coin Type: 140586)")
    print("=" * 60)
    print()
    
    try:
        test_simple_wallet()
        test_mnemonic_generation()
        test_wallet_from_mnemonic()
        test_complete_wallet_generation()
        test_multiple_accounts()
        
        print("=" * 60)
        print("ALL TESTS COMPLETED")
        print("=" * 60)
        print()
        print("SLIP-0044 Compliance Summary:")
        print(f"  Coin Type: {BEX_COIN_TYPE} (Official SLIP-0044)")
        print(f"  Chain ID: {BEX_CHAIN_ID}")
        print(f"  Derivation Path: {BIP44_PATH_BEX}")
        print(f"  Standard: BIP-39 (Mnemonic) + BIP-44 (Derivation)")
        print()
        
    except Exception as e:
        print(f"Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()