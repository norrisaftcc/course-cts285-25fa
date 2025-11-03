# Product Requirements Document: Hi-Low Card Game
## AlgoCratic Entertainment Division™

**Document Version:** 1.0  
**Last Updated:** November 3, 2025  
**Product Owner:** [To Be Assigned]  
**Target Framework:** Flask MVP  
**Estimated Complexity:** ORANGE Clearance

---

## 1. Product Overview

### 1.1 Purpose
A browser-based card prediction game that teaches fundamental web application concepts including session management, game state tracking, and basic probability mechanics.

### 1.2 Learning Objectives
Students building this application will practice:
- Flask routing and templating
- Session management (cookies/server-side sessions)
- Basic game logic implementation
- Front-end state management
- User input validation
- Responsive design principles

### 1.3 Target Users
- Players seeking quick, casual gaming experiences
- Users familiar with basic card game mechanics
- Browser users (desktop and mobile)

---

## 2. Core Game Mechanics

### 2.1 Game Flow
1. Player enters name on landing page
2. System deals initial card from standard 52-card deck
3. Player predicts whether next card will be higher or lower
4. System reveals next card and determines win/loss
5. Player continues or ends session
6. Win/loss statistics persist during session

### 2.2 Card Ranking
- **Lowest to Highest:** 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
- Suits are irrelevant (only rank matters)
- Ties (equal rank) count as player loss

### 2.3 Winning Conditions
- **Higher:** Next card rank > current card rank
- **Lower:** Next card rank < current card rank
- **Tie:** Next card rank = current card rank → Player loses

---

## 3. Functional Requirements

### 3.1 User Stories

**Story 1: Player Registration**
```
AS A player
I WANT TO enter my name at the start
SO THAT my game session is personalized
```
**Acceptance Criteria:**
- Input field accepts 1-20 alphanumeric characters
- Name displays throughout game session
- Empty submission shows validation message

**Story 2: Making Predictions**
```
AS A player
I WANT TO guess if the next card is higher or lower
SO THAT I can win the game
```
**Acceptance Criteria:**
- Two clearly labeled buttons: "Higher" and "Lower"
- Current card visible before making prediction
- Buttons disabled during card reveal animation (optional enhancement)

**Story 3: Tracking Performance**
```
AS A player
I WANT TO see my win/loss record
SO THAT I can track my progress
```
**Acceptance Criteria:**
- Wins and losses display clearly on screen
- Statistics update immediately after each round
- Win percentage calculated and displayed

**Story 4: Session Continuity**
```
AS A player
I WANT MY statistics to persist during my session
SO THAT I don't lose progress if I navigate away briefly
```
**Acceptance Criteria:**
- Session persists for 30 minutes of inactivity
- Browser refresh maintains current game state
- New session starts fresh

**Story 5: Starting Over**
```
AS A player
I WANT THE option to reset my statistics
SO THAT I can start a new game streak
```
**Acceptance Criteria:**
- "New Game" button clearly visible
- Reset requires confirmation (prevent accidental clicks)
- All statistics reset to zero

---

## 4. Technical Specifications

### 4.1 Technology Stack
- **Backend:** Python 3.8+ with Flask
- **Frontend:** HTML5, CSS3, JavaScript (vanilla or minimal library)
- **Session Management:** Flask-Session or Flask built-in sessions
- **Deployment:** Local development server (production considerations optional)

### 4.2 Data Models

**Session Data Structure:**
```python
session = {
    'player_name': str,
    'current_card': int,  # 2-14 (11=J, 12=Q, 13=K, 14=A)
    'wins': int,
    'losses': int,
    'total_games': int,
    'deck': list[int]  # Remaining cards in current deck
}
```

### 4.3 Core Routes
```
GET  /              → Landing page (name entry)
POST /start         → Initialize game session
GET  /game          → Main game interface
POST /predict       → Process higher/lower prediction
POST /reset         → Clear statistics, start new game
GET  /stats         → Display session statistics (optional API endpoint)
```

### 4.4 Deck Management
- **Approach 1: Finite Deck** (Recommended for MVP)
  - Shuffle standard 52-card deck at game start
  - Remove cards as they're drawn
  - Reshuffle when deck exhausted
  
- **Approach 2: Infinite Deck**
  - Generate random card each draw
  - No deck depletion
  - Simpler implementation but less realistic

**MVP Recommendation:** Use Approach 1 for more authentic card game experience.

---

## 5. User Interface Requirements

### 5.1 Visual Hierarchy
```
┌─────────────────────────────────────┐
│  Hi-Low Game      [Player: Name]    │
│                                      │
│  ┌──────────────────────────────┐  │
│  │                               │  │
│  │      [Current Card: K♠]      │  │
│  │                               │  │
│  └──────────────────────────────┘  │
│                                      │
│    [Higher Button] [Lower Button]   │
│                                      │
│  Wins: 5    Losses: 3    (62.5%)   │
│                                      │
│  [New Game]                          │
└─────────────────────────────────────┘
```

### 5.2 Design Requirements
- Responsive layout (mobile and desktop)
- Clear visual feedback for wins/losses (color coding recommended)
- Card display should be large and easily readable
- Buttons should be touch-friendly (minimum 44px height)

