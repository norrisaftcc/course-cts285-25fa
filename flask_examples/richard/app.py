"""
To-Do
arrival date, departure date, calc num of nights based on values. incorporate check boxes with url's 
end goal--email trip summary to individual.  Add email address to form.

 
    """

from flask import Flask, render_template, request
from datetime import datetime, timedelta #for date calculations

#from flask_mail import Mail, Message

#create a flask app object
app =   Flask(__name__)


ROOM_TYPE_IMAGE = {
    "deluxe": "static/delux.png",
    "ilima": "static/ilima.png",
    "ocean view":"static/ocean view room.png",
    "partial ocean view": "static/partial ocean view room.png",
    "resort view": "static/resort view.png",
}

def image_url_for_room(room_type: str) -> str:
    # Fallback image if unknown type
    filename = ROOM_TYPE_IMAGE.get(room_type, "rooms/default.png")
    rel = url_for('static', filename=filename)  # e.g., /static/rooms/studio.png
    # Make it absolute (https://yourdomain.com/static/rooms/studio.png)
    return f"{request.url_root.rstrip('/')}{rel}"


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

@app.route('/trip_summary', methods = ["GET" , "POST"])
def trip_summary():
    if request.method == "POST":
        stay_raw = request.form.get("Rooms")  # looks like "Deluxe Ocean Front|249.99"
        room_name, room_price = stay_raw.split("|")
        room_price = float(room_price)
        room_price = round(room_price,2)
        dates = request.form.get("dates")
        ticket_price = int(request.form.get("ticketPrice")) 
        # Get all selected activities (checkboxes with same name return a list)
        activities_raw = request.form.getlist("activity")

        # Parse each activity and calculate total cost
        activities = []
        activityCost = 0
        for item in activities_raw:
            name, cost = item.split("|")
            activities.append(name)
            activityCost += int(cost)

        # Join activity names for display
        activity = ", ".join(activities) if activities else "None"
        
        traveler_name = request.form.get("name")
        num_nights = int(request.form.get("num_nights"))
        cost_of_stay = num_nights * room_price
        # copilot suggestion: use datetime and timedelta to calculate end date
        start_date = request.form.get("dates") 
        end_date = datetime.strptime(start_date, "%Y-%m-%d") + timedelta (days=num_nights)
        dates = f"{start_date} to {end_date.strftime('%Y-%m-%d')}"
        
        email = request.form.get("userEmail")
       
        sub_total = cost_of_stay + ticket_price + activityCost
        
        tax = sub_total * .1025
        tax = round(tax,2)
        total = sub_total + tax
        #Formulate the email message
        #msg = Message("This is a test",sender = "rickytic12@gmail.com", recipients = [email])
        #msg.body = "TEST 1"
        #mail.send(msg)
        
    return render_template('trip_summary.html', type = room_name, cost = room_price, traveler_name = traveler_name,cost_of_stay = cost_of_stay,dates = dates,email = email,
                           ticket_price = ticket_price, activity = activity, activityCost = activityCost, sub_total = sub_total,
                           tax = tax, total = total)




#run the app 
if __name__ == "__main__":
    app.run(debug = True)
