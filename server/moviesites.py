from flask import Flask, jsonify
import oracledb
import connection

app = Flask(__name__)

# Oracle DB connection details
db_user = connection.db_user
db_password = connection.db_password
db_dsn = connection.db_dsn

# Google API key for Places API
google_api_key = "AIzaSyBVjq1GKBNCEJxz2-SSSi5E_JHICuPl8d"

# Create a connection to the Oracle DB
def create_connection():
    connection = oracledb.connect(user=db_user, password=db_password, dsn=db_dsn)
    return connection

@app.route('/moviesites', methods=['GET'])
def get_moviesites():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.callproc("MoviesitesPackage.GetAllMoviesites", [cursor.var(oracledb.CURSOR)])
    result = cursor.fetchone()[0]

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
        
        # Use Google Places API to get additional information
        # You need to implement this part based on the API documentation
        # Example: Call Google Places API to get details using latitude and longitude
        
        moviesites.append(moviesite)

    cursor.close()
    connection.close()

    return jsonify({'moviesites': moviesites})

if __name__ == '__main__':
    app.run(debug=True)

