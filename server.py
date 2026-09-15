from datetime import datetime, timezone

from flask import Flask

app = Flask(__name__)

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hello from Flask</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 34rem; margin: 15vh auto; padding: 0 1.5rem; line-height: 1.5; color: #222; }}
a {{ color: #0645ad; }}
</style>
</head>
<body>
<h1>Hello from Flask.</h1>
<p>This page is served by a small Flask app deployed with <a href="https://disco.cloud">Disco</a>.</p>
<p>The server time is {now}.</p>
</body>
</html>
"""


@app.route("/")
def index():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return PAGE.format(now=now)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
