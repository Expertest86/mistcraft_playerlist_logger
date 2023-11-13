import logging
import logging.handlers
import os

import requests


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    

    req = requests.get('https://api.mcstatus.io/v2/status/java/mistcraft.dathand.com')
    if req.status_code == 200:
        t = req.json()
        nlist = t["players"]["list"]
        
        if len(nlist) != 0:
            names = []
            for x in nlist:
                names.append(x["name_raw"]) 
            plist = "  ".join(names)
            logger.info(f'{plist}') 
        else:        
            logger.info(f'-Empty-')
