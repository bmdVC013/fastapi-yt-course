from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))

class Settings(BaseSettings):
  db_hostname: str
  db_port: str
  db_password: str
  db_name: str
  db_username: str
  secret_key: str
  algorithm: str
  access_token_expire_minutes: int

  model_config = SettingsConfigDict()

settings = Settings()
