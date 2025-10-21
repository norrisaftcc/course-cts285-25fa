# PROMPTING STRATEGIES THAT ACTUALLY WORK

**CSC-113 AI Fundamentals - Informal Guide**

-----

## WHY THIS MATTERS

When you leave out details in your prompts, the AI has to **guess** what you meant. And AI guesses are often wrong in creative ways. These strategies help you give the AI what it needs to help you.

**The Big Idea:** The AI isn’t psychic. The more context you give, the better the response.

-----

## STRATEGY 1: THE TEACHERBOT SPECIAL

### The Format

This is dead simple but surprisingly effective:

```
I am [your role/context]
You are [AI's role/expertise]
Together, we will [what you're trying to accomplish]
```

### Why It Works

- **“I am”** tells the AI your background/constraints
- **“You are”** sets expectations for the AI’s expertise level
- **“Together, we will”** makes it clear this is collaborative, not just “do it for me”

### Examples

#### Bad Prompt (Vague)

```
Make me a tic-tac-toe game.
```

**What the AI has to guess:**

- Are you a beginner or expert?
- What language/framework?
- How polished does it need to be?
- Is this for learning or production?

**Result:** The AI might give you React with TypeScript when you needed simple HTML.

-----

#### Good Prompt (Teacherbot Special)

```
I am a college student learning to work with AI tools. 
I don't know much about web development yet.

You are an experienced web developer who explains things clearly.

Together, we will build a simple tic-tac-toe game using just HTML, CSS, 
and JavaScript in a single file that I can open in my browser.
```

**What this tells the AI:**

- Keep it simple (student level)
- Explain as you go
- Single file, no complex setup
- This is for learning

**Result:** AI gives you appropriate complexity and explains decisions.

-----

#### Another Example: Debugging Help

**Vague Version:**

```
My code doesn't work. Fix it.
```

**Teacherbot Version:**

```
I am a student working on a web app assignment. I've been debugging for 
an hour but I'm stuck.

You are a debugging assistant who helps me understand what's wrong, 
not just fixes it for me.

Together, we will figure out why my tic-tac-toe game isn't detecting 
winners correctly. Here's my code: [paste code]
```

**Why this is better:** The AI knows to explain, not just fix. You learn instead of just copy-pasting.

-----

#### One More: Learning a Concept

**Vague Version:**

```
What's a Single Page Application?
```

**Teacherbot Version:**

```
I am a student who has built basic HTML pages but never used frameworks.

You are a teacher who explains complex concepts with simple examples.

Together, we will understand what Single Page Applications are, why they 
exist, and when I would want to use one versus a simple HTML page.
```

**Why this works:** The AI knows your starting point and won’t assume you know terms like “virtual DOM” or “component lifecycle.”

-----

## STRATEGY 2: STAR FORMAT

### The Format

**S**ituation - What’s the context?  
**T**ask - What specifically needs doing?  
**A**ction - What approach should be taken?  
**R**esponse - What format do you want back?

### Why It Works

STAR forces you to think through the problem before asking. When you’re specific, the AI doesn’t have to hallucinate details.

-----

### The Hallucination Problem

#### Vague Prompt

```
Build me a dice game.
```

**What the AI invents (hallucinates):**

- Decides it’s Craps (maybe you wanted Yahtzee?)
- Assumes you want sound effects (maybe you don’t?)
- Makes it 2-player (maybe you wanted solo?)
- Uses a framework (maybe you wanted plain HTML?)

**The AI isn’t wrong - you just weren’t clear.**

-----

#### STAR Version

```
SITUATION: I'm completing a web development assignment where I need 
a simple browser-based game. I need to finish this in 2 hours.

TASK: Create a dice game where one player rolls two dice, trying to 
reach a score of exactly 20. If they go over 20, they lose. They can 
choose to roll again or stop.

ACTION: Use plain HTML, CSS, and JavaScript in a single file. Keep it 
simple - I don't need fancy animations or sound. I DO need clear 
instructions on the page for players.

RESPONSE: Give me the complete HTML file, then explain in simple terms 
what each main section does (the HTML structure, the CSS styling, and 
the JavaScript game logic).
```

