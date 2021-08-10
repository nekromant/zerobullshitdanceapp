from flask import Flask
import yaml
import sqlalchemy

db = None
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This app will be big someday!</p>"

if __name__ == "__main__":
    with open("config.yaml", "r") as fd:
        cfg = yaml.load(fd)

    app.config.from_object(cfg)
    db = sqlalchemy.create_engine('sqlite:///database.sqlite', echo=True)
    app.run()