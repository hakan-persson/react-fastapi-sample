import uvicorn
import os
import sys


HTTP_SERVER_PORT = int(os.getenv("HTTP_SERVER_PORT", "8000"))
DEBUGGING = sys.gettrace() is not None
DEBUGLOG = os.getenv("DEBUG", "false").lower() == "true"

if __name__ == "__main__":
    uvicorn.run("sample.app:app", host="0.0.0.0", port=HTTP_SERVER_PORT, reload=DEBUGGING)
    