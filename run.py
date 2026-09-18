import subprocess
import time
import webbrowser

server = subprocess.Popen([
    "uvicorn",
    "main:app"
])

time.sleep(2)

webbrowser.open("http://localhost:8000")

try:
    server.wait()
except KeyboardInterrupt:
    print("\nShutting down...")
    server.terminate()
    server.wait()