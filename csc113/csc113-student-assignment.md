# ASSIGNMENT: VIBE CODING YOUR FIRST WEB APP

**CSC-113 AI Fundamentals**  
**Estimated Time:** 4-6 hours  
**Collaboration:** Individual (but discuss strategies with classmates!)

-----

## WHAT YOU’RE LEARNING

This assignment teaches you to work **with** AI to build something functional quickly, while also learning when AI helps and when it struggles. By the end, you’ll understand:

- How to collaborate with AI tools for rapid prototyping
- The difference between “it works” and “I understand why it works”
- When to trust AI suggestions and when to question them
- How different frameworks affect what’s possible

**Important:** This isn’t about becoming a web developer. It’s about understanding how to use AI as a tool while staying in control of the process.

-----

## PART 1: THE AI’S CHOICE (2-3 hours)

### Your Mission

Build a simple interactive web application using ONLY prompts. Let the AI decide how to build it.

### Step 1: Pick Your Game (15 minutes)

Choose ONE simple game or interactive tool:

**Option A: Tic-Tac-Toe**

- Two players take turns
- Check for winners
- Reset button

**Option B: Dice Game (Craps)**

- Roll two dice
- Display results
- Keep score

**Option C: Number Guessing Game**

- Computer picks random number 1-100
- Player guesses
- Give “higher/lower” hints

**Option D: Simple Calculator**

- Basic operations (+, -, ×, ÷)
- Display running total
- Clear button

**Option E: Your Choice**

- Must be similarly simple
- Must be interactive (not just display)
- Get instructor approval first

### Step 2: First Prompt (Start Simple!)

Open your AI tool of choice (Gemini with Canvas, ChatGPT, Claude, etc.) and try something like:

```
"Build me a complete, working [your game] that runs in a web browser. 
Make it a single HTML file that I can just open and use. 
Include all the JavaScript and CSS needed."
```

**Important:** Save this prompt and all your follow-up prompts! You’ll document them later.

### Step 3: Test & Iterate (1-2 hours)

1. **Copy the AI’s code** into a file called `attempt1.html`
1. **Open it in your browser** - does it work?
1. **If it works:** Great! Try to break it. Test edge cases.
1. **If it doesn’t work:**
- Ask the AI to fix the specific problem
- Try rephrasing your request
- Ask for explanations of what the code does

Keep making new files: `attempt2.html`, `attempt3.html`, etc.

**Document your iterations!** For each attempt, note:

- What you asked the AI to change
- Whether it worked
- What you learned

### Step 4: Make It Yours (30 minutes)

Once you have something working, ask the AI to:

- Change the colors or styling
- Add a feature (like score tracking)
- Make error messages more helpful
- Add instructions for players

**Goal:** Get it to a point where someone else could use it without your help.

-----

## PART 2: THE FRAMEWORK EXPERIMENT (1-2 hours)

### Your Mission

Discover what a “Single Page Application” (SPA) is and try building your game using a framework designed for SPAs.

### Step 1: Ask the AI About SPAs

Before you start coding, have a conversation with your AI:

```
"What is a Single Page Application? 
What frameworks are commonly used to build SPAs?
Which one would be best for rebuilding my [game name]? 
Explain why."
```

Take notes on what it recommends. Common frameworks it might suggest:

- React
- Vue
- Svelte
- Vanilla JavaScript (no framework)

### Step 2: The Framework Challenge

Now ask the AI to rebuild your game using the framework it recommended:

```
"Rebuild my [game name] as a Single Page Application using [framework name]. 
Create a complete working version I can test. 
Explain what's different about using [framework] for this."
```

### Step 3: Experience the Difference

You’ll probably notice:

- More complexity (maybe more files, build steps, setup)
- Different way of thinking about the problem
- Possibly harder to get working
- Maybe more powerful features?

**This is the lesson:** Sometimes “better” tools make simple things harder.

### Step 4: Get It Working (Or Don’t!)

Try to get the SPA version working. But here’s the thing: **it’s okay if you don’t succeed.**

The learning happens whether it works or not:

- **If it works:** Why was it harder? Was it worth it? When would you use this approach?
- **If it doesn’t:** What got in the way? When did you hit the wall? What was too complex?

**Document this experience!** Your struggles are valuable data.

-----

## PART 3: REFLECTION & SUBMISSION (30-45 minutes)

