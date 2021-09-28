# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/28/2021
# This is the Loop program
# The user enters in a positive integer
# The program tells the user the sum the numbers from 1 to the number typed in


def main():
    # this function uses a while loop and calculates the sum
    loop_counter = 0
    answer = 0

    # input
    number_as_string = input("Enter in a positive integer: ")
    print("")

    # process and output
    try:
        number_as_integer = int(number_as_string)
        while loop_counter < number_as_integer:
            loop_counter = loop_counter + 1
            answer = answer + loop_counter
        print(
            "The sum of all the positive numbers from 1 t0 {0} is {1}".format(
                number_as_string, answer
            )
        )

    except Exception:
        print("You didn’t enter in a positive integer.")

    print("\nDone")


if __name__ == "__main__":
    main()
