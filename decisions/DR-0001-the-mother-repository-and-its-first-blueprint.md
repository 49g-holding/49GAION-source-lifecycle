# DR-0001 · The mother repository of Source Lifecycle, and its first mother blueprint

- **Date:** 2026-10-16
- **Decided by:** the governing seat (GOV) of 49GAION
- **Sources:** `49GAION/DR-0024` (a mother repository for a Library part whose first instance holds an organisation's data); `49GAION/DR-0019` (the Library register) and `DR-0021` (mother and instance)

## Decision

1. **This repository.** `github.com/49g-holding/49GAION-source-lifecycle`, public, is the mother repository of the Library part 49GAION Source Lifecycle. It holds the mother blueprint only, laid out and checked as a writing repository.
2. **The first mother blueprint.** `blueprint/SL-BLUEPRINT.md` `v0.1.2`, written from the blueprint of the part's first instance, `v0.1.2`, with every value of that organisation removed: the organisation, its codes, its repositories, its code project, its seats and its history. Each is replaced by a `<organisation>`, `<org>` or `<filled>` placeholder, a position, or a public reference. No rule is added, changed or removed.
3. **The rules' own records.** The rules of `v0.1.1` rest on `49GAION/DR-0016` to `DR-0018`, and those of `v0.1.2` on `49GAION/DR-0023`. The first instance's own decision records stay in its writing repository.
4. **The fixed test.** TEST-SL v1, 91 cases, every one `NOT_RUN`, with the Library's TEST-SOURCE-LIFECYCLE v3 kept and mapped (`tests/TEST-SL.md`).
5. **The Library pin.** Once merged, this text is pinned in `49GAION-protocol` `library/README.md` by repository, path, version, commit and SHA-256.
6. **The first instance** keeps its private writing repository and names this mother by pin.

*Powered by 49GAION*
