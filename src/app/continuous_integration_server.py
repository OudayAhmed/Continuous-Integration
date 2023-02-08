from flask import request
from flask import Flask

from continuous_integration import ContinuousIntegration
from repo_github import RepoGitHub

app = Flask(__name__)


@app.route('/')
def get_continuous_integration():
    return "Continuous Integration Server"


@app.route('/', methods=['POST'])
def continuous_integration_post():
    dataJSON = request.json
    if 'pull_request' in dataJSON and (dataJSON['action'] == "opened" or dataJSON['action'] == 'synchronize' or dataJSON['action'] == "reopened"):
        repoGitHub = RepoGitHub(dataJSON)
        build_results = BuildResults(repoGitHub)
        repoGitHub.cloneRepo(build_results.resultFileName)
        if repoGitHub.isCloned:
            continuous_integration = ContinuousIntegration(repoGitHub.repo_path, build_results.resultFileName)
            continuous_integration.installRequirements()
            if continuous_integration.isRequirementsInstalled:
                continuous_integration.staticSyntaxCheck()
                continuous_integration.testing()
        repoGitHub.removeRepo(build_results.resultFileName)
        return "Succeeded"
    else:
        return "This action is not supported by the server."


if __name__ == '__main__':
    app.run(host="localhost", port=8015)
