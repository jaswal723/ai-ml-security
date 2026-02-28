# Easy: Configure the logging module to write to a file called secops.log. 
# Write one INFO log and one ERROR log to the file.

import logging
logging.basicConfig (
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename= ".\\Phase1 Automation Baseline & Data Engineering\\7. Enterprise Logging\\secops.log",
    filemode='w'
)

logging.info("This is a informative log")
logging.error("This is an error log")