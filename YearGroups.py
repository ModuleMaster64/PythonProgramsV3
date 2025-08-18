# Selection commands

# Subroutine to output Key Stage
def YearGroup(Year):
    if Year >= 1 and Year <13:
        print("You are in Key Stage 1-3!")
    else:
        print("You are in Key Stage 4-5!")

# Main program
YearGroup(10)
