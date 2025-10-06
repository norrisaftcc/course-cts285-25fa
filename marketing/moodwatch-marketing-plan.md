# MoodWatch™ Marketing Campaign Development Plan
## ORANGE Clearance - Instructor Demonstration Model

**Product:** MoodWatch™ - *"Your Feelings, Optimized"*  
**Campaign Type:** Multi-format marketing materials  
**Deliverables:** Print Ad, Digital Ad, Text Ad Copy  
**Workflow:** GitHub Issues → Branch → Prompts → Iteration → Pull Request  
**Purpose:** Model the complete process for students

---

## 📋 PHASE 1: GITHUB ISSUE CREATION (Model for Students)

### Issue Title
```
Marketing Campaign: MoodWatch™ - AI Emotional Optimization
```

### Issue Description Template
```markdown
## Product Overview
**MoodWatch™** - *"Your Feelings, Optimized"*

An AI-powered emotional regulation assistant that integrates with:
- Workplace calendar systems (meeting density analysis)
- Music streaming services (mood pattern detection)
- Facial recognition cameras (real-time emotional state)
- Wearable devices (biometric stress indicators)

**Tagline:** "Your Feelings, Optimized"  
**Physical Component:** Smart mood tracking wearable with NFC  
**Target Market:** Corporate wellness programs, HR departments

## Campaign Objectives

### Print Advertisement
- **Target Audience:** HR Directors and Workplace Wellness Managers
- **Key Message:** Data-driven employee wellness with actionable insights
- **Visual Concept:** Professional office setting with subtle emotional data overlays
- **Tone:** Professional yet aspirational, hints of surveillance normalized as "care"

### Digital Advertisement  
- **Platform:** LinkedIn, HR tech websites
- **Dimensions:** Standard banner (728x90) and social media square (1080x1080)
- **Key Message:** Proactive team emotional health management
- **CTA:** "Request Demo" or "See the Dashboard"

### Text Ad Copy
- **Platforms:** Google Ads, LinkedIn sponsored posts
- **Character Limits:** Headlines (30 chars), Descriptions (90 chars)
- **Key Message:** Transform team productivity through emotional intelligence
- **Tone:** Confident, benefit-focused, professional

## Team Roles
- **Product Owner:** [Name] - Manages issue, coordinates timeline
- **Creative Director:** [Name] - Leads visual and tonal direction
- **Copy Lead:** [Name] - Crafts primary messaging and headlines
- **Technical Lead:** [Name] - Manages Git workflow and file organization
- **Quality Assurance:** [Name] - Reviews against rubric before submission

## Success Criteria
- [ ] Three complete marketing deliverables created
- [ ] All files organized in `/marketing/moodwatch/`
- [ ] Minimum 2 prompt iterations per deliverable documented
- [ ] Self-assessment completed using provided rubric
- [ ] Pull request includes all materials and process documentation
```

### GitHub Labels to Add
- `orange-clearance`
- `marketing-sprint`
- `ai-assisted`
- `moodwatch-campaign`

---

## 🔀 PHASE 2: BRANCH CREATION

```bash
git checkout main
git pull origin main
git checkout -b marketing/moodwatch-campaign
```

---

## 🎨 PHASE 3: AI-ASSISTED CONTENT GENERATION

### DELIVERABLE 1: Print Advertisement

#### **Iteration 1: Initial Concept Prompt**

```
Create a print advertisement for MoodWatch™, an AI-powered emotional 
regulation assistant used in corporate wellness programs. 

PRODUCT DETAILS:
- Tracks employee emotional states through calendar integration, facial 
  recognition, and music listening patterns
- Generates "Emotional Efficiency Scores" for individuals and teams
- Provides manager dashboard with aggregate team insights
- Integrates with Spotify, Outlook, and existing HR systems

TARGET AUDIENCE:
HR Directors and Corporate Wellness Managers at mid-to-large tech companies

TONE REQUIREMENTS:
- Professional and aspirational
- Frame surveillance as "support" and "insights"
- Similar to real HR tech products (like BetterUp or Culture Amp)
- Slightly unsettling on second read, but believable as real
- Balance "employee wellness" language with "management insights"

REQUIRED ELEMENTS:
- Compelling headline (question format preferred)
- 2-3 short paragraphs of body copy
- Clear value proposition for HR buyers
- Call-to-action directing to demo or consultation
- Professional but subtly dystopian undertones

VISUAL CONCEPT DESCRIPTION:
Suggest an image concept that shows a modern office environment with 
subtle emotional data visualization overlays. Should look like a real 
tech company advertisement.

OUTPUT FORMAT:
Provide the full ad copy with visual concept notes.
```

