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

if __name__ == '__main__':
    app.run(debug=True)