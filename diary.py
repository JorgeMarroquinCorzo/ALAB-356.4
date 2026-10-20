import os
import datetime

FILENAME = "diary.txt"


def main():
    # 1. Check if diary.txt exists; create it if it doesn't
    if not os.path.exists(FILENAME):
        try:
            with open(FILENAME, "w") as f:
                pass  # create an empty file
            print(f"{FILENAME} did not exist, so a new file was created.")
        except OSError as e:
            print(f"Error: could not create {FILENAME}: {e}")
            return

    # 2. Prompt the user for a diary entry
    entry = input("Write your diary entry: ")

    # 3. Prepend a timestamp and append the entry to diary.txt
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(FILENAME, "a") as f:
            f.write(f"[{timestamp}] {entry}\n")
        print("Entry saved.")
    except OSError as e:
        print(f"Error: could not write to {FILENAME}: {e}")
        return

    # 4. Read back and print the entire diary
    print(f"\n--- Contents of {FILENAME} ---")
    try:
        with open(FILENAME, "r") as f:
            print(f.read(), end="")
    except OSError as e:
        print(f"Error: could not read {FILENAME}: {e}")


if __name__ == "__main__":
    main()