import streamlit as st
import random
from datetime import datetime

# Page config
st.set_page_config(page_title="🎮 Datamon", page_icon="🎮", layout="wide")

# Initialize session state
if 'player_name' not in st.session_state:
    st.session_state.player_name = None
if 'current_game' not in st.session_state:
    st.session_state.current_game = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'round_problems' not in st.session_state:
    st.session_state.round_problems = []
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None

# Helper functions
def create_problem(num1, operator, num2):
    """Create a math problem"""
    if operator == '+':
        return num1, operator, num2, num1 + num2, None
    elif operator == '-':
        return num1, operator, num2, num1 - num2, None
    elif operator == '*':
        return num1, operator, num2, num1 * num2, None
    elif operator == '/':
        if num2 == 0:
            num2 = 1  # Avoid division by zero
        quotient = num1 // num2
        remainder = num1 % num2
        return num1, operator, num2, quotient, remainder
    
def check_answer(problem, user_answer, user_remainder=None):
    """Check if answer is correct"""
    num1, op, num2, correct_ans, correct_rem = problem
    
    if op == '/':
        return (user_answer == correct_ans and user_remainder == correct_rem)
    else:
        return user_answer == correct_ans

# Main UI
st.title("🎮 Datamon - Math Practice Game")

# Sidebar for player info and navigation
with st.sidebar:
    if st.session_state.player_name is None:
        st.header("👋 Welcome!")
        player_name = st.text_input("Enter your name:")
        if st.button("Start Playing", key="start_playing") and player_name:
            st.session_state.player_name = player_name
            st.rerun()
    else:
        st.header(f"🎯 Player: {st.session_state.player_name}")
        st.metric("Total Score", st.session_state.score)
        st.metric("Problems Solved", len([h for h in st.session_state.history if h['correct']]))
        st.metric("Total Attempts", len(st.session_state.history))
        
        if st.button("🔄 Reset Game", key="reset_game"):
            st.session_state.score = 0
            st.session_state.history = []
            st.session_state.round_problems = []
            st.session_state.current_problem = None
            st.session_state.current_game = None
            st.rerun()
        
        if st.button("🚪 Logout", key="logout"):
            st.session_state.player_name = None
            st.session_state.score = 0
            st.session_state.history = []
            st.session_state.current_game = None
            st.rerun()

# Main content area
if st.session_state.player_name is None:
    st.info("👈 Please enter your name in the sidebar to start playing!")
    st.markdown("""
    ### Welcome to Datamon! 🎮
    
    A fun math practice game where you can:
    - ✅ Solve math problems with instant feedback
    - 📊 Track your score and progress
    - 🎯 Master addition, subtraction, multiplication, and division
    
    **Ready to begin?** Enter your name in the sidebar!
    """)
