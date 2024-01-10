from flask import Blueprint, render_template, request, redirect, url_for, flash, session, send_file, jsonify
import json

info_attack = Blueprint('info_attack', __name__, template_folder='templates', static_folder='static')


@info_attack.route('/info_attack')
def info_attack_botnet():
    with open('configs.json', 'r') as f:
        json_data = json.load(f)

    return jsonify(json_data)