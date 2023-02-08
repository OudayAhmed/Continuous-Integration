from git import Repo
import os
import tempfile
from git import rmtree


class RepoGitHub:

    def __init__(self, data):
        self.data = data
        self.repo_name = data['pull_request']['head']['repo']['name']
        self.branch_name = data['pull_request']['head']['ref']
        self.clone_url = data['pull_request']['head']['repo']['clone_url']
        self.userSender = data['sender']['login']
        self.action = data['action']
        self.repo_path = ""
        self.repo_folder_name = ""
        self.isCloned = False
        self.isRemoved = False

    def cloneRepo(self, resultFileName):
        with open(os.path.join(os.getcwd() + "\\results", resultFileName), 'a') as resultFile:
            resultFile.write(f'1. Cloning the Repo\n')
            resultFile.write("=================================================================================\n")
            if not self.repo_name:
                resultFile.write("The repo name is missing.\n\n")
            elif not self.branch_name:
                resultFile.write("The branch name is missing.\n\n")
            elif not self.userSender:
                resultFile.write("Username is missing.\n\n")
            else:
                resultFile.write(f'Cloning the {self.repo_name} repo from the {self.branch_name} branch after a '
                                 f'pull\nrequest is {self.action} by {self.userSender}.\n\n')
                self.repo_path = tempfile.mkdtemp(dir=os.getcwd())
                self.repo_folder_name = self.repo_path[len(os.getcwd()) + 1:]
                Repo.clone_from(self.clone_url, self.repo_path, branch=self.branch_name)
                self.isCloned = True
            if self.isCloned:
                print(f'{self.repo_name} repo cloning succeeded.')
            else:
                print(f'{self.repo_name} repo cloning failed.')

    def removeRepo(self, resultFileName):
        with open(os.path.join(os.getcwd() + "\\results", resultFileName), 'a') as resultFile:
            if not self.repo_path:
                resultFile.write("The repo path is missing.\n\n")
            else:
                rmtree(self.repo_path)
                self.isRemoved = True
            if self.isCloned:
                print(f'{self.repo_name} repo removing succeeded.')
            else:
                print(f'{self.repo_name} repo removing failed.')
