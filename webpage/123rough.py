import http.server
import socketserver
import os
import socket

# Define the port to serve on
PORT = 8001

# Path to the directory containing your HTML files
WEB_DIR = "webpage"  # Ensure this is a folder

# Change to the directory to serve files
os.chdir(WEB_DIR)

# Create an HTTP handler
handler = http.server.SimpleHTTPRequestHandler

# Function to get the local IP address
def get_local_ip():
    try:
        # Connect to a public server to determine the local IP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "localhost"

# Get the local IP address
local_ip = get_local_ip()

# Start the server
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on http://{local_ip}:{PORT}")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()
