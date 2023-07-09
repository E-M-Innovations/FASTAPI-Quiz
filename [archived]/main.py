from test_executor import *
from test_folder_utils import * 

def main():
    """
    Main entry point of the script.

    This function orchestrates the execution of the test. It performs the following steps:
    1. Retrieves a list of test folders in the current directory using the `get_test_folders()` function.
    2. Prompts the user to select a specific test folder using the `user_choice_test_folders()` function.
    3. Retrieves a list of test files in the selected test folder using the `get_test_files()` function.
    4. Prompts the user to select a specific test or all tests using the `get_user_choice()` function.
    5. Conducts the test based on the user's choice by calling the `conduct_test()` function.
    6. Displays the test results using the `show_test_results()` function.

    The test execution includes presenting questions to the user, recording their answers, evaluating the correctness
    of the answers, and calculating the overall test score.

    This function serves as the entry point of the script and ties together all the necessary steps to execute the test.

    Note: The `test_executor` module, which contains the functions required for test execution, is imported at the top
    of this file.

    Note: To handle the scenario where the user inputs 'back' during test selection, the `main()` function is recursively
    called again to restart the test execution process.
    """
    test_folders = get_test_folders()
    selected_test_folder = user_choice_test_folders(test_folders)
    test_files = get_test_files(selected_test_folder)
    user_choice = get_user_choice(test_files)
    if user_choice is not None:
      user_answers, num_correct, total_questions = conduct_test(user_choice, test_files)
      show_test_results(num_correct, total_questions)

    main()

if __name__ == "__main__":
    main()


