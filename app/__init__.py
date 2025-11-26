
from flask import Flask
from app.routes.home import home_bp
from app.routes.pages import pages_bp
from app.routes.portfolio import portfolio_bp
from app.routes.blog import blog_bp
from app.routes.contact import contact_bp



def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_bp)
    app.register_blueprint(pages_bp)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(contact_bp)

    return app
