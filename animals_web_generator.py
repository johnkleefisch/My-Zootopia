import json


def load_data(file_path: str) -> list:
    """
    Loads data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: Parsed JSON data as a Python list of dictionaries.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def print_animals_info(animals: list) -> None:
    """
    Iterates over animals and prints their details:
    - Name
    - Diet
    - First Location
    - Type (if available)

    Args:
        animals (list): List of animal dictionaries.
    """
    for animal in animals:
        # Print Name
        if "name" in animal:
            print(f"Name: {animal['name']}")

        # Print Diet
        if "diet" in animal:
            print(f"Diet: {animal['diet']}")

        # Print only the first Location if available
        if "locations" in animal and animal["locations"]:
            print(f"Location: {animal['locations'][0]}")

        # Print Type only if it exists
        if "type" in animal:
            print(f"Type: {animal['type']}")

        print()  # Blank line between animals


if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    print_animals_info(animals_data)
