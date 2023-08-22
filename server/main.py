from flask import Flask
from flask_cors import CORS
from dbconnection import *
import moviesites


app = Flask(__name__)

CORS(app)

app.add_url_rule('/add_moviesite', view_func=moviesites.add_moviesite, methods=['POST'])
app.add_url_rule('/get_moviesite/<int:site_id>', view_func=moviesites.get_moviesite, methods=['GET'])
app.add_url_rule('/get_all_moviesites', view_func=moviesites.get_all_moviesites, methods=['GET'])
app.add_url_rule('/update_moviesite/<int:site_id>', view_func=moviesites.update_moviesite, methods=['PUT'])
app.add_url_rule('/delete_moviesite/<int:site_id>', view_func=moviesites.delete_moviesite, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)


