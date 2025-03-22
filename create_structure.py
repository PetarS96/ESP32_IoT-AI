import os

# Define the folder structure
structure = {
    "smart-environment-monitoring": {
        "firmware": {
            "node1": {
                "src": ["main.cpp", "dht22.cpp", "lcd_spi.cpp", "mqtt.cpp", "buttons.cpp", "leds.cpp", "pwm_input.cpp"],
                "include": ["dht22.h", "lcd_spi.h", "mqtt.h", "buttons.h", "leds.h", "pwm_input.h"],
                "platformio.ini": ""
            },
            "node2": {
                "src": ["main.cpp", "dht22.cpp", "mqtt.cpp", "buttons.cpp", "leds.cpp", "pwm_input.cpp"],
                "include": ["dht22.h", "mqtt.h", "buttons.h", "leds.h", "pwm_input.h"],
                "platformio.ini": ""
            },
            "lib": {
                "README.md": ""
            }
        },
        "backend": {
            "app": {
                "__init__.py": "",
                "main.py": "",
                "mqtt_client.py": "",
                "database.py": "",
                "api": {
                    "sensors.py": "",
                    "control.py": ""
                },
                "utils": {
                    "helpers.py": ""
                }
            },
            "requirements.txt": "",
            "Dockerfile": "",
            "README.md": ""
        },
        "ml": {
            "data": {
                "raw": {},
                "processed": {},
                "preprocess.py": ""
            },
            "models": {
                "model.pkl": "",
                "train_model.py": ""
            },
            "inference": {
                "predict.py": "",
                "api.py": ""
            },
            "requirements.txt": "",
            "Dockerfile": "",
            "README.md": ""
        },
        "docker-compose.yml": "",
        "README.md": "",
        ".gitignore": ""
    }
}

# Function to create folders and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create folder
            os.makedirs(path, exist_ok=True)
            print(f"Created folder: {path}")
            # Recursively create subfolders and files
            create_structure(path, content)
        elif isinstance(content, list):
            # Create files in the list
            for file_name in content:
                file_path = os.path.join(base_path, file_name)
                with open(file_path, "w") as file:
                    file.write("")
                print(f"Created file: {file_path}")
        else:
            # Create file
            with open(path, "w") as file:
                file.write("")
            print(f"Created file: {path}")

# Run the script
if __name__ == "__main__":
    base_path = os.getcwd()  # Use the current working directory
    create_structure(base_path, structure)
    print("Folder structure created successfully!")