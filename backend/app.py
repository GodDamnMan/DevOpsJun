from http.server import BaseHTTPRequestHandler, HTTPServer
import os

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", "8080"))
RESPONSE_TEXT = b"Hello from Effective Mobile!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(RESPONSE_TEXT)))
            self.end_headers()
            self.wfile.write(RESPONSE_TEXT)
            return

        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Not Found")

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    server.serve_forever()
