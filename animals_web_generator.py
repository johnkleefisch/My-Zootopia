import json

def load_data(file_path: str) -> list:
    """
    Load JSON data from a given file path.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of animal dictionaries loaded from JSON.
    """
    with open(file_path, "r") as file:
        return json.load(file)

# Load animal data from JSON
animals_data = load_data("animals_data.json")

# Generate HTML cards for each animal
animals_html = ""
for animal in animals_data:
    animals_html += '<li class="cards__item">\n'

    # Add animal name if present
    if "name" in animal:
        animals_html += f"Name: {animal['name']}<br/>\n"

    # Add diet if available
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        animals_html += f"Diet: {animal['characteristics']['diet']}<br/>\n"

    # Add first location if available
    if "locations" in animal and len(animal["locations"]) > 0:
        animals_html += f"Location: {animal['locations'][0]}<br/>\n"

    # Add type if available
    if "characteristics" in animal and "type" in animal["characteristics"]:
        animals_html += f"Type: {animal['characteristics']['type']}<br/>\n"

    animals_html += "</li>\n"

# Read the HTML template
with open("animals_template.html", "r") as template_file:
    template_html = template_file.read()

# Insert animal cards into the template
final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_html)

# Write the final HTML file
with open("animals.html", "w") as output_file:
    output_file.write(final_html)

print("HTML generation complete: animals.html created successfully.")
