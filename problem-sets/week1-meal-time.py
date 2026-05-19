#!/usr/bin/env python3

# Pseudo Code:
# 1. Get user input for a time
# 2. Output whether breakfast, lunch or dinner based on time
# - 7:00 - 8:00 breakfast
# - 12:00 - 13:00 lunch
# - 18:00 - 19:00 dinner


def main():
    time = input("What time is it? ")
    meal_time = convert(time)

    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= meal_time <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
