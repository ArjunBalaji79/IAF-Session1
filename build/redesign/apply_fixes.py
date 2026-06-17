"""Apply QA + structural fixes to deck_records.json -> deck_records.json (in place).

Supports three patch kinds keyed by source slide id (string):
  REPLACE[src]  -> full replacement record (single)
  MERGE[src]    -> shallow-merge dict into the existing record
  SPLIT[src]    -> list of records that REPLACE the single src record (dense split)
"""
import json, copy

SRC_PATH = "deck_records_raw.json"   # pristine workflow output
REC_PATH = "deck_records.json"       # built deck reads this

# ---- full replacements -------------------------------------------------
REPLACE = {
    "2": {  # team names/roles were hidden in a note -> visible team archetype
        "src": "2", "arch": "team", "eyebrow": "WHO WE ARE", "title": "Meet the team",
        "people": [
            {"name": "Arjun Balaji", "role": "Co-founder & Program Lead",
             "sub": "MPA at Columbia University", "photo": "image12.jpg"},
            {"name": "Jyothika Raju", "role": "Co-founder & Program Lead",
             "sub": "MPA at Columbia University", "photo": "image13.png"},
            {"name": "Monish Raman", "role": "Creative Director",
             "sub": "MSCE at New York University", "photo": "image24.jpg"},
        ],
    },
    "55": {  # image62 letterboxes empty; use the real Projects screenshot
        "src": "55", "arch": "image_full", "eyebrow": "PROJECTS",
        "image": "image41.png", "dark": False,
    },
    "57": {  # image62 empty; use the real screenshot, drop invented body line
        "src": "57", "arch": "image_full", "eyebrow": "GRANT APPLICATIONS",
        "image": "image51.png", "dark": False,
    },
    "75": {  # bars mangled the long labels -> clean spectrum list (verbatim-faithful)
        "src": "75", "arch": "bullets", "eyebrow": "SPECTRUM OF CAUTION",
        "title": "Spectrum of Caution",
        "intro": "From most cautious to “live dangerously” — how much access you hand the tool:",
        "bullets": [
            "Don’t use it at all.",
            "Use it in the browser — it can’t access your computer.",
            "On your computer, low permissions — don’t approve anything, just observe.",
            "On your computer, medium permissions — review every approval.",
            "On your computer, lots of permissions — approve most things. YOLO!",
        ],
    },
}

# ---- shallow merges ----------------------------------------------------
MERGE = {
    "36": {"visual": "none"},   # full-width card; drop laptop so 4 lines + Q fit
    "77": {  # too much for the card + truncated "…"; tighten faithfully, drop laptop
        "visual": "none",
        "title": "Help me sort these applications",
        "card": [
            "ROLE & GOAL — You are an expert hiring manager helping me assess the technologists in this spreadsheet.",
            "STEPS — Score each volunteer on their technology skills, and on how many mentorship / advising roles they hold.",
        ],
        "question": "Create a visualization of this scored list I can run in my browser — let me sort and filter by all relevant fields.",
    },
    "15": {"note": "ugly-image — image16.png (Claude wordmark) doesn’t match the “Nano Banana” text-to-image example in the bullets; swap for an actual generated-image example on reshoot."},
    "50": {"note": "ugly-image — replace the thumbnails with clean, on-brand Create & Communicate examples (drafted newsletter, training doc, simple webpage) at a consistent crop."},
}

# ---- dense splits (one src -> several records) -------------------------
SPLIT = {
    "59": [
        {"src": "59a", "arch": "exercise", "eyebrow": "BUILDING A PROJECT · 10 MIN",
         "title": "The Organization Knowledge Base",
         "card": [
             "Build a Claude Project for your organisation.",
             "Step 1 — Start a new Claude Project and upload a document your team uses regularly. (No document? Use your website copy, an old annual report, or your programme brochure.)",
             "Step 2 — Write a system prompt telling Claude to only answer questions using that document.",
         ],
         "question": "Example: “You are a helpful assistant for [org name]. Answer questions only using the materials provided. If the answer isn’t in the document, say so.”"},
        {"src": "59b", "arch": "exercise", "eyebrow": "BUILDING A PROJECT · CONTINUED",
         "title": "The Organization Knowledge Base",
         "card": [
             "Step 3 — Try asking it:",
             "“What does our organisation do?”",
             "“Who are our beneficiaries?”",
             "“What did we achieve last year?”",
         ],
         "question": "The goal: can a new volunteer or donor understand your work just by chatting with this assistant? Could your team use it instead of digging through folders?"},
    ],
    "67": [
        {"src": "67a", "arch": "exercise", "eyebrow": "CODE · TRANSFORMING DATA",
         "title": "Build your ideal data interface",
         "card": [
             "Drag a data file you already use into the chat — beneficiary records, volunteer attendance, programme reach, anything you track in a spreadsheet.",
             "Ask Claude to show you that data the way you actually want to see it:",
             "• How do you wish you could see this information?",
             "• Which numbers matter most to your team or funders?",
             "• How would you want to look at it — graphs, filters, sorting by district or programme?",
         ]},
        {"src": "67b", "arch": "exercise", "eyebrow": "CODE · TRANSFORMING DATA",
         "title": "Build your ideal data interface",
         "card": [
             "Example prompt —",
             "“Can you look at our beneficiary data and make an interactive dashboard I can open in my browser, with a map by district and a breakdown by programme type?”",
         ],
         "question": "No data handy? Use your organisation’s public annual-report numbers, or ask Claude to generate sample data that looks like yours so you can test the interface first."},
    ],
}


def _merge_qa_image_notes(out):
    """Append every QA-flagged image issue into the matching slide's speaker note,
    so the user gets a complete 'reshoot' list (their 'flag uglies' choice)."""
    try:
        verdicts = json.load(open("qa_verdicts.json"))
    except Exception:
        return 0
    by_src = {}
    for r in out:
        by_src.setdefault(str(r["src"]), []).append(r)
    added = 0
    for v in verdicts:
        issue = (v.get("image_issue") or "").strip()
        # only carry genuine problems; skip slides already fixed via REPLACE
        if not issue or v.get("severity") not in ("minor", "major"):
            continue
        if str(v["n"]) in REPLACE:
            continue
        recs = by_src.get(str(v["n"]), [])
        for r in recs:
            if not (r.get("image") or r.get("images") or r["arch"] in
                    ("image_full", "image_text", "image_grid")):
                continue
            note = r.get("note", "")
            flag = "RESHOOT — " + issue
            if issue[:30] not in note:
                r["note"] = (note + "  " + flag).strip() if note else flag
                added += 1
    return added


def main():
    recs = json.load(open(SRC_PATH))
    out = []
    for r in recs:
        src = str(r.get("src"))
        if src in SPLIT:
            out.extend(copy.deepcopy(SPLIT[src]))
        elif src in REPLACE:
            out.append(copy.deepcopy(REPLACE[src]))
        elif src in MERGE:
            rr = copy.deepcopy(r); rr.update(MERGE[src]); out.append(rr)
        else:
            out.append(r)
    notes_added = _merge_qa_image_notes(out)
    json.dump(out, open(REC_PATH, "w"), ensure_ascii=False, indent=1)
    print(f"applied: {len(REPLACE)} replace, {len(MERGE)} merge, {len(SPLIT)} split, "
          f"{notes_added} image notes -> {len(out)} records (was {len(recs)})")


if __name__ == "__main__":
    main()
