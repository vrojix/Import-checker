import importlib
import subprocess

def lib():
    # Define custom library names
    required_libraries = {
        'ctk': 'tkinter',
        'tkmb': 'tkinter.messagebox',
        'sqlite3': 'sqlite3',
        'yagmail': 'yagmail'
    }


    for custom_name, actual_name in required_libraries.items():
        try:
            #tries to 
            importlib.import_module(actual_name)
            print(f"{custom_name} (as {actual_name}) is already installed.")
        except ImportError:
            print(f"{custom_name} (as {actual_name}) is not installed. Attempting to install...")
            try:
                subprocess.check_call(['pip', 'install', actual_name])
                print(f"{custom_name} (as {actual_name}) has been successfully installed.")
            except subprocess.CalledProcessError:
                print(f"Failed to install {custom_name} (as {actual_name}). Please install it manually.")
