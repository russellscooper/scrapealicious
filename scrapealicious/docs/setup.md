<!-----



Conversion time: 0.387 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Mon Nov 20 2023 17:34:04 GMT-0800 (PST)
* Source doc: Project Initialization
* This is a partial selection. Check to make sure intra-doc links work.
----->



<h1>Project Set Up and Management</h2>
<h2>Samuel Cooper</h2>
<h2>11/20/2023</h2>

* Set up project with Pipenv
    * Follow the [pipenv installtion guide](https://realpython.com/pipenv-guide/)
    * Create a new project directory and navigate to it in the terminal. 
    * Initialize a new pipenv environment 
        * pipenv –python3.8 #Or whatever python version is needed.
    * Install project dependencies
        * pipenv install sphinx bandit sqlalchemy cryptography bleach
    * Activate the virtual environment
        * pipenv shell
* Documentation with sphix
    * Install sphinx using [the sphinx installation guide](https://www.sphinx-doc.org/en/master/usage/installation.html)
        * sphinx-quickstart 
        * Create and organize documentation in the docs directory
* AST node security check 
    * Before pushing any code make sure to run the following command on the file:
        * Bandit -r project-directory-name
* Manage dependencies with pipenv 
    * Document project dependencies in the pipfile and pipfile.lock files. 
* Use SQLalchemy for secure SQL interactions  
* Data-related Tasks with Cryptography:
    * Follow the Cryptography documentation for [installation and usage](https://cryptography.io/en/latest/).
    * Integrate Cryptography for handling data-related tasks securely in your CLI application.
* Attribute Stripping and Escaping with Bleach:
    * Follow the Bleach documentation for[ installation and usage](https://pypi.org/project/bleach/).
* Use Bleach for stripping attributes and escaping data in your CLI application.
* Additional steps:
    * Regularly schedule updates to dependencies and check security advisories using pipenv. 
        * pipenv update
        * pipenv check