# VIBE CODING ASSIGNMENT - INSTRUCTOR GUIDE

**CSC-113 AI Fundamentals**  
**Assignment Duration:** ~1 week  
**Your Time Investment:** ~30 min/day monitoring + grading time

-----

## ASSIGNMENT GOALS (WHAT WE’RE REALLY TEACHING)

This isn’t about web development. This is about:

1. **AI Collaboration Literacy** - When AI helps vs. when it becomes a blocker
1. **Rapid Prototyping Skills** - Getting something working quickly
1. **Critical Evaluation** - Not accepting AI output blindly
1. **Failure as Data** - Documenting struggles as learning
1. **Tool Selection Awareness** - Understanding why frameworks exist

**The Hidden Curriculum:** Students will discover that “vibe coding” has real limits. This realization IS the assignment working correctly.

-----

## PRE-ASSIGNMENT SETUP (15 minutes)

### Day Before Launch

```bash
# Your prep checklist:
□ Test the assignment yourself (pick one game option)
□ Document your iteration count (you'll reference this)
□ Identify 2-3 common failure points in your test
□ Prepare "I struggled too" anecdotes
□ Set up monitoring schedule
```

### Demo Day (In Class)

**Don’t demo the whole assignment.** Instead, demo the PROCESS:

1. **Show your first prompt** (5 minutes)
- Pick tic-tac-toe or calculator
- Show your actual prompt to AI
- Show the output (even if broken)
1. **Show iteration** (3 minutes)
- “This didn’t work, so I asked…”
- Show how you refined your prompt
- Emphasize: “I had to try 3 times”
1. **Show the mess** (2 minutes)
- Show your `attempt1.html`, `attempt2.html` files
- “This is normal. This is what professional prototyping looks like.”

**Key message:** “I’m not expecting perfect. I’m expecting documented iterations and honest reflection.”

-----

## DAILY MONITORING ROUTINE

### Day 1-2: Part 1 Progress

**Morning Check (5 minutes)**

```bash
□ GitHub: How many students have created their folder?
□ Discord: Any early panic or confusion?
□ Office hours: Set up drop-in availability
```

**Expected Student States:**

- 30% started and making progress
- 40% picked game but haven’t begun
- 20% stuck on choosing game
- 10% haven’t looked at assignment yet

**Your Interventions:**

- **For stuck choosers:** “Pick the simplest one. You can always change.”
- **For the 10%:** Gentle nudge in Discord/email
- **For confused starters:** “Show me your first prompt and what happened”

### Day 3-4: Part 2 Struggles

**Mid-Week Check (10 minutes)**

```bash
□ Who has working Part 1 versions?
□ Who is attempting Part 2 (SPA)?
□ Who seems stuck in iteration hell?
```

**Expected Crisis Points:**

**Crisis Type 1: Iteration Paralysis**

- Student has 15 attempts, nothing works
- **Your response:** “Let’s start fresh. Show me your simplest prompt.”
- **Teaching moment:** “Sometimes the best move is to reset.”

**Crisis Type 2: Framework Overwhelm**

- Student can’t get SPA version working, frustrated
- **Your response:** “That’s totally fine! This is the lesson - complexity has costs.”
- **Teaching moment:** “Document why it was hard. That IS the assignment.”

**Crisis Type 3: Perfectionism Block**

- Student won’t move to Part 2 because Part 1 isn’t perfect
- **Your response:** “Part 1 doesn’t need to be perfect. Ship what works.”
- **Teaching moment:** “Done is better than perfect.”

### Day 5-6: Reflection Phase

**Late-Week Check (10 minutes)**

```bash
□ Who has submitted?
□ Who is working on reflection?
□ Who hasn't touched it yet?
```

**Common Patterns:**

**Pattern A: “I don’t know what to write”**

- They have code but blank reflection
- **Response:** “Tell me what frustrated you most. Start there.”

**Pattern B: “My app is terrible”**

- Self-deprecating, won’t submit
- **Response:** “Show me. I bet it’s better than you think. And even if not, the reflection matters more.”

**Pattern C: “I spent 12 hours on this”**

- Overengineered, exhausted
- **Response:** “That teaches you something about scope. Write about that.”

-----

## INTERVENTION SCRIPTS

### When They’re Stuck on Iteration 1

**Student:** “The AI’s code doesn’t work at all.”

**You:** “Okay, let’s debug this together. Open the browser console (F12). What error do you see?”

[They find error]

**You:** “Now ask the AI specifically: ‘I’m getting [error]. How do I fix this?’ The more specific your prompt, the better.”

**Learning moment:** Debugging is normal. Specificity matters.

-----

### When They Hit The Vibe Coding Ceiling

**Student:** “I’ve tried 10 times and it keeps breaking in new ways.”

