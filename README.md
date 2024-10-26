 
Rule Engine

Overview

The Rule Engine is a web application that allows users to create and evaluate rules based on specified criteria.
 It uses an Abstract Syntax Tree (AST) to parse and evaluate rules, making it suitable for scenarios like
 eligibility checks based on various attributes (e.g., age, department).


Codebase

The codebase is available on GitHub: https://github.com/Simsar7/rule_engine_project


Features

Create rules using a simple input form.
Evaluate rules against JSON data input.
Displays the generated AST for user-defined rules.


Design Choices
Architecture: The application follows a 3-tier architecture with a user interface (UI), an API layer,
              and a backend for data storage.
Database: SQLite is used for storing rules.
AST Implementation: The rule parsing and evaluation are handled through a custom AST representation,
                    allowing for flexible rule definitions.


Setup Instructions

1. Clone the Repository:
   
   git clone https://github.com/Simsar7/rule_engine_project.git
   cd rule_engine

2. Install Dependencies: Create a virtual environment and install the required dependencies:

    python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt


3. Run the Application: Start the Flask web server:

    python app.py
     
    The application will run on http://127.0.0.1:5000.

Dependencies
Flask: Web framework for building the application.
SQLite: Lightweight database for rule storage.
Docker: Optional for containerized deployment.

Usage

Access the application in your browser at http://127.0.0.1:5000.
Enter a rule in the specified format (e.g., age > 30 AND department = 'Sales') and submit.
View the generated AST and evaluate rules against provided data.




GitHub Link
Access the complete codebase on GitHub: https://github.com/Simsar7/rule_engine_project