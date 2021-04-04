import logging.config
from pathlib import Path

import yaml


def setup_logging(app_dir: Path):
    log_dir = app_dir / "log"
    with (app_dir / "config" / "logging.yaml").open("r") as f:
        logging_config = yaml.safe_load(f)
        logging_config['handlers']['file']['filename'] = log_dir / "app.log"
        logging.config.dictConfig(logging_config)
