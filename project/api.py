from flask_jwt_extended import JWTManager
from project.app.models.user import User
from flask_migrate import Migrate
from flask import Flask,jsonify
from datetime import timedelta
from project.app.db import db
from project import config

from project.blueprints.product import bp as product_bp
from project.blueprints.formula import bp as formula_bp
from project.blueprints.distributer import bp as ditributer_bp
from project.blueprints.customer import bp as customer_bp
from project.blueprints.company import bp as company_bp
from project.blueprints.order import bp as order_bp
from project.blueprints.user import bp as user_bp
from project.blueprints.stock import bp as stock_bp


def create_app():
    
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}"
    app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=30)
    
    migrate = Migrate()
    db.init_app(app)
    migrate.init_app(app=app, db=db) 
    jwt = JWTManager(app)
    
    @jwt.user_lookup_loader
    def user_lookup(jwt_header: dict, jwt_payload: dict):
        username = jwt_payload.get("sub")
        user = User.query.filter(User.username == username).first() 
        return user
        
    # @jwt.additional_claims_loader
    # def adding_additional_claims(identity):
    #     user = ... # fetch user
        
    #     return {"role": user.role}
    
    @app.errorhandler(422)
    def webargs_error_handler(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code
        
    app.register_blueprint(product_bp)
    app.register_blueprint(formula_bp)
    app.register_blueprint(ditributer_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(stock_bp)
    # with app.app_context():
    #     db.create_all()

    return app