from flask import request, jsonify
import dbconnection as db

def create_user():
    connection = db.create_connection()
    cursor = connection.cursor()
    user_name = request.json['user_name']
    user_pwd = request.json['user_pwd']
    cursor.callfunc('UsersPackage.CreateUser',
                    int, [user_name, user_pwd])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"status": "success"}), 201

def get_user(user_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    user_ref_cursor = cursor.callfunc('UsersPackage.GetUser', db.CURSOR, [user_id])
    comment_data = []
    for row in user_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(user_ref_cursor.description, row)}
        comment_data.append(row_as_dict)
    
    return jsonify(comment_data)

def get_all_users():
    connection = db.create_connection()    
    cursor = connection.cursor()
    user_ref_cursor = cursor.callfunc('UsersPackage.GetAllUsers', db.CURSOR)
    users_data = []
    for row in user_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(user_ref_cursor.description, row)}
        users_data.append(row_as_dict)
    return jsonify(users_data)

def update_user(user_id):
    connection = db.create_connection() 
    cursor = connection.cursor()
    user_name = request.json['user_name']
    user_pwd = request.json['user_pwd']
    
    cursor.callproc('UsersPackage.UpdateUser', [user_id, user_name, user_pwd])
    connection.commit()
    
    return jsonify({"status": "updated"}), 200


    
def delete_user(user_id):
    connection = db.create_connection() 
    cursor = connection.cursor()
    cursor.callproc('UsersPackage.DeleteUser', [user_id])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify(message= 'User deleted successfully')