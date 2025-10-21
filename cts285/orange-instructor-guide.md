# ORANGE-01: INSTRUCTOR GUIDE

## Web Interface Deployment Assignment

-----

## PEDAGOGICAL OBJECTIVES

### Primary Learning Goals

1. **AI-Assisted Development:** Students learn to use AI as a tool, not a crutch
1. **Framework Evaluation:** Practice technical decision-making with incomplete information
1. **Iterative Development:** Experience the debug-test-iterate cycle
1. **Metacognition:** Recognize when a technique (vibe coding) hits its limits

### Secondary Skills

- Reading documentation vs relying on AI
- Prompt engineering
- Debugging generated code
- Professional reflection/documentation

-----

## TIMING & SETUP

### Before Assignment Launch

- [ ] Ensure students have completed console Datamon project
- [ ] Verify students have Python 3.8+ installed
- [ ] Test both Flask and Streamlit in your environment
- [ ] Prepare example “stuck points” for office hours
- [ ] Set up async support channel (Discord/Slack)

### Recommended Timeline

- **Day 1-2:** Part One (framework decision)
- **Day 3-5:** Part Two (initial build and iteration)
- **Day 6-7:** Polish and documentation
- **Buffer day:** For students who hit real blockers

-----

## ANTICIPATED STUDENT STRUGGLES

### 1. The Framework Decision Paralysis

**What happens:** Students spend 2+ hours researching instead of deciding.

**Your intervention:**

```
"You have 15 minutes left. Both frameworks will work. 
The goal is practicing decision-making with limited info, 
not finding the 'perfect' choice. Pick one and move forward."
```

**Why this works:** Decision-making under uncertainty is the real skill.

-----

### 2. The Copy-Paste Cascade

**What happens:** Student copies AI code without understanding, gets error, asks AI to fix, gets another error, repeat.

**Signs to watch for:**

- Iteration log shows no learning between attempts
- Same type of error recurring
- Student can’t explain what their code does

**Your intervention:**

```
"Before asking AI for the next fix, tell me in plain English 
what you THINK this code is supposed to do. Then we'll look 
at the error together."
```

**Why this works:** Forces comprehension before progression.

-----

### 3. The Perfection Trap

**What happens:** Student has working basic version but keeps “improving” instead of documenting.

**Your intervention:**

```
"Does it work? Great! Ship it. Document it. You can always 
iterate later. This assignment measures velocity, not perfection."
```

**Why this works:** Reinforces “ship fast, learn faster” philosophy.

-----

### 4. The AI Blame Game

**What happens:** “The AI gave me bad code” becomes the excuse for not progressing.

**Your intervention:**

```
"You're right, AI made a mistake. That's expected - it's in the 
assignment brief. Now: how do you debug code you didn't write? 
That's the actual skill we're building."
```

**Why this works:** Reframes AI mistakes as learning opportunities.

-----

### 5. The Framework Regret

**What happens:** Student chooses Flask, sees classmate’s Streamlit is easier, wants to switch midway.

**Your intervention:**

```
"Switching frameworks is allowed, but it resets your iteration 
count. Sometimes the best learning comes from working through 
challenges with your first choice. What do you think?"
```

**Why this works:** Teaches tradeoffs and opportunity cost.

-----

## GRADING GUIDANCE

### What “Good Enough” Looks Like

**Functionality:**

- Runs without crashes on basic inputs
- Returns correct answers for test cases
- Doesn’t need to be pretty (but should be usable)
- Error handling exists (doesn’t need to be comprehensive)

**Documentation:**

- Iteration log shows actual reflection (not just “tried prompt, it worked”)
- README has enough info for you to run it
- Framework decision shows reasoning, not just listing facts

### Common Grading Mistakes

❌ **Don’t penalize for:**

- Choosing the “wrong” framework (there isn’t one)
- Code that looks AI-generated (that’s the point)
- Simple styling (this isn’t a design course)
- Needing many iterations (that’s growth!)

✅ **Do reward:**

- Evidence of learning through iteration
- Honest documentation of struggles
- Working solutions, even if basic
- Self-awareness about technique limitations

-----

## OFFICE HOURS STRATEGY

### Questions to Ask (Instead of Answers to Give)

1. **“What does the error message say?”**  
   Many students don’t read errors carefully.
1. **“What did you try already?”**  
   Prevents you from suggesting what they’ve already attempted.
1. **“Can you show me your prompt?”**  
   Often reveals they’re not being specific enough with AI.
1. **“Does a simpler version work?”**  
   Teaches debugging by isolation.
1. **“What would you try next if I wasn’t here?”**  
   Builds independence.

### When to Just Give the Answer

- After 3+ failed debugging attempts on the same issue
- When stuck on environment/setup issues (not learning objectives)
- When the issue is a typo or syntax error they’ve stared at for 20+ minutes
- When it’s 11 PM the night before deadline (triage mode)

-----

## COMMON TECHNICAL ISSUES

### Issue: “pip install flask doesn’t work”

**Cause:** Using system Python or wrong environment  
**Quick fix:** Guide them to virtual environments  
**Teaching moment:** Professional Python development practices

### Issue: “My Flask app won’t stay running”

