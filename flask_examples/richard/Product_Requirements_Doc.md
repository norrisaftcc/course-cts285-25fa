# Product Requirements Document (PRD)
## Hale Koa Hotel Booking System

**Project Name:** Island Flask App - Hale Koa Hotel Booking
**Author:** Richard Comins
**Version:** 1.0 (MVP)
**Last Updated:** December 2025
**Status:** Functional MVP with planned enhancements

---

## 1. Executive Summary

### 1.1 Product Overview
The Hale Koa Hotel Booking System is a Flask-based web application that allows users to plan and calculate the cost of a vacation at the Hale Koa Hotel in Hawaii. The application demonstrates fundamental web development concepts including form handling, data processing, date calculations, and email integration.

### 1.2 Purpose
This project serves as an educational example for CTS285 students, demonstrating:
- Flask web framework fundamentals
- HTML form creation and processing
- Server-side data validation and calculations
- Client-side JavaScript integration
- Third-party API integration (EmailJS)
- Template rendering with Jinja2

### 1.3 Target Audience
- **Primary:** Students learning Flask web development
- **Secondary:** Instructors demonstrating real-world web application patterns
- **Tertiary:** Users planning a hypothetical trip to the Hale Koa Hotel

---

## 2. User Stories

### 2.1 Core User Stories (MVP)

| ID | As a... | I want to... | So that... | Priority |
|----|---------|--------------|------------|----------|
| US-01 | Visitor | View the hotel landing page | I can learn about the Hale Koa Hotel | Must Have |
| US-02 | Visitor | See available room types with images | I can visualize my accommodation options | Must Have |
| US-03 | Guest | Enter my name and travel dates | My booking is personalized | Must Have |
| US-04 | Guest | Select a room type with pricing | I can choose accommodations within my budget | Must Have |
| US-05 | Guest | Specify the number of nights | The system can calculate my total stay cost | Must Have |
| US-06 | Guest | Select activities to add to my trip | I can plan a complete vacation experience | Must Have |
| US-07 | Guest | See a detailed trip summary | I understand the full cost breakdown | Must Have |
| US-08 | Guest | Receive an email confirmation | I have a record of my trip details | Should Have |

### 2.2 Enhanced User Stories (Future)

| ID | As a... | I want to... | So that... | Priority |
|----|---------|--------------|------------|----------|
| US-09 | Guest | Choose my preferred travel style | I can get tailored recommendations | Could Have |
| US-10 | Guest | Add comments to my booking | I can communicate special requests | Could Have |
| US-11 | Admin | View booking submissions | I can manage reservations | Won't Have (MVP) |

---

## 3. Functional Requirements

### 3.1 Landing Page (`/`)
- **FR-01:** Display welcome message with hotel branding
- **FR-02:** Show background image of Hawaii/hotel location
- **FR-03:** Provide navigation link to room selection page
- **FR-04:** Support both GET and POST methods

### 3.2 Room Selection Page (`/rooms`)
- **FR-05:** Display all available room types with images:
  - Deluxe Ocean Front ($395/night)
  - Ilima Ocean West ($345/night)
  - Ocean View ($295/night)
  - Partial Ocean View ($219/night)
  - Resort View ($189/night)

- **FR-06:** Provide booking form with the following fields:
  | Field | Type | Required | Validation |
  |-------|------|----------|------------|
  | Name | Text | Yes | Non-empty |
  | Travel Start Date | Date | Yes | Valid date |
  | Ticket Price | Number | Yes | Positive integer |
  | Room Type | Dropdown | Yes | Valid selection |
  | Number of Nights | Number | Yes | Positive integer |
  | Activities | Checkboxes | No | Multiple selection |
  | Travel Style | Radio | No | Single selection |
  | Email | Email | Yes | Valid email format |
  | Comments | Textarea | No | 500 char max |

- **FR-07:** Available activities with pricing:
  - Surfing ($125)
  - Hiking ($75)
  - Snorkeling ($149)
  - Attend a Luau ($130)

- **FR-08:** Embed promotional YouTube video

### 3.3 Trip Summary Page (`/trip_summary`)
- **FR-09:** Display personalized trip summary with traveler name
- **FR-10:** Calculate and display:
  - Travel date range (start date + number of nights)
  - Room type and nightly rate
  - Ticket price
  - Selected activities and their costs
  - Total cost of stay (nights × room rate)
  - Subtotal (stay + tickets + activities)
  - Tax (10.25% of subtotal)
  - Grand total
