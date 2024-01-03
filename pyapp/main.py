import uvicorn
import os


HTTP_SERVER_PORT = int(os.getenv("HTTP_SERVER_PORT", "8000"))

if __name__ == "__main__":
    uvicorn.run("sample.app:app", host="0.0.0.0", port=HTTP_SERVER_PORT, reload=True)
    