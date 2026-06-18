"""Apply branding + QA fixes to s4_deck_records_raw.json -> s4_deck_records.json."""
import json, copy, re

SRC_PATH = "s4_deck_records_raw.json"
REC_PATH = "s4_deck_records.json"

# global text substitutions applied to every VISIBLE string field (not notes)
SUBS = [
    (r"cohort\s*6", "cohort"),
    (r"Jenni Warren", "a teammate"),
    (r"\bthe the\b", "the"),     # cleanup any doubled article from the above
]

# authoring/merge scaffolding that leaked into visible caption/subtitle/body text
_MERGE_RE = re.compile(r"\s*Merged\b[^.]*\.\s*", re.I)

REPLACE = {
    "1": {  # use the source cover title; drop speculative date meta
        "src": "1", "arch": "cover", "eyebrow": "IMPACTAI FOUNDRY · SESSION 4",
        "title": "Bringing Your AI Into the World",
        "subtitle": "Customize your AI with connectors and skills, then build your prototype.",
    },
    "6": {  # DF's own Demo Day date/venue -> generic + TODO
        "src": "6", "arch": "statement", "eyebrow": "Demo Day",
        "title": "5-minute AI Solution Demos",
        "subtitle": "A celebration of how you're enhancing impact and workflows — date, time & venue to be confirmed.",
        "note": "TODO: set IAF's Demo Day date, time, and venue (source used the original program's own logistics).",
    },
    "54": {  # "Our Alumni" with NY-specific outcomes -> honest aspirational framing
        "src": "54", "arch": "bullets", "eyebrow": "What Teams Go On To Build",
        "title": "What teams go on to build",
        "intro": "Outcomes from the program model ImpactAI Foundry is built on:",
        "bullets": [
            "Build Policy — an AI policy for a 600-person organization",
            "Create Apps — an app to support nonprofits nationwide",
            "Lead Learning — an AI curriculum for a statewide network of Entrepreneurs Assistance Centers",
            "Get Funded — $500,000 in follow-on funding for AI tools",
            "Get Published — published on training the workforce for an AI era",
            "Scale — using AI to scale programming nationally",
        ],
        "note": "These are illustrative outcomes from the program model (IAF is cohort one). Swap for IAF's own alumni results once available.",
    },
}

MERGE = {}


def _apply_subs(rec):
    for k, v in list(rec.items()):
        if k == "note":
            continue
        rec[k] = _sub_value(v)
    # pull leaked "Merged ..." authoring notes out of visible text into the note
    for k in ("caption", "subtitle", "body", "intro"):
        v = rec.get(k)
        if isinstance(v, str) and _MERGE_RE.search(v):
            rec[k] = _MERGE_RE.sub(" ", v).strip()
            rec["note"] = (rec.get("note", "") + "  (merged animation-build slides)").strip()


def _sub_value(v):
    if isinstance(v, str):
        for pat, repl in SUBS:
            v = re.sub(pat, repl, v, flags=re.I)
        return v
    if isinstance(v, list):
        return [_sub_value(x) for x in v]
    if isinstance(v, dict):
        return {k: (_sub_value(val) if k != "note" else val) for k, val in v.items()}
    return v


def _fix_56(rec):
    # genericize the Demo Day logistics row inside "What's Next"
    for row in rec.get("rows", []):
        if "cajetan" in json.dumps(row).lower() or "lawrence way" in json.dumps(row).lower():
            row["body"] = "See you at Demo Day — date, time & venue to be confirmed."
            rec["note"] = (rec.get("note", "") + "  TODO: set IAF Demo Day logistics.").strip()
    return rec


def _merge_qa_notes(out):
    try:
        verdicts = json.load(open("s4_qa_verdicts.json"))
    except Exception:
        return 0
    by = {}
    for r in out:
        by.setdefault(str(r["src"]), []).append(r)
    n = 0
    for v in verdicts:
        issue = (v.get("image_issue") or "").strip()
        if not issue or v.get("severity") not in ("minor", "major") or str(v["n"]) in REPLACE:
            continue
        for r in by.get(str(v["n"]), []):
            if not (r.get("image") or r.get("images") or r["arch"] in ("image_full", "image_text", "image_grid")):
                continue
            if issue[:30] not in r.get("note", ""):
                r["note"] = (r.get("note", "") + "  RESHOOT — " + issue).strip(); n += 1
    return n


def main():
    recs = json.load(open(SRC_PATH))
    out = []
    for r in recs:
        s = str(r.get("src"))
        if s in REPLACE:
            out.append(copy.deepcopy(REPLACE[s]))
        elif s in MERGE:
            rr = copy.deepcopy(r); rr.update(MERGE[s]); out.append(rr)
        else:
            rr = copy.deepcopy(r); _apply_subs(rr)
            if s == "56":
                _fix_56(rr)
            out.append(rr)
    qn = _merge_qa_notes(out)
    json.dump(out, open(REC_PATH, "w"), ensure_ascii=False, indent=1)
    print(f"applied {len(REPLACE)} replace, {len(SUBS)} subs, 56-fix, {qn} qa notes -> {len(out)} records")


if __name__ == "__main__":
    main()
