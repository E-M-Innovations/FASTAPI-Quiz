# Multiple Choice Test Application

This is a command-line application that allows users to take multiple-choice tests loaded from TOML files. The application presents questions with multiple choices and evaluates the user's answers.

## Features

- Load multiple-choice tests from TOML files.
- Allow users to select specific test files or attempt all available tests.
- Combine questions from selected test files and shuffle them randomly.
- Validate user input and re-prompt if the input is invalid.
- Calculate and display the user's score as a percentage.

## Requirements

- Python 3.6 or above

## Usage

1. Clone the repository:

```bash
git clone https://github.com/E-M-Innovations/FASTAPI-Quiz.git
cd <repository-directory>
```

2. Install the required dependencies:

```bash
pip install toml
```

3. Prepare your multiple-choice test files in TOML format. Each test should be in a separate TOML file, following the structure described in the example below:

```toml
[[questions]]
question = "What is the capital of France?"
choices = ["London", "Paris", "Berlin", "Madrid"]
answer = 2

[[questions]]
question = "Who wrote the novel 'Pride and Prejudice'?"
choices = ["Jane Austen", "Charles Dickens", "Mark Twain", "William Shakespeare"]
answer = 1

...

[correct_answers]
correct_answers = [2, 1, ...]
```

4. Run the application:

```bash
python main.py
```

5. Follow the prompts to select a test or attempt all tests. Answer each question by entering the choice number. The application will provide feedback on your answers and display the test results at the end.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to modify and customize the README.md file according to your specific project needs.
