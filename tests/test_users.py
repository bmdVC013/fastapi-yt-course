import pytest
from app import schemas
from .database import client, session


@pytest.fixture()
def test_user(client):
  user_data = {"email": "bmdvc013@gmail.com", "password": "password123"}
  res = client.post("/users/", json=user_data)
  assert res.status_code == 201
  new_user = res.json()
  new_user['password'] = user_data['password']
  return new_user


def test_login_user(test_user, client):
  res = client.post(
    "/login",
    data={"username": test_user['email'], "password": test_user['password']}
  )
  assert res.status_code == 200