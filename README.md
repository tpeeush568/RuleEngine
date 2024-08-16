# Rule Engine with AST

## Overview

The Rule Engine with Abstract Syntax Tree (AST) is a simple 3-tier application designed to determine user eligibility based on various attributes such as age, department, income, and spend. The system utilizes AST to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Features

- **Rule Creation:** Define rules using a simple string format.
- **Rule Evaluation:** Evaluate rules against JSON data.
- **API Endpoints:** Expose functionality through RESTful APIs.
- **Static UI:** Basic user interface to submit rules and data for evaluation.

## Installation

### Prerequisites

- Python 3.x
- MySQL or compatible database

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tpeeush568/RuleEngine.git
   cd RuleEngine
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**

   - **Windows:**

     ```bash
     .venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the Database**

   Create and Update the `.env` file with your database credentials:

   ```
   DB_HOST=localhost
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=rule_engine
   ```

   Ensure that the database and `rules` table exist. You may need to create the table manually if it does not exist:

   ```sql
   CREATE TABLE rules (
       id INT AUTO_INCREMENT PRIMARY KEY,
       rule_string TEXT NOT NULL
   );
   ```

6. **Run the Application**

   ```bash
   python api.py
   ```

   The application will be available at `http://127.0.0.1:5000`.

## API Endpoints

### **Create Rule**

- **URL:** `/rules`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "rule_string": "age > 30 AND salary > 50000"
  }
  ```

- **Response:**
  ```json
  {
    "ast": {
      "type": "operator",
      "value": "AND",
      "left": {
        "type": "operand",
        "value": "age > 30"
      },
      "right": {
        "type": "operand",
        "value": "salary > 50000"
      }
    }
  }
  ```

### **Evaluate Rule**

- **URL:** `/evaluate`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "rule_string": "age > 30 AND salary > 50000",
    "data": {
      "age": 35,
      "salary": 60000
    }
  }
  ```

- **Response:**
  ```json
  {
    "result": true
  }
  ```

## Static Files

- **Static UI:** The application includes a basic static UI located in the `static` directory. The `index.html` file provides forms to submit rules and evaluate them.

## Security and Performance

- **Security:** Ensure to sanitize and validate input to prevent SQL injection and other security vulnerabilities.
- **Performance:** Consider optimizing rule evaluation logic for large datasets.

