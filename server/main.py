from flask import Flask, jsonify, request
import oracledb

app = Flask(__name__)

def create_connection():
    connection = oracledb.connect(user="kosa13", password="kosa2023oraclE", dsn="edudb_high",
                                  config_dir="C:\Dev\Python\Wallet_edudb",
                                  wallet_location="C:\Dev\Python\Wallet_edudb",
                                  wallet_password="pythonoracle21")
    return connection


#moviesite

@app.route('/moviesites')
def read_moviesites():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        # Call the GetAllMoviesites function from the package using callfunc
        result = cursor.callfunc("MoviesitesPackage.GetAllMoviesites", oracledb.CURSOR)
        
        moviesites = []

        for row in result:
            moviesite = {
                'site_id': row[0],
                'site_name': row[1],
                'province': row[2],
                'city': row[3],
                'street': row[4],
                'longitude': row[5],
                'latitude': row[6]
            }
            moviesites.append(moviesite)

        return jsonify({'moviesites': moviesites})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()
        
        
        
@app.route('/search_moviesite', methods=['GET'])
def search_moviesite():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        site_id = request.args.get('site_id')

        result = cursor.callfunc("MoviesitesPackage.GetMoviesite", oracledb.CURSOR, [site_id])
        
        moviesites = []

        for row in result:
            moviesite = {
                'site_id': row[0],
                'site_name': row[1],
                'province': row[2],
                'city': row[3],
                'street': row[4],
                'longitude': row[5],
                'latitude': row[6]
            }
            moviesites.append(moviesite)

        return jsonify({'moviesites': moviesites})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()
    
        
