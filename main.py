# Built a command-line diary tool with features to write, save, view, and search personal entries using CSV for persistent storage.
# Incorporated timestamping, entry labeling, and keyword-based search for user-friendly journaling.
import csv
from datetime import datetime

CSV_FILE = "diary.csv"

# Initialize CSV with headers if it doesn't exist
def init_csv():
    try:
        with open(CSV_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time", "Title", "Entry"])
    except FileExistsError:
        pass

# Add a new diary entry
def add_entry():
    title = input("\n📌 Entry Title: ")
    entry = input("📝 Write your diary entry:\n> ")

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    with open(CSV_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, time, title, entry])
    print("✅ Entry saved!")

# View all entries
def view_entries():
    try:
        with open(CSV_FILE, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            print("\n📚 Your Diary Entries:\n")
            for row in reader:
                print(f"📅 {row[0]} {row[1]} | 🏷 {row[2]}")
                print(f"   {row[3]}\n")
    except FileNotFoundError:
        print("❌ No diary entries found.")

# Search entries
def search_entries():
    keyword = input("🔍 Enter keyword or date to search: ").lower()
    found = False

    with open(CSV_FILE, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            if keyword in row[0].lower() or keyword in row[2].lower() or keyword in row[3].lower():
                found = True
                print(f"\n📅 {row[0]} {row[1]} | 🏷 {row[2]}")
                print(f"   {row[3]}")
    if not found:
        print("❌ No matching entries found.")

# Main menu
def main():
    init_csv()
    while True:
        print("\n📓 Personal Diary")
        print("1. ➕ Add Entry")
        print("2. 📖 View Entries")
        print("3. 🔍 Search")
        print("4. ❌ Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            search_entries()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
