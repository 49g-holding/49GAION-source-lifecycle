"""Case 85 of TEST-SL v1: the blueprint matches the PRD.

Reads the requirement IDs (FR-nn, NFR-nn) from the requirement tables of the product's PRD
and checks that blueprint/SL-BLUEPRINT.md cites every one of them, directly or inside a
range written "FR-06 to FR-10". The PRD lives in the instance's code project (docs/prd/);
pass its path.
Usage: python3 tools/check_trace.py <path to the product's PRD>   (exit 1 if any is missing)
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BP = ROOT / "blueprint" / "SL-BLUEPRINT.md"


def cited(text):
    ids = set(re.findall(r"(?<![A-Z])(N?FR-\d\d)\b", text))
    for kind, a, b in re.findall(r"(?<![A-Z])(N?FR)-(\d\d) to N?FR-(\d\d)", text):
        ids |= {f"{kind}-{i:02d}" for i in range(int(a), int(b) + 1)}
    return ids


def main(prd_path):
    prd = pathlib.Path(prd_path).read_text(encoding="utf-8")
    need = set(re.findall(r"^\| (N?FR-\d\d) \|", prd, re.M))
    if not need:
        sys.exit("no requirement rows found in the PRD")
    missing = sorted(need - cited(BP.read_text(encoding="utf-8")))
    for m in missing:
        print("NOT CITED", m)
    print(f"{len(need)} requirements in the PRD; {len(need) - len(missing)} cited by the blueprint; {len(missing)} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
