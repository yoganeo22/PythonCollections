import logging

# Logging level
logging.basicConfig(level=logging.DEBUG)

class Logger:
    def __init__(self):
        logging.info("__init__")
        
    def Test_debug(self, message):
        logging.debug("Test for {}".format(message))
     
    def Test_warning(self, message):
        logging.warning("Test for {}".format(message))
        
    def Test_error(self, message):
        logging.error("Test for {}".format(message))
    
    def Test_critical(self, message):
        logging.critical("Test for {}".format(message))
        
if __name__ == "__main__":
    logging.info("This is a Logging Sample...")
    
    myLog = Logger()
    myLog.Test_debug("Debug")
    myLog.Test_warning("Warning")
    myLog.Test_error("Error")
    myLog.Test_critical("Critical")
        
    
# --- Output --- #    
# $ python Logging.py
# INFO:root:This is a Logging Sample...
# INFO:root:__init__
# DEBUG:root:Test for Debug
# WARNING:root:Test for Warning
# ERROR:root:Test for Error
# CRITICAL:root:Test for Critical
