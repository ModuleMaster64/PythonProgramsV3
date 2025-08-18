def user_name(forename, last_name, year):
    username_out = year[2:4] + forename[0] + last_name

    print("Your user name is " + username_out)


    first_name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    joined = input("Enter the year you were born: ")

    user_name(first_name,surname,joined)
