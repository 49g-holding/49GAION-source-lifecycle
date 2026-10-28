# The sockets contract

**`[ORG]AIOC-SL` mother blueprint v0.1.5 · 29 October 2026.** The drafts are those of the Target Operating Model mother v0.6.1.

The sockets contract is how every connected part talks to Source Lifecycle (PRD FR-31, FR-46; blueprint §5.8). Its first drafts were written by `[ORG]AIOC-TOM` and are kept where they were written. They are named here by path and hash, not copied, so that there is one home for each. Source Lifecycle adopts them, changes them or replaces them under PRD D-20 (blueprint §13, H-02). Until then they are **Proposed**.

Source: `github.com/49g-holding/49aioc-tom`, v0.6.1, folder `contracts/`, at the merged commit `302e98b4937609484adb5164c20b5ef22211c411`; each file is named by its hash, read back at that commit on 19 October 2026. From v0.6.0 (`a8445cb`) only the needs request changed: its `raised_by` names the Target Operating Model's Chief of Staff by its COS code, `[ORG]CELL-COSTOM` (Naming Standard R16), and its `$id` moved to `v0.6.1`; the other five files are byte-identical. The v0.4.0 drafts (commit `2ec2373`) are superseded: v0.6 adds the proposed and decided priority of an element row, and the aggregation of an export request for records of the work (blueprint §5.8; Annex F.3).

| Contract | File | `$id` | SHA-256 |
|---|---|---|---|
| needs request | `needs-request.schema.json` | `urn:49gaion:library:tom:needs-request:v0.6.1` | `5293e10c6ee24dd38784628b415e7ed8e470f1b7c695aa53dea17e684345d4e4` |
| needs answer | `needs-answer.schema.json` | `urn:49gaion:library:tom:needs-answer:v0.6` | `a36a4cbe8add05f67c14ead05c26e068fe52ca55f1113f317ce9fb601371beb1` |
| needs status | `needs-status.schema.json` | `urn:49gaion:library:tom:needs-status:v0.3` | `5b9a397b888455d5e881b7cdbb1c2d3dbc8e4bbfdc9b1fa70a99da9c24aa44f2` |
| Missing Report | `missing-report.schema.json` | `urn:49gaion:library:tom:missing-report:v0.3` | `bce0dc4e66a01001a8700ce4ab301c0d47ec0f3efb2316931091df23dd904f11` |
| source reference | `source-reference.schema.json` | `urn:49gaion:library:tom:source-reference:v0.3` | `e9e2f4fe45be37307eaa4dbfb9abb2f48b04a5838221478c8b0ddfeb70624b93` |
| filing receipt | `tom-filing-receipt.schema.json` | `urn:49gaion:library:tom:tom-filing-receipt:v0.3` | `d2050bcef062ffd406dcba3dc7eee3a3617428179b430ec91816b250040183f3` |

## Points for adoption (PRD D-20)

These are noted for the decision, not decided here.

1. **Who may raise a request.** In the draft, `needs-request.raised_by` lists only the Pods and the Chief of Staff of `[ORG]AIOC-TOM`. A contract that any connected part can use would take the raising part's own codes, checked against its grant.
2. **Whose names.** The `$id`s sit under `library:tom`. When Source Lifecycle adopts them as its own published contract, they move under its own name, and each connected part pins the version it supports.
3. **Fixtures in CI.** The fixtures are in `github.com/49g-holding/49aioc-tom`, `contracts/examples/`. Once adopted, they run in the code project's CI on every change to the contract (PRD FR-46).

*Powered by 49GAION*
