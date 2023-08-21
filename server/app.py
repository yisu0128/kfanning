from flask import Flask, request, jsonify
import oracledb


app = Flask(__name__)

import oracledb

connection = oracledb.connect(user="kosa13", password="kosa2023oraclE", dsn="edudb_high",
                              config_dir="C:\Dev\Python\Wallet_edudb",
                              wallet_location="C:\Dev\Python\Wallet_edudb",
                              wallet_password="pythonoracle21")
cursor = connection.cursor()
    
    
@app.route('/')
def index():
    return "Welcome to the Oracle PL/SQL Package Demo with Flask!"
    
@app.route('/create_moviesite', methods=['GET','POST'])
def create_moviesite():
    data = request.json
    site_name = data.get('site_name')
    province = data.get('province')
    city = data.get('city')
    street = data.get('street')
    longitude = data.get('longitude')
    latitude = data.get('latitude')

    connection = create_connection()
    cursor = connection.cursor()

    try:
        # Call the CreateMoviesite function
        query = "BEGIN :result := MoviesitesPackage.CreateMoviesite(:site_name, :province, :city, :street, :longitude, :latitude); END;"
        bind_variables = {
            'result': oracledb.NUMBER,
            'site_name': site_name,
            'province': province,
            'city': city,
            'street': street,
            'longitude': longitude,
            'latitude': latitude
        }
        result = cursor.execute(query, bind_variables)
        connection.commit()
    except oracledb.DatabaseError as e:
        print("Error:", e)
        connection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

    return jsonify({"site_id": result})

# ... (UpdateMoviesite, DeleteMoviesite, GetMoviesite, GetAllMoviesites 함수 구현)

if __name__ == '__main__':
    app.run(debug=True)


