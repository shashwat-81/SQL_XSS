BLOCK_THRESHOLD = 5  # Number of malicious requests before blocking
LOG_FILE = 'logs/attack_logs.db'
# Configuration settings for the project
TARGET_URL = "http://127.0.0.1:5000/"  # Replace with your target website
SQLI_PATTERNS = ["'", '"', '--', '/*', '*/', ';', 'or 1=1']
XSS_PATTERNS = ["<script>", "</script>", "javascript:", "onerror=", "onload="]
SCRAPER_USER_AGENT = "WebsiteProtectionBot/1.0"  # For requests headers
