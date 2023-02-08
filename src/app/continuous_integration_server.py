from flask import request
from flask import Flask
import os

from continuous_integration import ContinuousIntegration
from repo_github import RepoGitHub

app = Flask(__name__)

@app.route('/results')
def get_results():
    dir_path = os.getcwd() + "\\results"
    page_content = ""
    numberResults = len(os.listdir(dir_path))
    if numberResults == 0:
        return "There are no results files."
    for filename in os.listdir(dir_path):
        page_content += "<a href='/results/"+filename+"'>" + filename + "</a><br>"
    return page_content


@app.route('/results/<filename>')
def get_resultFile(filename):
    content = ""
    with open(os.path.join(os.getcwd() + "\\results", filename), 'r') as resultFile:
        for l in resultFile.readlines():
            content += l + "<br>"
    return content


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
