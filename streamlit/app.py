"""
Citizen Wellness Portal™
ORANGE Clearance Streamlit Authorization Protocol

A dashboard for citizens to register, authenticate, and view
their Algorithmic Satisfaction Metrics™.
"""

import streamlit as st
import random

# Initialize session state variables
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'users' not in st.session_state:
    # In-memory user storage (username: password)
    st.session_state.users = {}
if 'user_metrics' not in st.session_state:
    # Store metrics for each user
    st.session_state.user_metrics = {}

def validate_username(username):
    """Validate username is not empty and doesn't already exist."""
    if not username or username.strip() == "":
        return False, "Username cannot be empty"
    if username in st.session_state.users:
        return False, "Username already taken"
    return True, "Valid username"

def validate_password(password):
    """Validate password meets minimum requirements."""
    if len(password) < 4:
        return False, "Password must be at least 4 characters"
    return True, "Valid password"

def register_user(username, password):
    """Register a new citizen in the system."""
    # Validate inputs
    valid_user, user_msg = validate_username(username)
    valid_pass, pass_msg = validate_password(password)

    if not valid_user:
        return False, user_msg
    if not valid_pass:
        return False, pass_msg

    # Store user credentials
    st.session_state.users[username] = password

    # Generate initial metrics for the user
    st.session_state.user_metrics[username] = {
        'productivity': random.randint(60, 100),
        'compliance': random.randint(85, 100),
        'happiness': random.randint(50, 90),
        'loyalty': random.randint(70, 100)
    }

    return True, "Registration successful! Please log in."

def authenticate_user(username, password):
    """Authenticate a citizen's credentials."""
    if username not in st.session_state.users:
        return False, "Invalid username or password"

    if st.session_state.users[username] != password:
        return False, "Invalid username or password"

    # Set session state
    st.session_state.authenticated = True
    st.session_state.username = username

    return True, "Authentication successful!"

def logout():
    """Log out the current citizen."""
    st.session_state.authenticated = False
    st.session_state.username = None

def render_metrics_bar(value, label, max_value=100):
    """Render a progress bar for a metric."""
    # Calculate number of filled blocks (out of 10)
    filled = int((value / max_value) * 10)
    empty = 10 - filled
    bar = "█" * filled + "░" * empty

    return f"{label}: {bar} {value}%"

def show_dashboard():
    """Display the citizen's wellness dashboard."""
    st.title(f"Welcome, Citizen {st.session_state.username}! 🎯")

    st.markdown("---")

    st.header("YOUR ALGORITHMIC SATISFACTION METRICS™")

    # Get user's metrics
    metrics = st.session_state.user_metrics[st.session_state.username]

    # Display metrics with progress bars
    st.text(render_metrics_bar(metrics['productivity'], "Productivity Score"))
    st.text(render_metrics_bar(metrics['compliance'], "Compliance Rating"))
    st.text(render_metrics_bar(metrics['happiness'], "Happiness Index"))
    st.text(render_metrics_bar(metrics['loyalty'], "Loyalty Quotient"))

    st.markdown("---")

    # Calculate overall status
    avg_score = sum(metrics.values()) / len(metrics)
    if avg_score >= 80:
        status = "✅ EXEMPLARY - THE ALGORITHM IS PLEASED"
        status_color = "green"
    elif avg_score >= 60:
        status = "⚠️ WITHIN ACCEPTABLE PARAMETERS"
        status_color = "orange"
    else:
        status = "⚠️ IMPROVEMENT REQUIRED"
        status_color = "red"

    st.markdown(f"**Status:** :{status_color}[{status}]")

    st.markdown("---")

    # Logout button
    if st.button("🚪 Logout", type="primary"):
        logout()
        st.rerun()

def show_login_register():
    """Display login and registration forms."""
    st.title("CITIZEN WELLNESS PORTAL™")
    st.subheader("ORANGE Clearance Authorization Required")

    st.markdown("---")

    # Create tabs for Login and Register
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])

    with tab1:
        st.subheader("Returning Citizens")

        with st.form("login_form"):
            login_username = st.text_input("Username", key="login_username")
            login_password = st.text_input("Password", type="password", key="login_password")
            login_submit = st.form_submit_button("Submit to The Algorithm", type="primary")

            if login_submit:
                success, message = authenticate_user(login_username, login_password)
                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

    with tab2:
        st.subheader("New Citizens")

        with st.form("register_form"):
            reg_username = st.text_input("Username", key="reg_username")
            reg_password = st.text_input("Password", type="password", key="reg_password")
            reg_password_confirm = st.text_input("Confirm Password", type="password", key="reg_password_confirm")
            register_submit = st.form_submit_button("Register with The Algorithm", type="primary")

            if register_submit:
                # Check if passwords match
                if reg_password != reg_password_confirm:
                    st.error("Passwords do not match")
                else:
                    success, message = register_user(reg_username, reg_password)
                    if success:
                        st.success(message)
                        st.info("Please switch to the Login tab to access your dashboard.")
                    else:
                        st.error(message)

def main():
    """Main application entry point."""
    # Configure page
    st.set_page_config(
        page_title="Citizen Wellness Portal™",
        page_icon="🎯",
        layout="centered"
    )

    # Custom CSS for better styling
    st.markdown("""
        <style>
        .stApp {
            max-width: 800px;
            margin: 0 auto;
        }
        </style>
    """, unsafe_allow_html=True)

    # Route based on authentication state
    if st.session_state.authenticated:
        show_dashboard()
    else:
        show_login_register()

if __name__ == "__main__":
    main()
