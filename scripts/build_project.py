import json

with open('data/BUILD.json', 'r') as file:
    json_data = file.read()

data = json.loads(json_data)

with open('markdowns/BUILD.md', 'w') as md_file:

    md_file.write("### Build With Push\n\n")

    with open('markdowns/EXAMPLES.md', 'r') as f:
        md_file.write(f.read())
        md_file.write('\n\n')

    for category in data:
        md_file.write(f"* **{category['category']}:**\n\n")
        for project in category['projects']:
            md_file.write(f"  * **[{project['name']}]({project['link']})**: {project['description']}\n")
        md_file.write("\n")