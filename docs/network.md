# BEXChain Network Parameters

Last validated: `2026-05-13`

## Canonical Values

- Network Name: `BEXChain`
- Chain Name: `bexchain`
- Chain ID (decimal): `140586`
- Chain ID (hex): `0x2252a`
- Native Coin: `BEX`
- Decimals: `18`

## Official Public Endpoints

- RPC (JSON-RPC): `https://rpc.bexchain.com`
- API Base: `https://api.bexchain.com/api`
- Chain Info: `https://api.bexchain.com/api/chain_info`
- Explorer UI: `https://scan.bexchain.com`

## Quick Validation Examples

Check chain ID via JSON-RPC:

```bash
curl -sS -H "content-type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}' \
  https://rpc.bexchain.com
```

Expected result:

```json
{"id":1,"jsonrpc":"2.0","result":"0x2252a"}
```

Check chain metadata:

```bash
curl -sS https://api.bexchain.com/api/chain_info
```

## Notes

- `https://rpc.bexchain.com/rpc` is not valid (returns `404`).
- `https://api.bexchain.com` serves web UI, while API paths are under `/api`.
- `https://api.bexchain.com/api/gas_fees` currently returns `Endpoint disabled` on the public endpoint.
