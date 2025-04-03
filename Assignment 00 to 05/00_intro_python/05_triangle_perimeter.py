# ANSI escape codes for bold and italic
BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"  # Reset text style


side1 = float(input(f"{BOLD}Enter the length of the first side: {RESET}"))
side2 = float(input(f"{BOLD}Enter the length of the second side: {RESET}"))
side3 = float(input(f"{BOLD}Enter the length of the third side: {RESET}"))

# Calculating perimeter
perimeter = side1 + side2 + side3

# Final Output
print(f"\n{BOLD}The perimeter of the triangle is {perimeter}{RESET}")
