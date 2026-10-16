# Contributing

**49GAION Source Lifecycle, mother blueprint `v0.1.2` · 16 October 2026.**

1. **One change, one pull request**, reviewed by someone other than its writer, and merged by the governing seat of 49GAION.
2. **No organisation's data.** No organisation's name, host, code, document or value is ever written here (Naming Standard R9). An instance keeps its own values in its own repositories.
3. **Positions, never people.** No person's name, initials or personal ID in any file.
4. **The PRD governs the product; the blueprint governs the AIOC.** A rule that changes what the product must do goes to the product's PRD first; the blueprint then cites it.
5. **Cite every rule** to its source: a 49GAION text by section and version, or a PRD requirement by ID. Never invent a fact, a version, a score or an appointment. `NOT_RUN` is never PASS.
6. **The blueprint governs the cards.** Edit the card data block of blueprint §17 only, then run `python3 tools/make_cards.py <49GAION-protocol/spec/schemas>`. It must report 0 errors.
7. **Decided texts are never edited.** A change is a new version that names what it supersedes. A decision record never changes once merged.
8. **A new version reaches the Library** only by a pull request to `49GAION-protocol` that moves the pin.
9. **English only, plain and short.**

*Powered by 49GAION*
