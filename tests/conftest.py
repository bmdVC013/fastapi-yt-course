import os
import pytest
from jose import jwt
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app import schemas
from app.database import get_db
from app.database import Base
from app.config import settings

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
engine = create_engine(SQLALCHEMY_DATABASE_URL + "_test")
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)
  db = TestingSessionLocal()
  try:
    yield db
  finally:
    db.close()

@pytest.fixture()
def client(session):
  def override_get_db():
    try:
      yield session
    finally:
      session.close()

  app.dependency_overrides[get_db] = override_get_db
  yield TestClient(app)

@pytest.fixture()
def test_user(client):
  user_data = {"email": "bmdvc013@gmail.com", "password": "password123"}
  res = client.post("/users/", json=user_data)
  assert res.status_code == 201
  new_user = res.json()
  new_user['password'] = user_data['password']
  return new_user
