from flask import Flask, render_template, request, jsonify
import oracledb

app = Flask(__name__)

# Database connection settings
db_user = 'your_db_user'
db_password = 'your_db_password'
db_dsn = 'your_db_dsn'

def execute_query(query, bind_variables=None):
    connection = oracledb.connect(db_user, db_password, db_dsn)
    cursor = connection.cursor()
    result = None
    
    try:
        if bind_variables:
            result = cursor.execute(query, bind_variables)
        else:
            result = cursor.execute(query)
        connection.commit()
    except oracledb.DatabaseError as e:
        print("Error:", e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
    
    return result

@app.route('/')
def index():
    return "Welcome to the PL/SQL Package Demo!"

@app.route('/create_comment', methods=['POST'])
def create_comment():
    # Parse request data
    data = request.json
    created_at = data.get('created_at')
    modified_at = data.get('modified_at')
    content = data.get('content')
    posting_id = data.get('posting_id')
    
    # Call the CreateComment function
    query = "BEGIN :result := CommentsPackage.CreateComment(:created_at, :modified_at, :content, :posting_id); END;"
    bind_variables = {
        'result': oracledb.NUMBER,
        'created_at': created_at,
        'modified_at': modified_at,
        'content': content,
        'posting_id': posting_id
    }
    result = execute_query(query, bind_variables)
    
    return jsonify({'comment_id': result})

# Add routes for other functions (UpdateComment, DeleteComment, GetComment, GetCommentsByPosting)
# Similar to the create_comment route above

if __name__ == '__main__':
    app.run(debug=True)