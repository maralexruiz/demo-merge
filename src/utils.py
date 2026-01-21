"""
Utility functions for the calculator application.
These helper functions can be modified independently to demonstrate merge scenarios.
"""


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
