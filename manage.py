import sys, os

def create_file(folder, name, suffix):
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"{name}_{suffix}.py")
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(f"# {suffix.capitalize()} for {name}\n")
        print(f"Created: {filename}")
    else:
        print(f"File already exists: {filename}")

if len(sys.argv) == 3:
    command, name = sys.argv[1], sys.argv[2]
    if command == "make:model":
        create_file("models", name, "model")
    elif command == "make:controller":
        create_file("controllers", name, "controller")
    elif command == "make:view":
        create_file("views", name, "view")
    else:
        print("Command not recognized.")
else:
    print("Usage: python manage.py make:model|controller|view <name>")