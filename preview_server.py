from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class PreviewHandler(SimpleHTTPRequestHandler):
    def guess_type(self, path):
        content_type = super().guess_type(path)
        if content_type == "text/html":
            return "text/html; charset=utf-8"
        return content_type


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8000), PreviewHandler)
    print("SunnyCoding preview: http://127.0.0.1:8000")
    server.serve_forever()
