import flask
import routes
# Import blueprints


app_register = [
    routes.download,
    routes.request,
    routes.info_attack,
    routes.control,
    routes.information
]

app = flask.Flask(__name__, static_folder='static', template_folder='templates')



for blueprint in app_register:
    app.register_blueprint(blueprint)

app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'secret!'

if __name__ == '__main__':
    app.run(debug=True)
