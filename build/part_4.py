# slides 49–62
PART = [

    # 49 — V3 principle aside
    {"v": 3, "eyebrow": "A QUICK ASIDE",
     "quote": "The right tool follows the problem — never the other way round. Name the work first; the technology second.",
     "attrib": "Keep the order straight"},

    # 50 — V4 progress recap (step 1 done)
    {"v": 4, "eyebrow": "THE AI DESIGN WORKFLOW",
     "title": "Step 1 down — four to go",
     "col1_head": "Done",
     "col1": ["01  Define the problem  ✓"],
     "col2_head": "Up next",
     "col2": ["02  Describe the current workflow",
              "03  Clarify the output",
              "04  Define success",
              "05  Prototype, test, iterate"]},

    # 51 — V2 Step 02 describe the workflow
    {"v": 2, "eyebrow": "STEP 02 · DESCRIBE THE WORKFLOW · 10 MIN",
     "title": "How do you do it today?",
     "body": [
         "Describe how the process runs now —",
         "",
         {"lead": "Who does what?  ", "text": "When do steps happen, and what relies on the step before?"},
         {"lead": "What information moves it forward?"},
         "",
         {"text": "Then map those steps into the “Steps” of your prompt.", "c": "mgold"},
     ]},

    # 52 — V4 progress recap (steps 1–2 done)
    {"v": 4, "eyebrow": "THE AI DESIGN WORKFLOW",
     "title": "Two down — keep going",
     "col1_head": "Done",
     "col1": ["01  Define the problem  ✓",
              "02  Describe the current workflow  ✓"],
     "col2_head": "Up next",
     "col2": ["03  Clarify the output",
              "04  Define success",
              "05  Prototype, test, iterate"]},

    # 53 — V2 Step 03 clarify the output
    {"v": 2, "eyebrow": "STEP 03 · CLARIFY THE OUTPUT · 10 MIN",
     "title": "What does “done” look like?",
     "body": [
         {"runs": [{"t": "Define the ", "c": "navy"},
                   {"t": "output", "b": True, "c": "terra"},
                   {"t": " for your prompt. ", "c": "navy"},
                   {"t": "Think how you’d brief a new hire.", "b": True, "c": "terra"}]},
         "",
         "It could be an answer, a document, an image, a spreadsheet — be concrete about the shape.",
         "",
         {"text": "If you can picture the finished thing, you can describe it to the model.", "c": "mgold"},
     ]},

    # 54 — V4 progress recap (steps 1–3 done)
    {"v": 4, "eyebrow": "THE AI DESIGN WORKFLOW",
     "title": "Three down — almost there",
     "col1_head": "Done",
     "col1": ["01  Define the problem  ✓",
              "02  Describe the current workflow  ✓",
              "03  Clarify the output  ✓"],
     "col2_head": "Up next",
     "col2": ["04  Define success",
              "05  Prototype, test, iterate"]},

    # 55 — V2 Step 04 define success
    {"v": 2, "eyebrow": "STEP 04 · DEFINE SUCCESS · 10 MIN",
     "title": "How will you know it’s good?",
     "body": [
         "This isn’t part of the prompt itself — but it’s how you’ll judge every result.",
         "",
         {"lead": "Write 3–5 things that would tell you the output is “good.”"},
         "",
         {"text": "The same standard you’d hold a new employee to.", "c": "mgold"},
     ]},

    # 56 — V3 the fun part (bridge into lunch / step 5)
    {"v": 3, "eyebrow": "THE FUN PART",
     "quote": "You should now have a draft prompt — or be on your way. After lunch, we run it, judge it against your success criteria, and start to iterate.",
     "attrib": "Step 5 — we pick this up at 2:00"},

    # 57 — V1 lunch divider
    {"v": 1, "eyebrow": "BREAK",
     "title": "Lunch — see you at 2:00",
     "subtitle": "Eat, talk, let the problem breathe. We pick up with prototyping."},

    # 58 — V3 prompt cookbook
    {"v": 3, "eyebrow": "A RUNNING START",
     "quote": "Welcome to the Prompt Cookbook — ready-to-use prompts organised by the five solution types, so you never start from a blank page.",
     "attrib": "impactaifoundry.com/cookbook"},

    # 59 — V1 Session 3 divider
    {"v": 1, "eyebrow": "SESSION THREE · 2:00 PM",
     "title": "Prototyping your solution",
     "subtitle": "By the end of this session, you should have something you can run."},

    # 60 — V2 prototyping steps
    {"v": 2, "eyebrow": "PROTOTYPING · 85 MIN",
     "title": "Build your custom solution",
     "body": [
         {"lead": "01  —  ", "text": "Make sure your problem from this morning feels specific."},
         {"lead": "02  —  ", "text": "(Optional) If you’re stuck, grab a cookbook prompt and iterate on that."},
         {"lead": "03  —  ", "text": "Iterate on the prompt to build your custom solution."},
         {"lead": "04  —  ", "text": "(Optional, advanced) Try a Custom GPT or a saved project."},
         {"text": "Mentors are circulating — every team has hands-on support.", "c": "mgold"},
     ]},

    # 61 — V3 mid-session check-in
    {"v": 3, "eyebrow": "MID-SESSION CHECK-IN · 15 MIN",
     "quote": "What’s working? What’s challenging?",
     "attrib": "Surface a blocker — someone else in the room has hit it too"},

    # 62 — V2 run the test
    {"v": 2, "eyebrow": "RUN THE TEST",
     "title": "Judge it against your success criteria",
     "body": [
         "Use the 3–5 things you wrote in Step 4 —",
         "",
         {"lead": "What works?  What doesn’t?  What surprised you?"},
         "",
         "Then change the prompt to close the gap.",
         {"text": "You’re refining the prompt, not hand-fixing the output.", "c": "mgold"},
     ]},

]
