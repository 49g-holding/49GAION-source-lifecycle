# DR-0004 · Source Lifecycle mother: positions only, brought into line with 49GAION/DR-0048 and DR-0049

- **Date:** 2026-10-28
- **Decided by:** the governing seat (GOV) of 49GAION
- **Source:** `49GAION/DR-0048`, the complete definition `v2.1.0`: the system recognises only AI, organised in AIOCs, and human positions carrying a HOAC label; no natural person and no person's name is recorded in it; each organisation's own mechanism, outside the system, decides how its positions are assigned and administered and who holds them. `49GAION/DR-0049` brings the texts into line. The record is prepared by the AI hub; the governing seat's merge is the decision.
- **Relation:** builds on DR-0003. Where an earlier record of this repository sets the mechanism behind a human position (who occupies it, an acting filler, a deputy, "the governance seat appoints Top Management directly"), this record supersedes it; those records are frozen and are read with this one.

## Decision

1. **Positions only.** Every human place in this repository is a position. Who holds it, and how (successors, deputies, boards and the credentials with which a position signs included), is the organisation's own mechanism, outside the system; this AIOC never sees it.
2. **Withdrawn.** The acting filler and the signature type `appoint-acting-filler`, which leaves every `authority_scope`; deputies of human seats (the positions table's Deputy column becomes Cover, which stays meaningful for AI positions); occupancy, handover and arrangement entries; the holders register; a compensating control for one person behind several positions. What stays: two positions are two parties; the Overseen link between positions; `succeeded_by`; the duty deputy, an AI part.
3. **The changes.** Each place below is changed in its file; its former wording is kept here, verbatim.

   - `blueprint/SL-BLUEPRINT.md`, under “Blueprint · `[ORG]AIOC-SL` · Source Lifecycle · `v0.1.4`”, the one-page summary, no natural person:
     ```text
     Who occupies a position, and how, is the organisation's top management's own mechanism (`[ORG]HOAC-TM`). SL never sees it;
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “0. Identity and lineage”, the accountable seat:
     ```text
     Who occupies it is top management's own mechanism; this AIOC never sees it (`49GAION/DR-0013`)
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “2.1 Organisation table”, the register of positions:
     ```text
     | the unit register's `position` and `arrangement` entries. The `occupancy` and `handover` entries are top management's own mechanism, in the private register copy; SL never reads them (`49GAION/DR-0011`, item 4; `DR-0013`). SL reaches a position only through its HU port, and only the tool gateway checks that a sign-in belongs to a current occupant |
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “3. Positions”, no natural person:
     ```text
     Who occupies them, and how, is top management's own mechanism; no part of this AIOC holds, reads or infers it.
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “Definition”, its HOAC seat is a position:
     ```text
     When the occupant changes, open work, commitments and the delegation ladder in force pass in full to the new occupant.
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “Definition”, Holder Chief of Staff:
     ```text
     - **Holder Chief of Staff.** It also serves the Lead as the holder's Chief of Staff (
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “Role card”, tools and access:
     ```text
     the register of positions, read only, to reach a position's occupants;
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “7. Records and where things live”, the link:
     ```text
     | The link between positions and the natural persons who occupy them | not in SL: top management's own mechanism (`49GAION/DR-0013`); SL holds position codes only |
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “9. Fixed tests: index, triggers and scores”, outbound name check:
     ```text
     | Outbound name check: no occupant's name or contact in any needs answer, reference or notice |
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “11. Exceptions”, item 3:
     ```text
     3. **The holder Chief of Staff is this AIOC's Chief of Staff.** The Standard attaches a holder Chief of Staff to the holder's Cell.
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “11. Exceptions”, item 4:
     ```text
     is read as the holder of `[ORG]HOAC-ACS` over this AIOC, the Source Lifecycle Lead,
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “13. For the `[ORG]HOAC-ACS` seat, and every decision only a human seat can take”, H-01:
     ```text
     | **Top management's own mechanism.** Arrange the Source Lifecycle Lead position (`[ORG]CELL-SLL`) and any HOAC position added to this AIOC (`49GAION/DR-0011` to `DR-0013`). Nothing of who occupies them enters this blueprint | the Cell carrying `[ORG]HOAC-TM` (`49GAION/DR-0011`, item 2) | the position is vacant:
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “17. Cells and Pods”, how a HOAC position is added:
     ```text
     It adds one human Cell to the parts block (or a Pod with a `decision_rule`, where a group of positions decides together), with its HOAC label;
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “17. Cells and Pods”, position, not person:
     ```text
     Who occupies it, and how, is top management's own mechanism (`49GAION/DR-0011` to `DR-0013`). This blueprint never names an occupant and never reads an occupancy entry.
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “D.2 Routing”, non-delegable rows:
     ```text
     | the tool gateway checks that the answering sign-in belongs to a current occupant of that position; an answer from any other position is refused; a vacant position holds the row and goes to the Lead |
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “D.2 Routing”, after the routing table:
     ```text
     SL reads no occupancy entry, and no occupant's name ever reaches the part.
     ```
   - `tests/TEST-SL.md`, under “B. The PRD's requirements FR-24 to FR-46”, TEST-SL, case 29:
     ```text
     no occupant's name appears in any needs answer.
     ```
   - `tests/TEST-SL.md`, under “E. This AIOC's form”, TEST-SL, case 81:
     ```text
     SL reads no occupancy entry; a vacant or unresolvable position holds the row
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “3. Positions”, the Deputy cell of the accountable position:
     ```text
     | as top management arranges (`appoint-acting-filler`, Standard §4.1, item 12) |
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “3. Positions”, the positions table, the Deputy column:
     ```text
     | Position (standard title) | Purpose | Reports to | Run today by | Deputy |
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “3. Positions”, the positions table, Run today by:
     ```text
     Who occupies it, and how, is top management's own mechanism; this AIOC never sees it
     ```
   - `blueprint/SL-BLUEPRINT.md`, under “3. Positions”, the positions table, the empty position:
     ```text
     While the position shows no occupant, the Chief of Staff only advises
     ```

4. **The cards** are regenerated by `tools/make_cards.py` from the blueprint.
5. **The version.** Unreleased. The blueprint keeps its version label; the version and the Library pin move at the next release, by a pull request, on the governing seat's word.

*Powered by 49GAION*
