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