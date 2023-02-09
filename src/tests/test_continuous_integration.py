from unittest import TestCase
from ..app.continuous_integration import ContinuousIntegration
import os

class TestContinuousIntegration(TestCase):

    def test_install_requirements_positive(self):
        ciTest = ContinuousIntegration(repo_path=os.getcwd(), resultFileName="testFile.txt", pathOSResults="/results", pathOSSrc="/src")
        ciTest.installRequirements()
        self.assertTrue(ciTest.isRequirementsInstalled)

    def test_install_requirements_negative(self):
        ciTest = ContinuousIntegration(repo_path=os.getcwd(), resultFileName="testFile.txt", pathOSResults="/results", pathOSSrc="/src")
        self.assertFalse(ciTest.installRequirements())

    def test_static_syntax_check_positive(self):
        self.fail()

    def test_static_syntax_check_negative(self):
        self.fail()

    def test_testin_positive(self):
        self.fail()

    def test_testing_negative_positive(self):
        self.fail()