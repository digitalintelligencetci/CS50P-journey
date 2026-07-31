#!/usr/bin/env python3

# Pseudo code:
# Prompt user for a time in 24 hour format (#:## or ##:##)
# Output what shift it is


def main():
    time = input("What time is it? ")
    shift_times = convert(time)

    if shift_times > 24.0:
        print("Off duty")
    elif 6.0 <= shift_times <= 14.0:
        print("Morning shift")
    elif 14.0 <= shift_times <= 22.0:
        print("Afternoon shift")
    elif shift_times >= 22.0 or shift_times <= 6.0:
        print("Night shift")
    else:
        print("Invalid")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