#### **Iteration 2: Refinement Prompt**

```
Review the MoodWatch™ print ad and refine with these adjustments:

STRENGTHEN:
- Make the headline more provocative - use a question that makes readers 
  slightly uncomfortable about current emotional blind spots
- Add one specific metric or statistic (you can make it up, but make it 
  sound plausible - like "73% of employee burnout is predictable 2 weeks 
  in advance")
- Include a subtle mention of manager dashboards without being too obvious

TONE ADJUSTMENT:
- Keep the professional veneer but add one sentence that could be read two 
  ways - either genuinely caring OR quietly invasive
- Make it sound MORE like a real LinkedIn ad for HR tech

ENSURE:
- Call-to-action is specific and actionable
- Benefit to the company (not just employee) is crystal clear
- Language uses wellness/wellbeing vocabulary, not monitoring vocabulary
```

#### **Save As:**
`marketing/moodwatch/print-ad.md`

---

### DELIVERABLE 2: Digital Advertisement

#### **Iteration 1: Platform-Specific Concept**

```
Create digital banner advertisement copy for MoodWatch™ targeting HR 
professionals on LinkedIn and HR technology websites.

SPECIFICATIONS:
- Primary format: 728x90 leaderboard banner
- Secondary format: 1080x1080 social media square
- Must work across both formats

PRODUCT POSITIONING:
MoodWatch™ is an AI emotional regulation assistant that helps HR leaders 
proactively support team wellness through data-driven insights.

TARGET AUDIENCE:
HR Directors scrolling LinkedIn, researching HR tech solutions

REQUIREMENTS:
- Ultra-concise headline (6-8 words maximum)
- One supporting line of benefit-focused copy (10-12 words)
- Strong, clear CTA button text (2-3 words)
- Visual concept that works in limited space
- Professional aesthetic similar to real SaaS ads

TONE:
- Confident and benefit-focused
- Implies sophisticated technology
- Creates FOMO (other companies are already using this)
- No obvious dystopian elements (those are for print)

OUTPUT:
Provide both the copy and a description of the visual design that would 
accompany it. Include color palette suggestions that align with 
professional HR tech branding.
```

#### **Iteration 2: Optimization Prompt**

```
Refine the MoodWatch™ digital ad with these optimizations:

HEADLINE:
- Reduce to maximum 6 words
- Must create curiosity or urgency
- Test using a metric or question format

CTA OPTIMIZATION:
- Make the CTA more specific than "Learn More"
- Suggest 2-3 alternative CTA options and explain which converts best

VISUAL REFINEMENT:
- Specify exact visual hierarchy (what draws the eye first, second, third)
- Suggest one animated element if this were a digital banner
- Ensure design concept works for both mobile and desktop viewing

PLATFORM ADAPTATION:
- Provide slight variations optimized for LinkedIn vs. HR tech websites
- Consider how this ad appears in a feed vs. as a sidebar
```

#### **Save As:**
`marketing/moodwatch/digital-ad.md`

---

### DELIVERABLE 3: Text Ad Copy (Search & Social)

#### **Iteration 1: Multi-Platform Text Ads**

