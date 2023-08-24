from flask import request, jsonify
import dbconnection as db

def create_comment():
    connection = db.create_connection()
    cursor = connection.cursor()
    created_at = request.json['created_at']
    modified_at = request.json['modified_at']
    content = request.json['content']
    user_id = request.json['user_id']
    posting_id = request.json['posting_id']
    cursor.callfunc('CommentsPackage.CreateComment',
                    int, [created_at, modified_at, content, user_id, posting_id])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"status": "success"}), 201

def read_comment(comment_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    comment_ref_cursor = cursor.callfunc('CommentsPackage.GetComment', db.CURSOR, [comment_id])
    comment_data = []
    for row in comment_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(comment_ref_cursor.description, row)}
        comment_data.append(row_as_dict)
    
    return jsonify(comment_data)

def update_comment(comment_id):
    connection = db.create_connection() 
    cursor = connection.cursor()
    modified_at = request.json['modified_at']
    content = request.json['content']
    posting_id = request.json['posting_id']
    
    cursor.callproc('MovieSitesPackage.UpdateMovieSite', [comment_id, modified_at, content, posting_id])
    connection.commit()
    
    return jsonify({"status": "updated"}), 200
    
def delete_comment(comment_id):
    connection = db.create_connection() 
    cursor = connection.cursor()
    cursor.callproc('MovieSitesPackage.DeleteMoviesite', [comment_id])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify(message= 'Comment deleted successfully')