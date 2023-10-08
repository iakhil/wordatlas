# Fancy Word Atlas
## Fancy Word Atlas is a word game to improve one's vocabulary.

### Rules

1. A word is said to be 'fancy' if it is not in the list of the most common 10,000 words used in the English language.
2. Computer would generate a fancy word.
3. You have to come up with a fancy word that starts with the last letter of the computer word.
4. The score represents the streak of valid and fancy words.
5. Any time an invalid or a word that is not *fancy* is entered, the score is set to 0.

### Playing the game and Contributing to the project

1. Fork the repository
2. Clone the repository
    ```shell
   git clone git@github.com/<your_username>/wordatlas
    ```
3. Install python 3.11 as it is required for running the game. You can download it from [here](https://www.python.org/downloads/release/python-3115/)
4. Create a virtual environment. We will be using venv to create and manage virtual env. Run the following command in the project directory.
   ```shell
   python3 -m venv venv
    ```
5. [Activate the virtual environment.](https://realpython.com/python-virtual-environments-a-primer/#activate-it)
6. Install the requirements mentioned in the requirements' directory. Run the following command
    ```shell
   pip3 install -r requirements/dev-requirements.txt
    ```
7. Make any migrations if required.
8. Run the game by
    ```shell
   python3 manage.py runserver
    ```

### Demo:

![Demo of the game](https://github.com/iakhil/wordatlas/blob/master/word_atlast_demo.gif)
