import pytest
from jose import jwt
from app import schemas
from .database import client, session
from app.config import settings


def test_login_user(test_user, client):
  res = client.post(
    "/login",
    data={"username": test_user['email'], "password": test_user['password']}
  )
  login_res = schemas.TokenOut(**res.json())
  payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
  id = payload.get("user_id")
  assert id == test_user['id']
  assert login_res.token_type == "bearer"
  assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
  ('wrongemail@gmail.com', 'password123', 403),
  ('minhdung.bui13@gmail.com', 'wrongpassword', 403),
  ('bmdvc013@gmail.com', 'wrongpassword', 403),
  (None, 'password123', 403),
  ('bmdvc013@gmail.com', None, 403)
])
def test_incorrect_login(test_user, client, email, password, status_code):
  res = client.post("/login", data = {"username": email, "password": password})
  assert res.status_code == status_code