from flask import Flask,jsonify
from project.app.db import db
from project.blueprints.product import bp as product_bp
from project.blueprints.formula import bp as formula_bp
from project.blueprints.distributer import bp as ditributer_bp
from project.blueprints.customer import bp as customer_bp
from project.blueprints.company import bp as company_bp
from project import config
import os
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pharmacy.db"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}"

    
    migrate = Migrate()
    db.init_app(app)
    migrate.init_app(app=app, db=db) 
    
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
    # with app.app_context():
    #     db.create_all()

    return app