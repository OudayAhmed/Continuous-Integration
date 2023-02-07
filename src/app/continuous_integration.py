import os


class ContinuousIntegration:

    def __init__(self, repo_path):
        self.repo_path = repo_path

    def installRequirements(self):
        print("=======================================================================")
        print("=============== 3. Installing the requirements ========================")
        print("=======================================================================")
        path_req = self.repo_path + "\\src\\requirements.txt"
        os.system("pip install -r " + path_req)
        print(f'The requirements have been successfully installed.')

    def staticSyntaxCheck(self):
        print("=======================================================================")
        print("======================== 4. Syntax checking ===========================")
        print("=======================================================================")
        print(f'.')
        path_req = self.repo_path + "\\src"
        os.system("pylint --disable=W,C,R,E0401 " + path_req)
        print(f'The syntax checking has been successfully completed.')

    def testing(self):
        print("=======================================================================")
        print("======================= 5. The testing is running =====================")
        print("=======================================================================")
        path_req = self.repo_path
        print(path_req)
        os.system("python -m unittest discover " + path_req)
        print(f'The testing has been successfully completed.')
