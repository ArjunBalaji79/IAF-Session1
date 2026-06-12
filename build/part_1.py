# slides 1–16
PART = [

    # 1 — V1 title / WiFi
    {"v": 1, "eyebrow": "DISCOVERY DAY · BANGALORE · JUNE 2026",
     "title": "ImpactAI Foundry",
     "subtitle": "Welcome — find a seat, grab breakfast.   WiFi: ImpactAI-Guest   ·   Password: foundry2026"},

    # 2 — V4 facilitators
    {"v": 4, "eyebrow": "WHO WE ARE",
     "title": "Meet your facilitators",
     "col1_head": "Arjun Balaji",
     "col1": ["Co-founder & Program Lead.",
              "",
              "Built ImpactAI Foundry so Bangalore’s NGO sector gets the same operational AI capacity well-resourced organisations take for granted."],
     "col2_head": "Jyothika Raju",
     "col2": ["Co-founder & Program Lead.",
              "",
              "Designs the cohort experience and works with each organisation to turn real workflow problems into tools your team can run."]},

    # 3 — V2 partners & advisors (NO third advisor)
    {"v": 2, "eyebrow": "PARTNERS & ADVISORS",
     "title": "We’re not doing this alone",
     "body": [
         {"lead": "Program partners"},
         "Tech:NYC’s Decoded Futures — the programme we’re modelled on, 220+ nonprofits served in New York.",
         "Bridging Ventures NYC.",
         "",
         {"lead": "Advisors"},
         "Prof. Sarah Holloway (Columbia SIPA) and Rajiv Joshi, advising in their individual capacity.",
         {"text": "Opening doors and pressure-testing our approach.", "c": "mgold"},
     ]},

    # 4 — V2 agenda
    {"v": 2, "eyebrow": "TODAY’S AGENDA",
     "title": "How we’ll spend the day",
     "body_size": 14,
     "body": [
         {"lead": "9:00  —  ", "text": "Arrival, breakfast, introductions."},
         {"lead": "9:30  —  ", "text": "What to expect across the cohort."},
         {"lead": "10:00  —  ", "text": "Session 1 — Prompting & design."},
         {"lead": "11:45  —  ", "text": "Session 2 — Defining AI problems."},
         {"lead": "1:00  —  ", "text": "Lunch."},
         {"lead": "2:00  —  ", "text": "Session 3 — Prototyping your solution."},
         {"lead": "3:45  —  ", "text": "Session 4 — Refining your solution."},
         {"lead": "4:45  —  ", "text": "Show & tell — demo what you built today."},
     ]},

    # 5 — V1 cohort divider
    {"v": 1, "eyebrow": "MEET YOUR COHORT",
     "title": "Eight organisations, one room",
     "subtitle": "Mix across tables — cross-pollination starts now."},

    # 6 — V3 framing quote
    {"v": 3, "eyebrow": "FRAMING",
     "quote": "Hi there. We’re going to spend a lot of time together over the next two months — let’s start with some introductions.",
     "attrib": "A note before we dive in"},

    # 7 — V2 table talk intros
    {"v": 2, "eyebrow": "TABLE TALK · 10 MIN",
     "title": "Let’s start with introductions",
     "body": [
         "Share with your table —",
         "",
         {"lead": "Your name and organisation."},
         {"lead": "Something that excites you — or worries you — about AI."},
         "",
         {"text": "Skepticism is welcome here. Naming a worry is as useful as naming a hope.", "c": "mgold"},
     ]},

    # 8 — V3 premise quote
    {"v": 3, "eyebrow": "WHY THIS, WHY NOW",
     "quote": "You know your work better than anyone in this room. Our job isn’t to tell you what to build — it’s to help you put AI to the work you already do.",
     "attrib": "The premise of the Foundry"},

    # 9 — V2 what's possible
    {"v": 2, "eyebrow": "WHAT’S POSSIBLE",
     "title": "What teams build in a programme like this",
     "body": [
         {"lead": "Build a policy  —  ", "text": "a usable internal AI policy for your org."},
         {"lead": "Automate the admin  —  ", "text": "reclaim hours from repetitive tasks."},
         {"lead": "Create & communicate  —  ", "text": "draft materials and content faster."},
         {"lead": "Answer & assist  —  ", "text": "handle repetitive questions at scale."},
         {"lead": "Learn & decide  —  ", "text": "turn your own data into insight."},
         {"text": "We’re a first cohort, so we’re learning together — but the destination is real, working tools you own and run.", "c": "mgold"},
     ]},

    # 10 — V1 what to expect divider
    {"v": 1, "eyebrow": "COHORT ONE · WHAT TO EXPECT",
     "title": "The next two months",
     "subtitle": "From friction in your day-to-day to a tool you can run."},

    # 11 — V2 learning path
    {"v": 2, "eyebrow": "THE LEARNING PATH",
     "title": "Five phases across four sessions",
     "body_size": 14,
     "body": [
         {"lead": "01  DISCOVER  —  ", "text": "build fluency with prompting; spot AI-shaped problems in your work."},
         {"lead": "02  DEFINE  —  ", "text": "narrow to one workflow; map inputs, steps, success."},
         {"lead": "03  DESIGN  —  ", "text": "build a reusable prototype with your tech mentor; test on real examples."},
         {"lead": "04  REFINE  —  ", "text": "stress-test edge cases; add validation; fit it into your team’s workflow."},
         {"lead": "05  DELIVER  —  ", "text": "Demo Day, August 1; share what you built and what’s next."},
     ]},

    # 12 — V4 Phase 01 DISCOVER
    {"v": 4, "eyebrow": "PHASE 01 · DISCOVER",
     "title": "Ideation & foundational learning",
     "col1_head": "Focus",
     "col1": ["Explore where AI can help and build hands-on fluency before committing to a problem."],
     "col2_head": "Goals",
     "col2": ["Explore high-impact AI use cases",
              "Build fluency with prompting and core tools",
              "Understand AI’s strengths and limits",
              "Spot workflows that feel unclear or manual"]},

    # 13 — V4 Phase 02 DEFINE
    {"v": 4, "eyebrow": "PHASE 02 · DEFINE",
     "title": "Problem scoping & workflow design",
     "col1_head": "Focus",
     "col1": ["Narrow from many ideas to one clear, AI-solvable workflow."],
     "col2_head": "Goals",
     "col2": ["Narrow to one workflow — your MVP",
              "Break the work into steps",
              "Define inputs, constraints, stakeholders",
              "Describe what success looks like, and how you’ll judge it"]},

    # 14 — V4 Phase 03 DESIGN
    {"v": 4, "eyebrow": "PHASE 03 · DESIGN",
     "title": "Building & testing the prototype",
     "col1_head": "Focus",
     "col1": ["Turn the scoped workflow into a reusable AI prototype."],
     "col2_head": "Goals",
     "col2": ["Build a reusable prototype aligned to the workflow",
              "Apply structured prompting and context-setting",
              "Test against real examples",
              "Compare outputs to your success criteria and refine"]},

    # 15 — V4 Phase 04 REFINE
    {"v": 4, "eyebrow": "PHASE 04 · REFINE",
     "title": "Testing the prototype for success",
     "col1_head": "Focus",
     "col1": ["Make it consistent, reliable, and ready for real use."],
     "col2_head": "Goals",
     "col2": ["Strengthen consistency through testing",
              "Find edge cases and failure modes",
              "Add validation steps",
              "Clarify how it fits your team’s decisions and workflow"]},

    # 16 — V4 Phase 05 DELIVER
    {"v": 4, "eyebrow": "PHASE 05 · DELIVER",
     "title": "Presenting & sharing impact",
     "col1_head": "Focus",
     "col1": ["Show what you built and how it changes the work."],
     "col2_head": "Goals",
     "col2": ["Present the workflow, prototype, and evidence of impact",
              "Share how you measured success",
              "Outline next steps for adoption and iteration"]},

]
