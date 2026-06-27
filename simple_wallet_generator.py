#!/usr/bin/env python3
"""
Simple wallet generator with copy instructions
Supports both legacy and BIP-44 compliant wallet generation
"""

import sys
import os

# Add the project directory to Python path
sys.path.append('/home/bexchain/bex_blockchain')

# Import the wallet generation functions
from wallet_api import (
    generate_wallet,
    generate_wallet_with_mnemonic,
    BEX_CHAIN_ID,
    BEX_COIN_TYPE,
    BIP44_PATH_BEX
)

def main():
    """
    Main function to generate wallet with clear copy instructions
    Supports both legacy and BIP-44 compliant methods
    """
    print("BEX BLOCKCHAIN - WALLET GENERATOR")
    print("=" * 40)
    print()
    print("Choose wallet generation method:")
    print("1. Legacy method (direct key generation)")
    print("2. BIP-44 compliant (BIP-39 mnemonic + SLIP-0044)")
    print()
    
    try:
        choice = input("Enter choice (1 or 2, default: 2): ").strip()
        if not choice:
            choice = "2"
    except (EOFError, KeyboardInterrupt):
        choice = "2"
    
    if choice == "1":
        # Legacy method
        print()
        print("LEGACY WALLET GENERATION")
        print("-" * 40)
        wallet = generate_wallet()
        
        print("\nWALLET INFORMATION:")
        print("-" * 40)
        print(f"ADDRESS:")
        print(f"{wallet['address']}")
        print()
        print(f"PRIVATE KEY:")
        print(f"{wallet['private_key']}")
        print()
        print(f"PUBLIC KEY:")
        print(f"{wallet['public_key']}")
        print("-" * 40)
        
    else:
        # BIP-44 compliant method
        print()
        print("BIP-44 COMPLIANT WALLET GENERATION")
        print("-" * 40)
        print(f"Coin Type: {BEX_COIN_TYPE} (SLIP-0044: BEXChain)")
        print(f"Chain ID: {BEX_CHAIN_ID}")
        print(f"Derivation Path: {BIP44_PATH_BEX}")
        print()
        
        wallet = generate_wallet_with_mnemonic()
        
        print("\nWALLET INFORMATION:")
        print("-" * 40)
        print(f"MNEMONIC PHRASE:")
        print(f"{wallet['mnemonic']}")
        print()
        print(f"ADDRESS:")
        print(f"{wallet['address']}")
        print()
        print(f"PRIVATE KEY:")
        print(f"{wallet['private_key']}")
        print()
        print(f"DERIVATION PATH:")
        print(f"{wallet['path']}")
        print("-" * 40)
        
        print("\nSLIP-0044 COMPLIANCE:")
        print(f"  Coin Type: {BEX_COIN_TYPE} (0x{BEX_COIN_TYPE:08x})")
        print(f"  Chain ID: {BEX_CHAIN_ID}")
        print(f"  Official Entry: BEXChain (140586)")
        print()
    
    print("COPY INSTRUCTIONS:")
    print("1. To copy your ADDRESS:")
    print("   - Click and drag to select the address line")
    print("   - Press Ctrl+C (or Cmd+C on Mac) to copy")
    print()
    print("2. To copy your PRIVATE KEY:")
    print("   - Click and drag to select the private key line")
    print("   - Press Ctrl+C (or Cmd+C on Mac) to copy")
    print()
    
    if choice != "1":
        print("3. To copy your MNEMONIC:")
        print("   - Click and drag to select the mnemonic phrase")
        print("   - Press Ctrl+C (or Cmd+C on Mac) to copy")
        print()
    
    print("SECURITY REMINDER:")
    print("⚠️  SAVE YOUR PRIVATE KEY IN A SECURE LOCATION")
    print("⚠️  NEVER SHARE YOUR PRIVATE KEY WITH ANYONE")
    print("⚠️  IF YOU LOSE YOUR PRIVATE KEY, YOU LOSE ACCESS TO YOUR FUNDS")
    
    if choice != "1":
        print("⚠️  SAVE YOUR MNEMONIC PHRASE IN A SECURE LOCATION")
        print("⚠️  NEVER SHARE YOUR MNEMONIC WITH ANYONE")
        print("⚠️  THE MNEMONIC CAN BE USED TO RESTORE YOUR WALLET")

if __name__ == "__main__":
    main()