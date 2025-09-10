import pytest
from app import create_app

@pytest.fixture
def app():
    """Cria e configura uma nova instância da aplicação para cada teste."""
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture
def client(app):
    """Um cliente de teste para a aplicação."""
    return app.test_client()