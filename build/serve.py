# -*- coding: utf-8 -*-
"""Serve site/ for review, with the two behaviours `python -m http.server` lacks.

    python build/serve.py            serve site/ on 4477
    python build/serve.py 8080       ...on another port

1. **Nothing is cached.** The plain handler sends `Last-Modified` and no
   `Cache-Control`, so browsers apply heuristic freshness: they invent an
   expiry and serve the document from memory without asking. Stylesheets
   carry `?v=` and assets carry a content hash, but the *page* that requests
   them has never had a cache-buster of its own — so a change to the markup
   could sit on disk, be served correctly by the server, and still not reach
   the screen. That happened twice today. `no-store` ends it.

2. **/404.html for anything unmatched**, which is what Sevalla will be asked
   to do, so a missing page looks the same here as in production.

Extensionless addresses resolve to `<path>.html` then `<path>/index.html`,
matching the way the built site links to itself.
"""

import os, sys, posixpath
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlsplit

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")


class Handler(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def __init__(self, *a, **kw):
        SimpleHTTPRequestHandler.__init__(self, *a, directory=ROOT, **kw)

    def end_headers(self):
        # Review server. Never cache anything, at any layer.
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        SimpleHTTPRequestHandler.end_headers(self)

    def translate_path(self, path):
        p = unquote(urlsplit(path).path)
        rel = posixpath.normpath(p).lstrip("/")
        full = os.path.join(ROOT, rel.replace("/", os.sep))
        if os.path.isdir(full):
            idx = os.path.join(full, "index.html")
            if os.path.isfile(idx):
                return idx
        if not os.path.splitext(full)[1]:
            for cand in (full + ".html", os.path.join(full, "index.html")):
                if os.path.isfile(cand):
                    return cand
        return full

    def send_error(self, code, message=None, explain=None):
        page = os.path.join(ROOT, "404.html")
        if code == 404 and os.path.isfile(page):
            body = open(page, "rb").read()
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        SimpleHTTPRequestHandler.send_error(self, code, message, explain)

    def log_message(self, fmt, *args):
        if "404" in (fmt % args):
            SimpleHTTPRequestHandler.log_message(self, fmt, *args)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4477
    print("site/ on http://localhost:%d  — nothing cached, /404.html on miss" % port)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
