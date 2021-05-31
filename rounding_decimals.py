#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program rounds an inputted number to a selected amount of decimals


def rounding(number_list):
    # this function rounds the inputted number

    number_list[0] = number_list[0] * (10 ** number_list[1]) + 0.5
    number_list[0] = int(number_list[0])
    number_list[0] = number_list[0] * (10 ** (-1 * number_list[1]))


def main():
    # this function receives input and calls another function

    # input
    number_list = []
    number_string = input("Enter a decimal number: ")
    decimals_string = input("How many decimals do you want to round to?: ")
    try:
        number = float(number_string)
        decimals = int(decimals_string)
        number_list.append(number)
        number_list.append(decimals)

        # output & call function
        rounding(number_list)
        if decimals >= 0:
            print("\n{0} rounded to {1} decimal place(s) is {2}\nDone.".format
                  (number_string, decimals_string, number_list[0]))
        else:
            print("Invalid Input\nDone.")
    except (Exception):
        print("Invalid Input\nDone.")


if __name__ == "__main__":
    main()
