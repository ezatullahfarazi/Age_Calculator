# This program counts age of the user

# This function counts the age of the user
def count_age():
    # Asks the user for the year of birth
    year_of_birth = int(input("Enter your year of birth: "))
    # Asks the user for the current year
    current_year = int(input("Enter the current year: "))
    # Counts the age of the user
    age = current_year - year_of_birth
    # Returns the age of the user
    return age

if __name__ == "__main__":
    # Calls the function count_age and stores the result in the variable age
    age = count_age()
    # Prints the age of the user
    print(f"You are {age} years old.")