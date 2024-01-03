# pylint: disable=missing-function-docstring
# pylint: disable=no-self-argument

"""
FastAPI server configuration
"""

from pydantic_settings import BaseSettings

# from pydantic import BaseModel


class Settings(BaseSettings):
    """Server config settings"""

    debug: bool = False  # Global DEBUG logging
    logformat: str = (
        "%(asctime)s %(funcName)-10s [%(levelname)s] %(message)s"  # Default log format
    )

    http_server_port: int = 8000
    http_static_dir: str = "./static"
    http_jsapp_dir: str = "./jsapp/out"


settings = Settings()