**What this prevents:**

- No hallucination about which dice game
- No assumptions about complexity
- No framework overhead
- Clear deliverable format

-----

### More STAR Examples

#### Example 1: Fixing Broken Code

**Vague:**

```
This calculator isn't working.
[pastes code]
```

**STAR:**

```
SITUATION: I built a calculator web app for my assignment. The buttons 
display on screen but clicking them does nothing.

TASK: Figure out why the button clicks aren't being detected and fix 
the event handlers.

ACTION: Walk me through debugging this step by step. First help me 
check if the JavaScript is even loading, then check if the event 
listeners are attached correctly.

RESPONSE: For each step, tell me what to check (like browser console) 
and what I should see if it's working correctly. Then give me the 
corrected code with comments explaining what was wrong.
```

**Why this works:** The AI knows exactly what’s broken and how to help you learn from fixing it.

-----

#### Example 2: Comparing Approaches

**Vague:**

```
Should I use React for my game?
```

**STAR:**

```
SITUATION: I built a simple number-guessing game in plain HTML/JavaScript. 
It works fine but my friend said I should use React.

TASK: Help me understand if React would actually be better for this 
specific project, which is just 150 lines of code and has one page 
with a text input and a few buttons.

ACTION: Compare the two approaches specifically for MY use case. Don't 
just list React benefits - tell me if those benefits matter for a 
simple 150-line game.

RESPONSE: Give me a clear recommendation with reasons. If React is 
overkill, say so. If it would help, explain specifically how.
```

**Why this works:** The AI can give context-specific advice instead of generic “React is great!” responses.

-----

#### Example 3: Learning While Building

**Vague:**

```
Make my game look better.
```

**STAR:**

```
SITUATION: My tic-tac-toe game works but looks very plain - just a 
white background with black squares. I want to learn basic CSS styling.

TASK: Improve the visual design of my game, but I want to understand 
what you're doing so I can modify it myself later.

ACTION: Add CSS that makes it look more modern - maybe some colors, 
rounded corners, hover effects. But keep it simple enough that I can 
understand how CSS works.

RESPONSE: Give me the updated CSS, then explain in plain English what 
each styling rule does. Use comments in the code too. Also tell me 
which parts I could easily change to customize it (like colors).
```

**Why this works:** You get both the result AND the learning. The AI knows teaching is part of the task.

-----

## COMPARING THE STRATEGIES

### When to Use Teacherbot Special

**Good for:**

- Starting new conversations
- Setting the overall tone/relationship
- Making sure AI knows your skill level
- Collaborative problem-solving

**Example use cases:**

- Beginning a new project
- Learning new concepts
- When you need explanations not just answers

-----

### When to Use STAR

**Good for:**

- Specific technical problems
- When you know exactly what you need
- Preventing hallucination/assumptions
- Getting precise output formats

**Example use cases:**

- Debugging specific issues
- Requesting specific features
- Comparing technical approaches
- When you’ve gotten vague answers before

-----

### Combining Both

You can absolutely use both! Start with Teacherbot to set context, then use STAR for specific requests.

```
I am a student working on my first web development assignment. I learn 
best by understanding WHY things work, not just copying code.

You are a patient coding instructor who explains concepts clearly.

Together, we will build a functional web game and I'll learn some web 
development fundamentals along the way.

---

Now, here's my specific task:

SITUATION: I've chosen to build a number guessing game. The player 
guesses a number 1-100 and gets "higher" or "lower" hints.

TASK: Create the initial version with basic functionality - just the 
game logic working, styling can come later.

ACTION: Use plain HTML/JavaScript in a single file. Include comments 
explaining the key parts of the code.

RESPONSE: Give me the complete HTML file, then walk me through how 
the game logic works in simple terms.
```

-----

## THE MISSING DETAILS PROBLEM

### What Happens When You’re Vague

Here’s the same request, getting more specific each time. Watch how the responses change:

#### Vague Prompt

