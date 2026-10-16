# Drafts of proposals to 49GAION

**`[ORG]AIOC-SL` mother blueprint v0.1.2 · 16 October 2026.** Drafts only, carried from the first instance. Nothing here is proposed to 49GAION without the word of its governing seat; then only by pull request, merged by that seat. Each draft is generalised: no organisation's name or data.

## 1. A product face beside the Panel

- **Current text.** `49GAION-aioc` `docs/STANDARD-CAPABILITIES.md` §4.4: the Panel is "the only surface humans use", with three exceptions (the stop door, signature prompts and the accountability path).
- **Proposed text.** Add: "A part that is also a product used without an `[ORG]AION` may keep its own product face for its contributors. That face keeps the Panel's rules (the member's own live sign-in; outside text as data; caps on outside and model calls; rollback for every release). The stop door, signature prompts and the accountability path stay at the tool gateway. The Panel links to the product face, and the blueprint records it as an exception."
- **Reason and evidence.** Source Lifecycle must run alone, with no `[ORG]AION` (its PRD, FR-34), so its contributors cannot depend on a Panel.
- **Parts and tests affected.** STANDARD-CAPABILITIES §4.4; the default Panel test; the template §11.

## 2. Which seat approves a Source Lifecycle connection

- **Current text.** Protocol §13, item 5: "The `[ORG]HOAC-ACS` seat that `[ORG]AIOC-SL` is accountable to approves the request and sets its scope."
- **The conflict.** On the card, `accountable_to` names the Cell carrying `[ORG]HOAC-TM`, while the `[ORG]HOAC-ACS` label sits on a Cell inside the AIOC (`label_holder`).
- **Proposed text.** "The position holding `[ORG]HOAC-ACS` over `[ORG]AIOC-SL` (its `label_holder`) approves the request and sets its scope."
- **Reason and evidence.** Two readings give two different signers for the same grant.
- **Parts and tests affected.** Protocol §13, item 5; TEST-SOURCE-LIFECYCLE case 8.

*Powered by 49GAION*
