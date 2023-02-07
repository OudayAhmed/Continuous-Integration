from flask import request
from flask import Flask

from continuous_integration import ContinuousIntegration
from repo_github import RepoGitHub

app = Flask(__name__)


@app.route('/')
def continuous_integration():
    return "Test 1"


@app.route('/', methods=['POST'])
def continuous_integration_post():
    dataJSON = request.json
    if 'pull_request' in dataJSON and (dataJSON['action'] == "opened" or dataJSON['action'] == "reopened"):
        repoGitHub = RepoGitHub(dataJSON)
        repoGitHub.cloneRepo()
        continuous_integration = ContinuousIntegration(repoGitHub.repo_path)
        continuous_integration.installRequirements()
        continuous_integration.staticSyntaxCheck()
        continuous_integration.testing()
        repoGitHub.removeRepo()
        return "Test 2"
    else:
        return "Test 3"


if __name__ == '__main__':
    app.run(host="localhost", port=8015, debug=True)