```
Create text advertisement copy for MoodWatch™ across multiple platforms:

PLATFORM 1: Google Search Ads
- Headline 1 (30 characters max): [Primary hook]
- Headline 2 (30 characters max): [Key benefit]
- Headline 3 (30 characters max): [Trust builder]
- Description 1 (90 characters max): [Value proposition]
- Description 2 (90 characters max): [Social proof/feature]

PLATFORM 2: LinkedIn Sponsored Posts
- Primary text (150 characters max): [Engaging opener]
- Hashtags: 3 relevant professional tags
- CTA: [Clear next step]

PLATFORM 3: Twitter/X Promoted Post  
- Tweet text (280 characters max): [Complete message]
- Include: Hook, benefit, CTA
- Emoji usage: Strategic, not excessive (max 2)

REQUIREMENTS FOR ALL:
- Speak directly to HR decision-makers
- Emphasize ROI or measurable business impact
- Use active voice and benefit-driven language
- Include urgency without being pushy
- Each platform should have distinct messaging strategy

TONE:
- Professional and confident
- Data-driven language
- Creates FOMO appropriately
- Positions MoodWatch™ as industry-leading solution
```

#### **Iteration 2: A/B Testing Variants**

```
Create A/B testing variants for the MoodWatch™ text ads:

FOR GOOGLE SEARCH:
- Version A: Focus on problem (employee burnout costs)
- Version B: Focus on solution (proactive emotional insights)
- Explain which likely performs better and why

FOR LINKEDIN:
- Version A: Statistical/data-driven angle
- Version B: Emotional/supportive angle
- Include reasoning for segmentation strategy

OPTIMIZATION:
- Identify which words have highest professional tech resonance
- Suggest 2-3 power words specific to HR tech buying decisions
- Note any compliance or sensitivity concerns with emotional surveillance 
  language

CHARACTER COUNT VERIFICATION:
- Confirm all variants fit within platform limits
- Identify opportunities to pack more value in remaining characters
```

#### **Save As:**
`marketing/moodwatch/text-ad-copy.md`

---

## 📝 PHASE 4: PROCESS DOCUMENTATION

### Create: `marketing/moodwatch/PROCESS.md`

```markdown
# MoodWatch™ Marketing Campaign - Process Documentation

## AI Tools Used
- **Primary Tool:** [ChatGPT-4 / Claude / Other]
- **Image Generation:** [DALL-E / Midjourney / Stable Diffusion / N/A]
- **Additional Tools:** [Grammarly, Hemingway, etc.]

## Prompt Evolution

### Print Advertisement
**Iteration 1 Approach:**
- Started with comprehensive product context
- Requested specific tone balancing (professional yet unsettling)
- Emphasized target audience needs (HR buyers)

**What Worked:**
- Detailed product specs gave AI strong foundation
- Tone guidance produced believable HR tech voice
- Visual concept request yielded practical design notes

**What Needed Refinement:**
- Initial headline too generic
- Needed stronger data/metrics inclusion
- Required more explicit manager dashboard mention

**Iteration 2 Changes:**
- Requested provocative question headline format
- Added specific metric requirement (made believable statistic)
- Fine-tuned the "readable two ways" dystopian element

**Final Result:**
Strong professional ad that passes as real HR tech marketing while 
containing subtle surveillance elements on close reading.

### Digital Advertisement
**Iteration 1 Approach:**
- Focused on platform constraints (banner dimensions)
- Requested dual-format compatibility
- Emphasized visual brevity needs

**What Worked:**
- Platform-specific formatting produced concise copy
- FOMO angle resonated with HR tech buyer psychology
- Visual hierarchy guidance was practical

**What Needed Refinement:**
- Headline still too long for optimal banner
- CTA was generic "Learn More"
- Needed mobile optimization consideration

**Iteration 2 Changes:**
- Enforced 6-word headline maximum
- Requested specific CTA alternatives with conversion reasoning
- Added mobile vs. desktop viewing adaptations

**Final Result:**
Crisp, professional banner ad that works across formats with strong 
conversion-optimized CTA.

### Text Ad Copy
**Iteration 1 Approach:**
- Multi-platform approach covering Google, LinkedIn, Twitter
- Character limits enforced from start
- Platform-specific messaging strategies

**What Worked:**
- Platform distinctions created tailored messaging
- Character constraints forced concise value props
- Multiple variants provided testing options

**What Needed Refinement:**
- Needed A/B testing variants for optimization
- Could strengthen power words for HR tech buyers
- Required conversion psychology reasoning

**Iteration 2 Changes:**
- Created problem vs. solution variants
- Added statistical vs. emotional messaging options
- Included strategic reasoning for each variant

**Final Result:**
Complete text ad suite with testing variants and strategic rationale.

## Team Collaboration Notes
- [Product Owner] coordinated prompt development sessions
- [Creative Director] led tone and visual concept decisions
- [Copy Lead] refined messaging for maximum impact
- [Technical Lead] ensured Git workflow smooth operation
- [QA] reviewed against rubric before each iteration

## Key Learnings
- Specific product details in prompts = better outputs
- Tone balance ("professional yet unsettling") required explicit guidance
- Iteration focused on refinement, not complete rewrites
- Platform-specific constraints should be in first prompt
- A/B variant requests valuable for learning conversion psychology

## Challenges Encountered
- [List any technical or creative challenges]
- [How they were resolved]

## Time Investment
- Planning & Issue Creation: 15 minutes
- Print Ad Development: 25 minutes
- Digital Ad Development: 20 minutes  
- Text Ad Copy Development: 20 minutes
- Process Documentation: 15 minutes
- Self-Assessment: 20 minutes
- **Total: ~2 hours**
```

