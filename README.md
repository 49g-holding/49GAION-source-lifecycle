# 49GAION Source Lifecycle · the mother blueprint

The mother repository of the Library part **49GAION Source Lifecycle**. In an `[ORG]AION`, the part is the AIOC `[ORG]AIOC-SL`. Public. It holds the mother blueprint only, for any organisation, with no organisation's data (`49GAION/DR-0024`; Naming Standard R9, addition 4).

> **Reading (49GAION DR-0041).** The complete definition of 49GAION, approved by its governing seat on 25 October 2026, is `49GAION-FRAMEWORK.md` in `github.com/49g-holding/49GAION`. Where this repository differs from it, the definition governs, and this text is read with it. Every rule here that names `[ORG]AIOC-OCO` or the human hub reads as the Top Management Group, the hub of the operation, human and AI. The panel is the organisation's own code interface, and the AI chat workspace is its back office. The readings are in [`decisions/DR-0003`](decisions/DR-0003-the-readings-of-dr-0041.md). Nothing here is removed.

Source Lifecycle keeps an organisation's own sources: its documents, and what its people say once they have approved it. It records each one, gives it a reference, classifies it and fixes it, so that every source has one valid version and a traceable origin. It is a product on its own, for any owner, and the first stage of every larger system: in 49GAION, every source enters through it (Protocol §13).

The one-page summary is at the top of the blueprint.

## What is here

| Path | What it is |
|---|---|
| [`blueprint/SL-BLUEPRINT.md`](blueprint/SL-BLUEPRINT.md) | the mother blueprint, `v0.1.4`, on the 49GAION AIOC template |
| [`tests/TEST-SL.md`](tests/TEST-SL.md) | the fixed test, TEST-SL v1: 95 cases, every one `NOT_RUN`, with the Library's TEST-SOURCE-LIFECYCLE v4 kept and mapped |
| [`cards/`](cards/) | the unit cards of its Pods and Cells, and the bot identity cards, generated from blueprint §17 |
| [`contracts/README.md`](contracts/README.md) | the sockets contract: where its first drafts are, by path, commit and hash |
| [`decisions/`](decisions/) | the decision records of this repository |
| [`upstream/PROPOSALS.md`](upstream/PROPOSALS.md) | drafts of proposals to 49GAION, not yet proposed |
| [`tools/`](tools/) | `make_cards.py` (the cards, case 84) and `check_trace.py` (the blueprint matches the product's PRD, case 85) |

## Mother and instance

- **The Library pins this text** by repository, path, version, commit and SHA-256 (`49GAION-protocol`, `library/README.md`). A new version reaches the Library only by a pull request that moves the pin.
- **Each organisation makes its own instance** from it: its writing repository `<org>aioc-sl`, private where it holds the organisation's data, with the `<organisation>`, `<org>` and `<filled>` values set (blueprint §0, §2.1). The organisation's values never come back here.
- **The product's code and its requirements** (the PRD) live in the instance's code project. The blueprint cites the PRD by requirement ID (blueprint §0, Product requirements).

## Checks

**The Protocol pin.** The checks are the one set of checks of the Library repositories, the action `library-checks` of `49GAION-protocol`, run at the commit in `PROTOCOL-PIN`, which also gives the schemas and the `no-org-names` scanner they read, never at `main`, so a change in the Protocol changes nothing here until this repository moves the pin by pull request.

On every pull request and on main (`.github/workflows/checks.yml`):

```
python3 tools/make_cards.py <49GAION-protocol>/spec/schemas      # 0 errors; the committed cards are the generated cards
bash <49GAION-protocol>/.github/scripts/no-org-names.sh          # no organisation name, host or prefixed code
```

and no Persian or Arabic-script character in any tracked file. In an instance, `python3 tools/check_trace.py <the product's PRD>` reports 0 missing.

## Owner and licence

- **Owner and licence.** The copyright holder, and the licences of the texts (CC BY 4.0, credit "Powered by 49GAION") and of the code (Apache-2.0), are in [`LICENSE.md`](LICENSE.md).

*Powered by 49GAION*
