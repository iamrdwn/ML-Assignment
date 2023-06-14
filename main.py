from src import init_application

import uvicorn

app = init_application()

uvicorn.run(app, host="0.0.0.0", port=8080)
