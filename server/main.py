from flask import Flask, jsonify
import oracledb

app = Flask(__name__)

def create_connection():
    connection = oracledb.connect(user="kosa13", password="kosa2023oraclE", dsn="edudb_high",
                                  config_dir="C:\Dev\Python\Wallet_edudb",
                                  wallet_location="C:\Dev\Python\Wallet_edudb",
                                  wallet_password="pythonoracle21")
    return connection

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

if __name__ == '__main__':
    app.run(debug=True)