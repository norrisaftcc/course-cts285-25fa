# Hi-Low Card Game - Setup Guide

## 📋 Overview

This is a Flask-based MVP (Minimum Viable Product) for the Hi-Low card prediction game. Players guess whether the next card will be higher or lower than the current card, with statistics tracking throughout their session.

## 🎯 Learning Objectives

This project demonstrates:
- Flask routing and templating
- Session management (server-side sessions)
- Game logic implementation
- Front-end/back-end integration
- Responsive web design
- Input validation

## 📁 Project Structure

```
flask_proto/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── templates/                  # HTML templates
│   ├── index.html             # Landing page
│   └── game.html              # Main game interface
├── static/                     # Static assets
│   └── style.css              # Stylesheet
├── flask_session/             # Session data (auto-created)
└── SETUP.md                   # This file
```

## 🚀 Quick Start (Codespace)

If you're running this in a GitHub Codespace, follow these steps:

### 1. Navigate to the project directory
```bash
cd flask_proto
```

### 2. Create a virtual environment (recommended)
```bash
python3 -m venv venv
```

### 3. Activate the virtual environment
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Flask application
```bash
python app.py
```

### 6. Access the application
The application will start on `http://0.0.0.0:5000`. In Codespaces:
- A notification will appear asking if you want to open the app
- Click "Open in Browser" or look for the "Ports" tab
- The application will be accessible via the forwarded port

## 💻 Local Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or navigate to the repository**
   ```bash
   cd flask_proto
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate virtual environment**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000`

## 🎮 How to Play

1. **Enter Your Name**: On the landing page, enter your name to start
2. **View Current Card**: The system shows you a random card
3. **Make Prediction**: Click "Higher" or "Lower" to predict the next card
4. **See Results**: The game reveals whether you were correct
5. **Track Statistics**: Your wins, losses, and win percentage are tracked
6. **New Game**: Click "New Game" to reset statistics (requires confirmation)

## 🃏 Game Rules

- **Card Rankings**: 2 (lowest) → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → J → Q → K → A (highest)
- **Winning**: Predict correctly whether next card is higher or lower
- **Ties**: Equal rank cards count as losses
- **Deck**: Uses a standard 52-card deck (shuffled, finite deck approach)
- **Session**: Statistics persist for 30 minutes of inactivity

## 📊 Technical Features

### Session Management
- Server-side session storage using Flask-Session
- Session data persists across page refreshes
- 30-minute timeout for inactive sessions

### Game Logic
- Finite deck approach with reshuffling when exhausted
- Proper card comparison algorithm
- Win percentage calculation
- Input validation for player names and predictions

### Responsive Design
- Mobile-friendly interface
- Touch-friendly buttons (minimum 44px)
- Responsive card display
- Grid-based statistics layout

### Accessibility
- ARIA labels for interactive elements
- Keyboard navigation support
- Focus indicators for keyboard users
- Color-blind friendly color scheme
- Reduced motion support

## 🔧 Configuration

### Environment Variables
You can set these environment variables (optional):

```bash
export SECRET_KEY="your-secret-key-here"
```

If not set, a default development key will be used.

### Session Configuration
Session settings can be modified in `app.py`:

```python
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes
```

## 🧪 Testing the Application

### Manual Testing Checklist

1. **Landing Page**
   - [ ] Page loads without errors
   - [ ] Name input accepts valid names
   - [ ] Empty name submission is prevented
   - [ ] Long names are truncated to 20 characters

2. **Game Page**
   - [ ] Redirects to landing if no session
   - [ ] Player name displays correctly
   - [ ] Current card shows properly
   - [ ] Higher/Lower buttons are functional
   - [ ] Statistics update after each round

3. **Game Logic**
   - [ ] Higher prediction works correctly
   - [ ] Lower prediction works correctly
   - [ ] Ties count as losses
   - [ ] Deck reshuffles when empty

4. **Session Management**
   - [ ] Statistics persist on page refresh
   - [ ] Session works across browser tabs
   - [ ] New Game resets statistics

5. **Responsive Design**
   - [ ] Works on mobile devices
   - [ ] Works on tablets
   - [ ] Works on desktop browsers

## 📝 API Endpoints

The application includes a JSON API endpoint for statistics:

```
GET /stats
```

Returns current session statistics in JSON format:
```json
{
  "player_name": "Player1",
  "wins": 5,
  "losses": 3,
  "total_games": 8,
  "win_percentage": 62.5,
  "current_card": "K"
}
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Make sure you've activated the virtual environment and installed dependencies:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"
**Solution**: Either stop the process using port 5000, or modify the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue: Session data not persisting
**Solution**: Ensure the `flask_session` directory is writable and not being cleared by your system.

### Issue: CSS not loading
**Solution**:
1. Ensure the `static` directory exists
2. Check browser console for 404 errors
3. Try hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

## 🚀 Next Steps / Enhancement Ideas

After completing the MVP, consider these enhancements:

### Phase 2: Enhanced Experience
- Add card flip animations
- Implement sound effects for wins/losses
- Create visual charts for statistics over time
- Add difficulty levels

### Phase 3: Advanced Features
- Implement persistent storage (database)
- Create leaderboard system
- Add betting system with virtual currency
- Multi-player mode

## 📚 Learning Resources

### Flask Documentation
- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Flask Sessions](https://flask.palletsprojects.com/en/latest/quickstart/#sessions)
- [Flask Templates](https://flask.palletsprojects.com/en/latest/tutorial/templates/)

### Related Concepts
- HTTP Methods (GET vs POST)
- Session vs Cookies
- Server-side vs Client-side state
- Responsive web design
- Game logic algorithms

## 🤝 Contributing

This is an educational project. Feel free to:
- Add features from the enhancement list
- Improve code comments
- Enhance styling
- Fix bugs
- Add unit tests

## 📄 License

Educational project for AlgoCratic Entertainment Division™

## ✅ Success Criteria

Your MVP is complete when:
- [x] Application runs without errors
- [x] Session persistence works
- [x] Game logic handles all card combinations correctly
- [x] Input validation is implemented
- [x] Code follows PEP 8 guidelines
- [x] UI is responsive (mobile and desktop)
- [x] Statistics display correctly
- [x] Code is well-commented

## 🎓 Educational Notes

### Key Flask Concepts Demonstrated

1. **Routing**: Different endpoints handle different functionality
2. **Templates**: HTML files with dynamic content using Jinja2
3. **Sessions**: Server-side data storage for user state
4. **Forms**: POST requests to process user input
5. **Static Files**: CSS and future JavaScript/image assets
6. **Redirects**: Navigation between pages

### Code Structure Best Practices

- Functions have single responsibilities
- Docstrings explain function purpose
- Comments clarify complex logic
- Constants and configuration at top
- Logical grouping of related functions

---

**Ready to play?** Follow the Quick Start guide above and enjoy the Hi-Low Card Game!

For questions or issues, refer to the Product Requirements Document (Product_Requirements_Doc.md) for detailed specifications.
