#!/usr/bin/env python3
"""Editorial review dashboard server (stdlib only).

Run:  python3 server.py [port]    (default 8199)
Open: http://localhost:8199

Endpoints:
  GET  /                -> index.html
  GET  /app.js|styles.css -> static assets
  GET  /api/data        -> stories + fact checks + selection + arcs
  GET  /api/review      -> current review state
  POST /api/review      -> save review state {story_id, status, comment}
"""
import json, os, sys, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

BASE = os.path.expanduser('~/Documents/projects/indian_apps/dailyX/daily_krishna_stories')
DATA = os.path.join(BASE, 'data')
REVIEW_FILE = os.path.join(DATA, 'pilot_review_state.json')
STATIC = os.path.dirname(os.path.abspath(__file__))

MIME = {'.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
        '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8'}

def load_review():
    if os.path.exists(REVIEW_FILE):
        try:
            return json.load(open(REVIEW_FILE))
        except Exception:
            return {}
    return {}

def save_review(state):
    json.dump(state, open(REVIEW_FILE, 'w'), indent=1, ensure_ascii=False)

class H(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # quiet

    def _send(self, code, body, ctype='application/json; charset=utf-8'):
        data = body if isinstance(body, bytes) else body.encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == '/api/data':
            payload = {'stories': [], 'fact_checks': {}, 'selection': {}, 'arcs': []}
            ps = os.path.join(DATA, 'stories.json')          # full corpus (537)
            if not os.path.exists(ps):
                ps = os.path.join(DATA, 'pilot_stories.json')  # fallback
            if os.path.exists(ps):
                payload['stories'] = json.load(open(ps)).get('stories', [])
            fc1 = os.path.join(DATA, 'full_fact_checks.json')
            if os.path.exists(fc1):
                payload['fact_checks'].update(json.load(open(fc1)))
            fc2 = os.path.join(DATA, 'pilot_fact_checks.json')
            if os.path.exists(fc2):
                payload['fact_checks'].update(json.load(open(fc2)))
            sel = os.path.join(DATA, 'pilot_story_selection.json')
            if os.path.exists(sel):
                payload['selection'] = json.load(open(sel))
            arcs = os.path.join(DATA, 'story_arcs.json')
            if os.path.exists(arcs):
                payload['arcs'] = json.load(open(arcs)).get('arcs', [])
            payload['review'] = load_review()
            self._send(200, json.dumps(payload, ensure_ascii=False))
        elif path == '/api/review':
            self._send(200, json.dumps(load_review(), ensure_ascii=False))
        elif path in ('/', '/index.html'):
            self._send(200, open(os.path.join(STATIC, 'index.html'), encoding='utf-8').read(), MIME['.html'])
        elif path in ('/app.js', '/styles.css'):
            self._send(200, open(os.path.join(STATIC, path.lstrip('/')), encoding='utf-8').read(), MIME.get(os.path.splitext(path)[1], 'text/plain'))
        else:
            self._send(404, json.dumps({'error': 'not found'}))

    def do_POST(self):
        if urlparse(self.path).path != '/api/review':
            self._send(404, json.dumps({'error': 'not found'}))
            return
        try:
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length) or b'{}')
        except Exception as e:
            self._send(400, json.dumps({'error': str(e)}))
            return
        state = load_review()
        sid = body.get('story_id')
        if not sid:
            self._send(400, json.dumps({'error': 'story_id required'}))
            return
        rec = state.setdefault(sid, {'status': 'unreviewed', 'comments': []})
        if 'status' in body and body['status'] in ('unreviewed', 'approved', 'needs_revision', 'rejected'):
            rec['status'] = body['status']
        if body.get('comment'):
            rec.setdefault('comments', []).append({'text': body['comment'], 'ts': time.strftime('%Y-%m-%d %H:%M:%S')})
        save_review(state)
        self._send(200, json.dumps(rec))

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8199
    print(f'Daily Krishna review dashboard -> http://localhost:{port}')
    ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()
