#!/usr/bin/env python3
"""Simple local preview server for the press kit site."""

import argparse
import http.server
import socketserver
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a local preview server for the DJ press kit.")
    parser.add_argument("--port", type=int, default=4173, help="Port to serve the site on (default: 4173)")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind to (default: 127.0.0.1)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *handler_args, **handler_kwargs):
            super().__init__(*handler_args, directory=str(root), **handler_kwargs)

        def log_message(self, format, *args):
            print(f"[{self.address_string()}] {format % args}")

    with socketserver.TCPServer((args.host, args.port), QuietHandler) as httpd:
        url = f"http://{args.host}:{args.port}/"
        print(f"Serving press kit from: {root}")
        print(f"Open this in your browser: {url}")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
