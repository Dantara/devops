import pytest
import os
from pytz import timezone
from datetime import datetime
from app_python.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_time(client, mocker):
    resp = client.get("/")

    time = datetime.now(timezone('Europe/Moscow')).strftime(os.environ.get('TIME_FORMAT', '%H:%M:%S'))

    html_string = f"<center><h1>Current time in Moscow is {time}</h1></center>"

    mocker.patch("app_python.app.get_moscow_time", return_value=time)

    assert resp.status_code == 200

    assert html_string in str(resp.data)
