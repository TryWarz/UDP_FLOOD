from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import json
information = Blueprint('information', __name__, template_folder='templates', static_folder='static')

request = 0

@information.route('/information')
def information_botnet():
    global request
    request += 1

    with open('request.json', 'r') as f:
        json_data = json.load(f)
        # write the new request
        json_data['request'] = request

    return render_template('information.html', request=request)
    


        