from flask import Flask
from database import init_db

server = Flask(__name__)


@server.route("/api/data")
def get_data():
    # This could be an endpoint to fetch data for other purposes
    pass


if __name__ == "__main__":
    init_db()
    server.run(debug=True)
