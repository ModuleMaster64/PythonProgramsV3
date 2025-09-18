import re

def is_valid_name(name):
    # Will only allow letters, spaces, hyphens, and apostrophes
    return re.fullmatch(r"[A-Za-z\s\-']+", name) is not None

# 👤 Collect and validate the users input
surname = input("Enter your surname: ")
forename = input("Enter your forename: ")

if not (is_valid_name(surname) and is_valid_name(forename)):
    print("\n⚠️ This was a invalid input. Please use only letters, spaces, hyphens, or apostrophes!")
else:
    full_name = f"{forename} {surname}"
    print("\n--- User Details ---")
    print(f"Full Name: {full_name}")
