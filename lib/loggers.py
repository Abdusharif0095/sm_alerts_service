import logging
import logging.config
from pathlib import Path

logging.config.fileConfig(str(Path.cwd()) + "/lib/logging.ini")
root_logger = logging.getLogger()
