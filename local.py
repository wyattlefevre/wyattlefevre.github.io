import http.server
import socketserver
import webbrowser
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the port number for the server
PORT = 8000

# Set the directory where the HTML file is located
DIRECTORY = './'

# Set the HTML file name
HTML_FILE = 'index.html'

# Handler to detect changes to the HTML file and reload the browser
class HTMLReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(HTML_FILE):
            print("HTML file modified, reloading browser...")
            webbrowser.reload()

# Create the HTTP server
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

# Start the HTTP server
print("Serving at port", PORT)
httpd.serve_forever()

# Watch the HTML file for changes
event_handler = HTMLReloadHandler()
observer = Observer()
observer.schedule(event_handler, path=DIRECTORY, recursive=False)
observer.start()

# Open the HTML file in the default browser
webbrowser.open('http://localhost:{}/{}'.format(PORT, HTML_FILE))

# Keep the script running to continue watching for changes
try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
