""" Programmer: Walter Reeves """
from collections import Counter

import math as math
import random as random

NUMBER_OF_BIRTHDAYS = 23
all_birthdays = []


def generate_birthday() -> tuple:
    """ Pseudo-randomly generates a birthday. """

    month_days = {"January": 31, "February": 28,
                  "March": 31, "April": 30, "May": 31, "June": 30,
                  "July": 31, "August": 31, "September": 30,
                  "October": 31, "November": 30, "December": 31}

    birth_month, max_days = random.choice(list(month_days.items()))
    birth_day = random.randint(1, max_days)

    return birth_month, birth_day


def display_birthdays() -> None:
    """ Displays all the birthdays. """
    global all_birthdays

    for item in range(0, len(all_birthdays)):
        month, day = all_birthdays[item]

        if item == len(all_birthdays) - 1:
            print(f"{month.title()} {day}.")
        else:
            print(f"{month.title()} {day}", end=", ")


def get_duplicate_birthdays() -> list:
    """ Gets the duplicate birthdays. """
    global all_birthdays

    return [day for day, num_duplicates in
            Counter(all_birthdays).items() if num_duplicates > 1]


def display_duplicate_birthdays() -> None:
    """ Displays the duplicate birthdays. """

    duplicates = get_duplicate_birthdays()

    print(f"In this simulation there are {len(duplicates)} "
          f"duplicate birthdays.\n")

    print("Duplicate birthdays:")
    for item in range(0, len(duplicates)):
        month, day = duplicates[item]

        if item == len(duplicates) - 1:
            print(f"{month.title()} {day}.\n")
        else:
            print(f"{month.title()} {day}", end=", ")


def get_all_birthdays(num_birthdays) -> None:
    """ Compiles all birthdays to a list. """

    for day in range(0, num_birthdays):
        all_birthdays.append(generate_birthday())


def single_iteration() -> None:
    """Displays the single iteration results"""

    number_of_birthdays = int(input("Enter the number of birthdays to generate "
                                    "between 1 and 100 > "))
    get_all_birthdays(num_birthdays=number_of_birthdays)

    display_birthdays()
    display_duplicate_birthdays()


def probability_calculation() -> None:
    """ Calculates the probability of many iterations. """
    global all_birthdays
    global NUMBER_OF_BIRTHDAYS

    notify_list = []

    duplicate_counter = 0

    iterations = int(input("How many iterations would you like to simulate? "))

    # Segments the iterations displayed.
    tenth_of_iterations = math.floor(iterations / 10)
    for num in range(1, 11):
        notify_list.append(tenth_of_iterations * num)

    for instance in range(0, iterations):
        all_birthdays = []

        # Check if duplicate
        get_all_birthdays(num_birthdays=NUMBER_OF_BIRTHDAYS)

        if len(get_duplicate_birthdays()) > 0:
            duplicate_counter += 1

        if instance in notify_list:
            print(instance)

    duplicate_probability = duplicate_counter / iterations * 100

    print(f"the probability of getting a duplicate in ", end="")
    print(f"{iterations} simulations is {round(duplicate_probability, 2)}%.")


# Displays Header
print("Welcome to the Birthday Paradox program!\n")
print("The first half of the program will generate a list of birthdays,")
print("and display how many duplicates there are.\n")
print("The second half of this program will display the probability")
print("of at least one duplicate birthday in a group of 23 people.\n")

single_iteration()
probability_calculation()
