"""
Simple HTTP Server for Website Blocking
Serves block page on localhost - no SSL certificates needed
"""

import http.server
import socketserver
import threading
import os
import ssl


class BlockPageHandler(http.server.SimpleHTTPRequestHandler):
    """Serves the custom block page for any request"""

    block_page_content = None

    def do_GET(self):
        """Handle GET requests - serve block page"""
        self.serve_block_page()

    def do_POST(self):
        """Handle POST requests - serve block page"""
        self.serve_block_page()

    def do_HEAD(self):
        """Handle HEAD requests"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def serve_block_page(self):
        """Serve the custom block page"""
        try:
            content = (
                self.block_page_content
                if self.block_page_content
                else self.get_fallback_page()
            )

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        except Exception as e:
            print(f"Error serving block page: {e}")

    def get_fallback_page(self):
        """Fallback block page if file not found"""
        return """<!DOCTYPE html>
<html>
<head>
    <title>Site Blocked</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: white;
        }
        .container {
            text-align: center;
            animation: fadeIn 0.5s;
        }
        h1 { font-size: 3em; margin: 0; animation: bounce 1s; }
        p { font-size: 1.5em; }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚫 Site Blocked</h1>
        <p>This website is blocked. Stay focused on your work!</p>
    </div>
</body>
</html>"""

    def log_message(self, format, *args):
        """Suppress log messages"""
        pass


class ProxyServer:
    """Manages HTTP server for serving block pages"""

    def __init__(self, block_page_path=None):
        self.http_server = None
        self.https_server = None
        self.http_thread = None
        self.https_thread = None
        self.running = False

        # Load block page content
        BlockPageHandler.block_page_content = self.load_block_page(block_page_path)

    def load_block_page(self, block_page_path):
        """Load the custom block page HTML"""
        if block_page_path and os.path.exists(block_page_path):
            try:
                with open(block_page_path, "r", encoding="utf-8") as f:
                    return f.read()
            except Exception:
                pass
        return None

    def start_http_server(self):
        """Start HTTP server on port 80"""
        try:
            # Use ThreadingTCPServer for better handling
            class ThreadedTCPServer(
                socketserver.ThreadingMixIn, socketserver.TCPServer
            ):
                allow_reuse_address = True
                daemon_threads = True

            self.http_server = ThreadedTCPServer(("", 80), BlockPageHandler)
            print("✓ Block page server started on port 80")
            self.http_server.serve_forever()
        except Exception as e:
            print(f"Server error: {e}")

    def start_https_server(self, cert_file):
        """Start HTTPS server on port 443"""
        try:

            class ThreadedTCPServer(
                socketserver.ThreadingMixIn, socketserver.TCPServer
            ):
                allow_reuse_address = True
                daemon_threads = True

            self.https_server = ThreadedTCPServer(("", 443), BlockPageHandler)

            # Wrap with SSL
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(cert_file)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

            self.https_server.socket = context.wrap_socket(
                self.https_server.socket, server_side=True
            )

            print("✓ HTTPS server started on port 443")
            self.https_server.serve_forever()
        except Exception as e:
            print(f"HTTPS server error: {e}")

    def start(self, cert_file=None):
        """Start HTTP and HTTPS servers"""
        if self.running:
            return

        self.running = True

        # Start HTTP server in background
        self.http_thread = threading.Thread(target=self.start_http_server, daemon=True)
        self.http_thread.start()

        # Start HTTPS server if certificate exists
        if cert_file and os.path.exists(cert_file):
            self.https_thread = threading.Thread(
                target=lambda: self.start_https_server(cert_file), daemon=True
            )
            self.https_thread.start()

    def stop(self):
        """Stop the server"""
        self.running = False

        if self.http_server:
            self.http_server.shutdown()
            self.http_server.server_close()

        if self.https_server:
            self.https_server.shutdown()
            self.https_server.server_close()


if __name__ == "__main__":
    # Test the server
    proxy = ProxyServer("block_page.html")
    print("Starting server...")
    proxy.start()
    print("Server running on http://localhost")
    print("Press Ctrl+C to stop.")

    try:
        import time

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping server...")
        proxy.stop()
        print("Server stopped.")
