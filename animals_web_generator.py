import json


def load_data(file_path):
    """
    Load a JSON file and return its content.
    
    :param file_path: Path to the JSON file
    :return: Parsed JSON data as Python objects
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Serialize a single animal object into an HTML list item.
    
    Includes the animal's name, diet, first location, and type if available.
    
    :param animal_obj: Dictionary containing animal data
    :return: HTML string for the animal
    """
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj.get("name", "")}</div>\n'
    output += '  <p class="card__text">\n'

    characteristics = animal_obj.get("characteristics", {})

    # Diet
    if "diet" in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    # Location (take the first if exists)
    locations = animal_obj.get("locations", [])
    if locations:
        output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    # Type (check main dictionary first, then characteristics)
    animal_type = animal_obj.get("type") or characteristics.get("type")
    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    """
    Main function to generate HTML file with all animals' data.
    """
    # Load JSON data
    animals_data = load_data("animals_data.json")

    # Read the HTML template
    with open("animals_template.html", "r") as template_file:
        template_html = template_file.read()

    # Generate HTML content for all animals
    animals_html = ""
    for animal in animals_data:
        animals_html += serialize_animal(animal)

    # Replace placeholder in template
    final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Write the final HTML to a new file
    with open("animals.html", "w") as output_file:
        output_file.write(final_html)


if __name__ == "__main__":
    main()
