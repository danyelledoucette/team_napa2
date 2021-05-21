from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask
from flask import request, jsonify,request,render_template
import psycopg2

 
app = flask.Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']  = "postgresql://postgres:postgres@wine-db.c0fgzkuoe2cb.us-east-2.rds.amazonaws.com:5432/wines"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
con = psycopg2.connect(database="wine", user="postgres", password="postgres", host="wine-db.c0fgzkuoe2cb.us-east-2.rds.amazonaws.com", port="5432")
cursor = con.cursor()

@app.route("/all", methods=['post', 'get'])
def test():  
    cursor.execute("select * from cart")
    result = cursor.fetchall()
    return render_template("index.html", data=result)

@app.route('/')
def home():
    '''<h1>wines</h1>'''
    return (
        f"Avaliable Routes:<br/>"
        f"/api/v1/resources/wines/all<br/>"
        f"Avliable Searches:<br/>"
        f"/api/v1/resources/wines<br/>"
        f"/api/v1/resources/wines?country=Australia<br/>"
        f"/api/v1/resources/wines?country=US<br/>"
        f"/api/v1/resources/wines?country=Canada<br/>"
        f"/api/v1/resources/wines?country=Italy<br/>"
        f"/api/v1/resources/wines?country=France<br/>"
        f"/api/v1/resources/wines?country=Spain<br/>"
        f"/api/v1/resources/wines?country=Argentina<br/>"

    )
# @app.route('/all',methods = ['GET'])
# def all_Wine():
#     wine = wines.query.all()

        # results = {
        # [
        #     "country": wine.country,
        #     "description": wine.description,
        #     "designation": wine.designation,
        #     "points": wine.points,
        #     "price": wine.price,
        #     "province": wine.province,
        #     "region_1": wine.region_1,
        #     "region_2": wine.region_2,
        #     "taster_name": wine.taster_name,
        #     "taster_twitter_handle": wine.taster_twitter_handle,
        #     "title": wine.title,
        #     "variety": wine.variety,
        #     "winery": wine.winery

        # ]
    # {


# @app.route('/all')
# def all():
#     mycursor.execute("select * from wine")
#     data = mycursor.fetchall()
#     return render_template('all.html', data=data)
# if __name__ == '__main__':
#     app.run(debug=True)

