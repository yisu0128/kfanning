from flask import Flask
from flask_cors import CORS
from dbconnection import *
import moviesites
import postings
import comments
import users

app = Flask(__name__)


@app.route('/')
def index():
    return 'FANNINGK'

CORS(app)

app.add_url_rule('/create_user', view_func=users.create_user, methods=['POST'])
app.add_url_rule('/get_user/<int:user_id>', view_func=users.get_user, methods=['GET'])
app.add_url_rule('/get_all_users', view_func=users.get_all_users, methods=['GET'])
app.add_url_rule('/update_user/<int:user_id>', view_func=users.update_user, methods=['POST'])
app.add_url_rule('/delete_user/<int:user_id>', view_func=users.delete_user, methods=['DELETE'])

app.add_url_rule('/add_moviesite', view_func=moviesites.add_moviesite, methods=['POST'])
app.add_url_rule('/get_moviesite/<int:site_id>', view_func=moviesites.get_moviesite, methods=['GET'])
app.add_url_rule('/get_all_moviesites', view_func=moviesites.get_all_moviesites, methods=['GET'])
app.add_url_rule('/update_moviesite/<int:site_id>', view_func=moviesites.update_moviesite, methods=['PUT'])
app.add_url_rule('/delete_moviesite/<int:site_id>', view_func=moviesites.delete_moviesite, methods=['DELETE'])

app.add_url_rule('/create_posting', view_func=postings.create_posting, methods=['POST'])
app.add_url_rule('/update_posting/<int:posting_id>', view_func=postings.update_posting, methods=['PUT'])
app.add_url_rule('/delete_posting/<int:posting_id>', view_func=postings.delete_posting, methods=['DELETE'])
app.add_url_rule('/get_posting/<int:posting_id>', view_func=postings.get_posting, methods=['GET'])
app.add_url_rule('/get_postings_by_site/<int:site_id>', view_func=postings.get_postings_by_site, methods=['GET'])
app.add_url_rule('/get_postings_by_liked/<int:site_id>', view_func=postings.get_postings_by_liked, methods=['GET'])

app.add_url_rule('/create_comment', view_func=comments.create_comment, methods=['POST'])
app.add_url_rule('/read_comment/<int:comment_id>', view_func=comments.read_comment, methods=['GET'])
app.add_url_rule('/update_comment/<int:comment_id>', view_func=comments.update_comment, methods=['PUT'])
app.add_url_rule('/delete_comment/<int:comment_id>', view_func=comments.delete_comment, methods=['DELETE'])




if __name__ == '__main__':
    app.run(debug=True)


