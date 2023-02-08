import json
import os.path
from unittest import TestCase
from src.app.repo_github import RepoGitHub
"""TestRepoGitHub"""


class TestRepoGitHub(TestCase):
    """TestRepoGitHub class

    contains the test cases for repository cloning and removing
    """

    def test_clone_repo_pos(self):
        """Positive test for cloning repository

        Check whether the function cloneRepo() succeeds to clone the repo to a local directory
        """
        with open("test_clone_repo_pos.txt", "r") as f:
            dataJSON_str = f.read()
            dataJSON = json.loads(dataJSON_str)
            print(dataJSON)
            repoGitHub = RepoGitHub(dataJSON)
            repoGitHub.cloneRepo()
            # print(repoGitHub.repo_folder_name)
        self.assertTrue(os.path.isdir(repoGitHub.repo_folder_name))
        repoGitHub.removeRepo()

    def test_clone_repo_neg(self):
        """Negative test for cloning repository

        Check whether the function cloneRepo() fails to clone the repo to a local directory
        """
        with open("test_clone_repo_neg.txt", "r") as f:
            dataJSON_str = f.read()
            dataJSON = json.loads(dataJSON_str)
            # print(dataJSON)
            repoGitHub = RepoGitHub(dataJSON)
            repo_folder_name_origin = repoGitHub.repo_folder_name
            repoGitHub.repo_folder_name = " "
            repoGitHub.cloneRepo()
            # print(repoGitHub.repo_folder_name)
        self.assertFalse(os.path.isdir(repo_folder_name_origin))
        repoGitHub.removeRepo()

    def test_remove_repo_pos(self):
        """Positive test for removing repository

        Check whether the function removeRepo() succeeds to remove the repo from a local directory
        """
        with open("test_clone_repo_pos.txt", "r") as f:
            dataJSON_str = f.read()
            dataJSON = json.loads(dataJSON_str)
            repoGitHub = RepoGitHub(dataJSON)
            repoGitHub.cloneRepo()
            repoGitHub.removeRepo()
        self.assertFalse(os.path.isdir(repoGitHub.repo_folder_name))

    def test_remove_repo_neg(self):
        """Negative test for removing repository

        Check whether the function removeRepo() fails to remove the repo from a local directory
        """
        with open("test_clone_repo_pos.txt", "r") as f:
            dataJSON = f.read()
            repoGitHub = RepoGitHub(dataJSON)
            repoGitHub.cloneRepo()
            wrong_path = " "
            repoGitHub.repo_path_name = wrong_path
            repoGitHub.removeRepo()
        self.assertTrue(os.path.isdir(repoGitHub.repo_folder_name))