### Create Your Submission Folder

Make a folder called `vibe-coding-[yourname]` with these files:

### Required File 1: `PROMPTS.md`

Document your key prompts (at least 5). For each one, note:

- What you asked
- What worked about the AI’s response
- What didn’t work
- What you learned

**Format:**

```markdown
# My Vibe Coding Prompts

## Prompt 1: Initial Build
**What I asked:** "Build me a tic-tac-toe game..."

**What the AI did:** It generated a complete HTML file with CSS and JavaScript

**What worked:** The file opened in my browser and showed a grid

**What didn't work:** Clicking squares didn't do anything - the click handlers were broken

**What I learned:** AI can create the structure quickly but may miss functionality

## Prompt 2: Fix Click Handlers
[Continue with more prompts...]
```

### Required File 2: Your Best Working Version

Include your best working version from Part 1:

- `[gamename]-final.html` (e.g., `tictactoe-final.html`)

If you got Part 2 working, include those files in a subfolder:

- `spa-version/` folder with all necessary files

### Required File 3: `REFLECTION.md`

Answer these questions (1-2 paragraphs each):

#### 1. The AI as Collaborator

- When did the AI help you most?
- When did it frustrate you most?
- What surprised you about working with AI?

#### 2. The Framework Experiment

- What did the AI recommend and why?
- What was different about building an SPA?
- Which approach felt better for YOUR game? Why?
- If you were building something bigger, would your answer change?

#### 3. The “Vibe Coding Ceiling”

- Did you hit a point where AI couldn’t help anymore?
- When did you realize you needed to understand the code yourself?
- What would you do differently next time?

#### 4. Growth Moment

- What did this teach you about AI tools?
- What did this teach you about web development?
- What question do you have now that you didn’t have before?

-----

## SUBMITTING TO GITHUB

### The Simple Way (No Command Line Needed!)

1. Go to your CSC-113 GitHub repository
1. Click “Add file” → “Upload files”
1. Drag your entire `vibe-coding-[yourname]` folder onto the page
1. Add commit message: “Complete vibe coding assignment”
1. Click “Commit changes”

**That’s it!** GitHub will keep your folder structure intact.

-----

## GRADING RUBRIC

Use this rubric to self-assess before submission. You can even paste it into your AI tool and ask: “Based on my work, what would my grade be?”

### Part 1: Functionality (30 points)

|Criteria                        |Excellent (Full Points)                                        |Good (Most Points)                           |Needs Work (Some Points)             |Incomplete (Few/No Points)            |
|--------------------------------|---------------------------------------------------------------|---------------------------------------------|-------------------------------------|--------------------------------------|
|**Working Application** (15 pts)|App works completely, handles all inputs correctly, no crashes |App works for most cases, minor bugs present |App works partially, several bugs    |App doesn’t work or crashes frequently|
|**Usability** (10 pts)          |Clear instructions, intuitive interface, error messages helpful|Interface makes sense, some guidance provided|Confusing interface, minimal guidance|Unusable by others without explanation|
|**Iteration Evidence** (5 pts)  |Multiple attempts documented, clear progression                |Some iteration shown                         |Minimal iteration evident            |No evidence of testing/refinement     |

### Part 2: AI Collaboration (30 points)

|Criteria                         |Excellent (Full Points)                                |Good (Most Points)                 |Needs Work (Some Points)           |Incomplete (Few/No Points)        |
|---------------------------------|-------------------------------------------------------|-----------------------------------|-----------------------------------|----------------------------------|
|**Prompt Documentation** (10 pts)|5+ prompts documented with detailed context            |5 prompts with good notes          |3-4 prompts or minimal notes       |Fewer than 3 prompts or no context|
|**Iteration Process** (10 pts)   |Clear refinement strategy, learned from failures       |Shows some iteration and adaptation|Minimal iteration documented       |Little evidence of process        |
|**Critical Engagement** (10 pts) |Questions AI output, fixes mistakes, understands limits|Identifies some AI errors          |Accepts most AI output uncritically|Copy-paste without evaluation     |

### Part 3: Framework Exploration (20 points)

