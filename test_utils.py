import toml

'''
 Provides utility functions for working with multiple-choice test data in TOML format.
 It includes functions for loading test data, presenting questions, 
 and evaluating answers.
'''


def load_test_data(test_file):
    """
    Loads test data from a TOML file.

    Args:
        test_file (str): File path to the TOML file.

    Returns:
        dict: Test data loaded from the TOML file.
    """
    with open(test_file, 'r') as file:
        test_data = toml.load(file)
    return test_data

def present_question(question, choices):
    """
    Presents a question and its choices to the user and retrieves their answer.

    Args:
        question (str): The question to present.
        choices (list): List of choices for the question.

    Returns:
        int: The user's choice number.
    """
    print("\n" + question)
    for index, choice in enumerate(choices):
        print(f'{index+1}. {choice}')

    user_choice = None
    while not user_choice:
        user_input = input("Your answer (enter the choice number): ")
        try:
            user_choice = int(user_input)
            if user_choice < 1 or user_choice > len(choices):
                print("Invalid input. Please enter a valid choice number.")
                user_choice = None
        except ValueError:
            print("Invalid input. Please enter a valid choice number.")

    return user_choice

def evaluate_answers(answers, correct_answers):
    """
    Evaluates the user's answers against the correct answers.

    Args:
        answers (list): List of user's answers.
        correct_answers (list): List of correct answers.

    Returns:
        int: Number of correct answers.
    """
    num_correct = 0
    for index, answer in enumerate(answers):
        if answer == correct_answers[index]:
            num_correct += 1
    return num_correct
