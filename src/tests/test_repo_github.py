import os.path
from unittest import TestCase
from ..app.repo_github import RepoGitHub

"""TestRepoGitHub"""


class TestRepoGitHub(TestCase):
    """TestRepoGitHub class

    contains the test cases for repository cloning and removing
    """

    def test_clone_repo_pos(self):
        """Positive test for cloning repository

        Check whether the function cloneRepo() succeeds to clone the repo to local a local directory
        """
        with open("test_clone_repo_pos.txt", "r") as f:
            dataJSON = f.read()
            repoGitHub = RepoGitHub(dataJSON)
            repoGitHub.cloneRepo()
        self.assertTrue(os.path.isdir())

    def test_clone_repo_neg(self):
        """Negative test for cloning repository

        Check whether the function cloneRepo() fails to clone the repo to local a local directory
        """
        with open("test_clone_repo_neg.txt", "r") as f:
            dataJSON = f.read()
            repoGitHub = RepoGitHub(dataJSON)
            repoGitHub.cloneRepo()
        self.assertFalse(os.path.isdir())

    def test_remove_repo_pos(self):
        with open("test_clone_repo_pos.txt", "r") as f:
            dataJSON = f.read()
            repoGitHub = RepoGitHub(dataJSON)
            repoGitHub.cloneRepo()
            repoGitHub.removeRepo()
        self.assertFalse(os.path.isdir())

    def test_remove_repo_neg(self):
        with open("test_clone_repo_pos.txt", "r") as f:
            dataJSON = f.read()
            repoGitHub = RepoGitHub(dataJSON)
            repoGitHub.cloneRepo()
            wrong_path = " "
            repoGitHub.repo_path = wrong_path
            repoGitHub.removeRepo()
        self.assertTrue(os.path.isdir())
