import os

def generate_tree(root_dir, indent="", exclusions=None):
    """
    Recursively generates a tree representation of the file structure.
    :param root_dir: The root directory to generate the tree from.
    :param indent: The current indentation level (used for recursive calls).
    :param exclusions: List of directory names to exclude from the tree.
    """
    if exclusions is None:
        exclusions = []

    # Make sure the root directory exists
    if not os.path.exists(root_dir):
        print("Directory does not exist:", root_dir)
        return

    # Get all entries in the directory
    entries = sorted([e for e in os.listdir(root_dir) if e not in exclusions])

    for i, entry in enumerate(entries):
        # Check if it's the last entry in the directory for proper formatting
        is_last = i == len(entries) - 1
        # Get the full path
        full_path = os.path.join(root_dir, entry)
        # Print the entry
        print(indent + ("└── " if is_last else "├── ") + entry)

        # If it's a directory, recurse
        if os.path.isdir(full_path) and entry not in exclusions:
            # Update the indentation for the next level
            next_indent = indent + ("    " if is_last else "│   ")
            generate_tree(full_path, next_indent, exclusions)

if __name__ == "__main__":
    root_directory = input("Enter the path of the root directory: ")
    exclusions = ['node_modules', '.git', 'other_directories_to_exclude']
    generate_tree(root_directory, exclusions=exclusions)