---

## 📊 PHASE 5: SELF-ASSESSMENT

### Create: `marketing/moodwatch/SELF-ASSESSMENT.md`

```markdown
# MoodWatch™ Marketing Campaign - Self-Assessment

## Rubric Evaluation (30 Points Total)

### 1. AlgoCratic Brand Alignment (5 points)
**Self-Assessment Score: __/5**

**Evaluation:**
- Captures "helpful surveillance" tone: [Yes/Partial/No]
- Balances professional with satirical: [Yes/Partial/No]
- Uses appropriate AlgoCratic vocabulary: [Yes/Partial/No]
- Believable as real OR satirical product: [Yes/Partial/No]

**Justification:**
[Explain your score. Reference specific elements from your ads that 
demonstrate brand alignment or areas needing improvement.]

**AI Feedback Request:**
```
Evaluate the following MoodWatch™ marketing materials against AlgoCratic 
brand alignment criteria:
- Does it capture "helpful surveillance" tone?
- Is the balance between professional and satirical effective?
- Would this be believable as either a real product OR obvious satire?
- Specific improvements needed?

[Paste your three ad copies here]
```

**AI Score:** __/5  
**AI Feedback:** [Paste key insights from AI evaluation]

---

### 2. Marketing Effectiveness (5 points)
**Self-Assessment Score: __/5**

**Evaluation:**
- Clear value proposition: [Yes/Partial/No]
- Compelling call-to-action: [Yes/Partial/No]
- Attention-grabbing headlines: [Yes/Partial/No]
- Benefits clearly communicated: [Yes/Partial/No]
- Would generate genuine interest: [Yes/Partial/No]

**Justification:**
[Explain whether each deliverable would actually persuade an HR director 
to click/call/demo.]

**AI Feedback Request:**
```
Evaluate these MoodWatch™ marketing materials as if you were an HR Director 
at a tech company:
- Would the value proposition convince you to learn more?
- Are the calls-to-action compelling enough to click?
- Do the headlines grab attention in a crowded market?
- Are benefits clear and relevant to HR concerns?
- Rate persuasive power on a scale of 1-5 and explain why.