**You:** “That’s actually great data. This is the limit of vibe coding. You’ve discovered something important.”

**Follow-up:** “For your reflection, write about this moment. When did you realize AI couldn’t solve it? What would you need to learn to fix it yourself?”

**Learning moment:** AI assistance has boundaries. Recognizing them is valuable.

-----

### When They’re Intimidated by SPAs

**Student:** “I don’t understand what the AI is telling me about React/Vue.”

**You:** “That’s the point. SPAs are more complex. The question isn’t ‘can you make it work,’ it’s ‘do you see WHY it’s more complex?’”

**Follow-up:** “Try asking the AI: ‘Explain the tradeoffs between my simple HTML version and this React version.’ Then write about what it says.”

**Learning moment:** Frameworks solve problems but add complexity. Understanding tradeoffs matters.

-----

### When They Want to Change Games Mid-Stream

**Student:** “Can I switch from tic-tac-toe to calculator? Mine isn’t working.”

**You:** “How many attempts have you tried?”

**Student:** “Like 3.”

**You:** “Push to 5 attempts first. Document what’s breaking. THEN if you want to switch, go ahead.”

**Rationale:** We want them to learn persistence, but not bang their head forever. 5 attempts is the minimum learning threshold.

-----

## OFFICE HOURS STRATEGY

### Most Effective Questions to Ask

Instead of debugging their code directly:

1. **“Walk me through your prompts. What were you trying to get the AI to do?”**
- Reveals their mental model
1. **“Which attempt got closest to working? What broke there?”**
- Focuses on progress, not failure
1. **“What does the browser console say?”**
- Teaches debugging process
1. **“If you were explaining this problem to the AI, what would you say?”**
- Helps them clarify their ask

### When to Give Direct Help

**DO help with:**

- Browser developer tools (how to open, what to look for)
- File structure confusion (where files go)
- GitHub upload issues (technical, not conceptual)

**DON’T help with:**

- Writing their prompts for them
- Debugging their code directly
- Telling them which framework to use
- Making their game work perfectly

**The line:** Help with tools and process. Don’t solve the AI collaboration for them.

-----

## GRADING GUIDANCE

### Time Investment: ~10 minutes per student

**Fast Grading Process:**

1. **Check for files (30 seconds)**
- Working HTML file exists?
- PROMPTS.md exists?
- REFLECTION.md exists?
1. **Test the app (2 minutes)**
- Open the HTML file
- Try to use it
- Does it mostly work?
1. **Skim prompts (3 minutes)**
- At least 5 documented?
- Show iteration?
- Evidence of refinement?
1. **Read reflection (4 minutes)**
- Honest about struggles?
- Shows learning?
- Asks good questions?
1. **Assign grade (30 seconds)**
- Most students: 85-95 range
- Exceptional work: 96-100
- Incomplete: Below 80

### Grading Red Flags

**Automatic point deduction triggers:**

- Only 1-2 prompts documented (not enough iteration)
- Reflection is generic (“AI is cool”)
- No evidence of testing/refinement
- Didn’t attempt Part 2 at all (SPA investigation)

**Don’t penalize:**

- Non-working SPA version (attempting matters)
- Simple/basic games (as long as complete)
- “Messy” code (that’s expected)
- Honest struggles (that’s the point)

### Sample Feedback Templates

**For strong work:**

> “Your iteration process is excellent - I can see you learned from each attempt. Your reflection about [specific insight] shows real understanding of AI’s limits. The fact that your SPA version didn’t work but you documented WHY is perfect. 94/100”

**For good work:**

> “Good functional app and clear documentation of your process. Your reflection could go deeper - what specifically did you learn about when to use frameworks? Try connecting your experience to future projects. 87/100”

**For incomplete work:**

> “I can see you got something working, but I need more evidence of iteration (only 2 prompts documented). The reflection also needs more depth - what did this teach you about AI collaboration? Please expand and resubmit. 72/100”

-----

## SUCCESS INDICATORS

### What Good Outcomes Look Like

**Not:** Perfect, polished web apps  
**Yes:** Honest documentation of messy iterations

**Not:** Everything works flawlessly  
**Yes:** Students can explain what broke and why

**Not:** Everyone completes SPA version  
**Yes:** Everyone attempts SPA and reflects on difficulty

**Not:** Students become web developers  
**Yes:** Students understand AI collaboration better

### Class-Level Metrics

After grading, you should see:

- **60-70%** got Part 1 fully working
- **30-40%** got Part 2 (SPA) working
- **90%+** documented meaningful iterations
- **80%+** wrote reflections showing insight

If numbers are way off:

- **Too high (95%+ perfect):** Assignment was too easy
- **Too low (40%- working):** Need to add more scaffolding next time

-----

## COMMON INSTRUCTOR MISTAKES

### Mistake 1: Helping Too Much

