"""
Utility functions for the calculator application.
These helper functions can be modified independently to demonstrate merge scenarios.
"""
import hashlib


def display_banner():
    """Display the application banner."""
    banner = """
    ╔══════════════════════════════════════════════════╗
    ║          Demo Merge Calculator v1.0              ║
    ║     Testing Git Merge Strategies                 ║
    ╚══════════════════════════════════════════════════╝
    """
    print(banner)


def get_user_input(prompt):
    """
    Get numeric input from the user.

    Args:
        prompt: The prompt to display to the user

    Returns:
        float: The numeric value entered by the user

    Raises:
        ValueError: If the input is not a valid number
    """
    user_input = input(prompt).strip()
    try:
        return float(user_input)
    except ValueError:
        raise ValueError(f"'{user_input}' is not a valid number")


def format_result(result, decimals=2):
    """
    Format a numeric result for display.

    Args:
        result: The numeric result to format
        decimals: Number of decimal places (default: 2)

    Returns:
        str: Formatted result string
    """
    return f"{result:.{decimals}f}"


def greet_user(name: str = "User"):
    """Returns a personalized greeting message."""
    return f"Hello, {name}! Hope you are having a productive day."


def calculate_tax(tax: int, tax_rate=0.016):
    """Calculate tax based on the given tax rate."""
    return tax * tax_rate


def generate_product_code(product_id: int, prefix="PROD"):
    """Generate a product code with a given prefix."""
    bytes_to_hash = str(product_id).encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(bytes_to_hash)
    hex_hash = hasher.hexdigest()
    return f"{prefix}-{hex_hash[:8]}"
