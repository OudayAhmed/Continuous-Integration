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

@app.route('/', methods=['POST'])
def api_git_new_issue():
    info = request.json
    path = os.getcwd()
    print(path)
    f = tempfile.mkdtemp(dir=path)
    print(f)
    Repo.clone_from(info['repository']['clone_url'], f, branch=info['repository']['default_branch'])
    rmtree(f)

    return "Test 2"

if __name__ == '__main__':
    app.run(host="localhost", port=8015, debug=True)
