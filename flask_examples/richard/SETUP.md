# Setup Guide
## Hale Koa Hotel Booking System

This guide walks you through setting up and running the Hale Koa Hotel Booking application.

---

## Prerequisites

Before you begin, ensure you have:
- **Python 3.8+** installed
- **pip** (Python package manager)
- A code editor (VS Code recommended)
- A web browser

### Verify Python Installation
```bash
python --version
# or on some systems:
python3 --version
```

Expected output: `Python 3.x.x`

---

## Installation Options

### Option A: Quick Setup (Global Installation)

Best for: Local laptop, quick testing

```bash
# 1. Navigate to the project directory
cd flask_examples/richard

# 2. Install Flask globally
pip install flask

# 3. Run the application
python app.py
```

### Option B: Virtual Environment (Recommended)

Best for: Other machines, isolated development

```bash
# 1. Navigate to the project directory
cd flask_examples/richard

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install flask

# 5. Run the application
python app.py
```

### Option C: Windows Batch Script

Use the provided batch script for Windows:

```batch
# Double-click startenv.bat
# or run from command prompt:
startenv.bat
```

---

## Running the Application

### Method 1: Direct Python Execution
```bash
python app.py
```

### Method 2: Flask CLI
```bash
# Set the Flask app (optional, auto-detected)
export FLASK_APP=app.py  # macOS/Linux
set FLASK_APP=app.py     # Windows

# Run Flask
flask run
```

### Method 3: With Custom Port
```bash
flask run -p 5001
```

### Expected Output
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```

---

## Accessing the Application

Open your web browser and navigate to:

| URL | Page |
|-----|------|
| http://127.0.0.1:5000 | Home page |
| http://127.0.0.1:5000/rooms | Room selection & booking form |

---

## Project Files Overview

### Core Application Files

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with routes and logic |
| `requirements.txt` | Python dependencies (create if needed) |

### Templates (Jinja2 HTML)

| File | Route | Purpose |
|------|-------|---------|
| `templates/index.html` | `/` | Landing page with Hawaii background |
| `templates/ROOMS.html` | `/rooms` | Room gallery and booking form |
| `templates/results.html` | `/submit` | Form submission results |
| `templates/trip_summary.html` | `/trip_summary` | Cost breakdown display |

### Static Assets

| File | Purpose |
|------|---------|
| `static/deluxe.png` | Deluxe Ocean Front room image |
| `static/ilima.png` | Ilima Ocean West room image |
| `static/ocean view room.png` | Ocean View room image |
| `static/partial ocean view room.png` | Partial Ocean View room image |
| `static/resort view.png` | Resort View room image |
| `static/rainbow_map.jpg` | Homepage background image |
| `static/halekoa_Hotel.webp` | Hotel branding image |

---

## Testing the Application

### Basic Flow Test

1. **Visit Home Page**
   - Go to http://127.0.0.1:5000
   - Verify background image loads
   - Click "Rooms" link

2. **Browse Rooms**
   - Verify all 5 room images display
   - Check room type dropdown has all options

3. **Submit Booking**
   - Fill out the form:
     - Name: `Test User`
     - Date: Tomorrow's date
     - Ticket Price: `500`
     - Room: `Deluxe Ocean Front`
     - Nights: `3`
     - Activities: Check `Surfing` and `Luau`
     - Email: `test@example.com`
   - Click Submit

4. **Verify Trip Summary**
   - Check name displays correctly
   - Verify date range calculation
   - Confirm cost breakdown:
     - Room: $395.00/night
     - Stay: $1,185.00 (3 nights)
     - Activities: $255.00
     - Subtotal: $1,940.00
     - Tax (10.25%): $198.85
     - Total: $2,138.85

### Test Scenarios

| Scenario | Input | Expected |
|----------|-------|----------|
| No activities | Leave unchecked | Activities: "None", Cost: $0 |
| Single night | Nights = 1 | Stay = room rate |
| All activities | Select all 4 | Activity cost = $479 |
| Cheapest room | Resort View | $189/night |

---

## EmailJS Configuration

The application uses EmailJS for sending confirmation emails.

### Current Configuration (in ROOMS.html)
```javascript
emailjs.init("ctanCThOR0TUbRkv-");
const SERVICE_ID = "service_i62n0vq";
const TEMPLATE_ID = "template_wmznpsj";
```

### To Use Your Own EmailJS Account:
1. Sign up at [emailjs.com](https://www.emailjs.com/)
2. Create an email service
3. Create an email template with these variables:
   - `to_email`, `name`, `dates`, `ticketPrice`
   - `roomType`, `roomCost`, `nights`, `costOfStay`
   - `aname`, `acost`, `subTotal`, `tax`, `totalCostOfStay`
4. Update the credentials in `templates/ROOMS.html`

---

## Troubleshooting

### Python/Flask Issues

| Problem | Solution |
|---------|----------|
| `python: command not found` | Install Python or use `python3` |
| `No module named flask` | Run `pip install flask` |
| `Address already in use` | Use different port: `flask run -p 5001` |

### VS Code Issues

If Flask stops working in VS Code:
1. Press `Ctrl+Shift+P` (Command Palette)
2. Type "Python: Select Interpreter"
3. Select the correct Python environment
4. Restart the terminal

### Template Not Found

Ensure you're running from the correct directory:
```bash
# Correct:
cd flask_examples/richard
python app.py

# Incorrect (wrong directory):
python flask_examples/richard/app.py  # Templates won't be found!
```

### Images Not Loading

1. Check file names match exactly (case-sensitive)
2. Verify files exist in `static/` folder
3. Check browser developer tools (F12) for 404 errors

---

## Development Tips

### Enable Debug Mode (already enabled)
Debug mode is enabled in `app.py`:
```python
app.run(debug=True)
```

Benefits:
- Auto-reload on code changes
- Detailed error pages
- Debugger console

### View Flask Routes
```bash
flask routes
```

### Check Application Logs
Watch the terminal for:
- Request logs
- Form data (printed to console)
- Error messages

---

## Creating requirements.txt

If you need to share this project:

```bash
# Generate requirements file
pip freeze > requirements.txt

# Or manually create with just Flask:
echo "flask" > requirements.txt
```

To install from requirements:
```bash
pip install -r requirements.txt
```

---

## Security Notes

**For Development Only:**
- Debug mode is enabled (never use in production)
- Email credentials are visible in code
- No HTTPS encryption
- No input sanitization

**For Production:**
- Set `debug=False`
- Use environment variables for secrets
- Enable HTTPS
- Add server-side validation
- Use a production WSGI server (Gunicorn, uWSGI)

---

## Next Steps

After getting the application running:

1. Read the [Product Requirements Document](Product_Requirements_Doc.md)
2. Explore the code in `app.py`
3. Modify templates to customize the look
4. Add new features (see PRD for enhancement ideas)
5. Try adding server-side email with Flask-Mail

---

## Getting Help

- Check the [README.md](README.md) for overview
- Review [Product_Requirements_Doc.md](Product_Requirements_Doc.md) for specifications
- Ask your instructor for assistance
