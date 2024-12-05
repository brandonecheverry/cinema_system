from flask import Flask
from routes.user_routes import user_bp
from routes.movie_routes import movie_bp
from routes.purchase_routes import purchase_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(movie_bp)
app.register_blueprint(purchase_bp)

if __name__ == '__main__':
    app.run(debug=True)
