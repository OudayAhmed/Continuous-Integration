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
        self.user = data['pull_request']['user']['login']
        self.repo_path = ""
        self.repo_folder_name = ""

    def cloneRepo(self):
        print("=======================================================================")
        print("======================== 1. Cloning the Repo ==========================")
        print("=======================================================================")
        print(f'- Cloning the {self.repo_name} repo from the {self.branch_name} branch \nafter a pull request is '
              f'opened by {self.user}.')
        path = os.getcwd()
        self.repo_path = tempfile.mkdtemp(dir=path)
        self.repo_folder_name = self.repo_path[len(path) + 1:]
        Repo.clone_from(self.clone_url, self.repo_path, branch=self.branch_name)
        print(f'- The repo has been successfully cloned inside the {self.repo_folder_name} folder.')

    def removeRepo(self):
        print("=======================================================================")
        print("======================= 6. Removing the Repo ==========================")
        print("=======================================================================")
        print(f'Removing the {self.repo_name} repo.')
        rmtree(self.repo_path)
        print(f'The repo has been successfully removed.')