from flask_app.app import create_app
from flask_app.configuration import DevelopmentConfig

if __name__ == "__main__":
    APP = create_app(DevelopmentConfig)
    APP.run(host="0.0.0.0", port=5000)
