#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 19, 2025
# This program tells you the squares of the numbers up to the users number


def main():

    # Get the user number
    user_number_as_string = input("Enter a positive whole number: ")
    try:

        # Converts user num to int
        user_number_as_int = int(user_number_as_string)

        # If its negative this happens
        if user_number_as_int < 0:
            print((user_number_as_int), "is not a positive integer")

        # If not, code continues
        else:

            # calculate the square of each number from 0 to the user's number
            for counter in range(user_number_as_int + 1):
                power_of_two = counter ** 2
                print("{}^2 = {}".format(counter, power_of_two))

    # If user num is not a int this happens
    except Exception:
        print((user_number_as_string), "is not a positive integer")


if __name__ == "__main__":
    main()
