# System Configuration Mock Constants
DEFAULT_LOCALE = "en_US"
DEFAULT_CURRENCY = "USD"
MAX_LOGIN_ATTEMPTS = 5
SESSION_TIMEOUT_MINUTES = 30

# User Roles & Statuses
ROLE_ADMIN = "ADMIN"
ROLE_EDITOR = "EDITOR"
ROLE_VIEWER = "VIEWER"

STATUS_ACTIVE = "active"
STATUS_INACTIVE = "inactive"
STATUS_PENDING = "pending"

# Mock Company Data
MOCK_COMPANY_NAME = "Acme Corporation"
MOCK_TAX_ID = "12-3456789"
MOCK_COMPANY_ADDRESS = "123 Business Ave, Tech City, CA 94043"

# Mock Invoice Data
INVOICE_PREFIX = "INV-2026-"
TAX_RATE_MULTIPLIER = 0.15  # 15% Tax
MIN_INVOICE_AMOUNT = 5.00

# Error Messages
ERR_USER_NOT_FOUND = "User account does not exist."
ERR_INVOICE_EXPIRED = "This invoice is no longer valid for payment."
ERR_PERMISSION_DENIED = "You do not have access to this resource."

# List of Mock Domains (Useful for generating random emails)
MOCK_DOMAINS = ["example.com", "testmail.org", "company.net", "service.io"]
