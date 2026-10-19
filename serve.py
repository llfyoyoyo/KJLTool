#!/usr/bin/env python3
"""Static server with correct JS MIME types (Windows Python defaults .js to text/plain)."""
from __future__ import annotations

import argparse
import mimetypes
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


# Force modern MIME types so ES modules work in the browser.
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("application/javascript", ".mjs")
mimetypes.add_type("application/json", ".json")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("text/html", ".html")


class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **getattr(SimpleHTTPRequestHandler, "extensions_map", {}),
        ".js": "application/javascript",
        ".mjs": "application/javascript",
        ".json": "application/json",
        ".css": "text/css",
        ".html": "text/html",
        ".wasm": "application/wasm",
    }

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def main() -> None:
    parser = argparse.ArgumentParser(description="KJL viewer static server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parent),
        help="Directory to serve (repo root)",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    handler = partial(Handler, directory=str(root))
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving {root}")
    print(f"Viewer: http://{args.host}:{args.port}/viewer/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
