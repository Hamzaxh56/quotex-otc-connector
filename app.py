import os
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory, Response

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
app = Flask(__name__, static_folder=str(STATIC), static_url_path="/static")
HOME = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Quotex OTC Connector</title><style>body{background:#0b1020;color:#e8eefb;font:16px system-ui;margin:0;padding:24px}main{max-width:700px;margin:5vh auto;background:#121a2d;border:1px solid #263451;border-radius:16px;padding:24px}a{color:#43d9a3}p{line-height:1.6}</style></head><body><main><h1>Quotex OTC Connector</h1><p>Backend is running. The live candle adapter is not configured yet.</p><p><a href="/api/health">Check backend health</a></p><p>No simulated prices are provided.</p></main></body></html>"""
ALLOWED = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-#")

@app.get("/")
def index():
    if (STATIC / "index.html").is_file():
        return send_from_directory(str(STATIC), "index.html")
    return Response(HOME, mimetype="text/html")

@app.get("/favicon.ico")
def favicon():
    return Response(status=204)

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "quotex-otc-connector-starter", "simulated_data": False, "adapter_ready": False, "note": "Backend running; real candle adapter is not configured."})

@app.get("/api/candles")
def candles():
    symbol = request.args.get("symbol", "EURUSD_otc")
    try:
        tf = int(request.args.get("tf", "60"))
        limit = int(request.args.get("limit", "100"))
    except ValueError:
        return jsonify({"error": "tf and limit must be integers"}), 400
    if not symbol or len(symbol) > 40 or any(c not in ALLOWED for c in symbol):
        return jsonify({"error": "Invalid symbol"}), 400
    if not 1 <= tf <= 86400:
        return jsonify({"error": "Timeframe must be 1–86400 seconds"}), 400
    if not 1 <= limit <= 300:
        return jsonify({"error": "limit must be 1–300"}), 400
    return jsonify({"error": "Real candle adapter is not configured. No data was simulated.", "symbol_requested": symbol, "timeframe_seconds": tf, "limit_requested": limit, "adapter_ready": False}), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "10000")))
