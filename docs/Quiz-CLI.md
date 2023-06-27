# Quiz CLI Documentation

## Objective

The chief objective of this project is to establish a structure and instrument for administering multiple-choice assessments. The project strives to simplify the procedure involved in designing, arranging, and implementing tests by utilizing TOML-formatted test documents.

### Components

1. **`test_folder_utils.py`**: This module provides utility functions for working with test folders. It includes functions for retrieving test folders in the current directory, retrieving test files within a specific test folder, and prompting the user to select a test folder.
    
```mermaid
    graph TB
    
        style A fill:lightpink, stroke:#333, stroke-width:2px
        style B fill:lightpurple, stroke:#333, stroke-width:2px
        style C fill:lightblue, stroke:#333, stroke-width:2px
        style D fill:lightgreen, stroke:#333, stroke-width:2px
        style E fill:lightblue, stroke:#333, stroke-width:2px
        style F fill:lightgreen, stroke:#333, stroke-width:2px
        style G fill:lightgreen, stroke:#333, stroke-width:2px
        style H fill:lightpurple, stroke:#333, stroke-width:2px
        style I fill:lightpink, stroke:#333, stroke-width:2px
    
        A(Start) --> B[Get Test Folders]
        B --> C{Any Test Folders?}
        C -- Yes --> D[Retrieve Test Folders]
        C -- No --> I[Display Error and Exit]
        D --> E{Any Test Files?}
        E -- Yes --> F[Select Test Folder]
        E -- No --> I
        F --> G[Retrieve Test Files]
        G --> H[Process Test Files]
    ```
    
2. **`text_executor.py`**: This module contains additional core functionality for conducting multiple-choice tests. It includes functions for clearing the screen, getting user choices for tests and test folders, conducting tests, and displaying test results.
    
```mermaid
    graph TB
        style A fill:lightpink, stroke:#333, stroke-width:2px
        style C fill:lightblue, stroke:#333, stroke-width:2px
        style D fill:lightblue, stroke:#333, stroke-width:2px
        style E fill:lightyellow, stroke:#333, stroke-width:2px
        style F fill:lightyellow, stroke:#333, stroke-width:2px
        style G fill:lightgreen, stroke:#333, stroke-width:2px
        style H fill:lightgreen, stroke:#333, stroke-width:2px
        style K fill:lightcyan, stroke:#333, stroke-width:2px
        style L fill:lightblue, stroke:#333, stroke-width:2px
        style M fill:lightgreen, stroke:#333, stroke-width:2px
        style N fill:lightgreen, stroke:#333, stroke-width:2px
        style O fill:lightpink, stroke:#333, stroke-width:2px
    
        A(Start) --> C{Get User Choice}
        C -- Test Selection --> D{All Tests?}
        D -- No --> E[Select Test Files]
        D -- Yes --> F[All Test Files]
        E --> G(Process Questions)
        F --> G
        G --> H[Randomize Questions & Present Question]
        H -- Answered Correctly? --> K[Increment Correct Count]
        K --> L{More Questions?}
        L -- Yes --> G
        L -- No --> M[Evaluate Answers]
        M --> N[Show Test Results]
        N --> O[End]
    ```
    
3. The **`main.py`** script utilizes the functions from **`test_utils.py`**, **`test_folder_utils.py`**, and **`text_executor.py`** to facilitate the selection and execution of multiple-choice tests. It interacts with the user, presents questions, collects answers, evaluates them, and displays the test results.
    
```mermaid
    flowchart TB
        A[Start] --> B(Load Test Data)
        B --> C{Test Data Loaded?}
        C -- Yes --> D(Present Question)
        D --> E{User's Answer}
        E -- Valid --> F(Evaluate Answers)
        F --> G{More Questions?}
        G --> H[Display Results]
        H --> I[End]
        E -- Invalid --> J[Invalid Answer]
        J --> D
        C -- No --> I
    
        style A fill:lightpink, stroke:#333, stroke-width:2px
        style B fill:lightyellow, stroke:#333, stroke-width:2px
        style C fill:lightblue, stroke:#333, stroke-width:2px
        style D fill:lightgreen, stroke:#333, stroke-width:2px
        style E fill:lightblue, stroke:#333, stroke-width:2px
        style F fill:lightgreen, stroke:#333, stroke-width:2px
        style G fill:lightgreen, stroke:#333, stroke-width:2px
        style H fill:lightblue, stroke:#333, stroke-width:2px
        style I fill:lightpink, stroke:#333, stroke-width:2px
        style J fill:lightpink, stroke:#333, stroke-width:2px
    ```
    

Here is the directory structure for the project:
```
project/
├── main.py
├── test_utils.py
├── test_folder_utils.py
├── <test-theme-1>/
│   ├── test-1.toml
│   ├── test-2.toml
│   └── ...
├── <test-theme-2>/
│   ├── test-1.toml
│   ├── test-2.toml
│   └── ...
├── <test-theme-3>/
│   ├── test-1.toml
│   ├── test-2.toml
│   └── ...
└── ...
```

The **`*.toml`** files represent individual tests in TOML (Tom's Obvious, Minimal Language) format. Each test file contains a set of multiple-choice questions along with their choices and correct answers. The **`main.py`** script loads these test files, selects questions randomly, presents them to the user, collects their answers, and evaluates them against the correct answers.

TOML file format:
```toml
[[questions]]
question = "<Question 1>"
choices = [
  "Choice 1",
  "Choice 2",
  "Choice 3",
  "Choice 4"
]
# Answer: Choice X (X)
[[questions]]
question =  "<Question 2>"
choices = [
  "Choice 1",
  "Choice 2",
  "Choice 3",
  "Choice 4",
  "Choice 5"
]
# Answer: Choice X (X)
...
[correct_answers]
correct_answers = [X1, X2, ...]
```

## **Benefits and Features**

1. Flexibility: Users can create and customize multiple-choice tests by editing TOML-formatted test files. They can add new questions, modify choices, and define correct answers.
2. Organization: The project supports the organization of tests into test folders, allowing users to categorize and manage their tests effectively.
3. Randomization: The script randomly selects questions from the available test files, providing variation and preventing predictable patterns in the tests.
4. Interactivity: The project engages users by presenting questions one by one and collecting their answers interactively.
5. Evaluation: The project automatically evaluates the user's answers against the correct answers, providing feedback on the number of correct responses.
