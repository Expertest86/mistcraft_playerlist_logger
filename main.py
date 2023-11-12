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
    logger.info(f"Token value: {SOME_SECRET}")

    req = requests.get('https://api.mcstatus.io/v2/status/java/mistcraft.dathand.com')
    if r.status_code == 200:
        t = json.loads(req.text)
        nlist = t['players']['list']
        
        if len(nlist) != 0:
            for x in nlist:
                names = x['name_raw']
                logger.info(f'{names}')
        else:
            names = '-Empty-'
            logger.info(f'{names}')
