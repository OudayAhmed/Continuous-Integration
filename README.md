# Assignment 2 - Continuous-Integration
This repository consist of code for the Continuous Integration lab (course DD2480) at KTH. 

The program in this repository is an implementation of a small continuous integration CI server. The features of the server is:
- Compilation
    - The server supports compiling the group project.
    - The server has a syntax check that is performed for languages without compilers. 
    - Compilation is triggered as webhook.
- Testing
    - The server supports executing the automated tests for the group project. 
    - Testing is triggered as webhook on the branch where the change has been made (as specified in the HTTP payload).
- Notification
    - The server supports notification of CI results.
    - The server sends an email to the project member about the build result. 

## Installation
In order to run the code properly, a version of Python >= 3.8 is required.

### Run code and tests
To run the program, navigate to the src folder, then the app folder, then run this command in the terminal to install the requirements:

    python3 continuous_integration.py

To troubleshoot any potential requirement installations, the packages could be installed manually in the terminal as well with these following commands:

    pip install Flask
    pip install pylint
    pip install Flask-Mail
    pip install GitPython




## Contributions

- **Ouday Ahmed**: Ouday designed and implemented the general code architecture of the project, including the class skeletons.  He has also written the code for the methods in continouous_integraton.py
- **Yiming Ju**: Yiming has implemented the tests and written documentation for the repo_github.py methods. 
- **Oscar Knowles**: Oscar has implemented the tests and written documentation for the continuous_integration.py methods and written SEMAT and project documentation (README) together with Christofer and Elin. 
- **Elin Liu**: Elin was the stakeholder for building and implemententing the Sphinx tests and written SEMAT togheter with Oscar and Christofer.
- **Christofer Vikström**: Christofer created the code, documentation and tests for the notification system that sends email from the CI server to the team member with the build results. He also created the SEMAT and project documentation (README) together with Oscar. 

