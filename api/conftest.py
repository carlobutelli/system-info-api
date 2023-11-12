from . import create_app
import pytest

app = create_app()


@pytest.fixture
def client():
    with app.test_client() as client:
        ctx = app.app_context()
        ctx.push()
        yield client
