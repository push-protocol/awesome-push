import json

# Your JSON data as a string
with open('data/BUILD.json', 'r') as file:
    json_data = file.read()

# Parse the JSON data
data = json.loads(json_data)

# Open the BUILD.md file to write
with open('markdowns/BUILD.md', 'w') as md_file:
    # Start the Markdown with a header
    md_file.write("### Build With Push\n\n")

    # Iterate over the categories and projects
    for category in data:
        # Write the category name
        md_file.write(f"* **{category['category']}:**\n\n")
        
        # Iterate over the projects within the category
        for project in category['projects']:
            # Write the project name and description
            md_file.write(f"  * **[{project['name']}]({project['link']})**: {project['description']}\n")
        # Add an extra newline for better formatting
        md_file.write("\n")