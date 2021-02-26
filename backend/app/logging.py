# todo find some way to log all requests:
# use background tasks
    # how to access the request and response ? 
# use middleware
    # whw to access response body ? 

from datetime import datetime
from fastapi import Request, Response
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.log'


async def simple_logging(request: Request, response: Response):
    message = (
            f'{datetime.now()},'
            f'{request.method},'
            f'{request.url},'
            f'{response.status_code}'
        )
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(message + '\n')
