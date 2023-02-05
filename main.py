from git import Repo
from flask import request, json
from flask import Flask
import os
import tempfile
import subprocess
from git import rmtree



app = Flask(__name__)


@app.route('/')
def api_root():
    return "Test 1"


@app.route('/github', methods=['POST'])
def api_git_new_issue():
    if request.headers['Content-Type'] == 'application/json':

        info = request.get_json()
        print(info)

        path = os.getcwd()
        print(path)
        f = tempfile.mkdtemp(dir=path)
        print(f)
        Repo.clone_from(info['repository']['clone_url'], f, branch=info['repository']['default_branch'])
        path_main = f + '\main.py'
        subprocess.call(['python', path_main], shell=True)
        rmtree(f)

        return "Test 2"


if __name__ == '__main__':
    app.run(port=8015, debug=True)
