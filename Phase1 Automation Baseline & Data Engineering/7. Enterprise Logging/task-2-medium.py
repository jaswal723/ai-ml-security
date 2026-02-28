# Medium: Refactor your Easy task from the File Handling section (writing malicious URLs to a file). 
# Remove all print() statements and replace them with logging.info() (e.g., "Successfully wrote domain X to file").

import logging
logging.basicConfig(
    level=logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename=".\\Phase1 Automation Baseline & Data Engineering\\7. Enterprise Logging\\task-2.log",
    filemode='w'
)
malicious_urls = ["www.mal-url-1.com","www.mal-url-2.com","www.mal-url-3.com"]
with open(".\\Phase1 Automation Baseline & Data Engineering\\7. Enterprise Logging\\suspect_domains.txt","w") as f:
    for x in malicious_urls:
        f.write(x+"\n")
        logging.info(f'Successfully wrote domain {x} to file')

    
    