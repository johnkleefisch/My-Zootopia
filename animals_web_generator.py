import json

def load_data(file_path):
    """
    Load a JSON file and return the data as a Python object.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: List of animal dictionaries.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Serialize a single animal dictionary into an HTML card string.

    Args:
        animal_obj (dict): Animal information.

    Returns:
        str: HTML string representing the animal card.
    """
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'

    characteristics = animal_obj.get("characteristics", {})
    
    if "diet" in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
    if "locations" in characteristics and characteristics["locations"]:
        output += f'      <strong>Location:</strong> {characteristics["locations"][0]}<br/>\n'
    if "type" in characteristics:
        output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'
    
    # Bonus fields
    if "lifespan" in characteristics:
        output += f'      <strong>Lifespan:</strong> {characteristics["lifespan"]}<br/>\n'
    if "weight" in characteristics:
        output += f'      <strong>Weight:</strong> {characteristics["weight"]}<br/>\n'
    if "height" in characteristics:
        output += f'      <strong>Height:</strong> {characteristics["height"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_html(animals_data, template_path, output_path):
    """
    Generate a full HTML page from animal data and a template.

    Args:
        animals_data (list): List of animal dictionaries.
        template_path (str): Path to the HTML template.
        output_path (str): Path to write the generated HTML.
    """
    with open(template_path, "r") as file:
        template_content = file.read()

    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open(output_path, "w") as file:
        file.write(final_html)


if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    generate_html(animals_data, "animals_template.html", "animals.html")
    print("HTML generated successfully: animals.html")
