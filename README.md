# Rule Engine with AST

## Overview
This project is a simple 3-tier rule engine application developed using Python. It determines user eligibility based on attributes like age, department, income, spend, etc. The system uses an **Abstract Syntax Tree (AST)** to represent conditional rules, allowing dynamic creation, combination, and modification of these rules.

## Project Structure

```
Assignment-1/
├── main.py
├── requirements.txt
├── README.md
├── rule_engine/
│   ├── __init__.py
│   ├── ast_node.py
│   ├── combiner.py
│   ├── evaluator.py
│   └── parser.py
└── tests/
    ├── __init__.py
    ├── test_parser.py
    ├── test_combiner.py
    └── test_evaluator.py
```

### Modules:
- **main.py**: Entry point for the application, handles rule creation, combination, and evaluation.
- **rule_engine/ast_node.py**: Defines the `Node` class used to build the AST.
- **rule_engine/parser.py**: Parses a rule string and converts it into an AST.
- **rule_engine/combiner.py**: Combines multiple AST nodes into a single AST.
- **rule_engine/evaluator.py**: Evaluates an AST against a given data dictionary.
- **tests/**: Contains unit tests to validate the functionality of each module.

## Prerequisites

- **Python 3.6+**
- Virtual environment (`venv` or similar)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Assignment-1
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the rule engine:

1. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

3. **Output**:
   The program will create rules, combine them, and evaluate the sample data. It will print whether the sample data satisfies the combined rule (`True` or `False`).

## Examples

### Sample Rules:
- Rule 1: `(age > 30 AND department = Sales)`
- Rule 2: `(age < 25 AND department = Marketing)`

### Sample Data:
```python
sample_data = {
    "age": 28,
    "department": "Marketing",
    "salary": 60000,
    "experience": 3
}
```
The program combines these rules and evaluates them against the provided sample data.

## Running Tests

To run the unit tests:

```bash
pytest tests/
```

## Features

- **Dynamic AST Construction**: Supports creating ASTs for rules dynamically based on user input.
- **Rule Combination**: Combines multiple ASTs with `AND` or `OR` logic.
- **Rule Evaluation**: Evaluates combined rules against user data.

## Future Enhancements

- **Error Handling**: Better handling for malformed rule strings.
- **User-Defined Functions**: Support for adding user-defined functions to enhance rule flexibility.
- **Web API**: Expose functionality as a web API using Flask for remote usage.

## Contributing

Feel free to fork this project, make modifications, and submit a pull request. Contributions are welcome!

## License

This project is open-source and available under the MIT License.
