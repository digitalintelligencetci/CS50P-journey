# Store the correct PIN
# Start attempts at zero

# While attempts remain:
#   ask for a PIN

#   if it is correct:
#       print access granted
#       stop the loop

#   otherwise:
#       increase attempts
#       show attempts remaining

# After the loop:
#   decide whether access was denied


actual_pin = "1111"     # store the correct PIN
max_attempts = 3        # Maximum allowed tries
attempts_taken = 0      # start attempts at zero      

while attempts_taken < max_attempts:     # while attempts remain
    pin = input("Enter Pin: ")      # ask for pin
    if pin == actual_pin:       # if it is correct:
        print("Access granted!")        # print access granted
        break       # stop the loop

    else:       # otherwise
        attempts_taken += 1       # increase attempts
        remaining = max_attempts - attempts_taken   # show attempts taken
        print(f"Incorrect PIN. Attempts remaining: {remaining}")

    if attempts_taken == max_attempts:      # after the loop
        print("Access denied. Account locked.")  # decide whether access was denied











