"""
Hale Koa Hotel Booking System
Author: Richard Comins

A Flask web application for planning and calculating vacation costs
at the Hale Koa Hotel in Hawaii.
"""

from flask import Flask, render_template, request
from datetime import datetime, timedelta

# Create the Flask application
app = Flask(__name__)

# =============================================================================
# ROOM DATA - Single source of truth for room information
# =============================================================================
# Each room has a display name (key), nightly price, and image filename
ROOMS = {
    "Deluxe Ocean Front": {"price": 395, "image": "deluxe.png"},
    "Ilima Ocean West": {"price": 345, "image": "ilima.png"},
    "Ocean View": {"price": 295, "image": "ocean-view-room.png"},
    "Partial Ocean View": {"price": 219, "image": "partial-ocean-view-room.png"},
    "Resort View": {"price": 189, "image": "resort-view.png"},
}

def get_room_image(room_name: str) -> str:
    """
    Get the image filename for a given room name.

    Args:
        room_name: The display name of the room (e.g., "Deluxe Ocean Front")

    Returns:
        The image filename, or a default if room not found
    """
    room = ROOMS.get(room_name)
    if room:
        return room["image"]
    return "halekoa_Hotel.webp"  # Fallback to hotel image


#email configurations
# currently not working b/c needs app password and 2fa (we might do this)
"""
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# To loginto emailJS, use FTCC email and password

Once logged in, use the credentials below:
app.config['MAIL_USERNAME'] = 'rickytic12@gmail.com'
app.config['MAIL_PASSWORD'] = 'Capri1946'
service ID = service_i62n0vq
"""
# mailtrap settings (log into mailtrap.io with the rickytic12 gmail acct)
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '553f6d833a4c0e'
app.config['MAIL_PASSWORD'] = '221ee560e64e8b'
#mail = Mail(app)


#Create a route for index.html
@app.route("/", methods = ["GET" , "POST"])
def home_page():
    name = "Hale Koa Hotel"
    """
    #Pull name from the form
  if request.method == "POST":
        player_name = request.form.get("name")
        category = request.form.get("category")
        
        print(player_name)
        print(category)
        """
        
    return render_template("index.html", hotelname = name)

@app.route("/submit", methods = ["GET" , "POST"])
def submit():
    #name = "Drew"
    
    #Pull name from the form
    if request.method == "POST":
        player_name = request.form.get("name")
        category = request.form.get("category")
        
        print(player_name)
        print(category)
        
    return render_template("results.html", player_name = player_name,category = category)

@app.route('/rooms')
def rooms():
    return render_template('rooms.html')

@app.route('/trip_summary', methods=["GET", "POST"])
def trip_summary():
    if request.method == "POST":
        # Parse room selection (format: "Room Name|price")
        stay_raw = request.form.get("Rooms")
        room_name, room_price = stay_raw.split("|")
        room_price = float(room_price)
        room_price = round(room_price, 2)

        # Look up the room image using our helper function
        room_image = get_room_image(room_name)

        # Get form data
        traveler_name = request.form.get("name")
        ticket_price = int(request.form.get("ticketPrice"))
        num_nights = int(request.form.get("num_nights"))
        email = request.form.get("userEmail")

        # Parse activities (format: "activity_name|cost")
        activities_raw = request.form.getlist("activity")
        activities = []
        activityCost = 0
        for item in activities_raw:
            name, cost = item.split("|")
            activities.append(name)
            activityCost += int(cost)
        activity = ", ".join(activities) if activities else "None"

        # Calculate date range
        start_date = request.form.get("dates")
        end_date = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=num_nights)
        dates = f"{start_date} to {end_date.strftime('%Y-%m-%d')}"

        # Calculate costs
        cost_of_stay = num_nights * room_price
        sub_total = cost_of_stay + ticket_price + activityCost
        tax = round(sub_total * 0.1025, 2)
        total = sub_total + tax

    return render_template(
        'trip_summary.html',
        traveler_name=traveler_name,
        type=room_name,
        room_image=room_image,  # NEW: pass room image to template
        cost=room_price,
        dates=dates,
        num_nights=num_nights,
        cost_of_stay=cost_of_stay,
        ticket_price=ticket_price,
        activity=activity,
        activityCost=activityCost,
        sub_total=sub_total,
        tax=tax,
        total=total,
        email=email
    )




#run the app 
if __name__ == "__main__":
    app.run(debug = True)