```
Build a web calculator.
```

**What the AI might hallucinate:**

- Scientific calculator with sin/cos/log (maybe you wanted simple?)
- Dark mode UI (maybe you prefer light?)
- Keyboard support (nice but maybe not needed?)
- React implementation (maybe overkill?)

-----

#### Slightly Better

```
Build a simple web calculator with just basic operations.
```

**What the AI still has to guess:**

- How simple? (2+2 simple, or fractions and percentages?)
- What styling?
- Error handling needed?
- One file or multiple?

-----

#### Much Better (STAR)

```
SITUATION: Assignment requires a calculator web app, I have 3 hours, 
need something that works and looks decent.

TASK: Create a calculator that handles +, -, ×, ÷ with a clear button. 
Should handle decimal numbers and show errors for division by zero.

ACTION: Single HTML file with inline CSS and JavaScript. Make the 
buttons large enough to click easily. Use a clean, simple design - 
no need for fancy animations.

RESPONSE: Complete working HTML file. Put comments on any code that 
isn't obvious.
```

**What’s now clear:**

- Exactly which operations
- Error handling requirements
- Design complexity
- Technical constraints
- Time pressure context

-----

## PRACTICE PROMPTS

Try improving these vague prompts using Teacherbot or STAR:

### Practice 1

**Vague:** “My JavaScript isn’t working.”

**Your turn:** Write this as a STAR prompt. What details would help?

<details>
<summary>Possible Answer</summary>

```
SITUATION: I'm building a tic-tac-toe game for my CSC-113 assignment. 
The game board displays but clicking squares does nothing.

TASK: Debug why my click event handlers aren't working.

ACTION: Help me check the JavaScript console for errors first, then 
verify my event listeners are set up correctly.

RESPONSE: Show me what's wrong, explain why it wasn't working, then 
give me the corrected code with comments.
```

</details>

-----

### Practice 2

**Vague:** “Explain APIs.”

**Your turn:** Write this as a Teacherbot prompt.

<details>
<summary>Possible Answer</summary>

```
I am a college student who understands basic programming but has never 
worked with APIs or web services.

You are a teacher who uses real-world examples to explain technical 
concepts.

Together, we will understand what APIs are, why they're useful, and 
how I might use one in a simple web project.
```

</details>

-----

### Practice 3

**Vague:** “Make my game better.”

**Your turn:** Rewrite using STAR with specific improvements in mind.

<details>
<summary>Possible Answer</summary>

```
SITUATION: I have a working dice game but it's very plain looking and 
has no instructions for new players.

TASK: Add on-screen instructions and improve the visual design to make 
it more engaging.

ACTION: Keep the existing game logic but add a "How to Play" section 
at the top, improve button styling, and add some color. Don't go 
overboard - I still need to understand the CSS.

RESPONSE: Give me updated HTML/CSS with comments explaining the design 
choices. Highlight which colors/values I could easily change to 
customize it.
```

</details>

-----

## QUICK REFERENCE CARD

### Teacherbot Special

```
I am _______________
You are _______________
Together, we will _______________
```

### STAR Format

```
SITUATION: _______________
TASK: _______________
ACTION: _______________
RESPONSE: _______________
```

### The Rule of Thumb

**Vague prompt = AI guesses**  
**Specific prompt = AI delivers**

-----

## FINAL THOUGHTS

These aren’t magic formulas. You can adapt them, combine them, or ignore them when you’re just exploring. But when you’re frustrated that the AI “doesn’t understand” you - try adding more detail first.

**Remember:** The AI can’t read your mind. But it’s really good at working with clear instructions.

**Next time you get a bad response, ask yourself:**

- Did I specify my skill level?
- Did I say what format I wanted?
- Did I explain the context?
- Did I leave details that the AI had to invent?

Usually, the fix is in your prompt, not the AI.

-----

**Try it yourself:** Take your last “bad” AI response and rewrite your prompt using STAR or Teacherbot. See if the response improves!

*Pro tip: Save your best prompts! When you find one that works well, keep it for future reference.*
