# BEXChain Whitepaper v1.0 (Draft)

Tanggal: 6 Maret 2026  
Status: Draft internal

## 1. Ringkasan Eksekutif
BEXChain adalah ekosistem blockchain dengan koin native **BEX** sebagai mata uang utama untuk transaksi dalam game, aplikasi pihak ketiga, pembayaran layanan, dan utilitas DeFi di dalam ekosistem BEX. Whitepaper ini mendefinisikan fondasi ekonomi, distribusi token, model utilitas, dan parameter teknis awal jaringan.

## 2. Visi dan Tujuan
Tujuan BEXChain adalah membangun ekosistem digital terintegrasi di mana:
- Pengguna dapat memperoleh BEX melalui aktivitas mining dan partisipasi ekosistem.
- Pengembang game/aplikasi pihak ketiga dapat mengadopsi BEX sebagai alat pembayaran.
- Produk inti BEX saling terhubung melalui wallet, DEX, dan layanan API/RPC.

Visi jangka panjang: BEX menjadi medium of exchange utama lintas produk dalam ekosistem BEXChain.

## 3. Produk Ekosistem
Produk dan kanal utilitas yang menjadi fokus:
- **Mining Bot Telegram**: onboarding dan reward mining berbasis aktivitas komunitas.
- **BEX Miner Android**: antarmuka mobile untuk aktivitas mining dan monitoring reward.
- **BEX DEX**: pertukaran/swap aset di dalam ekosistem.
- **BEX Wallet Multichain**: manajemen aset BEX dan aset lintas jaringan.
- **Integrasi pihak ketiga**: game dan aplikasi eksternal yang menerima BEX sebagai mata uang.

## 4. Fondasi Teknis
BEXChain menggunakan pendekatan **custom EVM-compatible architecture** agar kompatibel dengan pola integrasi dan tooling EVM.

Parameter teknis saat ini (mengacu konfigurasi source code):
- Chain Name: `bexchain`
- Chain ID: `140586`
- Native Coin: `BEX`
- Decimals: `18`
- RPC URL (default): `http://localhost:8545`
- API URL (default): `http://localhost:8545/api`

Endpoint yang tersedia di implementasi saat ini:
- JSON-RPC: `/rpc`
- Chain info API: `/api/chain_info`
- Gas fee API: `/api/gas_fees`
- Explorer UI: `/explorer/`

## 5. Model Gas
BEX digunakan sebagai biaya eksekusi transaksi di jaringan.

Konfigurasi gas fee default saat ini:
- Standard transaction: `0.01 BEX`
- Token transfer: `0.01 BEX`
- Token contract execution: `0.02 BEX`
- NFT transfer: `0.015 BEX`
- NFT contract execution: `0.025 BEX`

Catatan:
- Model ini dapat disesuaikan oleh governance/admin sesuai kebutuhan operasional jaringan.
- Gas fee wallet saat ini diarahkan ke alamat treasury operasional yang dikonfigurasi pada node.

## 6. Tokenomics BEX
### 6.1 Total Supply
- Total suplai BEX: **10,000,000 BEX**
- Sifat suplai: **fixed supply** (tidak bertambah)

### 6.2 Distribusi Token
- Mining Reward: **1,500,000 BEX** (15%)
- Presale: **1,000,000 BEX** (10%)
- Ads Reward: **500,000 BEX** (5%)
- Founder: **1,000,000 BEX** (10%)
- Team: **1,000,000 BEX** (10%)
- Alokasi Game & Aplikasi Pihak Ketiga: **5,000,000 BEX** (50%)

Total: **10,000,000 BEX** (100%)

### 6.3 Presale Vesting
Alokasi presale sebesar **1,000,000 BEX** mengikuti skema:
- **Cliff 12 bulan**: bulan 1-12 tidak ada unlock.
- **Mulai bulan ke-13**: unlock **10% per bulan** dari alokasi presale.
- Besaran unlock bulanan: **100,000 BEX/bulan**.
- Durasi unlock: **10 bulan** (bulan ke-13 sampai bulan ke-22).
- Bulan ke-22: **100% alokasi presale telah unlocked**.

## 7. Kebijakan Likuiditas
Likuiditas awal ekosistem akan diisi dari dua sumber utama:
- **10% dari pendapatan iklan bulanan**.
- **Dana dari presale BEX**.

Kebijakan ini bertujuan menjaga kedalaman pasar awal, mendukung aktivitas swap di BEX DEX, dan menurunkan friksi adopsi untuk pengguna baru.

## 8. Keamanan dan Audit
Keamanan implementasi saat ini mencakup:
- Audit trail operasi aplikasi (logging internal).
- Endpoint audit trail API untuk monitoring (`/api/security/audit_trail`).
- Rate limiting API.
- Validasi input transaksi.
- Dukungan multi-signature wallet pada modul keamanan.

Status audit:
- **Belum mencantumkan audit eksternal independen** pada draft ini.
- Rekomendasi tahap berikutnya: smart contract audit dan security assessment oleh pihak ketiga sebelum ekspansi skala besar.

## 9. Tata Kelola dan Operasional
Pada fase awal, pengelolaan parameter jaringan (termasuk gas fee dan operasional treasury) dilakukan oleh tim inti untuk stabilisasi ekosistem. Seiring maturitas jaringan, model governance dapat dikembangkan menuju mekanisme yang lebih terbuka dan partisipatif.

## 10. Roadmap Ringkas (Draft)
- Fase 1: Stabilitas main service (RPC, explorer, wallet flow, gas policy).
- Fase 2: Ekspansi utilitas BEX di game dan aplikasi pihak ketiga.
- Fase 3: Peningkatan likuiditas DEX dan integrasi multichain.
- Fase 4: Audit eksternal, hardening keamanan, dan skalabilitas ekosistem.

## 11. Risiko
Risiko utama yang perlu dikelola:
- Volatilitas harga aset digital.
- Risiko keamanan aplikasi/smart contract.
- Risiko adopsi (pengguna dan mitra pihak ketiga).
- Perubahan kebijakan/regulasi di wilayah operasional.

## 12. Disclaimer
Dokumen ini adalah whitepaper teknis dan ekonomi untuk tujuan informasi, bukan nasihat investasi, hukum, atau pajak. Partisipasi dalam ekosistem aset digital memiliki risiko tinggi dan menjadi tanggung jawab masing-masing pihak.

---

## Lampiran A - Sumber Parameter Teknis (Codebase)
Parameter teknis dalam dokumen ini disusun dari konfigurasi dan implementasi yang ada pada repository:
- `config.py` (chain, supply, RPC/API)
- `blockchain.py` (gas fee defaults)
- `app.py` (endpoint RPC, API, explorer, audit trail)
