from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
import logging


class apiTimer(BaseHTTPMiddleware):

  def __init__(
    self,
    app,
  ):
    super().__init__(app)

  async def dispatch(self, request: Request, call_next):

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time.__round__(3))
    logging.info(f'Time Taken to process the request: {process_time}')
    return response
