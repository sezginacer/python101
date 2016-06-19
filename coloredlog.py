#!/usr/bin/python3.5
# import logging
# logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d.%m.%y %I:%M:%S %p', filename="example.log", level=logging.DEBUG)

import logging
import coloredlogs
coloredlogs.install(level="DEBUG")

logging.debug("message with level 'debug'")
logging.info("message with level 'info'")
logging.warning("message with level 'warning'")
logging.error("message with level 'error'")
logging.critical("message with level 'critical'")
