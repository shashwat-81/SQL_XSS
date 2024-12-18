from middleware.logger import log_attack
from flask import request

SQLI_PATTERNS = ["'", '"', '--', '/*', '*/', ';', 'or 1=1']
XSS_PATTERNS = ["<script>", "</script>", "javascript:", "onerror=", "onload="]
def request_filter(request_data):
    """
    Filter the request for potential malicious inputs.
    """
    for input_name, input_data in request_data.items():
        print(f"Checking input field '{input_name}': {input_data}")
        # Check for SQL Injection patterns
        if any(pattern in input_data for pattern in SQLI_PATTERNS):
            print(f"Blocked malicious input: {input_data}")
            log_attack(request.remote_addr, input_data, request_data)
            return False
        # Check for Cross-Site Scripting (XSS) patterns
        elif any(pattern in input_data for pattern in XSS_PATTERNS):
            print(f"Blocked malicious input: {input_data}")
            log_attack(request.remote_addr, input_data, request_data)
            return False
    return True
