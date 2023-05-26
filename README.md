# Quiz App

This is a Flask-based quiz application that allows users to create quizzes, add questions with multiple-choice options, and test their knowledge by answering the questions. The app uses SQLite for database storage.

## Features

- Create new quizzes
- Add questions with multiple-choice options
- Retrieve quizzes and questions
- Update quizzes and questions

## Installation

1. Clone the repository:

   ```shell
   git clone <repository_url>
   
Navigate to the project directory:
cd <project_directory>

Create a virtual environment (optional):
python -m venv venv

Activate the virtual environment (optional):
For Windows:
venv\Scripts\activate

For Unix or Linux:
source venv/bin/activate


Install the required dependencies:
pip install -r requirements.txt


Usage
Start the Flask development server:
python run.py
Open your web browser and navigate to http://localhost:5000 to access the Quiz App.

Use the app to create new quizzes, add questions, and test your knowledge by answering the questions.

File Structure:

`/app directory: Contains the Flask application code.
/__init__.py: Initializes the Flask app and sets up the database.
/urls.py: Defines the app's URL routes.
/views.py: Implements the views and logic for different routes.
/models.py: Defines the database models for quizzes and questions.
/templates directory: Contains the HTML templates for the app's views.
/index.html: Displays the quiz questions and options.
/base.html: Base template for other HTML files.
/new-quiz.html: Allows users to add new quizzes and questions.
/static directory: Contains the static files (e.g., CSS and JavaScript) for the app.
/js/index.js: Provides client-side functionality for the quiz app.
/run.py: Entry point for running the Flask app.
/requirements.txt: Specifies the required Python dependencies for the app.`

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Make sure to replace `<repository_url>` and `<project_directory>` with the appropriate values for your project.






