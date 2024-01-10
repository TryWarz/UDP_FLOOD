from flask import Blueprint, render_template, request, redirect, url_for, flash, session, send_file, jsonify
import json
request = Blueprint('request', __name__, template_folder='templates', static_folder='static')

@request.route('/request')
def request_botnet():
    with open('request.json', 'r') as f:
        json_data = json.load(f)

    return jsonify(json_data)