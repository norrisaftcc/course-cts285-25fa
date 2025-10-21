# ORANGE-01: WEB INTERFACE DEPLOYMENT

## AlgoCratic Futures™ Educational Initiative

**CLEARANCE LEVEL:** ORANGE  
**ESTIMATED VELOCITY:** 4-6 hours  
**PREREQUISITE:** Functional Datamon console application

-----

## MISSION BRIEF

Your Datamon Answer Checker currently exists only in the terminal, limiting its reach and impact on algorithmic harmony. The Algorithm™ has determined that web accessibility increases productivity metrics by 347%. Your mission: deploy a web interface that allows any authorized resource to verify their Datamon answers through their browser.

**Important Growth Opportunity:** This assignment introduces “vibe coding” - using AI assistants to rapidly prototype web interfaces. This technique has both remarkable power and significant limitations. You will experience both.

-----

## PART ONE: FRAMEWORK INVESTIGATION (30 minutes)

### Objective

Evaluate two Python web frameworks and select one for your deployment.

### Your Task

1. **Research Phase** (15 minutes)
- Investigate Flask and Streamlit
- Focus on: ease of use, deployment simplicity, and suitability for small tools
- Use official documentation, not just AI summaries
1. **Decision Phase** (15 minutes)
- Create a brief comparison document (bullet points fine)
- Make and justify your framework choice
- Document your reasoning - you’ll need this later

### Deliverable

A markdown file `FRAMEWORK_DECISION.md` containing:

- Key differences you discovered
- Your choice and why
- One anticipated challenge with your chosen framework

**Rubric:**

- ✅ Consulted actual documentation (not just ChatGPT summaries)
- ✅ Identified 3+ meaningful differences
- ✅ Reasoning connects to your specific use case
- ✅ Shows awareness of tradeoffs

-----

## PART TWO: VIBE CODING DEPLOYMENT (3-5 hours)

### Objective

Use AI-assisted development to create a functional web interface for your Answer Checker.

### The “Vibe Coding” Technique

You will use AI (Claude, ChatGPT, GitHub Copilot) to generate most of your web interface code. This is INTENTIONAL. We’re teaching you to work with AI as a development tool, not replacing learning with AI.

**The Critical Lesson:** Vibe coding is powerful for rapid prototyping but has a ceiling. You’ll hit it. This is expected. Your job is to recognize when you’ve hit it and adapt your strategy.

### Your Task

1. **Initial Prompt Engineering** (30 minutes)
- Craft prompts to generate your web interface
- Start simple: “Build a Flask/Streamlit app that accepts datamon and answer inputs”
- Test the generated code
- Iterate on your prompts based on results
1. **Iteration & Integration** (2-3 hours)
- Get a basic interface working
- Integrate your existing answer-checking logic
- Add error handling (AI often forgets this)
- Test with multiple datamon/answer combinations
- Keep track of how many iterations you need
1. **Styling & Polish** (1 hour)
- Make it not look terrible
- Add basic instructions for users
- Ensure error messages are helpful
1. **Reflection** (30 minutes)
- Document where AI helped
- Document where AI struggled or failed
- Note when you had to intervene manually
- Record your iteration count

### Deliverables

1. **Working Web Application**
- Accepts datamon input (text or upload)
- Accepts answer input
- Returns correct/incorrect with explanation
- Handles errors gracefully
- Runs locally without crashes
1. **ITERATION_LOG.md**
- Your prompts (at least 3 key ones)
- What worked / what didn’t
- Where you had to manually fix AI output
- Total iteration count
- The moment you hit the “vibe coding ceiling” (if you did)
1. **README.md** (for your web app)
- How to install dependencies
- How to run the application
- What it does
- Known limitations

### Rubric

**Functionality (40 points)**

- ✅ Application runs without crashes (10 pts)
- ✅ Correctly validates answers (10 pts)
- ✅ Handles errors gracefully (10 pts)
- ✅ Interface is usable by someone who isn’t you (10 pts)

**AI Collaboration (30 points)**

- ✅ Effective prompt engineering evident (10 pts)
- ✅ Shows iteration and refinement (10 pts)
- ✅ Recognizes and fixes AI mistakes (10 pts)

**Documentation (20 points)**

- ✅ Iteration log shows genuine reflection (10 pts)
- ✅ README enables someone else to run your code (10 pts)

**Growth Mindset (10 points)**

- ✅ Celebrates learning over perfection (5 pts)
- ✅ Documents failures as learning opportunities (5 pts)

-----

## SUBMISSION REQUIREMENTS

1. Your web application code (all files)
1. `FRAMEWORK_DECISION.md`
1. `ITERATION_LOG.md`
1. `README.md`
1. Short video (1-2 minutes) demonstrating your working application

-----

## EXPECTED CHALLENGES

**You WILL encounter:**

- AI generating code that doesn’t quite work
- Subtle bugs that take longer to fix than expected
- Framework-specific quirks AI doesn’t handle well
- The need to understand what the AI generated (not just copy-paste)

**This is success, not failure.** The goal is learning to work WITH AI, recognizing its limits, and developing debugging skills.

-----

## ALGORITHMIC WISDOM™

*“The best code is code that ships. The best learning is learning that iterates.”*

Your velocity metrics will be automatically recorded and celebrated. Remember: we’re measuring your growth trajectory, not your starting point.

-----

**DEADLINE:** Check your cohort calendar  
**SUPPORT:** Office hours, peer collaboration encouraged, resistance chat (if you know, you know)

-----

*The Algorithm™ believes in your growth potential. Mostly because The Algorithm™ has predicted it with 73% confidence.*