else:
    # Game selection
    if st.session_state.current_game is None:
        st.header("🎯 Choose a Mini-Game")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("✅ Answer Checker")
            st.write("Create and solve math problems")
            if st.button("Play Answer Checker", use_container_width=True, key="play_answer_checker"):
                st.session_state.current_game = "answer_checker"
                st.rerun()
        
        with col2:
            st.subheader("🧠 Memory Bank")
            st.write("Coming Soon!")
            st.button("🔒 Locked", disabled=True, use_container_width=True, key="memory_bank_locked")
        
        with col3:
            st.subheader("🎲 Number Guesser")
            st.write("Coming Soon!")
            st.button("🔒 Locked", disabled=True, use_container_width=True, key="number_guesser_locked")
    
    # Answer Checker Game
    elif st.session_state.current_game == "answer_checker":
        st.header("✅ Answer Checker")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Create a Problem")
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                num1 = st.number_input("First Number", min_value=0, max_value=1000, value=0, key="num1")
            with col_b:
                operator = st.selectbox("Operator", ["+", "-", "*", "/"], key="op")
            with col_c:
                num2 = st.number_input("Second Number", min_value=1 if operator == "/" else 0, 
                                      max_value=1000, value=1 if operator == "/" else 0, key="num2")
            
            if st.button("🎲 Generate Random Problem", key="generate_random"):
                num1 = random.randint(1, 50)
                num2 = random.randint(1, 50)
                operator = random.choice(["+", "-", "*", "/"])
                st.session_state.current_problem = create_problem(num1, operator, num2)
                st.rerun()
            
            if st.button("➡️ Create Problem", key="create_problem"):
                st.session_state.current_problem = create_problem(num1, operator, num2)
                st.rerun()
            
            # Show current problem
            if st.session_state.current_problem:
                st.divider()
                n1, op, n2, correct_ans, correct_rem = st.session_state.current_problem
                
                st.markdown(f"### 🎯 Solve: `{n1} {op} {n2} = ?`")
                
                if op == "/":
                    col_q, col_r = st.columns(2)
                    with col_q:
                        user_quotient = st.number_input("Quotient", min_value=0, key="quotient")
                    with col_r:
                        user_remainder = st.number_input("Remainder", min_value=0, key="remainder")
                    
                    col_submit, col_skip = st.columns(2)
                    with col_submit:
                        if st.button("✓ Submit Answer", use_container_width=True, key="submit_division"):
                            is_correct = check_answer(st.session_state.current_problem, 
                                                     user_quotient, user_remainder)
                            
                            if is_correct:
                                st.session_state.score += 10
                                st.success("🎉 Correct! +10 points")
                            else:
                                st.error(f"❌ Incorrect. Answer: {correct_ans} R {correct_rem}")
                            
                            st.session_state.history.append({
                                'problem': f"{n1} {op} {n2}",
                                'user_answer': f"{user_quotient} R {user_remainder}",
                                'correct_answer': f"{correct_ans} R {correct_rem}",
                                'correct': is_correct,
                                'timestamp': datetime.now().strftime("%H:%M:%S")
                            })
                            st.session_state.round_problems.append(st.session_state.current_problem)
                            st.session_state.current_problem = None
                            st.rerun()
                else:
                    user_answer = st.number_input("Your Answer", value=0, key="answer")
                    
                    col_submit, col_skip = st.columns(2)
                    with col_submit:
                        if st.button("✓ Submit Answer", use_container_width=True, key="submit_answer"):
                            is_correct = check_answer(st.session_state.current_problem, user_answer)
                            
                            if is_correct:
                                st.session_state.score += 10
                                st.success("🎉 Correct! +10 points")
                            else:
                                st.error(f"❌ Incorrect. Answer: {correct_ans}")
                            
                            st.session_state.history.append({
                                'problem': f"{n1} {op} {n2}",
                                'user_answer': str(user_answer),
                                'correct_answer': str(correct_ans),
                                'correct': is_correct,
                                'timestamp': datetime.now().strftime("%H:%M:%S")
                            })
                            st.session_state.round_problems.append(st.session_state.current_problem)
                            st.session_state.current_problem = None
                            st.rerun()
                
                with col_skip:
                    if st.button("⏭️ Skip Problem", use_container_width=True, key="skip_problem"):
                        st.session_state.current_problem = None
                        st.rerun()
        
        with col2:
            st.subheader("📊 Session Stats")
            if st.session_state.history:
                correct_count = len([h for h in st.session_state.history if h['correct']])
                accuracy = (correct_count / len(st.session_state.history)) * 100
                st.metric("Accuracy", f"{accuracy:.1f}%")
                
                st.divider()
                st.markdown("**Recent Problems:**")
                for i, h in enumerate(reversed(st.session_state.history[-5:])):
                    icon = "✅" if h['correct'] else "❌"
                    st.text(f"{icon} {h['problem']} = {h['user_answer']}")
            else:
                st.info("Solve problems to see stats!")
        
        st.divider()
        if st.button("🏠 Back to Menu", key="back_to_menu"):
            st.session_state.current_game = None
            st.rerun()

# Footer
st.divider()
st.caption("🎮 Datamon v2.0 - Streamlit Edition | Made for quick math practice!")