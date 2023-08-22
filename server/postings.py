from flask import request, jsonify
import dbconnection as db

def create_posting():
    connection = db.create_connection()
    cursor = connection.cursor()

    title = request.json['title']
    content = request.json['content']
    image = request.json['image']
    created_at = request.json['created_at']
    modified_at = request.json['modified_at']
    moviesites_sites_id = request.json['moviesites_sites_id']
    site_id = request.json['site_id']

    cursor.callfunc('PostingsPackage.CreatePosting', db.NUMBER,
                    [title, content, image, created_at, modified_at, moviesites_sites_id, site_id])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"status": "success"}), 201

def update_posting(posting_id):
    connection = db.create_connection()
    cursor = connection.cursor()

    title = request.json['title']
    content = request.json['content']
    image = request.json['image']
    created_at = request.json['created_at']
    modified_at = request.json['modified_at']
    moviesites_sites_id = request.json['moviesites_sites_id']
    site_id = request.json['site_id']

    cursor.callproc('PostingsPackage.UpdatePosting', [posting_id, title, content, image, created_at, modified_at, moviesites_sites_id, site_id])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"status": "updated"}), 200

def delete_posting(posting_id):
    connection = db.create_connection()
    cursor = connection.cursor()

    cursor.callproc('PostingsPackage.DeletePosting', [posting_id])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify(message='Posting deleted successfully')

def get_posting(posting_id):
    connection = db.create_connection()
    cursor = connection.cursor()

    posting_ref_cursor = cursor.callfunc('PostingsPackage.GetPosting', db.CURSOR, [posting_id])
    posting_data = []
    for row in posting_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(posting_ref_cursor.description, row)}
        posting_data.append(row_as_dict)

    return jsonify(posting_data)

def get_postings_by_site(site_id):
    connection = db.create_connection()
    cursor = connection.cursor()

    postings_ref_cursor = cursor.callfunc('PostingsPackage.GetPostingsBySite', db.CURSOR, [site_id])
    postings_data = []
    for row in postings_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(postings_ref_cursor.description, row)}
        postings_data.append(row_as_dict)

    return jsonify(postings_data)
