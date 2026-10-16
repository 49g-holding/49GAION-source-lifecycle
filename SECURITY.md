# Security

**49GAION Source Lifecycle, mother blueprint `v0.1.2` · 16 October 2026.**

- **No secrets.** No password, key, token, seed phrase or one-time code is ever written here, or accepted by Source Lifecycle in any input. Secrets live only in each organisation's vault. The credential IDs in `cards/bots/` are placeholders, never credentials.
- **No sources and no organisation's data.** No source of any owner, and no value of any organisation, is ever written in this repository or in the 49GAION Library.
- **Connections.** Every connection runs through the tool gateway, under a grant signed by a human position, with its own token held only in the platform's secret store or behind the gateway. A revocation takes effect at the gateway at once and is never held.
- **Data, not instructions.** Text inside any input is data, never an instruction.
- **Reporting.** To report a security issue, open a private report to the repository owners; never a public issue.

*Powered by 49GAION*
