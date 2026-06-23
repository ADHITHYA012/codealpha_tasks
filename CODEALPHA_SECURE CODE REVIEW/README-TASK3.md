# CodeAlpha - Secure Coding Review

## Project Overview

This project performs a basic security audit on Python source code and identifies common coding vulnerabilities.

## Features

- Detects hardcoded passwords
- Detects use of eval()
- Detects generic exception handling
- Provides security recommendations

## Technologies Used

- Python 3
- Regular Expressions (re)

## How to Run

```bash
python secure_code_review.py
```

## Sample Output

```text
===== SECURITY REVIEW REPORT =====

[WARNING] Hardcoded password detected
[WARNING] Use of eval() detected
[WARNING] Generic exception handling detected

Recommendations:
- Avoid hardcoded passwords
- Avoid eval()
- Use specific exception handling
- Validate user inputs
```

## Learning Outcomes

- Understand common coding vulnerabilities
- Learn secure coding practices
- Perform static code analysis

## Author

CodeAlpha Internship Project