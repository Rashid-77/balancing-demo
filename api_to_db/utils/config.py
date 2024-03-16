import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    msql_user: str = os.getenv("MYSQL_USER", "")
    msql_pass: str = os.getenv("MYSQL_PASSWORD", "")
    msql_host: str = os.getenv("LOAD_BALANCE_HOST", "")
    msql_port: str = os.getenv("MYSQL_PORT", "")
    msql_db: str = os.getenv("MYSQL_DATABASE", "")
    msql_url: str = f"mysql+pymysql://{msql_user}:{msql_pass}@{msql_host}/{msql_db}"

    app_port: str = os.getenv("APP_PORT", "")


# TODO Make this settings a global object
def get_settings():
    return Settings()