- **FR-11:** Format all currency values with comma separators and 2 decimal places
- **FR-12:** Provide navigation link back to home page

### 3.4 Email Integration
- **FR-13:** Send trip summary email via EmailJS on form submission
- **FR-14:** Include all booking details in email template
- **FR-15:** Continue to Flask route regardless of email success/failure

---

## 4. Technical Requirements

### 4.1 Technology Stack
| Component | Technology | Version |
|-----------|------------|---------|
| Backend Framework | Flask | 3.x |
| Template Engine | Jinja2 | (bundled) |
| Programming Language | Python | 3.8+ |
| Frontend | HTML5, CSS3, JavaScript | - |
| Email Service | EmailJS | 3.x |
| Development Server | Werkzeug | (bundled) |

### 4.2 Application Architecture

```
flask_examples/richard/
├── app.py                 # Main Flask application
├── README.md              # Project documentation
├── startenv.bat           # Windows environment setup
├── static/                # Static assets
│   ├── deluxe.png
│   ├── ilima.png
│   ├── ocean view room.png
│   ├── partial ocean view room.png
│   ├── resort view.png
│   ├── halekoa_Hotel.webp
│   ├── rainbow_map.jpg
│   └── ...
└── templates/             # Jinja2 templates
    ├── index.html         # Landing page
    ├── ROOMS.html         # Room selection & booking form
    ├── results.html       # Form submission results
    └── trip_summary.html  # Trip cost calculation
```

### 4.3 Route Specifications

| Route | Method(s) | Handler | Template | Description |
|-------|-----------|---------|----------|-------------|
| `/` | GET, POST | `home_page()` | `index.html` | Landing page |
| `/rooms` | GET | `rooms()` | `ROOMS.html` | Room selection |
| `/submit` | GET, POST | `submit()` | `results.html` | Legacy form handler |
| `/trip_summary` | GET, POST | `trip_summary()` | `trip_summary.html` | Cost calculation |

### 4.4 Data Flow

```
User visits homepage (/)
         │
         ▼
Clicks "Rooms" link
         │
         ▼
Views room images & fills booking form (/rooms)
         │
         ▼
JavaScript intercepts submit
         │
         ├──► EmailJS sends email (async)
         │
         ▼
Form POSTs to /trip_summary
         │
         ▼
Flask calculates costs:
  • Parse room type and price
  • Calculate date range
  • Sum activity costs
  • Apply 10.25% tax
  • Compute grand total
         │
         ▼
Render trip_summary.html with all values
```

### 4.5 Calculation Logic

```python
# Room cost calculation
cost_of_stay = num_nights * room_price

# Date range calculation
end_date = start_date + timedelta(days=num_nights)

# Activity cost (sum of selected activities)
activity_cost = sum(cost for name, cost in selected_activities)

# Final calculations
sub_total = cost_of_stay + ticket_price + activity_cost
tax = sub_total * 0.1025  # Hawaii lodging tax rate
total = sub_total + tax
```

---

## 5. User Interface Requirements

### 5.1 Landing Page
- Full-screen background image (`rainbow_map.jpg`)
- White text on transparent background
- Prominent "Rooms" navigation link (lime green)
- Welcoming headline message

