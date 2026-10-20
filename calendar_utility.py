import calendar
import datetime


def main():
    # 1. Prompt the user for a year and a month
    try:
        year = int(input("Enter a year (e.g., 2025): "))
        month = int(input("Enter a month number (1-12, e.g., 3 for March): "))
    except ValueError:
        print("Error: please enter whole numbers for the year and month.")
        return

    if not 1 <= month <= 12:
        print("Error: month must be between 1 and 12.")
        return

    # 2. Display the calendar for that month in a formatted grid
    month_name = calendar.month_name[month]
    print(f"\n--- Calendar for {month_name} {year} ---")
    print(calendar.month(year, month), end="")

    # 3-4. Use datetime to check whether today falls in that month/year
    today = datetime.date.today()
    print(f"--- Checking against today: {today.strftime('%B %-d, %Y')} ---")
    if today.year == year and today.month == month:
        print(f"Today is {today.strftime('%B %-d, %Y')} - it falls within "
              f"{month_name} {year}!")
    else:
        print(f"Today is {today.strftime('%B %-d, %Y')}, which is NOT in "
              f"{month_name} {year}.")


if __name__ == "__main__":
    main()