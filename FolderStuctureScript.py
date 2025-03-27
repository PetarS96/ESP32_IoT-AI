import os

# Define project structure
project_structure = {
    "iot_project/esp32_firmware/esp32_node1/main": [],
    "iot_project/esp32_firmware/esp32_node1/components": [],
    "iot_project/esp32_firmware/esp32_node1/build": [],
    "iot_project/esp32_firmware/esp32_node1/flash": [],
    "iot_project/esp32_firmware/esp32_node2/main": [],
    "iot_project/esp32_firmware/esp32_node2/components": [],
    "iot_project/esp32_firmware/esp32_node2/build": [],
    "iot_project/esp32_firmware/esp32_node2/flash": [],
    "iot_project/backend/mqtt_handler": [],
    "iot_project/backend/database": [],
    "iot_project/backend/api": [],
    "iot_project/mlops/data_collection": [],
    "iot_project/mlops/training": [],
    "iot_project/mlops/deployment": [],
    "iot_project/mlops/docker": [],
    "iot_project/configs": [],
    "iot_project/scripts": [],
    "iot_project/docs": []
}

# Files with content
files_content = {
    # ESP32 Node 1
    "iot_project/esp32_firmware/esp32_node1/CMakeLists.txt": "cmake_minimum_required(VERSION 3.5)\nproject(esp32_node1)\n",
    "iot_project/esp32_firmware/esp32_node1/Kconfig.projbuild": "# ESP32 Node 1 Config\n",
    "iot_project/esp32_firmware/esp32_node1/sdkconfig": "# CONFIG FILE\n",
    "iot_project/esp32_firmware/esp32_node1/main/main.c": '#include "stdio.h"\nvoid app_main() { printf("ESP32 Node 1\\n"); }\n',

    # ESP32 Node 2
    "iot_project/esp32_firmware/esp32_node2/CMakeLists.txt": "cmake_minimum_required(VERSION 3.5)\nproject(esp32_node2)\n",
    "iot_project/esp32_firmware/esp32_node2/Kconfig.projbuild": "# ESP32 Node 2 Config\n",
    "iot_project/esp32_firmware/esp32_node2/sdkconfig": "# CONFIG FILE\n",
    "iot_project/esp32_firmware/esp32_node2/main/main.c": '#include "stdio.h"\nvoid app_main() { printf("ESP32 Node 2\\n"); }\n',

    # Backend
    "iot_project/backend/mqtt_handler/main.py": "# MQTT Handler\n",
    "iot_project/backend/database/schema.sql": "-- Database Schema\n",
    "iot_project/backend/api/main.py": "# REST API\n",

    # MLOps
    "iot_project/mlops/data_collection/collect.py": "# Data Collection\n",
    "iot_project/mlops/training/train.py": "# Model Training\n",
    "iot_project/mlops/deployment/deploy.py": "# Deployment Script\n",
    "iot_project/mlops/docker/Dockerfile": "# Dockerfile\n",

    # Configs
    "iot_project/configs/wifi_config.json": "{}",
    "iot_project/configs/mqtt_config.json": "{}",
    "iot_project/configs/db_config.json": "{}", 

    # Scripts
    "iot_project/scripts/setup.sh": "#!/bin/bash\n# Setup Script\n",
    "iot_project/scripts/deploy.sh": "#!/bin/bash\n# Deployment Script\n",

    # Docs
    "iot_project/docs/README.md": "# IoT Project\n",
    
    # Gitignore
    "iot_project/.gitignore": "*.pyc\n__pycache__/\nbuild/\n"
}

# Function to create directories
def create_directories():
    for path in project_structure.keys():
        os.makedirs(path, exist_ok=True)

# Function to create files with content
def create_files():
    for filepath, content in files_content.items():
        os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Ensure directory exists
        with open(filepath, "w") as f:
            f.write(content)

# Run script
create_directories()
create_files()

print("✅ Project structure and files created successfully.")