### 5.3 Accessibility
- ARIA labels for interactive elements
- Keyboard navigation support
- Color blind friendly color scheme (don't rely solely on color for win/loss feedback)
- Screen reader compatible

---

## 6. Business Logic Details

### 6.1 Card Comparison Algorithm
```python
def evaluate_prediction(current_card: int, next_card: int, prediction: str) -> bool:
    """
    Returns True if prediction is correct, False otherwise
    Ties count as losses
    """
    if prediction == "higher":
        return next_card > current_card
    elif prediction == "lower":
        return next_card < current_card
    return False
```

### 6.2 Win Percentage Calculation
```python
win_percentage = (wins / total_games) * 100 if total_games > 0 else 0
```

### 6.3 Edge Cases to Handle
- **Empty deck:** Reshuffle and continue
- **Invalid prediction input:** Return error, don't count as loss
- **Session timeout:** Show friendly message, allow restart
- **Concurrent predictions:** Disable buttons until response received
- **First card is Ace or 2:** Game still playable (accept the probability challenge)

---

## 7. Success Metrics

### 7.1 Technical Success Criteria
- [ ] Application runs without errors in development environment
- [ ] Session persistence works across page refreshes
- [ ] Game logic correctly evaluates all card combinations
- [ ] No security vulnerabilities (basic input validation)
- [ ] Code follows PEP 8 style guidelines

### 7.2 User Experience Goals
- [ ] Player can complete full game round in under 30 seconds
- [ ] UI is intuitive without written instructions
- [ ] Win/loss feedback is immediate and clear
- [ ] Statistics display is always visible during gameplay

### 7.3 Educational Outcomes
- [ ] Students understand Flask session management
- [ ] Students implement basic game state logic
- [ ] Students practice front-end/back-end integration
- [ ] Students handle edge cases defensively

---

## 8. Implementation Phases

### Phase 1: MVP (Minimum Viable Product)
**Scope:** Core game loop functional
- Landing page with name entry
- Basic game interface with higher/lower buttons
- Card comparison logic
- Win/loss tracking in session
- Simple CSS styling

**Estimated Complexity:** 4-6 hours for new Flask developers

### Phase 2: Enhanced Experience
**Scope:** Improved UX and visual polish
- Card flip animations
- Win/loss sound effects (optional)
- Improved styling and visual feedback
- Statistics visualization (chart showing win/loss over time)

**Estimated Complexity:** 2-4 additional hours

### Phase 3: Advanced Features (Optional)
**Scope:** Additional game modes and features
- Difficulty levels (finite deck vs infinite deck)
- Leaderboard (requires database)
- Betting system with virtual currency
- Multi-player mode

**Estimated Complexity:** 8+ additional hours

---

## 9. Testing Requirements

### 9.1 Unit Tests
- Card comparison logic for all rank combinations
- Win/loss statistics calculation
- Deck shuffling and card distribution
- Session data persistence

### 9.2 Integration Tests
- Complete game round flow
- Session timeout handling
- Reset functionality
- Navigation between routes

### 9.3 Manual Testing Scenarios
1. Play 10 consecutive rounds without errors
2. Refresh browser mid-game and verify state persists
3. Test on mobile device for responsive behavior
4. Verify tie conditions work correctly
5. Test "New Game" reset functionality

---

## 10. Future Considerations

### 10.1 Known Limitations (MVP)
- No persistent storage (statistics lost when browser closes)
- Single player only
- No authentication system
- Basic visual design

### 10.2 Potential Enhancements
- Add card suit display for visual interest
- Implement streak tracking (consecutive wins)
- Add difficulty modifiers (probability hints)
- Create API endpoints for statistics tracking
- Implement database for persistent leaderboards

---

## 11. Documentation Requirements

### 11.1 Code Documentation
- Docstrings for all functions
- Inline comments for complex game logic
- README with setup instructions
- Requirements.txt for dependencies

### 11.2 User Documentation
- Brief rules explanation on landing page
- Tooltips or help section for game mechanics
- FAQ section (if needed)

---

## Appendix A: Card Reference

| Display | Value | Notes |
|---------|-------|-------|
| 2       | 2     | Lowest rank |
| 3       | 3     | |
| 4       | 4     | |
| 5       | 5     | |
| 6       | 6     | |
| 7       | 7     | |
| 8       | 8     | |
| 9       | 9     | |
| 10      | 10    | |
| J       | 11    | Jack |
| Q       | 12    | Queen |
| K       | 13    | King |
| A       | 14    | Ace (highest) |

---

## Appendix B: Session Configuration

**Recommended Flask-Session Settings:**
```python
app.config['SESSION_TYPE'] = 'filesystem'  # or 'redis' for production
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes
```

---

## Document Approval

**Technical Review:** [Pending]  
**Educational Review:** [Pending]  
**ORANGE Clearance Authorization:** [Pending]

---

*This PRD serves as a teaching example for proper product documentation. Students should use this as a reference for understanding how product requirements translate into technical implementation.*

**Remember:** Good documentation is the foundation of good code. Plan thoroughly, implement incrementally, iterate constantly.