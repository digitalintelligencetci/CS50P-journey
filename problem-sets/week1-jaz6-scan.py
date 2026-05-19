#!/usr/bin/env python3


# JAZ6 Scan Program


# First: initialise_scan function:
# 1. Prompt officer for name → .strip() .title()
# 2. Prompt for case ID
# 3. Prompt for time of scan (24hr format)
# 4. Print 🟡 JAZ6 initialising...
# 5. Print officer name, case ID, time
# 6. Print 🟢 Ready to scan

# Second: convert function:
# 7. Take time string "HH:MM"
# 8. Split into hours and minutes
# 9. Return float (hours + minutes/60)

# Third: main function:
# 10. Call initialise_scan
# 11. Prompt RF detected (yes/no)
# 12. Prompt thermal detected (yes/no)
# 13. if both → 🔴 HIGH CONFIDENCE
# 14. elif one → 🟡 MEDIUM CONFIDENCE
# 15. else (neither) → 🟢 LOW CONFIDENCE
# 16. Print scan summary

# Output scan summary:
# f"Officer: {name}"
# f"Case ID: {case_id}"
# f"Scan time: {time}"
# f"Confidence: {confidence}"


#
# if __name__ == "__main__":
# 17. Call main()


def initialise_scan():
    officer_name = input("Enter firstname surname: ").strip().title()
    case_id = input("Enter the case id: ")
    scan_time = input("Enter scan time (HH:MM): ")
    print("🟡 JAZ6 initialising...")
    print(f"Officer: {officer_name}")
    print(f"Case ID: {case_id}")
    print(f"Scan time: {scan_time}")
    print("🟢 Ready to scan")
    return officer_name, case_id, scan_time


def convert(scan_time):
    hours, minutes = scan_time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


def main():
    officer_name, case_id, scan_time = initialise_scan()
    time_float = convert(scan_time)

    rf_detection = input("RF Detected (yes/no): ").lower()
    rf_detection = rf_detection in ("y", "yes")

    thermal_detection = input("Thermal Detected (yes/no): ").lower()
    thermal_detection = thermal_detection in ("y", "yes")

    if rf_detection and thermal_detection:
        confidence = "🔴 HIGH CONFIDENCE"
    elif rf_detection or thermal_detection:
        confidence = "🟡 MEDIUM CONFIDENCE"
    else:
        confidence = "🟢 LOW CONFIDENCE"

    print(confidence)
    print(f"\nScan Summary:")
    print(f"Officer: {officer_name}")
    print(f"Case ID: {case_id}")
    print(f"Scan time: {scan_time} ({time_float:.2f} hrs)")
    print(f"Confidence: {confidence}")


if __name__ == "__main__":
    main()
