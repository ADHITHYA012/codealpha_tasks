import re

def review_code(filename):
    findings = []

    try:
        with open(filename, "r") as file:
            code = file.read()

        # Check for hardcoded passwords
        if re.search(r'password\s*=\s*[\'"].+[\'"]', code, re.IGNORECASE):
            findings.append("Hardcoded password detected")

        # Check for eval()
        if "eval(" in code:
            findings.append("Use of eval() detected")

        # Check for generic exception handling
        if re.search(r'except\s*:', code):
            findings.append("Generic exception handling detected")

        print("\n===== SECURITY REVIEW REPORT =====")

        if findings:
            for issue in findings:
                print(f"[WARNING] {issue}")
        else:
            print("No major security issues found.")

        print("\nRecommendations:")
        print("- Avoid hardcoded passwords")
        print("- Avoid eval()")
        print("- Use specific exception handling")
        print("- Validate user inputs")

    except FileNotFoundError:
        print("File not found.")

review_code("sample_code.py")