### 5.2 Room Selection Page
- Room images displayed in bordered table
- Booking form with white background, rounded corners
- Color-coded travel style radio buttons:
  - Luxury: Tomato red (#ff6347)
  - Budget: Steel blue (#4682b4)
  - Adventure: Lime green (#32cd32)
- Cyan submit button (#00ced1)
- Orange-red reset button (#ff4500)
- Green comment textarea (lightgreen)

### 5.3 Trip Summary Page
- Clean layout with navigation
- Currency formatting with commas and decimals
- Bold grand total for emphasis
- Return link to home page

---

## 6. EmailJS Integration

### 6.1 Configuration
```javascript
// Service configuration
emailjs.init("ctanCThOR0TUbRkv-");
const SERVICE_ID = "service_i62n0vq";
const TEMPLATE_ID = "template_wmznpsj";
```

### 6.2 Email Template Variables
| Variable | Description |
|----------|-------------|
| `to_email` | Recipient email address |
| `name` | Traveler's name |
| `dates` | Travel date range |
| `ticketPrice` | Airfare cost |
| `roomType` | Selected room type |
| `roomCost` | Room price per night |
| `nights` | Number of nights |
| `costOfStay` | Total lodging cost |
| `aname` | Selected activity names |
| `acost` | Total activity cost |
| `subTotal` | Pre-tax total |
| `tax` | Tax amount |
| `totalCostOfStay` | Grand total |
| `comments` | User comments |

---

## 7. Room Inventory

| Room Type | Nightly Rate | Image File |
|-----------|--------------|------------|
| Deluxe Ocean Front | $395 | `deluxe.png` |
| Ilima Ocean West | $345 | `ilima.png` |
| Ocean View | $295 | `ocean view room.png` |
| Partial Ocean View | $219 | `partial ocean view room.png` |
| Resort View | $189 | `resort view.png` |

---

## 8. Activity Catalog

| Activity | Price | Value String |
|----------|-------|--------------|
| Surfing | $125 | `surfing|125` |
| Hiking | $75 | `hiking|75` |
| Snorkeling | $149 | `snorkeling|149` |
| Attend a Luau | $130 | `luau|130` |

---

## 9. Testing Scenarios

### 9.1 Basic Flow Test
1. Navigate to home page (`/`)
2. Click "Rooms" link
3. Fill form with valid data:
   - Name: "Test User"
   - Date: Tomorrow's date
   - Ticket Price: 500
   - Room: Deluxe Ocean Front
   - Nights: 3
   - Activities: Surfing, Luau
   - Email: test@example.com
4. Submit form
5. Verify trip summary shows:
   - Dates: Start to Start+3 days
   - Room cost: $395.00/night
   - Stay cost: $1,185.00
   - Activity cost: $255.00
   - Subtotal: $1,940.00
   - Tax: $198.85
   - Total: $2,138.85

### 9.2 Edge Cases
| Test | Input | Expected Result |
|------|-------|-----------------|
| No activities | Leave all unchecked | Activities: "None", Cost: $0 |
| Single night | nights = 1 | Stay cost = room rate |
| All activities | Select all 4 | Activity cost = $479 |
| Minimum room | Resort View | $189/night |

---

## 10. Known Limitations & Future Enhancements

### 10.1 Current Limitations
1. No input validation on server side (relies on HTML5 validation)
2. No user authentication or session management
3. No database persistence (data lost on page refresh)
4. Email sending is client-side only (EmailJS)
5. No error handling for invalid form data
6. Travel style radio buttons not used in calculations
7. Comments field not displayed in summary

### 10.2 Planned Enhancements (Future Versions)

#### Phase 2: Enhanced Features
- [ ] Server-side form validation
- [ ] Flask-Mail integration for server-side email
- [ ] Database storage (SQLite/PostgreSQL)
- [ ] Booking confirmation numbers
- [ ] Admin dashboard for viewing bookings

#### Phase 3: Advanced Features
- [ ] User authentication and accounts
- [ ] Multiple room booking
- [ ] Real-time availability checking
- [ ] Payment integration (Stripe)
- [ ] Responsive mobile design
- [ ] Accessibility improvements (ARIA labels)

---

## 11. Glossary

| Term | Definition |
|------|------------|
| **Flask** | Python micro web framework |
| **Jinja2** | Template engine used by Flask |
| **EmailJS** | Client-side email service API |
| **Hale Koa** | Military resort hotel in Waikiki, Hawaii |
| **MVP** | Minimum Viable Product |
| **PRD** | Product Requirements Document |

---

## 12. Appendix

### A. Sample Form Data Structure
```python
# Request form data received at /trip_summary
{
    "name": "John Doe",
    "dates": "2025-06-15",
    "ticketPrice": "450",
    "Rooms": "Deluxe Ocean Front|395",
    "num_nights": "5",
    "activity": ["surfing|125", "snorkeling|149"],
    "style": "luxury",
    "userEmail": "john@example.com",
    "comments": "Anniversary trip"
}
```

### B. Rendered Template Variables
```python
# Variables passed to trip_summary.html
{
    "type": "Deluxe Ocean Front",
    "cost": 395.00,
    "traveler_name": "John Doe",
    "dates": "2025-06-15 to 2025-06-20",
    "ticket_price": 450,
    "activity": "surfing, snorkeling",
    "activityCost": 274,
    "cost_of_stay": 1975.00,
    "sub_total": 2699.00,
    "tax": 276.65,
    "total": 2975.65,
    "email": "john@example.com"
}
```
