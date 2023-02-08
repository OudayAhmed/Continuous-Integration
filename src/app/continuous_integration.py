import os
import re

import subprocess


class ContinuousIntegration:

    def __init__(self, repo_path, resultFileName):
        self.repo_path = repo_path
        self.resultFileName = resultFileName
        self.isRequirementsInstalled = False
        self.isSyntaxCheckingSucceeded = True
        self.isTestingSucceeded = False

    def installRequirements(self):
        with open(os.path.join(os.getcwd() + "\\results", self.resultFileName), 'a') as resultFile:
            resultFile.write(f'2. Installing the requirements\n')
            resultFile.write("=================================================================================\n")
        path_req = self.repo_path + "\\src\\requirements.txt"
        if not path_req:
            with open(os.path.join(os.getcwd() + "\\results", self.resultFileName), 'a') as resultFile:
                resultFile.write("The requirements file is missing.\n\n")
        else:
            with open(os.path.join(os.getcwd() + "\\results", self.resultFileName), 'a') as resultFile:
                subprocess.call("pip install -r " + path_req, shell = True, stdout=resultFile)
            self.isRequirementsInstalled = True
        if self.isRequirementsInstalled:
            print(f'Requirements installing succeeded.')
        else:
            print(f'Requirements installing failed.')

    def staticSyntaxCheck(self):
        with open(os.path.join(os.getcwd() + "\\results", self.resultFileName), 'a') as resultFile:
            resultFile.write(f'\n2. Syntax checking\n')
            resultFile.write("=================================================================================\n")
        with open(os.path.join(os.getcwd() + "\\results", self.resultFileName), 'a') as resultFile:
            subprocess.call("pylint --disable=W,C,R,E0401 " + self.repo_path + "\\src", shell = True, stdout=resultFile)
        with open("results\\" + self.resultFileName, 'r') as resultFile:
            result = None
            for l in resultFile:
                result = re.search('E\d\d\d\d:', l)
                if result is not None:
                    self.isSyntaxCheckingSucceeded = False
        if self.isSyntaxCheckingSucceeded:
            print(f'Syntax checking succeeded.')
        else:
            print(f'Syntax checking failed.')

    def testing(self):
        with open(os.path.join(os.getcwd() + "\\results", self.resultFileName), 'a') as resultFile:
            resultFile.write(f'3. Testing\n')
            resultFile.write("=================================================================================\n")
        with open(os.path.join(os.getcwd() + "\\results", self.resultFileName), 'a') as resultFile:
            subprocess.call("python -m unittest discover " + self.repo_path, shell=True, stderr=resultFile)
        with open("results\\" + self.resultFileName, 'r') as f:
            if not ("FAILED" in f.read()):
                self.isTestingSucceeded = True
        if self.isTestingSucceeded:
            print(f'Testing succeeded.')
        else:
            print(f'Testing failed.')