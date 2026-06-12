# Content Schema — how to write slide dicts for deckbuild.py

You are authoring Python dicts that `deckbuild.py` turns into finished slides.
Each slide is ONE dict. Your file defines a list named `PART`. Do **not** build
the deck or import deckbuild — just produce data.

## Hard rules (read twice)
- **FORBIDDEN words — must NEVER appear anywhere:** `Mohit`, `Mohit Jain`,
  `Microsoft`, `Microsoft Research`, `MSR`, `MSR India`. Advisors are ONLY
  **Prof. Sarah Holloway (Columbia SIPA)** and **Rajiv Joshi**.
- Partners are ONLY **Tech:NYC's Decoded Futures** and **Bridging Ventures NYC**.
- Facts: 8 Bangalore NGOs · June–July 2026 · 4 sessions · dedicated tech mentors ·
  Demo Day **August 1, 2026** · website **impactaifoundry.com** · facilitators
  **Arjun Balaji** and **Jyothika Raju**.
- Tone: collaborative, warm, never evaluative. They are partners we invited.
- Use straight apostrophes are fine, but curly quotes “ ” ‘ ’ read better — use
  curly quotes/apostrophes in user-facing copy (’ not ').
- Keep text within the slot — V2 body ≈ up to ~6 short lines; V4 column body
  ≈ up to ~4 short lines or one short paragraph. Be concise.
- Do NOT set the brand label or page number — the builder does that.

## The dict, by variant

Every dict has `"v"` (1–4) and `"eyebrow"` (ALL CAPS short kicker string).

### V1 — centered divider / title
```python
{"v": 1, "eyebrow": "SESSION ONE · 10:00 AM",
 "title": "Prompting and design",
 "subtitle": "The shortest path from blank prompt to useful output."}
```

### V3 — featured quote / single idea
```python
{"v": 3, "eyebrow": "SAVE THE DATE",
 "quote": "Demo Day — August 1, 2026. Each organisation presents a working tool you’ve built and the workflow it transforms.",
 "attrib": "The destination we’re building toward together"}
```

### V2 — workhorse content block (`body` = list of paragraph items)
```python
{"v": 2, "eyebrow": "THE AI DESIGN WORKFLOW",
 "title": "Five steps, in order, every time",
 "body": [
   {"lead": "01  Define the problem  —  ", "text": "name the friction in concrete terms."},
   {"lead": "02  Describe the current workflow  —  ", "text": "who does what, when, with what info."},
   {"lead": "03  Clarify the output  —  ", "text": "what does “done” look like, in a form you can hold?"},
   {"lead": "04  Define success  —  ", "text": "three to five things that tell you the result is good."},
   {"lead": "05  Prototype, test, iterate  —  ", "text": "refine the prompt, not the output."},
 ]}
```

### V4 — two columns (`col1`/`col2` = list of paragraph items)
```python
{"v": 4, "eyebrow": "PROBLEM IDENTIFICATION",
 "title": "Weak vs strong framing",
 "col1_head": "Weak",
 "col1": ["“My pain point is that I spend too much time trying to raise money…”",
          "", "A real problem — but not one AI can directly solve."],
 "col2_head": "Strong",
 "col2": ["“I spend hours answering repetitive enquiries each week. If I automated half, I’d gain ~5 hours.”",
          "", "Specific task, specific change, measurable gain."]}
```
(col1 heading auto-renders terracotta; col2 heading auto-renders green.)

## Paragraph items — the mini-language (used inside `body`, `col1`, `col2`)
Each list element is ONE of:
- `""`  → a blank spacer line (use between groups for breathing room).
- `"plain string"` → one line, Calibri, navy (body) / column color.
- `{"lead": "Bold label — ", "text": "rest of the line."}`
  → `lead` renders Georgia **bold terracotta**, `text` renders Calibri navy.
  This is the dominant pattern for numbered/labelled lists. Optional:
  `"lead_c": "navy"|"green"|...` to recolor the lead; `"c": "mgold"` to recolor text.
- `{"text": "A softer closing note.", "c": "mgold"}`
  → muted-gold note line. Use for the reflective closer the reference decks put
  at the bottom of many content slides.
- Full control: `{"runs": [{"t": "We’ll teach you a ", "c": "navy"},
  {"t": "design-thinking approach", "b": true, "c": "terra"},
  {"t": " to spotting where AI fits.", "c": "navy"}]}`
  → arbitrary inline bold/color. `t`=text, `b`=bold, `c`=color, `font`,`size`,`i`(italic).
  Colors: `"navy" "terra" "gold" "mgold" "green"`.

### Optional per-slide sizing
- V2: add `"body_size": 14` (default 15) for text-heavy slides; `17` for sparse ones.
- V4: add `"col_size": 13` (default 13).

## Style patterns to follow (from the finished reference deck)
- Numbered lists: `{"lead": "01  Title  —  ", "text": "explanation."}`.
- Sub-section headers inside a V2 body: a `{"lead": "Program partners"}` line
  (lead only, no text) followed by a plain paragraph, a `""`, then the next header.
- Many content slides END with a muted-gold takeaway: `{"text": "…", "c": "mgold"}`.
- Quotes in examples use curly quotes “ ”. Em dash — with spaces around it.
- Titles: sentence case, no terminal period. Eyebrows: ALL CAPS, use ` · ` to join
  (e.g. `"SESSION TWO · 11:45 AM"`, `"TABLE TALK · 10 MIN"`).

## Output format (exactly this)
Write a file `PART = [ ... ]` — a Python list of the dicts for your assigned
slide range, **in order**. First line a comment with the range, e.g. `# slides 1–16`.
Then self-check: `python3 -c "import part_N as m; print(len(m.PART))"` equals your
slide count, and grep your file for the forbidden words (must be zero hits).
