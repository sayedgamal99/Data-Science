import os

# Add any other directories to exclude
EXCLUDED_DIRS = {'.git', '__pycache__', '.vscode'}
# Add any other files to exclude
EXCLUDED_FILES = {
    # 'README.md', 'update_readme.py'
}
ORDERED_CATEGORIES = ['ML', 'DL', 'Educational']


def generate_tree_structure(base_path, prefix=""):
    tree_structure = ""

    # Prioritize ordered categories
    items = sorted(item for item in os.listdir(base_path)
                   if item not in EXCLUDED_FILES and item not in EXCLUDED_DIRS)
    ordered_items = [item for item in ORDERED_CATEGORIES if item in items]
    other_items = [item for item in items if item not in ORDERED_CATEGORIES]

    all_items = ordered_items + other_items

    for index, item in enumerate(all_items):
        item_path = os.path.join(base_path, item)
        connector = "├── " if index < len(all_items) - 1 else "└── "
        tree_structure += f"{prefix}{connector}{item}\n"
        if os.path.isdir(item_path):
            extension = "│   " if index < len(all_items) - 1 else "    "
            tree_structure += generate_tree_structure(
                item_path, prefix + extension)
    return tree_structure


def generate_readme(base_path):
    readme_content = "# Data Science Projects\n\n"
    readme_content += "This repository contains a collection of machine learning and deep learning projects organized by categories.\n\n"
    readme_content += "```\n"
    readme_content += f"{os.path.basename(base_path)}/\n"
    readme_content += generate_tree_structure(base_path)
    readme_content += "```\n"

    readme_path = os.path.join(base_path, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(readme_content)

    print(f"README.md has been updated at {readme_path}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = script_dir  # Assuming script is in the root of Data-Science repo

    print(f"Script directory: {script_dir}")
    print(f"Repo directory: {repo_dir}")

    generate_readme(repo_dir)
