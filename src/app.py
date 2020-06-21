# Imports #####################################################################
###############################################################################

import random
import string
import json

from flask import (
    Flask,
    redirect,
    request
)

# Flask Setup #################################################################
###############################################################################

# Initialise app
app = Flask(__name__, static_folder='static')


# Routes ######################################################################
###############################################################################

@app.route("/oauth2/auth", methods=['GET'])
def auth():
    # response_type = request.args.get('response_type')
    # client_id = request.args.get('client_id')
    redirect_uri = request.args.get('redirect_uri')
    state = request.args.get('state')
    code = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(32)))
    return redirect(redirect_uri + '?code=' + code + '&state=' + state)


@app.route("/oauth2/token", methods=['POST'])
def token():
    access_token = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(32)))
    response = {
        "access_token": access_token,
        "token_type": "bearer"
    }
    return json.dumps(response)


@app.route("/userinfo", methods=['GET'])
def userinfo():
    return app.send_static_file("profile.json")


# Main ########################################################################
###############################################################################

if __name__ == "__main__":
    app.run(ssl_context="adhoc", port=4444)
