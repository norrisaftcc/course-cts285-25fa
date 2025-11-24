# Citizen Wellness Portal™

> *ORANGE Clearance Streamlit Authorization Protocol*

A rapid-development dashboard built with Streamlit for citizen registration, authentication, and wellness metric monitoring.

## 🎯 Overview

The Citizen Wellness Portal™ demonstrates the power of Streamlit for building data-driven dashboards quickly. What would take hundreds of lines in Flask (routes, templates, forms, static files) is accomplished in ~200 lines of Python.

## ✨ Features

- **🔐 Authentication System**
  - New citizen registration with validation
  - Secure login for returning citizens
  - Session persistence across interactions

- **📊 Wellness Dashboard**
  - Algorithmic Satisfaction Metrics™ display
  - Visual progress bars for each metric
  - Overall status calculation

- **🎨 User Experience**
  - Tab-based navigation (Login/Register)
  - Clear error messaging
  - Clean, centered layout

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

1. Navigate to the streamlit directory:
```bash
cd streamlit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

## 📖 Usage

### First Time Citizens (Registration)

1. Click the **Register** tab
2. Enter a unique username
3. Create a password (min 4 characters)
4. Confirm your password
5. Click "Register with The Algorithm"
6. Switch to Login tab to access your dashboard

### Returning Citizens (Login)

1. On the **Login** tab
2. Enter your username and password
3. Click "Submit to The Algorithm"
4. View your wellness metrics

### Dashboard

Once authenticated, you'll see:
- Your personalized wellness metrics
- Overall status assessment
- Logout option

## 🏗️ Architecture

### File Structure
```
streamlit/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── PROCESS.md            # Learning journey documentation
├── SELF-ASSESSMENT.md    # Rubric-based evaluation
└── README.md             # This file
```

### Key Components

**Session State Management**
```python
st.session_state.authenticated  # Login status
st.session_state.username       # Current user
st.session_state.users          # User credentials (in-memory)
st.session_state.user_metrics   # Wellness data per user
```

**Core Functions**
- `validate_username()` - Username validation
- `validate_password()` - Password requirements check
- `register_user()` - New citizen registration
- `authenticate_user()` - Login verification
- `show_dashboard()` - Metrics display
- `show_login_register()` - Auth UI

## 🔍 Technical Details

### Streamlit Concepts Demonstrated

1. **Rerun Model**: The entire script re-executes on every interaction
2. **Session State**: Persistent data across reruns
3. **Forms**: Batch inputs to prevent premature reruns
4. **Tabs**: Organize related UI sections
5. **Conditional Rendering**: Show different views based on state

### Flask vs Streamlit

| Aspect | Flask | Streamlit |
|--------|-------|-----------|
| **Paradigm** | Request/Response | Rerun on Interaction |
| **Routing** | Explicit routes | State-based rendering |
| **Templates** | Jinja2 HTML | Python functions |
| **Forms** | Flask-WTF | st.form() |
| **Session** | Server-side | st.session_state |
| **Development Speed** | Moderate | Very Fast |

## ⚠️ Known Limitations

This is a learning project with intentional simplifications:

- **Security**: Passwords stored in plain text (production would use hashing)
- **Persistence**: Data lost on restart (no database integration)
- **Scalability**: In-memory storage (single user session)
- **Validation**: Basic checks (production needs more robust validation)

These limitations are acceptable for the assignment scope and learning objectives.

## 🎓 Learning Outcomes

Building this portal demonstrated:

1. **Rapid prototyping** with Streamlit
2. **Session state management** patterns
3. **Form handling** to prevent rerun issues
4. **UI/UX design** for authentication flows
5. **AI-assisted learning** techniques

See `PROCESS.md` for detailed learning journey.

## 🛠️ Future Enhancements

Potential improvements for production use:

- [ ] Password hashing (bcrypt)
- [ ] SQLite/PostgreSQL integration
- [ ] Password reset functionality
- [ ] Email verification
- [ ] Role-based access control
- [ ] Metrics history tracking
- [ ] Data visualization charts
- [ ] Export metrics to CSV/PDF

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Session State Guide](https://docs.streamlit.io/library/api-reference/session-state)
- [Streamlit Forms](https://docs.streamlit.io/library/api-reference/control-flow/st.form)

## 📝 Assignment Context

This project fulfills the requirements for:
- **Assignment**: ORANGE-STREAMLIT-001
- **Objective**: Learn Streamlit through AI-assisted development
- **Duration**: 6-8 hours over 1-week window
- **Focus**: Rapid application development for dashboards

## 🎯 Success Metrics

- ✅ Functional registration and login
- ✅ Session persistence
- ✅ Dashboard with metrics
- ✅ Clean, professional UI
- ✅ Comprehensive documentation
- ✅ Git workflow compliance

---

**Status**: ✅ WITHIN ACCEPTABLE PARAMETERS

*The Algorithm is pleased with this implementation.*