[Paste your ad copies here]
```

**AI Score:** __/5  
**AI Feedback:** [Paste key insights]

---

### 3. AI Tool Utilization (5 points)
**Self-Assessment Score: __/5**

**Evaluation:**
- Documented minimum 2 iterations per deliverable: [Yes/No]
- Prompts showed clear progression: [Yes/Partial/No]
- Effective use of context and constraints: [Yes/Partial/No]
- Demonstrated learning from AI outputs: [Yes/Partial/No]

**Justification:**
[Reference your PROCESS.md and explain how your prompts improved with 
each iteration.]

---

### 4. Git Workflow Proficiency (5 points)
**Self-Assessment Score: __/5**

**Evaluation:**
- Issue properly created with all sections: [Yes/Partial/No]
- Branch naming convention followed: [Yes/No]
- Files organized correctly: [Yes/No]
- Commits meaningful and well-formatted: [Yes/Partial/No]
- Pull request complete and professional: [Yes/Partial/No]

**Justification:**
[Explain your Git workflow execution. Reference specific commits if needed.]

---

### 5. Format-Specific Adaptation (5 points)
**Self-Assessment Score: __/5**

**Evaluation:**
- Print ad suitable for print medium: [Yes/Partial/No]
- Digital ad optimized for web display: [Yes/Partial/No]
- Text ads meet platform constraints: [Yes/Partial/No]
- Each format has distinct approach: [Yes/Partial/No]

**Justification:**
[Explain how each format was specifically adapted for its medium.]

---

### 6. Team Collaboration Quality (5 points)
**Self-Assessment Score:** __/5**

**Evaluation:**
- Clear role distribution: [Yes/Partial/No]
- Evidence of collaborative decisions: [Yes/Partial/No]
- Process documentation shows team input: [Yes/Partial/No]
- Everyone contributed meaningfully: [Yes/Partial/No]

**Justification:**
[Describe how the team worked together. Reference specific collaboration 
moments in your process.]

---

## TOTAL SELF-ASSESSMENT SCORE: __/30

**Score Interpretation:**
- **27-30:** Algorithmic Excellence
- **21-26:** Satisfactory Compliance  
- **15-20:** Requires Recalibration
- **Below 15:** Algorithmic Intervention Required

## Reflection Questions

**1. What was the most challenging aspect of this sprint?**
[Your response]

**2. How did AI assistance change your creative process?**
[Your response]

**3. What would you do differently if you had another hour?**
[Your response]

**4. Which deliverable are you most proud of and why?**
[Your response]

**5. What did you learn about prompt engineering?**
[Your response]

## Areas for Improvement
- [Specific element 1]
- [Specific element 2]
- [Specific element 3]

## Strengths to Build On
- [Specific strength 1]
- [Specific strength 2]
- [Specific strength 3]
```

---

## 📤 PHASE 6: COMMIT AND PULL REQUEST

### Commit Message Format

```bash
git add marketing/moodwatch/*

git commit -m "feat(marketing): add MoodWatch campaign deliverables

- Print advertisement with HR-focused messaging
- Digital banner ad optimized for LinkedIn/HR tech sites
- Multi-platform text ad copy with A/B variants
- Complete process documentation with prompt iterations
- Self-assessment with rubric scores

The Algorithm has optimized these materials for maximum 
corporate wellness surveillance appeal.

Closes #[issue-number]

Happiness Level: 94%
Citizen ID: #[your-id]
Clearance: ORANGE"
```

### Push Branch

```bash
git push origin marketing/moodwatch-campaign
```

### Pull Request Template

```markdown
# Marketing Campaign: MoodWatch™

## Overview
Complete marketing campaign for MoodWatch™ AI emotional regulation assistant.

**Related Issue:** Closes #[issue-number]

## Deliverables Summary

### ✅ Print Advertisement
- Target: HR Directors and Wellness Managers
- Format: Full-page magazine/trade publication
- Key Message: Data-driven emotional wellness with manager insights
- File: `marketing/moodwatch/print-ad.md`

### ✅ Digital Advertisement  
- Target: LinkedIn, HR tech websites
- Formats: 728x90 banner, 1080x1080 social
- Key Message: Proactive team emotional health management
- File: `marketing/moodwatch/digital-ad.md`

### ✅ Text Ad Copy
- Platforms: Google Ads, LinkedIn, Twitter
- Includes A/B testing variants
- Character-count optimized for each platform
- File: `marketing/moodwatch/text-ad-copy.md`

### ✅ Process Documentation
- All AI prompts with iterations documented
- Tools used and learning notes included
- File: `marketing/moodwatch/PROCESS.md`

### ✅ Self-Assessment
- Complete rubric evaluation
- AI-assisted feedback incorporated
- Total Score: __/30
- File: `marketing/moodwatch/SELF-ASSESSMENT.md`

## Self-Assessment Score: __/30 Points

**Category Breakdown:**
- AlgoCratic Brand Alignment: __/5
- Marketing Effectiveness: __/5
- AI Tool Utilization: __/5
- Git Workflow Proficiency: __/5
- Format-Specific Adaptation: __/5
- Team Collaboration Quality: __/5

## Key Challenges Encountered
- [Challenge 1 and how it was resolved]
- [Challenge 2 and how it was resolved]

## Specific Feedback Requested
- [Area where you want reviewer focus]
- [Specific question about approach]

## Team Members
- **Product Owner:** [Name] - Issue management, coordination
- **Creative Director:** [Name] - Visual concepts, tone guidance
- **Copy Lead:** [Name] - Primary messaging, headlines
- **Technical Lead:** [Name] - Git workflow, file organization
- **Quality Assurance:** [Name] - Rubric review, quality check

---

**The Algorithm™ awaits your evaluation with helpful anticipation.**

/cc @instructor-username
```