|Criteria                         |Excellent (Full Points)                                           |Good (Most Points)          |Needs Work (Some Points)          |Incomplete (Few/No Points)|
|---------------------------------|------------------------------------------------------------------|----------------------------|----------------------------------|--------------------------|
|**SPA Investigation** (10 pts)   |Asked AI about frameworks, documented recommendation and reasoning|Got framework recommendation|Asked about SPAs but superficially|Didn’t investigate SPAs   |
|**Comparison & Insight** (10 pts)|Thoughtful comparison of approaches, recognizes tradeoffs         |Notes some differences      |Surface-level observations        |No meaningful comparison  |

### Part 4: Reflection Quality (20 points)

|Criteria                         |Excellent (Full Points)                                 |Good (Most Points)     |Needs Work (Some Points)|Incomplete (Few/No Points)|
|---------------------------------|--------------------------------------------------------|-----------------------|------------------------|--------------------------|
|**Honest Assessment** (10 pts)   |Candid about struggles, specific examples, growth-minded|Honest about challenges|Generic or vague        |Superficial or missing    |
|**Learning Demonstrated** (5 pts)|Clear insights about AI collaboration                   |Shows some learning    |Minimal insight         |No evidence of learning   |
|**Curiosity & Questions** (5 pts)|Asks thoughtful follow-up questions                     |Some curiosity shown   |Generic questions       |No questions              |

### TOTAL: 100 points

**Note:** A perfect app is NOT required for full points. We value honest reflection about struggles over polished products.

-----

## AI SELF-EVALUATION PROMPT

Want to check your work before submitting? Try this:

```
I've completed a vibe coding assignment for my AI Fundamentals class. 
Can you evaluate my work against this rubric? [paste rubric above]

Here's what I'm submitting:
- [Describe your working app]
- [Number of iterations]
- [Key challenges faced]
- [Framework attempted]
- [Main insights]

What areas are strong? Where could I improve before final submission?
```

-----

## COMMON STRUGGLES (And Why They’re Okay!)

**“My game doesn’t work perfectly”**
→ That’s fine! Document what went wrong and what you tried. (Still qualifies for full points!)

**“I don’t understand half the code the AI wrote”**
→ Perfect! That’s one of the key insights. Document what confused you. (This IS the learning!)

**“The SPA version is a disaster”**
→ Excellent! Why was it harder? That’s valuable learning. (Your reflection will be great!)

**“I had to start over 8 times”**
→ Those 8 attempts are part of your learning. Document them! (Shows excellent iteration!)

**“The AI kept making the same mistake”**
→ Great observation! When does AI struggle? Write about it. (Critical thinking points!)

-----

## TIPS FOR SUCCESS

1. **Start with the simplest possible version**
- Get SOMETHING working before adding features
1. **Test frequently**
- Don’t accumulate 100 lines before checking if line 1 works
1. **Save your iterations**
- `attempt1.html`, `attempt2.html`, etc.
- You’ll want to refer back
1. **Read the code the AI gives you**
- Even if you don’t understand it all
- Try to identify what parts do what
1. **Don’t suffer in silence**
- Post questions in Discord/Slack
- Show classmates where you’re stuck
- Come to office hours with your code and specific questions

-----

## TIMELINE SUGGESTION

- **Day 1 (2 hours):** Part 1 - Get initial version working
- **Day 2 (2 hours):** Part 1 - Refine and polish
- **Day 3 (2 hours):** Part 2 - Framework experiment
- **Day 4 (1 hour):** Part 3 - Documentation and reflection

**Total: 6-7 hours** (but take breaks!)

-----

## WHAT SUCCESS LOOKS LIKE

By the end of this assignment, you should be able to:

✅ Quickly prototype something functional using AI  
✅ Recognize when AI suggestions work and when they don’t  
✅ Articulate the difference between simple and complex approaches  
✅ Document your development process  
✅ Ask better questions about web development

You do NOT need to:
❌ Understand every line of code  
❌ Build a perfect, bug-free application  
❌ Successfully complete the SPA version  
❌ Become a web developer

-----

**Due Date:** [Check course calendar]

**Questions?** Post in class Discord with:

- What you’re trying to do
- What you’ve tried
- Your specific error or confusion
- Screenshots if helpful

**Remember:** “Failure is just exercise.” Every iteration teaches you something. Document the mess!

-----

*The goal isn’t to produce perfect code. The goal is to understand how AI collaboration works, where it helps, and where it struggles. Your honest reflection is worth more than a polished app.*
