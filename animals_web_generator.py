import json

def load_data(file_path: str) -> list:
    """
    Load a JSON file and return its content as a Python list.
    
    :param file_path: Path to the JSON file
    :return: List containing data from the JSON file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_cards(data: list) -> str:
    """
    Serialize each animal's data into an HTML list item with proper styling.
    Handles optional fields gracefully.

    :param data: List of animal dictionaries
    :return: HTML string containing all animal cards
    """
    output = ""
    for animal in data:
        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{animal.get("name")}</div>\n'
        output += '  <p class="card__text">\n'

        # Diet (required)
        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            output += f'      <strong>Diet:</strong> {diet}<br/>\n'

        # Location (take the first if exists)
        locations = animal.get("locations")
        if locations and len(locations) > 0:
            output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

        # Type (optional, handle case differences)
        animal_type = animal.get("characteristics", {}).get("type") or \
                      animal.get("characteristics", {}).get("Type")
        if animal_type:
            output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    return output


def main():
    """
    Main function to read the template, inject animal cards, and save the final HTML.
    """
    # Load data
    animals_data = load_data("animals_data.json")

    # Generate HTML cards
    animal_cards_html = generate_animal_cards(animals_data)

    # Read HTML template
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    # Replace placeholder with generated HTML
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_cards_html)

    # Write final HTML to a new file
    with open("animals.html", "w") as output_file:
        output_file.write(final_html)

    print("HTML file generated successfully: animals.html")


if __name__ == "__main__":
    main()
