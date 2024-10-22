from app import schemas
from .database import client, session


def test_root(client):
  res = client.get("/", )
  assert res.status_code == 200

def test_create_user(client):
  res = client.post("/users/", json={"email": "hello123457@gmail.com", "password": "password123"})
  new_user = schemas.UserOut(**res.json())
  assert new_user.email == "hello123457@gmail.com"
  assert res.status_code == 201

def test_login_user(client):
  res = client.post(
    "/login",
    data={"username": "hello123457@gmail.com", "password": "password123"}
  )
  assert res.status_code == 200