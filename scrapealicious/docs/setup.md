1. Set up project with Pipenv
    1. Follow the [pipenv installtion guide](https://realpython.com/pipenv-guide/)
    2. Create a new project directory and navigate to it in the terminal. 
    3. Initialize a new pipenv environment 
        1. pipenv –python3.8 #Or whatever python version is needed.
    4. Install project dependencies
        2. pipenv install sphinx bandit sqlalchemy cryptography bleach
    5. Activate the virtual environment
        3. pipenv shell
2. Documentation with sphix
    6. Install sphinx using [the sphinx installation guide](https://www.sphinx-doc.org/en/master/usage/installation.html)
        4. sphinx-quickstart 
        5. Create and organize documentation in the docs directory
3. AST node security check 
    7. Before pushing any code make sure to run the following command on the file:
        6. Bandit -r project-directory-name
4. Manage dependencies with pipenv 
    8. Document project dependencies in the pipfile and pipfile.lock files. 
5. Use SQLalchemy for secure SQL interactions  
6. Data-related Tasks with Cryptography:
    9. Follow the Cryptography documentation for [installation and usage](https://cryptography.io/en/latest/).
    10. Integrate Cryptography for handling data-related tasks securely in your CLI application.
7. Attribute Stripping and Escaping with Bleach:
    11. Follow the Bleach documentation for[ installation and usage](https://pypi.org/project/bleach/).
8. Use Bleach for stripping attributes and escaping data in your CLI application.
9. Additional steps:
    12. Regularly schedule updates to dependencies and check security advisories using pipenv. 
        7. pipenv update
        8. pipenv check