from app import create_app
from pytest import fixture

@fixture(scope="module")
def app():
     _app = create_app()
     _app.testing = True
     _app.config['SERVER_NAME'] = 'example.com'
     with _app.app_context():
         yield _app
