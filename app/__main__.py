import logging
import os
from pathlib import Path

from app.config import load_config
from app.config.logging_config import setup_logging
from app.models.config.main import Paths
from app.services.foo import foo


logger = logging.getLogger(__name__)


def main():
    paths = get_paths()

    setup_logging(paths)
    config = load_config(paths)

    logger.info("started")
    try:
        foo(config)
    finally:
        logger.info("stopped")


def get_paths() -> Paths:
    if path := os.getenv("APP_PATH"):
        return Paths(Path(path))
    return Paths(Path(__file__).parent.parent)


if __name__ == '__main__':
    main()
