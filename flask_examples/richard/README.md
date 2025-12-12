# Hale Koa Hotel Booking System
## A Flask Web Application by Richard Comins

A vacation planning and cost calculator web application built with Flask, demonstrating fundamental web development concepts for CTS285 students.

---

## Overview

This application simulates a hotel booking system for the Hale Koa Hotel in Hawaii. Users can:
- Browse available room types with images
- Select travel dates and accommodations
- Choose optional activities
- Receive a detailed trip cost breakdown
- Get an email confirmation of their booking

## Features

| Feature | Description |
|---------|-------------|
| Room Gallery | Visual display of 5 room types with pricing |
| Booking Form | Comprehensive form with validation |
| Cost Calculator | Automatic calculation of stay, activities, and taxes |
| Email Integration | EmailJS-powered confirmation emails |
| Trip Summary | Detailed breakdown of all costs |

## Quick Start

```bash
# Navigate to the project directory
cd flask_examples/richard

# Install Flask (if not already installed)
pip install flask

# Run the application
flask run
# or
python app.py
```

Then open your browser to: **http://127.0.0.1:5000**

## Project Structure

```
richard/
├── app.py                      # Main Flask application (143 lines)
├── README.md                   # This file
├── Product_Requirements_Doc.md # Detailed specifications
├── SETUP.md                    # Installation guide
├── startenv.bat                # Windows environment setup
├── static/                     # Static assets
│   ├── deluxe.png             # Room images
│   ├── ilima.png
│   ├── ocean view room.png
│   ├── partial ocean view room.png
│   ├── resort view.png
│   ├── halekoa_Hotel.webp     # Hotel branding
│   └── rainbow_map.jpg        # Background image
└── templates/                  # Jinja2 HTML templates
    ├── index.html             # Landing page
    ├── ROOMS.html             # Room selection & booking form
    ├── results.html           # Form submission results
    └── trip_summary.html      # Cost calculation display
```

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET, POST | Landing page with hotel welcome |
| `/rooms` | GET | Room gallery and booking form |
| `/trip_summary` | POST | Calculate and display trip costs |
| `/submit` | POST | Legacy form handler |

## Room Pricing

| Room Type | Nightly Rate |
|-----------|--------------|
| Deluxe Ocean Front | $395 |
| Ilima Ocean West | $345 |
| Ocean View | $295 |
| Partial Ocean View | $219 |
| Resort View | $189 |

## Activities

| Activity | Price |
|----------|-------|
| Surfing | $125 |
| Hiking | $75 |
| Snorkeling | $149 |
| Attend a Luau | $130 |

## How It Works

1. **Home Page** - User sees welcome message with Hawaii background
2. **Room Selection** - User views room images and fills out booking form
3. **Form Submission** - JavaScript sends email via EmailJS, then POSTs to Flask
4. **Trip Summary** - Flask calculates all costs and renders summary:
   - Room cost = nights × nightly rate
   - Activity cost = sum of selected activities
   - Subtotal = room + tickets + activities
   - Tax = 10.25% of subtotal
   - **Total = subtotal + tax**

## Technologies Used

- **Python 3.x** - Programming language
- **Flask** - Web framework
- **Jinja2** - Template engine
- **HTML5/CSS3** - Frontend markup and styling
- **JavaScript** - Client-side interactivity
- **EmailJS** - Email delivery service

## Educational Value

This project demonstrates:
- Flask routing and view functions
- HTML form creation and processing
- Jinja2 template rendering with variables
- Python datetime calculations
- Client-side JavaScript integration
- Third-party API integration (EmailJS)
- CSS inline styling techniques

## Documentation

- [Product Requirements Document](Product_Requirements_Doc.md) - Detailed specifications
- [Setup Guide](SETUP.md) - Installation and configuration instructions

## Troubleshooting

### VS Code Python Interpreter Issues
If Flask stops working in VS Code:
1. Press `Ctrl+Shift+P` (Command Palette)
2. Type "Python: Select Interpreter"
3. Choose the global Python installation

### Common Issues
| Problem | Solution |
|---------|----------|
| Module not found | Run `pip install flask` |
| Port already in use | Kill other Flask instances or use `flask run -p 5001` |
| Template not found | Ensure you're running from the `richard/` directory |

## Author

**Richard Comins**
CTS285 - Web Application Development

---

*This project is part of the Flask Examples collection for educational purposes.*
