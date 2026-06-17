"""Apply branding + QA fixes to s2_deck_records_raw.json -> s2_deck_records.json."""
import json, copy

SRC_PATH = "s2_deck_records_raw.json"
REC_PATH = "s2_deck_records.json"

# full replacements (keyed by src)
REPLACE = {
    "40": {  # strip DF email; IAF-generic contact + flag for real handle
        "src": "40", "arch": "numbered", "eyebrow": "What's Next", "title": "What's next",
        "rows": [
            {"num": "01", "lead": "Session 3", "body": "See you here in two weeks — [insert date and time]!"},
            {"num": "02", "lead": "For Next Time", "body": "Prepare your inputs (data, decisions, documents)."},
            {"num": "03", "lead": "Questions?", "body": "Chat on the cohort channel or reach out to the ImpactAI Foundry team."},
        ],
        "note": "TODO: set the real cohort channel + team contact for questions.",
    },
    "13": {  # source screenshot is a live capture of the DF website (logos + URL) -> drop it
        "src": "13", "arch": "statement", "eyebrow": "Code · Building a Website",
        "title": "Recreate a site from its URL",
        "subtitle": "Ask Claude to recreate a site at a URL — it reads the front-end design for best practices, fetches details, and rebuilds the page.",
        "note": "Original slide showed a live website-recreation screenshot of the source org's own site (off-brand for IAF). On reshoot, drop in a screenshot of an IAF or brand-neutral site being rebuilt.",
    },
}

# shallow merges
MERGE = {
    "37": {
        "intro": "Post in the cohort channel, or email the ImpactAI Foundry team.",
        "note": "TODO: set the real cohort channel + team email.",
    },
    "39": {
        "subtitle": "Find this week's survey link in your cohort channel.",
        "note": "TODO: add IAF's own weekly-survey link.",
    },
}

SPLIT = {}


def _merge_qa_notes(out):
    try:
        verdicts = json.load(open("s2_qa_verdicts.json"))
    except Exception:
        return 0
    by = {}
    for r in out:
        by.setdefault(str(r["src"]), []).append(r)
    added = 0
    for v in verdicts:
        issue = (v.get("image_issue") or "").strip()
        if not issue or v.get("severity") not in ("minor", "major") or str(v["n"]) in REPLACE:
            continue
        for r in by.get(str(v["n"]), []):
            if not (r.get("image") or r.get("images") or r["arch"] in ("image_full", "image_text", "image_grid")):
                continue
            note = r.get("note", "")
            if issue[:30] not in note:
                r["note"] = (note + "  RESHOOT — " + issue).strip()
                added += 1
    return added


def main():
    recs = json.load(open(SRC_PATH))
    out = []
    for r in recs:
        s = str(r.get("src"))
        if s in SPLIT:
            out.extend(copy.deepcopy(SPLIT[s]))
        elif s in REPLACE:
            out.append(copy.deepcopy(REPLACE[s]))
        elif s in MERGE:
            rr = copy.deepcopy(r); rr.update(MERGE[s]); out.append(rr)
        else:
            out.append(r)
    n = _merge_qa_notes(out)
    json.dump(out, open(REC_PATH, "w"), ensure_ascii=False, indent=1)
    print(f"applied {len(REPLACE)} replace, {len(MERGE)} merge, {len(SPLIT)} split, {n} qa notes -> {len(out)} records")


if __name__ == "__main__":
    main()
