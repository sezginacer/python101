import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                    # datefmt='%d.%m.%y %I:%M:%S %p', filename="log", level=logging.DEBUG)

logging.debug("message with level 'debug'")
logging.info("message with level 'info'")
logging.warning("message with level 'warning'")
logging.error("message with level 'error'")
logging.critical("message with level 'critical'")

