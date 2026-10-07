import http.server
import socketserver
import os

PORT = 8000
NIM = os.environ.get("STUDENT_NIM", "UNKNOWN")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Praktikum Cloud Computing - Docker</title>
    <style>
        body {{ font-family: system-ui, -apple-system, sans-serif; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .card {{ background: #1e293b; padding: 2rem; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; border: 1px solid #334155; }}
        h1 {{ color: #38bdf8; margin-bottom: 0.5rem; }}
        p {{ font-size: 1.25rem; color: #94a3b8; }}
        .nim {{ color: #4ade80; font-weight: bold; font-size: 1.5rem; }}
        .badge {{ display: inline-block; padding: 0.25rem 0.75rem; background: #0284c7; color: white; border-radius: 9999px; font-size: 0.875rem; margin-top: 1rem; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>Praktikum Docker Berhasil!</h1>
        <p>Aplikasi web berjalan di dalam kontainer.</p>
        <p>Dikembangkan oleh NIM: <span class="nim">{NIM}</span></p>
        <div class="badge">Cloud Computing BS1TT-47</div>
    </div>
</body>
</html>"""
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        # Clean logging for container stdout
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Serving HTTP on port {PORT} with STUDENT_NIM={NIM}")
        httpd.serve_forever()
