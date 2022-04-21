import pytest


@pytest.fixture
def app():
    from app.main import create_app
    app = create_app()
    app.config['WTF_CSRF_ENABLED'] = False
    return app


@pytest.fixture
def client(app):
    app.testing = True
    return app.test_client()
