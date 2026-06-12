# slides 17–33
PART = [
    # 17 — V2 · THE WHOLE ARC · Where it all leads
    {"v": 2, "eyebrow": "THE WHOLE ARC",
     "title": "Where it all leads",
     "body": [
         "Five phases. Four in-person sessions. One destination —",
         "",
         {"runs": [
             {"t": "at least one working internal tool", "b": True, "c": "terra"},
             {"t": ", built by your team, for your team.", "c": "navy"},
         ]},
         "",
         {"text": "Every session returns to these phases. You’ll always know where you are.", "c": "mgold"},
     ]},

    # 18 — V3 · SAVE THE DATE · Demo Day quote
    {"v": 3, "eyebrow": "SAVE THE DATE",
     "quote": "Demo Day — August 1, 2026. Each organisation presents a working tool you’ve built and the workflow it transforms.",
     "attrib": "The destination we’re building toward together"},

    # 19 — V2 · WHAT WE'RE LEARNING ABOUT AI · Fluency takes time
    {"v": 2, "eyebrow": "WHAT WE’RE LEARNING ABOUT AI",
     "title": "Fluency takes time",
     "body": [
         {"lead": "Building fluency takes time  —  ", "text": "nobody walks in fluent; that’s the point of two months."},
         "",
         {"lead": "You learn best by doing  —  ", "text": "we build more than we lecture."},
         "",
         {"lead": "The fun comes in iterating  —  ", "text": "the second and third tries are where it gets good."},
     ]},

    # 20 — V1 · BEFORE WE BUILD · A quick word on ethics
    {"v": 1, "eyebrow": "BEFORE WE BUILD",
     "title": "A quick word on ethics",
     "subtitle": "Guardrails first — then we experiment freely."},

    # 21 — V3 · THE LANDSCAPE · navigating a new frontier
    {"v": 3, "eyebrow": "THE LANDSCAPE",
     "quote": "We’re navigating a new frontier together. None of us has all the answers yet — and that’s exactly why we start by agreeing on how we’ll move.",
     "attrib": "Why ethics comes first"},

    # 22 — V1 · AI ETHICS · You're in control
    {"v": 1, "eyebrow": "AI ETHICS",
     "title": "You’re in control",
     "subtitle": "Adopt AI in the way that’s right for your organisation."},

    # 23 — V2 · THREE GUARDRAILS · Build with care, but build
    {"v": 2, "eyebrow": "THREE GUARDRAILS",
     "title": "Build with care, but build",
     "body_size": 14,
     "body": [
         {"lead": "01  Protect personal information  —  ", "text": "free AI tools aren’t private by default. Beneficiary and donor data stays out unless the platform is secure and configured for it."},
         {"lead": "02  Keep a human in the loop  —  ", "text": "until you fully understand how a tool behaves on your work, review outputs before relying on them."},
         {"lead": "03  Customise for your community  —  ", "text": "out-of-the-box AI doesn’t reflect every context. Adapt it to truly serve the people you serve."},
         "",
         {"text": "… but don’t let these get in the way of getting started.", "c": "mgold"},
     ]},

    # 24 — V1 · SESSION ONE · 10:00 AM · Prompting and design
    {"v": 1, "eyebrow": "SESSION ONE · 10:00 AM",
     "title": "Prompting and design",
     "subtitle": "The shortest path from blank prompt to useful output."},

    # 25 — V2 · QUICK PROMPT · 15 MIN · Ask AI to solve a real work problem
    {"v": 2, "eyebrow": "QUICK PROMPT · 15 MIN",
     "title": "Ask AI to solve a real work problem",
     "body": [
         "Open the AI tool of your choice. Type a real problem you’re facing at work in plain language — no technique yet, no structure.",
         "",
         {"runs": [
             {"t": "There is no single ", "c": "navy"},
             {"t": "“right” prompt.", "b": True, "c": "terra"},
             {"t": " Type anything. Revise as many times as you want.", "c": "navy"},
         ]},
         "",
         {"text": "The point is to feel the raw experience first — we’ll add structure next.", "c": "mgold"},
     ]},

    # 26 — V2 · TABLE TALK · 10 MIN · Reflect on that first attempt
    {"v": 2, "eyebrow": "TABLE TALK · 10 MIN",
     "title": "Reflect on that first attempt",
     "body": [
         {"lead": "What did the model ask you?"},
         {"lead": "What did it recommend?"},
         {"lead": "What was unexpected?"},
         {"lead": "What could be improved?"},
     ]},

    # 27 — V3 · THE TEACHING CORE · what patterns make a prompt work better
    {"v": 3, "eyebrow": "THE TEACHING CORE",
     "quote": "What patterns make a prompt work better?",
     "attrib": "From a messy first try to a repeatable structure"},

    # 28 — V2 · PROMPTING IN THREE PARTS · Role, steps, output
    {"v": 2, "eyebrow": "PROMPTING IN THREE PARTS",
     "title": "Role, steps, output",
     "body_size": 14,
     "body": [
         {"lead": "01  Give it a role and a goal"},
         {"runs": [{"t": "“You are a fundraising communications specialist. Your objective is to draft donor thank-you emails.”", "i": True, "c": "navy"}]},
         "",
         {"lead": "02  List the steps and context"},
         {"runs": [{"t": "“To complete this, follow these steps: Step 1… Step 2… Step 3…”", "i": True, "c": "navy"}]},
         "",
         {"lead": "03  Describe the final output"},
         {"runs": [{"t": "“When you’re done, give me a summary paragraph and three bullet points of next steps.”", "i": True, "c": "navy"}]},
     ]},

    # 29 — V2 · RE-RUN · 10 MIN · Try your prompt again, with structure
    {"v": 2, "eyebrow": "RE-RUN · 10 MIN",
     "title": "Try your prompt again, with structure",
     "body": [
         "Start a fresh conversation. Re-ask using",
         {"runs": [
             {"t": "Role & Goal → Steps & Context → Output.", "b": True, "c": "terra"},
         ]},
         "",
         {"text": "You’re refining your prompt — not trying to perfect the output. The contrast with your first try is the lesson.", "c": "mgold"},
     ]},

    # 30 — V2 · TABLE TALK · 10 MIN · What changed?
    {"v": 2, "eyebrow": "TABLE TALK · 10 MIN",
     "title": "What changed?",
     "body": [
         {"lead": "Role & Goal  —  ", "text": "where did you define the model’s expertise or purpose?"},
         {"lead": "Steps & Context  —  ", "text": "where did you guide how it works with you?"},
         {"lead": "Output  —  ", "text": "where did you specify what “done” looks like?"},
         "",
         "Which part was hardest to make explicit, and why?",
     ]},

    # 31 — V1 · PAUSE · Break — 15 minutes
    {"v": 1, "eyebrow": "PAUSE",
     "title": "Break — 15 minutes",
     "subtitle": "Stretch, refill, compare notes. Back at the top of the hour."},

    # 32 — V2 · TOOL TIPS & TRICKS · Make the tools work for you
    {"v": 2, "eyebrow": "TOOL TIPS & TRICKS",
     "title": "Make the tools work for you",
     "body": [
         {"lead": "Privacy & data controls  —  ", "text": "find where to turn off model training on your data. Critical for NGOs handling sensitive beneficiary information."},
         "",
         {"lead": "Attachments, web search, tools  —  ", "text": "see what the input bar can actually do."},
         "",
         {"text": "Free tools aren’t private by default — we’ll come back to this in the ethics of your real workflows.", "c": "mgold"},
     ]},

    # 33 — V2 · TOOL TIPS & TRICKS · A few habits that pay off
    {"v": 2, "eyebrow": "TOOL TIPS & TRICKS",
     "title": "A few habits that pay off",
     "body": [
         {"lead": "Save your best prompts  —  ", "text": "reuse beats rewriting."},
         "",
         {"lead": "Iterate in the same chat  —  ", "text": "give feedback instead of starting over."},
         "",
         {"lead": "Be specific about format  —  ", "text": "tell it the shape of the answer you want."},
         "",
         {"text": "Small habits compound across a two-month build.", "c": "mgold"},
     ]},
]
