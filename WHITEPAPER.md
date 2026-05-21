# BEXChain Whitepaper v1.0 (Draft)

Date: March 6, 2026
Status: Public draft

## 1. Executive Summary
BEXChain is a blockchain ecosystem with its native coin **BEX** as the primary currency for in-game transactions, third-party applications, service payments, and DeFi utilities within the BEX ecosystem. This whitepaper defines the economic foundation, token distribution, utility model, and initial technical parameters of the network.

## 2. Vision and Goals
BEXChain's goal is to build an integrated digital ecosystem where:
- Users can earn BEX through mining activities and ecosystem participation.
- Third-party game/app developers can adopt BEX as a means of payment.
- BEX's core products are interconnected through wallets, DEXs, and API/RPC services.

Long-term vision: BEX becomes the primary medium of exchange across products within the BEXChain ecosystem.

## 3. Ecosystem Products
Focused utility products and channels:
- **Mining Bot Telegram**: onboarding and mining rewards based on community activity.
- **BEX Miner Android**: mobile interface for mining activities and reward monitoring.
- **BEX DEX**: asset exchange/swapping within the ecosystem.
- **BEX Wallet Multichain**: BEX asset and cross-chain asset management.
- **Third-party integrations**: external games and applications that accept BEX as currency.

## 4. Technical Foundation
BEXChain uses a custom EVM-compatible architecture approach to ensure compatibility with EVM integration patterns and tooling.

Current technical parameters:
- Chain Name: `bexchain`
- Chain ID: `140586`
- Native Coin: `BEX`
- Decimals: `18`
- RPC URL (production): `https://rpc.bexchain.com`
- API Base URL (production): `https://api.bexchain.com/api`
- Explorer UI (production): `https://scan.bexchain.com`

Public integration endpoints:
- JSON-RPC: `https://rpc.bexchain.com`
- Chain info API: `https://api.bexchain.com/api/chain_info`
- Gas fee API: `https://api.bexchain.com/api/gas_fees` (currently disabled on public endpoint)

- Metadata chainlist:
- Network ID: `140586`
- EVM Features: `EIP155`, `EIP1559`
- Explorer Standard: `EIP3091`
- URL info: `https://bexchain.com`

Listing status note:
- Listed on Chainlist (Chain ID 140586), verified on May 21, 2026.

## 5. Gas Model
BEX is used as a fee for executing transactions on the network.

Current default gas fee configuration:
- Standard transaction: `0.01 BEX`
- Token transfer: `0.01 BEX`
- Token contract execution: `0.02 BEX`
- NFT transfer: `0.015 BEX`
- NFT contract execution: `0.025 BEX`

Note:
- This model can be adjusted by governance/admins to suit the network's operational needs.
- Wallet gas fees are currently directed to the operational treasury address configured on the node.

## 6. BEX Tokenomics
### 6.1 Total Supply
- Total BEX supply: **10,000,000 BEX**
- Supply type: **fixed supply** (does not increase)

### 6.2 Token Distribution
- Mining Reward: **1,500,000 BEX** (15%)
- Presale: **1,000,000 BEX** (10%)
- Ads Reward: **500,000 BEX** (5%)
- Founder: **1,000,000 BEX** (10%)
- Team: **1,000,000 BEX** (10%)
- Game & Third-Party App Allocation: **5,000,000 BEX** (50%)

Total: **10,000,000 BEX** (100%)

### 6.3 Presale Vesting
The presale allocation of **1,000,000 BEX** follows the following scheme:
- **12-month Cliff**: No unlocking for months 1-12.
- **Starting from the 13th month**: 10% per month of the presale allocation is unlocked.
- Monthly unlock amount: **100,000 BEX/month**.
- Unlock duration: **10 months** (months 13 to 22).
- Month 22: **100% of the presale allocation has been unlocked**.

## 7. Liquidity Policy
Initial liquidity in the ecosystem will be provided by two main sources:
- **10% of monthly advertising revenue**.
- **Funds from the BEX presale**.

This policy aims to maintain initial market depth, support swap activity on the BEX DEX, and reduce adoption friction for new users.

## 8. Security and Audit
Current security implementation includes:
- Application operation audit trail (internal logging).
- API audit trail endpoint for monitoring (`/api/security/audit_trail`).
- Rate limiting API.
- Transaction input validation.
- Multi-signature wallet support in the security module.

Audit status:
- **Independent external audit not yet included** in this draft.
- Recommended next phase: smart contract audit and security assessment by a third party before large-scale expansion.

## 9. Governance and Operations
In the initial phase, network parameter management (including gas fees and treasury operations) is carried out by the core team to stabilize the ecosystem. As the network matures, the governance model can be evolved towards a more open and participatory mechanism.

## 10. Summary Roadmap (Draft)
- Phase 1: Stability of main services (RPC, explorer, wallet flow, gas policy).
- Phase 2: Expansion of BEX utility in games and third-party applications.

- Phase 3: DEX liquidity enhancement and multichain integration.
- Phase 4: External audit, security hardening, and ecosystem scalability.

## 11. Risks
Key risks to manage:
- Digital asset price volatility.
- Application/smart contract security risks.
- Adoption risks (users and third-party partners).
- Policy/regulatory changes in operational regions.

## 12. Disclaimer
This document is a technical and economic whitepaper for informational purposes and does not constitute investment, legal, or tax advice. Participation in the asset ecosystem Digital assets carry high risks and are the responsibility of each party.

---

## Appendix A - Technical Parameter Sources
Public references in this repository:
- `README.md` (official network profile and endpoint summary)
- `docs/network.md` (integration endpoints and request examples)

Runtime implementation details may exist in internal/private services and are published here as public-facing integration parameters.