@app.route('/create_moviesite', methods=['POST'])
def create_moviesite():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        data = request.json  # JSON 데이터 받아오기
        site_name = data.get('site_name')
        province = data.get('province')
        city = data.get('city')
        street = data.get('street')
        longitude = data.get('longitude')
        latitude = data.get('latitude')

        # Call the CreateMoviesite function from the package using callfunc
        site_id = cursor.callfunc("MoviesitesPackage.CreateMoviesite", oracledb.INTEGER, 
                                  [site_name, province, city, street, longitude, latitude])
        connection.commit()
        
        return jsonify({'site_id': site_id, 'message': 'Movie site created successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()

@app.route('/update_moviesite', methods=['GET','PUT'])
def update_moviesite():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        data = request.json  # JSON 데이터 받아오기
        site_id = data.get('site_id')

        # Retrieve the existing movie site data
        cursor.callproc("MoviesitesPackage.GetMoviesite", [site_id])
        existing_data = cursor.fetchone()

        if not existing_data:
            return jsonify({'error': 'Movie site not found'}), 404

        # Parse JSON data and update relevant columns
        site_name = data.get('site_name', existing_data[1])
        province = data.get('province', existing_data[2])
        city = data.get('city', existing_data[3])
        street = data.get('street', existing_data[4])
        longitude = data.get('longitude', existing_data[5])
        latitude = data.get('latitude', existing_data[6])

        # Call the UpdateMoviesite procedure to update the database
        cursor.callproc("MoviesitesPackage.UpdateMoviesite", [
            site_id, site_name, province, city, street, longitude, latitude
        ])
        connection.commit()

        return jsonify({'site_id': site_id, 'message': 'Movie site updated successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()
        
@app.route('/delete_moviesite', methods=['GET','DELETE'])
def delete_moviesite():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        site_id = request.args.get('site_id')

        # Call the DeleteMoviesite procedure to delete the movie site
        cursor.callproc("MoviesitesPackage.DeleteMoviesite", [site_id])
        connection.commit()

        return jsonify({'site_id': site_id, 'message': 'Movie site deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()
        
        
        
        
#posting
@app.route('/read_posting', methods=['GET'])
def read_post():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        posting_id = request.args.get('posting_id')

        result = cursor.callfunc("PostingsPackage.GetPosting", oracledb.CURSOR, [posting_id])
        
        postings = []

        for row in result:
            posting = {
                'posting_id': row[0],
                'title': row[1],
                'content': row[2],
                'image': row[3],
                'created_at': row[4].strftime('%Y-%m-%d %H:%M:%S'),
                'modified_at': row[5].strftime('%Y-%m-%d %H:%M:%S'),
                'moviesites_sites_id': row[6],
                'site_id': row[7]
            }
            postings.append(posting)

        return jsonify({'postings': postings})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()


@app.route('/create_posting', methods=['POST'])
def create_posting():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        data = request.json  # JSON 데이터 받아오기
        title = data.get('title')
        content = data.get('content')
        image = data.get('image')
        created_at = data.get('created_at')
        modified_at = data.get('modified_at')
        moviesites_sites_id = data.get('moviesites_sites_id')
        site_id = data.get('site_id')

        # Call the CreatePosting function from the package using callfunc
        posting_id = cursor.callfunc("PostingsPackage.CreatePosting", oracledb.INTEGER, 
                                     [title, content, image, created_at, modified_at, 
                                      moviesites_sites_id, site_id])
        connection.commit()
        
        return jsonify({'posting_id': posting_id, 'message': 'Posting created successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()

@app.route('/update_posting', methods=['PUT'])
def update_posting():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        data = request.json  # JSON 데이터 받아오기
        posting_id = data.get('posting_id')

        # Retrieve the existing posting data
        cursor.callproc("PostingsPackage.GetPosting", [posting_id])
        existing_data = cursor.fetchone()

        if not existing_data:
            return jsonify({'error': 'Posting not found'}), 404

        # Parse JSON data and update relevant columns
        title = data.get('title', existing_data[1])
        content = data.get('content', existing_data[2])
        image = data.get('image', existing_data[3])
        created_at = data.get('created_at', existing_data[4])
        modified_at = data.get('modified_at', existing_data[5])
        moviesites_sites_id = data.get('moviesites_sites_id', existing_data[6])
        site_id = data.get('site_id', existing_data[7])

        # Call the UpdatePosting procedure to update the database
        cursor.callproc("PostingsPackage.UpdatePosting", [
            posting_id, title, content, image, created_at, modified_at,
            moviesites_sites_id, site_id
        ])
        connection.commit()

        return jsonify({'posting_id': posting_id, 'message': 'Posting updated successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()

@app.route('/delete_posting', methods=['DELETE'])
def delete_posting():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        posting_id = request.args.get('posting_id')

        # Call the DeletePosting procedure to delete the posting
        cursor.callproc("PostingsPackage.DeletePosting", [posting_id])
        connection.commit()

        return jsonify({'posting_id': posting_id, 'message': 'Posting deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()

       
        
        
#comment    
   
@app.route('/read_comment', methods=['GET'])
def read_comment():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        comment_id = request.args.get('comment_id')

        result = cursor.callfunc("CommentsPackage.GetComment", oracledb.CURSOR, [comment_id])
        
        comments = []

        for row in result:
            comment = {
                'comment_id': row[0],
                'created_at': row[1],
                'modified_at': row[2],
                'content': row[3],
                'posting_id': row[4]
            }
            comments.append(comment)

        return jsonify({'comments': comments})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()
        


@app.route('/create_comment', methods=['POST'])
def create_comment():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        data = request.json
        created_at = data.get('created_at')
        modified_at = data.get('modified_at')
        content = data.get('content')
        posting_id = data.get('posting_id')

        comment_id = cursor.callfunc("CommentsPackage.CreateComment", oracledb.INTEGER,
                                     [created_at, modified_at, content, posting_id])
        connection.commit()

        return jsonify({'comment_id': comment_id, 'message': 'Comment created successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()

@app.route('/update_comment', methods=['PUT'])
def update_comment():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        data = request.json
        comment_id = data.get('comment_id')

        cursor.callproc("CommentsPackage.GetComment", [comment_id])
        existing_data = cursor.fetchone()

        if not existing_data:
            return jsonify({'error': 'Comment not found'}), 404

        created_at = data.get('created_at', existing_data[1])
        modified_at = data.get('modified_at', existing_data[2])
        content = data.get('content', existing_data[3])
        posting_id = data.get('posting_id', existing_data[4])

        cursor.callproc("CommentsPackage.UpdateComment", [
            comment_id, created_at, modified_at, content, posting_id
        ])
        connection.commit()

        return jsonify({'comment_id': comment_id, 'message': 'Comment updated successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()

@app.route('/delete_comment', methods=['DELETE'])
def delete_comment():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        comment_id = request.args.get('comment_id')

        cursor.callproc("CommentsPackage.DeleteComment", [comment_id])
        connection.commit()

        return jsonify({'comment_id': comment_id, 'message': 'Comment deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
