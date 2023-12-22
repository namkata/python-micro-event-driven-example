from flask import Flask

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import UniqueConstraint
from flask import jsonify
from flask import Blueprint
from producer import publish
import requests

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

# Models:
class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    result_no_stop_words = db.Column(JSON)

    def __repr__(self):
        return "<id {}>".format(self.id)


class ProductUser(db.Model):
    __tablename__ = "product_user"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint("user_id", "product_id", name="user_product_unique")


def create_app(config_class=Config):
    """
    Creates and configures the Flask application.

    Returns:
        Flask: The Flask application instance.
    """
    # Create Flask app instance
    app = Flask(__name__)

    # Load configurations from Config class
    app.config.from_object(config_class)

    # Initialize extensions with the app
    initialize_extensions(app)

    # Register blueprints or routes
    register_blueprints(app)

    return app


def initialize_extensions(app):
    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    # Initialize other extensions here if needed


def register_blueprints(app):
    @app.route("/")
    def hello():
        return "Hello World!"

    @app.route("/<name>")
    def hello_name(name):
        return "Hello {}!".format(name)


    bp = Blueprint('api', __name__, url_prefix='/api')

    @bp.route("/products")
    def index():
        return jsonify(Product.query.all())


    @bp.route("/products/<int:id>/like", methods=["POST"])
    def like(id):
        try:
            req = requests.get("http://backend:8000/api/user")
            productUser = ProductUser(user_id=req.json().get("id"), product_id=id)
            db.session.add(productUser)
            db.session.commit()

            publish("product_liked", id)
        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 400

        return jsonify({"message": "success"})

    # Import and register blueprints or routes
    app.register_blueprint(
        bp, url_prefix="/api"
    )  # Register the blueprint with a URL prefix


# Create the app instance
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
