import os
import sys

'''
 Provides utility functions for working with test folders.
 It includes functions for retrieving test folders in the current directory,
 retrieving test files within a specific test folder, and prompting the user
 to select a test folder.
'''


def get_test_folders():
    """
    Retrieves a list of test folders in the current directory that contain one or more .toml files.

    Returns:
        list: List of test folder names.
    """
    test_folders = []
    for folder in os.listdir('.'):
        if os.path.isdir(folder):
            folder_path = os.path.join('.', folder)
            test_files = [file for file in os.listdir(folder_path) if file.endswith('.toml')]
            if len(test_files) > 0:
                test_folders.append(folder)
    if len(test_folders) == 0:
        print("No test folders found in the current directory that contain .toml files.")
        sys.exit(1)
    return test_folders

def get_test_files(test_folder):
    """
    Retrieves a list of test files in the specified test folder.

    Args:
        test_folder (str): Path of the test folder.

    Returns:
        list: List of test file paths.
    """
    test_folder_path = os.path.join('.', test_folder)
    test_files = [os.path.join(test_folder_path, file) for file in os.listdir(test_folder_path) if file.endswith('.toml')]
    if len(test_files) == 0:
        print("No test files found in the selected test folder.")
        sys.exit(1)
    return test_files
