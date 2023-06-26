# FASTAPI Website Design

## **Objective:**

The objective of this project is to create an interactive quiz platform that allows users to select and answer multiple-choice quizzes. The platform will provide randomized questions from selected tests, provide immediate feedback on the correctness of user answers, and display the final score.

## **Components:**

1. Main Page: The initial page where users can select the theme for the quizzes by choosing one of the folders in the CLI project.
2. Test Selection: Users can select tests by clicking on the corresponding test boxes. Selected tests will be visually indicated by appearing darker in color. Users can undo their selection by clicking the test again. Once all tests are selected, users can click the "Done" button to proceed.
3. Question Presentation: Randomized questions from the selected tests will be presented one by one to the user. Users can choose one of the choices and click "Submit" to check if their answer is correct. Users cannot go back to previous questions after submitting an answer. The correctness of the answer can be visually displayed using animations.
4. Grading Process: After submitting all the questions, the grading process will display the user's score as a percentage and the number of questions they answered correctly out of all the questions asked.

## Requirements

Steps: 

- Main page selecting the theme for the quizzes, essentially selecting one of the folders in the CLI project
- Then the user will Select test(s) by clicking a test box
    - The tests that are clicked on will appear darker in color
    - The user can undo selection by clicking the test once again
    - After all the tests are selected then the user can click on the "Done" button to continue.
        - The done button will appear darker in color after clicked on
- The Randomized selection of questions from the test(s) will appear one by one presented to the  user
    - The user will click on one of the choice and then press submit. It will then display if the user has gotten the correct answer for the question.
    - The user cannot go back to questions after submitting it
    - The Correct and Incorrect could have a simple animation to it
    - After all the questions are submitted the user can press submit all for the Grading Process
- In the Grading process it will display the user's score as a percentage and the number of questions they got right out of all questions asked

## Timeline:

1. Design and Development:
    - Create the main page with the theme selection feature.
    - Implement the test selection functionality with visual feedback.
    - Develop the question presentation system with randomized questions.
    - Implement the user answer submission and correctness display.
    - Design the grading process to calculate and display the final score.
2. Testing and Refinement:
    - Test the platform for functionality and usability.
    - Conduct thorough testing to ensure the platform is bug-free.
    - Fine-tune the user interface and animations for a seamless experience.
3. Deployment:
    - Prepare the project for deployment.
    - Deploy the quiz platform to a suitable hosting environment.
    - Conduct final testing to ensure the platform is working correctly in the deployment environment.
    - Deploy on [Deta Space](https://fastapi.tiangolo.com/deployment/deta/)