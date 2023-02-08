import os.path
from unittest import TestCase
from ..app.repo_github import RepoGitHub



class TestRepoGitHub(TestCase):

    def test_clone_repo_pos(self):
        with open("test_clone_repo_pos.txt", "r") as f:
            dataJSON = f.read()
            repoGitHub = RepoGitHub(dataJSON)
            repoGitHub.cloneRepo()
        self.assertTrue(os.path.isdir())

    def test_clone_repo_neg(self):
        with open("test_clone_repo_neg.txt", "r") as f:
            dataJSON = f.read()
            repoGitHub = RepoGitHub(dataJSON)
            repoGitHub.cloneRepo()
        self.assertFalse(os.path.isdir())

    def test_remove_repo(self):
        self.fail()