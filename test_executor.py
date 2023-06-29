import random
import os 
from test_utils import load_test_data, present_question, evaluate_answers
from main import main
from test_folder_utils import * 
'''
 Contains the core functionality for conducting multiple-choice tests.
 It includes functions for getting user input, selecting test files,
 conducting tests, and displaying test results.
'''

def clear_screen():
    # Clear the screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_choice(test_files):
    """
    Prompts the user to select a test and returns the selected test file(s).

    Args:
        test_files (list): List of test file paths.

    Returns:
        list: List of selected test file paths.

    Note: If the user inputs 'back', it returns None to restart the main() function in main.py.
    """
    clear_screen()
    print("Available Tests:")
    total_questions = 0
    for index, test_file in enumerate(test_files):
        test_file_name = os.path.basename(test_file)
        test_file_name = os.path.splitext(test_file_name)[0]  # Remove the file extension
        test_file_name = test_file_name.replace("_", " ")  # Replace underscores with spaces
        test_data = load_test_data(test_file)
        questions = test_data.get('questions', [])
        num_questions = len(questions)
        total_questions += num_questions
        print(f"{index+1}. {test_file_name} ({num_questions} questions)")
    print(f"\nThe total number of questions across all tests: {total_questions}\n")

    user_choice = None
    while not user_choice:
        test_input = input("Select test(s) (enter the number(s) separated by commas), type 'all' for all tests, or 'back' to go back: ")
        if test_input.lower() == 'all':
            user_choice = test_files
        elif test_input.lower() == 'back':
            return None # Restart the main() function in main.py
        else:
            test_numbers = test_input.split(',')
            try:
                test_numbers = [int(number) for number in test_numbers]
                invalid_numbers = [number for number in test_numbers if number < 1 or number > len(test_files)]
                if invalid_numbers:
                    print("Invalid input. Please enter valid test numbers.")
                elif len(set(test_numbers)) != len(test_numbers):
                    print("Invalid input. Please do not repeat test numbers.")
                else:
                    user_choice = [test_files[number - 1] for number in test_numbers]
            except ValueError:
                print("Invalid input. Please enter valid test numbers or 'all'.")
    return user_choice


def user_choice_test_folders(test_folders):
    """
    Prompts the user to select a test folder and returns the selected folder path.

    Args:
        test_folders (list): List of test folder names.

    Returns:
        str: Path of the selected test folder.
    """
    clear_screen()
    print("Available Test Folders:")
    for index, folder in enumerate(test_folders):
        print(f"{index+1}. {folder}")

    user_choice = None
    while not user_choice:
        folder_input = input("Select a test folder (enter the number): ")
        try:
            folder_index = int(folder_input)
            if folder_index < 1 or folder_index > len(test_folders):
                print("Invalid input. Please enter a valid folder number.")
            else:
                user_choice = test_folders[folder_index - 1]
        except ValueError:
            print("Invalid input. Please enter a valid folder number.")
    return user_choice

def conduct_test(user_choice, test_files):
    """
    Conducts a multiple-choice test based on the user's choice of test files.

    Args:
        user_choice (list): List of test files chosen by the user.
        test_files (list): List of available test files.

    Returns:
        tuple: A tuple containing the user's answers, the number of correct answers,
            and the total number of questions.
    """
    user_answers = []
    num_correct = 0
    total_questions = 0
    all_questions = []
    all_correct_answers = []

    for test_file in user_choice:
        if test_file not in test_files:
            print(f"Invalid test file: {test_file}. Skipping this test.")
            continue

        test_data = load_test_data(test_file)
        questions = test_data.get('questions', [])
        correct_answers = test_data.get('correct_answers', {}).get('correct_answers', [])

        if len(questions) != len(correct_answers) or not questions or not correct_answers:
            print(f"Invalid test file format: {test_file}. Skipping this test.")
            continue

        all_questions.extend(questions)
        all_correct_answers.extend(correct_answers)

    if not all_questions or not all_correct_answers:
        print("No valid questions found. Exiting test.")
        return user_answers, num_correct, total_questions

    combined = list(zip(all_questions, all_correct_answers))
    random.shuffle(combined)
    questions, correct_answers = zip(*combined)

    clear_screen()
    print("\nWelcome to the Multiple Choice Test!")
    print("Please answer the following questions:")

    for index, question in enumerate(questions):
        user_choice = present_question(index+1, question.get('question', ''), question.get('choices', []))
        user_answers.append(user_choice)
        last_correct_answers = correct_answers[len(user_answers) - 1]
        if user_choice == last_correct_answers:
            print("Correct!")
        else:
            print("Incorrect.")
            print(f"The Correct Answer was: {question.get('choices', [])[last_correct_answers-1]}")

    num_correct = evaluate_answers(user_answers, correct_answers)
    total_questions = len(questions)

    return user_answers, num_correct, total_questions

def show_test_results(num_correct, total_questions):
    """
    Displays the test results.

    Args:
        num_correct (int): Number of correct answers.
        total_questions (int): Total number of questions.
    """
    mark_percentage = (num_correct / total_questions) * 100
    clear_screen()
    print("\nTest Results:")
    print(f"You answered {num_correct} out of {total_questions} questions correctly.")
    print(f"Mark: {round(mark_percentage,2)}%")
    
    input("\nPress Enter to continue...")