from flask import Flask, request, jsonify
import oracledb

app = Flask(__name__)

# Database connection settings
db_user = "kosa30"
db_password = "kosa2023oraclE"
db_dsn = "edudb_high"
db_wallet_location = "C:\\Dev\\Python\\Wallet_edudb"  # Backslashes should be escaped
db_wallet_password = "pythonoracle21"

# Create a connection
def create_connection():
    connection = oracledb.connect(user=db_user, password=db_password, dsn=db_dsn,
                                  config_dir=db_wallet_location, wallet_location=db_wallet_location,
                                  wallet_password=db_wallet_password)
    return connection

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
