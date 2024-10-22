from routes.home import home_resource
from routes.pessoa import pessoa_resource
from database.database import db
from database.models.pessoa import Pessoa
import os

def configure_all(app):
    configure_routes(app)
    configure_db()
    
def configure_routes(app):
    app.register_blueprint(home_resource)
    app.register_blueprint(pessoa_resource, url_prefix='/pessoa')
    
def configure_db():
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'pessoa.db')
    
    if not os.path.exists(db_path):
        db.connect()
        db.create_tables([Pessoa])
        db.close()