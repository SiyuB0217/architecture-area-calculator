"""
Architecture Area Calculator

A small command-line Python tool that helps organize room/program areas.
It was inspired by architectural programming workflows, where designers often
need to track spaces by category and compare total area against a target.

Run:
    python main.py
"""

from typing import Dict, List, Tuple


VALID_CATEGORIES = {
    "public": "Public spaces such as lobby, exhibition, cafeteria",
    "teaching": "Teaching or learning spaces such as classrooms and seminar rooms",
    "service": "Service spaces such as restrooms, storage, and cleaning rooms",
    "office": "Office or meeting spaces",
    "circulation": "Circulation and core spaces such as corridors and stairs",
    "other": "Other spaces",
}


Room = Tuple[str, str, float]


def get_positive_float(prompt: str) -> float:
    """Ask the user for a positive number and validate the input."""
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            if value < 0:
                print("Please enter a number greater than or equal to 0.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, such as 120 or 85.5.")


def get_category() -> str:
    """Ask the user to choose a room category."""
    print("\nChoose a category:")
    for key, description in VALID_CATEGORIES.items():
        print(f"  - {key}: {description}")

    while True:
        category = input("Category: ").strip().lower()
        if category in VALID_CATEGORIES:
            return category
        print("Invalid category. Please choose one from the list above.")


def add_room(rooms: List[Room]) -> None:
    """Collect room information from the user and add it to the room list."""
    room_name = input("\nRoom name: ").strip()
    if not room_name:
        print("Room name cannot be empty.")
        return

    category = get_category()
    area = get_positive_float("Area in square meters: ")

    rooms.append((room_name, category, area))
    print(f"Added: {room_name} | {category} | {area:.2f} sqm")


def calculate_totals(rooms: List[Room]) -> Dict[str, float]:
    """Calculate total area by category."""
    totals = {category: 0.0 for category in VALID_CATEGORIES}

    for _, category, area in rooms:
        totals[category] += area

    return totals


def print_summary(rooms: List[Room], target_area: float) -> None:
    """Print a formatted area summary."""
    if not rooms:
        print("\nNo rooms have been added yet.")
        return

    totals = calculate_totals(rooms)
    grand_total = sum(totals.values())
    difference = grand_total - target_area

    print("\n" + "=" * 50)
    print("AREA SUMMARY")
    print("=" * 50)

    print("\nRooms:")
    for room_name, category, area in rooms:
        print(f"  - {room_name:<25} {category:<12} {area:>8.2f} sqm")

    print("\nTotals by category:")
    for category, total in totals.items():
        if total > 0:
            percentage = (total / grand_total) * 100 if grand_total else 0
            print(f"  - {category:<12} {total:>8.2f} sqm   ({percentage:>5.1f}%)")

    print("\nProject total:")
    print(f"  Target area:      {target_area:>8.2f} sqm")
    print(f"  Current total:    {grand_total:>8.2f} sqm")

    if difference > 0:
        print(f"  Status: Over target by {difference:.2f} sqm")
    elif difference < 0:
        print(f"  Status: Under target by {abs(difference):.2f} sqm")
    else:
        print("  Status: Exactly on target")

    print("=" * 50 + "\n")


def load_sample_project() -> List[Room]:
    """Return a sample project so users can test the calculator quickly."""
    return [
        ("Cafeteria", "public", 130),
        ("Exhibition Foyer", "public", 200),
        ("Reception", "public", 30),
        ("Classroom A", "teaching", 120),
        ("Classroom B", "teaching", 120),
        ("Flexible Classroom", "teaching", 150),
        ("Meeting Room", "office", 80),
        ("Public Restrooms", "service", 80),
        ("Storage", "service", 30),
        ("Circulation/Core", "circulation", 50),
    ]


def main() -> None:
    """Run the command-line program."""
    rooms: List[Room] = []
    target_area = 1000.0

    print("Architecture Area Calculator")
    print("This tool helps track room areas by category.\n")

    while True:
        print("Menu:")
        print("  1. Add a room")
        print("  2. Set target area")
        print("  3. View summary")
        print("  4. Load sample project")
        print("  5. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_room(rooms)
        elif choice == "2":
            target_area = get_positive_float("\nTarget area in square meters: ")
            print(f"Target area set to {target_area:.2f} sqm\n")
        elif choice == "3":
            print_summary(rooms, target_area)
        elif choice == "4":
            rooms = load_sample_project()
            target_area = 1000.0
            print("\nSample project loaded.\n")
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please choose 1, 2, 3, 4, or 5.\n")


if __name__ == "__main__":
    main()
