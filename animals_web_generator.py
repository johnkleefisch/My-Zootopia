import json


def load_data(file_path: str):
    """
    Load a JSON file and return its content as a Python object.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: List of animals data.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj: dict) -> str:
    """
    Serialize a single animal object into HTML with proper styling.

    Args:
        animal_obj (dict): Dictionary containing animal information.

    Returns:
        str: HTML string representing a single animal card.
    """
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj.get("name", "Unknown")}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul>\n'

    characteristics = animal_obj.get("characteristics", {})

    if "diet" in characteristics:
        output += f'      <li><strong>Diet:</strong> {characteristics["diet"]}</li>\n'
    if "locations" in characteristics and characteristics["locations"]:
        output += f'      <li><strong>Location:</strong> {characteristics["locations"][0]}</li>\n'
    if "type" in characteristics:
        output += f'      <li><strong>Type:</strong> {characteristics["type"]}</li>\n'
    if "skin_type" in characteristics:
        output += f'      <li><strong>Skin Type:</strong> {characteristics["skin_type"]}</li>\n'

    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'
    return output


def main():
    # Load JSON data
    animals_data = load_data("animals_data.json")

    # Get unique skin types and display them
    skin_types = set(
        characteristics.get("skin_type", "Unknown")
        for animal in animals_data
        for characteristics in [animal.get("characteristics", {})]
        if characteristics.get("skin_type")
    )

    print("Available skin types:")
    for st in sorted(skin_types):
        print(f"- {st}")

    selected_skin = input("Enter a skin type from the list above: ").strip()

    # Filter animals case-insensitively
    filtered_animals = [
        animal for animal in animals_data
        if animal.get("characteristics", {}).get("skin_type", "").lower() == selected_skin.lower()
    ]

    if not filtered_animals:
        print(f"No animals found with skin type '{selected_skin}'. Exiting...")
        return

    # Serialize filtered animals
    html_animals = "".join(serialize_animal(animal) for animal in filtered_animals)

    # Read HTML template
    with open("animals_template.html", "r", encoding="utf-8") as f:
        template_html = f.read()

    # Replace placeholder with animal cards
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", html_animals)

    # Write final HTML file
    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    print("HTML file 'animals.html' generated successfully.")


if __name__ == "__main__":
    main()
