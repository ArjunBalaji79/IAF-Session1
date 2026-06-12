# slides 34–48
PART = [
    # 34 — V1 divider into Session 2
    {"v": 1, "eyebrow": "SESSION TWO · 11:45 AM",
     "title": "Defining AI problems",
     "subtitle": "The friction in your work is the starting point — not the tool."},

    # 35 — V2 bring the prompting skill forward
    {"v": 2, "eyebrow": "BRINGING IT FORWARD",
     "title": "You already know how to build a prompt",
     "body": [
         {"runs": [
             {"t": "You’ve got the three parts — ", "c": "navy"},
             {"t": "Role & Goal, Steps & Context, Output", "b": True, "c": "terra"},
             {"t": ".", "c": "navy"}]},
         "Now we point them at a real problem worth solving.",
         "",
         {"text": "Good prompts start with a well-defined problem. That’s what this session is about.", "c": "mgold"},
     ]},

    # 36 — V2 the AI Design Workflow, five steps
    {"v": 2, "eyebrow": "THE AI DESIGN WORKFLOW",
     "title": "Five steps, in order, every time",
     "body": [
         {"lead": "01  Define the problem  —  ", "text": "name the friction in concrete terms."},
         {"lead": "02  Describe the current workflow  —  ", "text": "who does what, when, with what info."},
         {"lead": "03  Clarify the output  —  ", "text": "what does “done” look like, in a form you can hold?"},
         {"lead": "04  Define success  —  ", "text": "three to five things that tell you the result is good."},
         {"lead": "05  Prototype, test, iterate  —  ", "text": "refine the prompt, not the output."},
     ]},

    # 37 — V3 start-here prompt
    {"v": 3, "eyebrow": "START HERE",
     "quote": "What part of your work feels repetitive, slow, or more manual than it should be?",
     "attrib": "That feeling is your starting point"},

    # 38 — V2 Step 01, define the problem template
    {"v": 2, "eyebrow": "STEP 01 · DEFINE THE PROBLEM · 10 MIN",
     "title": "Name your pain point",
     "body": [
         "Fit a challenge into this template —",
         "",
         {"lead": "My pain point at work is that I spend time ", "text": "(specific task)."},
         {"lead": "If I could reduce or change this by ", "text": "(specific improvement),"},
         {"lead": "I would gain ", "text": "(time, quality, or clarity impact)."},
         "",
         {"text": "Big challenges and small ones both count — a fundraising goal, or one type of email.", "c": "mgold"},
     ]},

    # 39 — V4 weak vs strong framing
    {"v": 4, "eyebrow": "PROBLEM IDENTIFICATION",
     "title": "Weak vs strong framing",
     "col1_head": "Weak",
     "col1": ["“My pain point is that I spend too much time trying to raise money. If I could fix this by getting more money, I’d gain greater impact.”",
              "",
              "A real problem — but not one AI can directly solve. Specificity is missing."],
     "col2_head": "Strong",
     "col2": ["“I spend hours answering repetitive enquiries about our programmes each week. If I automated even half, I’d gain ~5 hours a week for higher-value work.”",
              "",
              "Specific task, specific change, measurable gain."]},

    # 40 — V2 Step 01 second pass, make it sharper
    {"v": 2, "eyebrow": "STEP 01 · A SECOND PASS · 10 MIN",
     "title": "Make it sharper",
     "body": [
         "Push on your own framing —",
         "",
         {"lead": "Can AI actually touch this", "text": " — or is it a resourcing problem in disguise?"},
         "The more specific the task, the more solvable it becomes.",
         "",
         {"text": "Rewrite your pain point until a colleague could act on it without asking you a question.", "c": "mgold"},
     ]},

    # 41 — V3 from problem to solution type
    {"v": 3, "eyebrow": "NICE WORK",
     "quote": "Great — you’ve identified a problem. So how do we know whether AI can actually solve it?",
     "attrib": "From problem to solution type"},

    # 42 — V2 the five solution types overview
    {"v": 2, "eyebrow": "THE FIVE SOLUTION TYPES",
     "title": "Where AI actually fits",
     "body": [
         {"lead": "Answer & Assist  —  ", "text": "“I get a lot of questions and can’t keep up.”"},
         {"lead": "Automate the Admin  —  ", "text": "“I keep doing the same task over and over.”"},
         {"lead": "Create & Communicate  —  ", "text": "“I need to write or make something to share.”"},
         {"lead": "Sort & Scan  —  ", "text": "“I spend too long reviewing things that follow a pattern.”"},
         {"lead": "Learn & Decide  —  ", "text": "“I want insight to make a smarter choice.”"},
     ]},

    # 43 — V4 Solution Type 01: Answer & Assist
    {"v": 4, "eyebrow": "SOLUTION TYPE · 01",
     "title": "Answer & Assist",
     "col1_head": "Sounds like",
     "col1": ["“I get a lot of questions and can’t keep up with answering them all.”"],
     "col2_head": "Examples",
     "col2": ["Handling repetitive enquiries from constituents",
              "Answering staff questions about a new HR policy",
              "A first-line FAQ for your programmes"]},

    # 44 — V4 Solution Type 02: Automate the Admin
    {"v": 4, "eyebrow": "SOLUTION TYPE · 02",
     "title": "Automate the Admin",
     "col1_head": "Sounds like",
     "col1": ["“I keep doing the same tasks over and over, and it’s taking time from more important work.”"],
     "col2_head": "Examples",
     "col2": ["Cross-checking volunteer timesheets across spreadsheets",
              "Scanning receipts for expense reports",
              "Reformatting data from one layout to another"]},

    # 45 — V4 Solution Type 03: Create & Communicate
    {"v": 4, "eyebrow": "SOLUTION TYPE · 03",
     "title": "Create & Communicate",
     "col1_head": "Sounds like",
     "col1": ["“I need to write or create something to share with others.”"],
     "col2_head": "Examples",
     "col2": ["Drafting blog posts and newsletters",
              "Building volunteer training materials",
              "Generating a simple programme webpage"]},

    # 46 — V4 Solution Type 04: Sort & Scan
    {"v": 4, "eyebrow": "SOLUTION TYPE · 04",
     "title": "Sort & Scan",
     "col1_head": "Sounds like",
     "col1": ["“I spend too much time reviewing information that follows a pattern.”"],
     "col2_head": "Examples",
     "col2": ["Ranking volunteer or grant applications",
              "Triaging incoming requests",
              "Reviewing submissions against a rubric"]},

    # 47 — V4 Solution Type 05: Learn & Decide
    {"v": 4, "eyebrow": "SOLUTION TYPE · 05",
     "title": "Learn & Decide",
     "col1_head": "Sounds like",
     "col1": ["“I want to learn something new, or need better insight to make smarter choices.”"],
     "col2_head": "Examples",
     "col2": ["Analysing qualitative survey data about your programmes",
              "Planning whether to expand to a new area",
              "Summarising a long report into a decision"]},

    # 48 — V2 Table Talk, which type is yours
    {"v": 2, "eyebrow": "TABLE TALK · 5 MIN",
     "title": "Which type is yours?",
     "body": [
         "Run your problem against the five —",
         "",
         {"lead": "Answer & Assist · Automate the Admin · Create & Communicate · Sort & Scan · Learn & Decide."},
         "",
         "Discuss with your table which category each of your problems fits, and why.",
     ]},
]