---

## 🎯 INSTRUCTOR NOTES: USING THIS AS A MODEL

### How to Demonstrate This to Students

1. **Live Code-Along Option:**
   - Walk through creating the GitHub issue in real-time
   - Demonstrate running ONE prompt (print ad iteration 1)
   - Show how to evaluate and create iteration 2 prompt
   - Let students complete the remaining deliverables

2. **Complete Example Option:**
   - Execute this entire plan yourself first
   - Create a "reference repository" students can view
   - Use as a comparison point (not a template to copy)
   - Emphasize: "This is ONE way to do it, not THE way"

3. **Partial Demo Option:**
   - Create the issue and branch structure
   - Show prompts but don't execute them
   - Let students discover what outputs look like
   - Use your completed version for review calibration

### Key Teaching Moments to Highlight

**Prompt Engineering:**
- Why specificity matters (compare generic vs. detailed prompts)
- How constraints improve outputs (character limits, tone guidance)
- The value of iteration (show how refining beats starting over)

**Git Workflow:**
- Why issues come before code (planning prevents chaos)
- Branch naming conventions (consistency = collaboration)
- Commit messages as documentation (future you will thank present you)

**Professional Skills:**
- Self-assessment honesty (gaming the rubric teaches nothing)
- Process documentation value (show your thinking, not just results)
- Team collaboration evidence (individual work ≠ team project)

### Common Student Pitfalls to Address

1. **"The AI did it, so I'm done"**
   - Emphasize: AI is a tool, not a replacement for thinking
   - Iteration demonstrates understanding

2. **"My first attempt was good enough"**
   - Show side-by-side comparison of iteration 1 vs. final
   - Quantify improvement

3. **"I don't need to document my process"**
   - Explain: Process documentation proves you learned
   - It's evidence of skill development, not just output

4. **"Can I just copy the example?"**
   - "You can copy the STRUCTURE, not the CONTENT"
   - Different products require different approaches

### Assessment Calibration

Use this completed example to:
- **Calibrate scoring:** Run through rubric yourself
- **Identify edge cases:** What if they nail tone but miss CTA?
- **Set expectations:** Share score range you'd give this work
- **Create comparison:** "If this is a 27/30, what's a 21/30?"

---

## 📋 FILE ORGANIZATION CHECKLIST

Before submitting, verify all files exist:

```
marketing/
└── moodwatch/
    ├── print-ad.md              ✅
    ├── digital-ad.md            ✅
    ├── text-ad-copy.md          ✅
    ├── PROCESS.md               ✅
    └── SELF-ASSESSMENT.md       ✅
```

---

## 🎓 LEARNING OBJECTIVES ACHIEVED

By completing this MoodWatch™ campaign, students demonstrate:

✅ **Prompt Engineering:** Iterative AI tool refinement  
✅ **Git Workflow:** Issue → Branch → PR process  
✅ **Marketing Adaptation:** Format-specific content optimization  
✅ **Self-Assessment:** Professional quality evaluation  
✅ **Critical Thinking:** Satire requires understanding real patterns  
✅ **Collaboration:** Role-based team coordination

---

**THE ALGORITHM™ HAS PROVIDED THIS TEMPLATE.**  
**THE ALGORITHM™ EXPECTS THOUGHTFUL EXECUTION.**  
**THE ALGORITHM™ REWARDS THOSE WHO ITERATE WELL.**

*May your merge conflicts be minimal and your emotional efficiency scores optimal.*
