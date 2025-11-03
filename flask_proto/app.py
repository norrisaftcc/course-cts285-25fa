"""
Hi-Low Card Game - Flask MVP
A browser-based card prediction game for learning Flask fundamentals.

Game Rules:
- Player predicts if next card will be higher or lower than current card
- Card rankings: 2 (lowest) through Ace (highest)
- Ties count as losses
- Statistics persist during session
"""

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_session import Session
import random
import os
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============================================================================
# Flask Application Setup
# ============================================================================

app = Flask(__name__)

# Secret key for session encryption (should be environment variable in production)
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = 'dev-secret-key-change-in-production'
    # Security warning: Log when using default secret key
    logger.warning(
        "WARNING: Using default SECRET_KEY. This is insecure for production! "
        "Set the SECRET_KEY environment variable."
    )

app.config['SECRET_KEY'] = SECRET_KEY

# Session configuration - stores session data on server filesystem
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes

# Initialize Flask-Session
Session(app)


# ============================================================================
# Game Logic Functions
# ============================================================================

def create_deck():
    """
    Create a standard 52-card deck using numeric values.

    Card Values:
    - 2-10: Face value
    - 11: Jack
    - 12: Queen
    - 13: King
    - 14: Ace (highest)

    Returns:
        list: Deck of 52 cards (4 suits × 13 ranks)
    """
    # Create 4 cards of each rank (representing 4 suits)
    deck = []
    for rank in range(2, 15):  # 2 through 14 (Ace)
        for _ in range(4):  # 4 suits per rank
            deck.append(rank)

    return deck


def shuffle_deck():
    """
    Create and shuffle a new deck.

    Returns:
        list: Shuffled deck of 52 cards
    """
    deck = create_deck()
    random.shuffle(deck)
    return deck


def draw_card(deck):
    """
    Draw a card from the deck. Reshuffle if deck is empty.

    Args:
        deck (list): Current deck of cards

    Returns:
        tuple: (card_value, updated_deck)
    """
    # If deck is empty, create and shuffle a new one
    if not deck:
        deck = shuffle_deck()

    # Draw the top card
    card = deck.pop()

    return card, deck


def card_to_display(card_value):
    """
    Convert numeric card value to display string.

    Args:
        card_value (int): Numeric card value (2-14)

    Returns:
        str: Display string (e.g., "2", "J", "Q", "K", "A")
    """
    card_names = {
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A'
    }

    # Return face card name or numeric value
    return card_names.get(card_value, str(card_value))


def evaluate_prediction(current_card, next_card, prediction):
    """
    Determine if player's prediction was correct.

    Args:
        current_card (int): Current card value
        next_card (int): Next card value
        prediction (str): Player's prediction ("higher" or "lower")

    Returns:
        bool: True if prediction correct, False otherwise

    Rules:
        - Ties (equal values) count as losses
        - Higher: next_card > current_card
        - Lower: next_card < current_card
    """
    if prediction == "higher":
        return next_card > current_card
    elif prediction == "lower":
        return next_card < current_card

    # Invalid prediction defaults to False
    return False


def calculate_win_percentage(wins, total_games):
    """
    Calculate win percentage from statistics.

    Args:
        wins (int): Number of wins
        total_games (int): Total games played

    Returns:
        float: Win percentage (0-100), or 0 if no games played
    """
    if total_games == 0:
        return 0.0

    return round((wins / total_games) * 100, 1)


def initialize_session(player_name):
    """
    Initialize a new game session with default values.

    Args:
        player_name (str): Player's name

    Side Effects:
        Updates Flask session with initial game state
    """
    # Create and shuffle initial deck
    deck = shuffle_deck()

    # Draw first card
    current_card, deck = draw_card(deck)

    # Initialize session data structure
    session['player_name'] = player_name
    session['current_card'] = current_card
    session['wins'] = 0
    session['losses'] = 0
    session['total_games'] = 0
    session['deck'] = deck
    session['last_result'] = None  # Track result of last prediction
    session['last_card'] = None    # Track previous card for display


# ============================================================================
# Flask Routes
# ============================================================================

