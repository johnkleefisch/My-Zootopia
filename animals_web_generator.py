import json


def load_data(file_path: str) -> list:
    """Loads data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def generate_animals_string(animals: list) -> str:
    """Generates a string with animal info for HTML output."""
    output = ""
    for animal in animals:
        if "name" in animal:
            output += f"Name: {animal['name']}\n"
        if "diet" in animal:
            output += f"Diet: {animal['diet']}\n"
        if "locations" in animal and animal["locations"]:
            output += f"Location: {animal['locations'][0]}\n"
        if "type" in animal:
            output += f"Type: {animal['type']}\n"
        output += "\n"  # blank line between animals
    return output


def generate_html(template_path: str, animals_output: str, output_path: str) -> None:
    """Reads template, replaces placeholder, and writes final HTML file."""
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # Replace the placeholder with our generated animal data
    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    # Write the final HTML
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(new_html_content)


if __name__ == "__main__":
    # Step 1: Load JSON data
    animals_data = load_data("animals_data.json")

    # Step 2: Generate formatted string
    animals_output = generate_animals_string(animals_data)

    # Step 3: Replace in HTML and save to new file
    generate_html("animals_template.html", animals_output, "animals.html")