**Problem:** You debug their code directly

**Why it’s bad:** They learn debugging, not AI collaboration

**Instead:** Ask questions that lead them to better prompts

-----

### Mistake 2: Expecting Web Developer Quality

**Problem:** You grade like it’s a web dev course

**Why it’s bad:** Misses the learning objective (AI collaboration)

**Instead:** Grade the process and reflection heavily

-----

### Mistake 3: Dismissing Frustration

**Problem:** Student is frustrated their app doesn’t work, you say “it’s fine”

**Why it’s bad:** They don’t feel heard

**Instead:** “That frustration is data. What does it tell you about the limits of this approach?”

-----

### Mistake 4: Not Celebrating Failure

**Problem:** Only praising students with working apps

**Why it’s bad:** Misses the “failure as exercise” philosophy

**Instead:** “Your reflection about hitting the wall is excellent insight.”

-----

## MID-ASSIGNMENT CHECK-IN (Recommended)

**Day 3 or 4: 10-minute class discussion**

**Ask the room:**

1. “Raise your hand if you’ve started” (gauge progress)
1. “How many iterations so far?” (normalize iteration counts)
1. “What’s the most frustrating thing the AI has done?” (share struggles)
1. “Anyone tried the SPA part yet?” (preview coming difficulty)

**Share your own experience:**

- “I tried this too. Took me 7 attempts to get tic-tac-toe working.”
- “The React version was a mess. I learned that frameworks are overkill for simple stuff.”

**Key message:** “Your struggles are the data. Document them. That’s what I’m grading.”

-----

## POST-ASSIGNMENT DEBRIEF

### In-Class Discussion (15 minutes)

**After submissions, before grading:**

**Question 1:** “When did AI help you most?” (collect examples)

**Question 2:** “When did you realize AI couldn’t solve it?” (the ceiling moment)

**Question 3:** “Would you use this approach for bigger projects? Why or why not?”

**Question 4:** “What would you need to learn to build this yourself?” (sets up next learning)

**Synthesis:**

- “You all discovered that vibe coding is powerful for prototyping but has limits.”
- “The students who struggled the most often learned the most.”
- “This is preparing you for the rest of the semester where we’ll use AI more strategically.”

-----

## ADAPTING FOR NEXT SEMESTER

### Data to Collect

```bash
□ Average iteration count (from student submissions)
□ % who completed Part 1 successfully
□ % who attempted Part 2
□ % who got Part 2 working
□ Common failure points (from reflections)
□ Time spent (ask in anonymous survey)
```

### Adjustment Triggers

**If Part 1 too hard (< 60% working):**

- Add more scaffolding
- Demo more iteration
- Simplify game options

**If Part 1 too easy (> 90% working):**

- Add complexity requirements
- Require additional features
- Raise quality bar

**If Part 2 too intimidating (< 20% attempted):**

- Add more SPA explanation
- Make attempt more low-stakes
- Provide more framework guidance

**If Part 2 too successful (> 60% working):**

- Increase complexity
- Require deployment
- Add more features

-----

## EMERGENCY PROTOCOLS

### “Everyone is stuck”

**If 50%+ students struggling by Day 3:**

1. **Pause and reset** - Class discussion about common blockers
1. **Live demo** - You walk through fixing a broken attempt
1. **Pair programming** - Students help each other
1. **Extend deadline** - Add 2 days if needed

-----

### “AI tools are down”

**If Gemini/ChatGPT has outage:**

1. **Announce immediately** - “AI outage is not your fault”
1. **Extend timeline** - Add days equal to outage
1. **Alternative tools** - Suggest Claude, Copilot, local models
1. **Pivot option** - “Write about what you would have tried”

-----

### “Student having crisis”

**If student is melting down:**

1. **Validate feelings** - “This is harder than expected. That’s real.”
1. **Reduce scope** - “Pick the simplest game. Get SOMETHING working.”
1. **Extend personally** - “You have 48 extra hours.”
1. **Refocus on learning** - “The reflection matters more than perfect code.”

-----

## FINAL THOUGHTS

### What Success Really Looks Like

By the end of this assignment, students should be able to articulate:

✅ When AI collaboration accelerates work  
✅ When AI collaboration becomes a blocker  
✅ Why frameworks exist (and when they’re overkill)  
✅ That iteration is normal, not failure  
✅ How to document their development process

### Your Role

You’re not teaching web development. You’re teaching:

- Critical thinking about tools
- Self-awareness about learning process
- Comfort with iteration and “failure”
- Documentation as learning

**Remember:** The messy, struggling students often have the best reflections. Grade the insight, not the polish.

-----

**When in doubt:** Celebrate the mess. Document the learning. Trust the process.

*“Failure is just exercise. Your job is to make sure they’re exercising, not giving up.”*