@app.route('/')
def index():
    """
    Landing page - player enters name to start game.

    Returns:
        Rendered landing page template
    """
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_game():
    """
    Initialize new game session with player name.

    Form Data:
        player_name (str): Player's name (1-20 characters, alphanumeric + spaces)

    Returns:
        Redirect to game page or back to landing with error
    """
    # Get player name from form
    player_name = request.form.get('player_name', '').strip()

    # Validate player name - must not be empty
    if not player_name:
        logger.info("Player name validation failed: empty name")
        return redirect(url_for('index'))

    # Server-side validation: ensure name matches allowed pattern
    # Only alphanumeric characters and spaces allowed
    if not re.match(r'^[A-Za-z0-9 ]+$', player_name):
        logger.info(f"Player name validation failed: invalid characters in '{player_name}'")
        return redirect(url_for('index'))

    # Limit name length to 20 characters
    if len(player_name) > 20:
        player_name = player_name[:20]

    # Initialize new game session
    initialize_session(player_name)

    return redirect(url_for('game'))


@app.route('/game')
def game():
    """
    Main game interface - displays current card and prediction buttons.

    Returns:
        Rendered game page or redirect to landing if no session
    """
    # Check if player has started a game
    if 'player_name' not in session:
        return redirect(url_for('index'))

    # Prepare data for template
    game_data = {
        'player_name': session['player_name'],
        'current_card': card_to_display(session['current_card']),
        'current_card_value': session['current_card'],
        'wins': session['wins'],
        'losses': session['losses'],
        'total_games': session['total_games'],
        'win_percentage': calculate_win_percentage(session['wins'], session['total_games']),
        'last_result': session.get('last_result'),
        'last_card': card_to_display(session['last_card']) if session.get('last_card') else None
    }

    return render_template('game.html', **game_data)


@app.route('/predict', methods=['POST'])
def predict():
    """
    Process player's higher/lower prediction.

    Form Data:
        prediction (str): "higher" or "lower"

    Returns:
        Redirect to game page with updated state
    """
    # Ensure player has active session
    if 'player_name' not in session:
        return redirect(url_for('index'))

    # Get prediction from form
    prediction = request.form.get('prediction', '').lower()

    # Validate prediction
    if prediction not in ['higher', 'lower']:
        # Invalid prediction - don't process
        return redirect(url_for('game'))

    # Store current card for result display
    current_card = session['current_card']
    session['last_card'] = current_card

    # Draw next card from deck
    next_card, updated_deck = draw_card(session['deck'])

    # Evaluate prediction
    is_correct = evaluate_prediction(current_card, next_card, prediction)

    # Update statistics
    session['total_games'] += 1

    if is_correct:
        session['wins'] += 1
        session['last_result'] = 'win'
    else:
        session['losses'] += 1
        session['last_result'] = 'loss'

    # Update game state
    session['current_card'] = next_card
    session['deck'] = updated_deck

    # Mark session as modified (required for mutable objects)
    session.modified = True

    return redirect(url_for('game'))


@app.route('/reset', methods=['POST'])
def reset_game():
    """
    Reset game statistics and start fresh game.

    Returns:
        Redirect to game page with reset statistics
    """
    # Ensure player has active session
    if 'player_name' not in session:
        return redirect(url_for('index'))

    # Keep player name, reset everything else
    player_name = session['player_name']
    initialize_session(player_name)

    return redirect(url_for('game'))


@app.route('/stats')
def stats():
    """
    API endpoint for current session statistics.

    Returns:
        JSON object with current game statistics
    """
    # Check if player has started a game
    if 'player_name' not in session:
        return jsonify({'error': 'No active session'}), 404

    # Return current statistics as JSON
    return jsonify({
        'player_name': session['player_name'],
        'wins': session['wins'],
        'losses': session['losses'],
        'total_games': session['total_games'],
        'win_percentage': calculate_win_percentage(session['wins'], session['total_games']),
        'current_card': card_to_display(session['current_card'])
    })


# ============================================================================
# Application Entry Point
# ============================================================================

if __name__ == '__main__':
    # Configuration from environment variables for security
    DEBUG_MODE = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 'yes')
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    PORT = int(os.environ.get('FLASK_PORT', '5000'))

    # Security warning for production deployment
    if DEBUG_MODE and HOST == '0.0.0.0':
        logger.warning(
            "WARNING: Running with debug=True and host='0.0.0.0' exposes debug console "
            "to external networks. Only use this configuration in development environments. "
            "For production, set FLASK_DEBUG=False"
        )

    # Run Flask development server
    app.run(debug=DEBUG_MODE, host=HOST, port=PORT)
