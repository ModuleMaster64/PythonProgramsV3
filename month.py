# Selection commands

# Subroutine to validate month
def VaildMonth(Month):
    if Month > 0 and Month < 13:
        print("Vaild month!")
    else:
        print("Invalid!")

# Main program
VaildMonth(6)