from flask import request, jsonify
import dbconnection as db

#데이터 베이스에 191까지 identity 로 부여된 site_id라는 default id 키가 있는데, 새로 인풋을 받을 때, 1부터 플라스크가 id를 받아 오류가 생기는 듯함. 
#해당 오류 혼자 해결 역부족. 교수님께 여쭤보기
'''
def add_moviesite():
    connection = db.create_connection()
    cursor = connection.cursor()
    site_name = request.json['site_name']
    province = request.json['province']
    city = request.json['city']
    street = request.json['street']
    longtitude = request.json['longtitude']
    latitude = request.json['latitude']
    
    
    cursor.callfunc('MoviesitesPackage.CreateMoviesite',
                    [site_name, province, city, street, longtitude, latitude])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"status": "success"}), 201
'''

def get_moviesite(site_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    moviesite_ref_cursor = cursor.callfunc('MoviesitesPackage.GetMoviesite', db.CURSOR, [site_id])
    moviesite_data = []
    for row in moviesite_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(moviesite_ref_cursor.description, row)}
        moviesite_data.append(row_as_dict)
    return jsonify(moviesite_data)


def get_all_moviesites():
    connection = db.create_connection()    
    cursor = connection.cursor()
    moviesites_ref_cursor = cursor.callfunc('MovieSitesPackage.GetAllMoviesites', db.CURSOR)
    moviesites_data = []
    for row in moviesites_ref_cursor:
        row_as_dict = {desc[0]: value for desc, value in zip(moviesites_ref_cursor.description, row)}
        moviesites_data.append(row_as_dict)
    return jsonify(moviesites_data)


def update_moviesite(site_id):
    connection = db.create_connection() 
    cursor = connection.cursor()
    site_name = request.json['site_name']
    province = request.json['province']
    city = request.json['city']
    street = request.json['street']
    longtitude = request.json['longtitude']
    latitude = request.json['latitude']
    
    cursor.callproc('MovieSitesPackage.UpdateMovieSite', [site_id, site_name, province, city, street, longtitude,latitude])
    connection.commit()
    return jsonify({"status": "updated"}), 200


def delete_moviesite(site_id):
    connection = db.create_connection()
    cursor = connection.cursor()
    cursor.callproc('MovieSitesPackage.DeleteMoviesite', [site_id])
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify(message='Moviesite deleted successfully')