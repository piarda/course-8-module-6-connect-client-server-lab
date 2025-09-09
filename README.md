# Lab: Building a Front-to-Back Event Catalog

This is a lightweight full-stack web application that allows users to view and submit events. It demonstrates interaction between a JavaScript front end and a Flask back end using HTTP requests and JSON.

## Features:
- View a list of events served from the back end
- Submit a new event using a form
- New events appear instantly on the page without reloading
- Data is exchanged via JSON using the Fetch API
- CORS is enabled to support cross-origin requests

## Project Structure:
main/
├── server.py          # Flask server
├── data.py            # Event storage logic
tests/
├── test_app.py        # Pytest test suite
client/
├── index.html         # Front-end HTML
├── script.js          # JavaScript logic
├── styles.css         # CSS styles

## Running the Application:
Start the Flask Server from the main folder directory:
    python3 server.py
This runs the server on http://localhost:5001.

Start the Frontend Server from the client folder directory:
    python3 -m http.server 8000
Visit the app in your browser at http://localhost:8000.

## Running Tests:
From the project root:
    pytest tests/test_app.py


-----------------------------------

## Learning Goals

- Serve a homepage using Flask
- Create API routes that return and accept JSON
- Handle GET and POST requests on the back end
- Connect a Flask back end to a static front end
- Pass all provided back end tests

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo-url>
cd course-8-module-6-connect-client-server-lab
```

### 2. Create Your Environment

**Using Pipenv:**
```bash
pipenv install
pipenv shell
```

---

## Running the App

```bash
python server.py
```

Then open `client/index.html` in your browser to view the frontend.

---

## Running the Tests

To check your work, run:

```bash
pytest
```

All tests must pass to complete the lab.

---

## Your Tasks

- [ ] Implement the `/` route to return a welcome message in JSON
- [ ] Implement a `GET /events` route that returns all event data
- [ ] Implement a `POST /events` route that accepts a new event and returns it with status 201
- [ ] Return a `400 Bad Request` if required data is missing in a POST

---

## File Structure

```
.
├── client/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── server.py
├── tests/
│   └── test_app.py
├── Pipfile
├── Pipfile.lock
├── README.md
```

---

Good luck! 🚀
