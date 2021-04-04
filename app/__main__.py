import logging
from pathlib import Path

from app.logging_config import setup_logging


from app.config import load_config
from app.services.foo import foo


def main():
    app_dir = Path(__file__).parent.parent
    setup_logging(app_dir)

    logger = logging.getLogger(__name__)
    logger.info("started")

    config = load_config(app_dir)
    foo(config)


if __name__ == '__main__':
    main()
