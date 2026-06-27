# BEXChain SLIP-0044 Compliance

## SatoshiLabs Registration
- **Repository**: trezor/slip-0044
- **Coin Type**: 140586 (0x8002252a)
- **Symbol**: BEX
- **Status**: Registered

## Wallet Implementation
- **BIP-39**: Compliant (12/24-word mnemonic seed standard)
- **BIP-44 Derivation Path**: `m/44'/140586'/0'/0/0`
- **HD Wallet**: Fully Supported

## Trezor Integration Quick Guide
1. Open Trezor Suite.
2. Enable custom EVM networks.
3. Add BEXChain using Chain ID: `140586` and RPC URL: `https://bexchain.com`.
4. The derivation path will automatically match the standard BEXChain index.
