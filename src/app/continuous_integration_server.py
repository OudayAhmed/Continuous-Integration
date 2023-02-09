from flask import request
from flask import Flask
from flask_mail import Mail
import os

from src.app.build_results import BuildResults
from src.app.continuous_integration import ContinuousIntegration
from src.app.repo_github import RepoGitHub
from src.app.continuous_integration_notification import send_message

app = Flask(__name__)

team_dict = {}
team_dict['OudayAhmed'] = "oydddua@gmail.com"
team_dict['ChristoferVikstroem'] = "christofer.vikstrom@outlook.com"
team_dict['eliu1217'] = "eliu@kth.se"
team_dict['OscarKnowles'] = "Oscar@knowles.se"
team_dict['Taomyee'] = "yimingju2000@gmail.com"

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_POST'] = 465
app.config['MAIL_USERNAME'] = "cigroup15vt23@gmail.com"
app.config['MAIL_PASSWORD'] = "contintg15"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

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
            continuous_integration = ContinuousIntegration(repoGitHub.repo_path, build_results.resultFileName, repoGitHub.OSPathResults, repoGitHub.OSPathSrc)
            continuous_integration.installRequirements()
            if continuous_integration.isRequirementsInstalled:
                continuous_integration.staticSyntaxCheck()
                continuous_integration.testing()
#                send_message(team_dict[repoGitHub.userSender[0]], continuous_integration.isSyntaxCheckingSucceeded, continuous_integration.isTestingSucceeded)
        repoGitHub.removeRepo(build_results.resultFileName)
        return "Succeeded"
    else:
        return "This action is not supported by the server."


if __name__ == '__main__':
    app.run(host="localhost", port=8015)