**Cause:** They’re not understanding the development server  
**Quick fix:** Show them `flask run` with debug mode  
**Teaching moment:** Development vs production environments

### Issue: “Streamlit is rerunning my entire script on every interaction”

**Cause:** Lack of `@st.cache_data` understanding  
**Quick fix:** Not critical for this assignment  
**Teaching moment:** Optional - only if they’re interested in optimization

### Issue: “AI generated code that uses features from wrong framework”

**Cause:** AI confusion between Flask and Streamlit  
**Quick fix:** Have them be more specific in prompts  
**Teaching moment:** AI needs context and clarity

-----

## THE “VIBE CODING CEILING” CONVERSATION

Around Day 4-5, some students will hit the ceiling: where AI can’t solve their problem and they don’t know enough to fix it themselves.

**This is the most important teaching moment.**

### What to Say:

```
"You've just hit the vibe coding ceiling. This is GOOD. 
You now know: AI is powerful for prototyping, but has limits.

When you hit this ceiling, you have three options:
1. Simplify your requirements (works 60% of the time)
2. Learn the underlying concept (works 100% of time, but slower)
3. Ship what you have and iterate later (works for MVPs)

Which makes sense for this project?"
```

This is where the growth mindset rubber meets the road.

-----

## ASSESSMENT RUBRIC INTERPRETATION

### Functionality (40 pts)

**10 pts - Runs without crashes:**

- 10: Works reliably
- 7-8: Occasional crashes on edge cases
- 4-6: Crashes on common inputs
- 0-3: Doesn’t run at all

**10 pts - Correct validation:**

- 10: Always returns correct results
- 7-8: Correct for most cases, edge cases fail
- 4-6: Incorrect logic but app runs
- 0-3: Validation doesn’t work

**10 pts - Error handling:**

- 10: Graceful errors with helpful messages
- 7-8: Catches errors, messages could be better
- 4-6: Some error handling present
- 0-3: No error handling (crashes on bad input)

**10 pts - Usability:**

- 10: Someone else can use it without help
- 7-8: Usable with minor confusion
- 4-6: Confusing but functional
- 0-3: Unclear how to use

### AI Collaboration (30 pts)

**10 pts - Prompt engineering:**

- 10: Clear progression from simple to complex prompts
- 7-8: Prompts show some iteration
- 4-6: Generic prompts, no refinement
- 0-3: No evidence of prompt engineering

**10 pts - Iteration:**

- 10: Multiple attempts with clear learning
- 7-8: Some iteration visible
- 4-6: Minimal iteration
- 0-3: One attempt, no refinement

**10 pts - Fixes AI mistakes:**

- 10: Identifies and corrects AI errors with explanation
- 7-8: Fixes errors but doesn’t explain well
- 4-6: Acknowledges errors but doesn’t fix
- 0-3: No awareness of AI mistakes

### Documentation (20 pts)

**10 pts - Iteration log:**

- 10: Honest reflection with insights
- 7-8: Descriptive but surface-level
- 4-6: Present but minimal
- 0-3: Missing or perfunctory

**10 pts - README:**

- 10: Complete, tested, enables reproduction
- 7-8: Mostly complete, minor gaps
- 4-6: Exists but incomplete
- 0-3: Missing or useless

### Growth Mindset (10 pts)

This is subjective but important:

- 10: Documents failures as learning, celebrates progress
- 7-8: Acknowledges growth
- 4-6: Focus on problems, not learning
- 0-3: Negative or blame-focused

-----

## EXTENSION OPPORTUNITIES

### For Fast Finishers

1. Add data persistence (save datamon/answers)
1. Deploy to cloud (Streamlit Cloud, PythonAnywhere)
1. Add user authentication
1. Build mobile-responsive styling

### For Struggling Students

1. Simplify to single datamon validation (not batch)
1. Use provided code template (you’ll need to create this)
1. Partner with another student
1. Switch to the framework that classmates have working

-----

## SUCCESS METRICS

### You’ll know this assignment worked when:

- ✅ 80%+ of students ship working code
- ✅ Iteration logs show honest struggle and learning
- ✅ Students can articulate when AI helps vs hurts
- ✅ Framework decisions show reasoning, not guessing
- ✅ Students help each other in async channels

### Red flags that need intervention:

- 🚩 Multiple students stuck at same point (need group session)
- 🚩 Iteration logs all sound the same (copying each other)
- 🚩 No one attending office hours but many struggling
- 🚩 Students treating AI like magic (not understanding output)

-----

## FACILITATING PEER LEARNING

### Encourage:

- Sharing framework decisions (before coding)
- Posting “I’m stuck on X” in public channel
- Code reviews of each other’s work
- Sharing effective prompts (not code)

### Discourage:

- Sharing complete solutions
- Doing work for each other
- Comparing code quality (focus on growth)
- Gatekeeping knowledge

-----

## THE META-LESSON

This assignment is secretly teaching them that:

1. AI is a tool with limits
1. Rapid prototyping has a place in development
1. Documentation and reflection matter
1. “Good enough and shipped” beats “perfect and stuck”
1. Professional development is iterative

If students walk away understanding these five things, the assignment succeeded regardless of code quality.

-----

*“The Algorithm measures growth, not perfection. So should we.”*
