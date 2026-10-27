# Quotex OTC Connector — fixed starter v2

## Render settings
- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`
- Root Directory: leave blank if `app.py` is at repository root.

Upload the contents of this ZIP to the top level of your GitHub repository, not just the ZIP file.

## Test
- `/` should show the homepage.
- `/api/health` should return JSON with `status: ok`.
- `/api/candles?symbol=EURUSD_otc&tf=60&limit=20` intentionally returns HTTP 503 until a real candle adapter is implemented.

Important: this is not yet a live candle feed. It does not simulate data or place trades. A compatible, tested QuotexPy adapter is still required. Never commit passwords, SSIDs, cookies, or tokens.
