from flask import Flask, Blueprint
from flask_cors import CORS
from config import Config


#blueprint imports dito naman

from user.routes import user_bp
from scores.routes import scores_bp
from logs.routes import logs_bp
from elements.routes import elements_bp

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)


#blueprints dito ilalagay
app.register_blueprint(user_bp)
app.register_blueprint(scores_bp)
app.register_blueprint(logs_bp)
app.register_blueprint(elements_bp)

if __name__ == '__main__':
    app.run(debug=True)