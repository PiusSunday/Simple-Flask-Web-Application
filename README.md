# Simple Flask Web Application

A basic Flask web application with three routes: Default (Index), Home and About. This project demonstrates the structure of a Flask application with template rendering and routing.


## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/simple-flask-web-app.git
   
   cd simple-flask-web-app
   
2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv_name
    source venv_name/bin/activate  # On Windows use: venv_name\Scripts\activate
   
3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
   
### Running the Application

1. **Start the Flask server:**

    ```bash
    python run.py

2. **Access the application: Open your web browser and navigate to http://127.0.0.1:5000/**

### Application Features

- Index Page: Accessible at **/**, displays a welcome message, and a button to retrieve data from the **/api/data** route and a link to the Home page.

- Home Page: Accessible at **/home**, displays a welcome message and a link to the About page.

- About Page: Accessible at **/about**, provides information about the application and a link back to the Home page.

### Project Files

- app/: Main application package.

  - __init__.py: Initializes the Flask application.

  - routes.py: Defines the routes and views for the application.

  - templates/: Contains HTML templates for rendering views.

    - index.html: Template for the Landing page.

    - home.html: Template for the Home page.

    - about.html: Template for the About page.

- run.py: The main script to run the Flask application.

- requirements.txt: Lists the Python dependencies for the project.

