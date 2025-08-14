# Hansabit Monorepo

Hansabit provides automation and digitalisation services. This monorepo contains the frontend (Next.js) and backend (FastAPI) applications and infrastructure for local development and production with Docker Compose and Caddy reverse proxy.

## Voraussetzungen
- Docker & Docker Compose
- Make
- Node.js 20+ for local frontend development
- Python 3.11 for local backend development

## Lokale Entwicklung

### Mit Docker
```bash
cp .env.example .env
make up
```
Die Seite ist unter http://localhost erreichbar. Die API unter http://localhost/api.

### Ohne Docker
1. Backend:
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```
2. Frontend:
```bash
cd frontend
npm install
npm run dev
```

## .env Variablen
```
POSTGRES_USER=hansabit
POSTGRES_PASSWORD=change_me
POSTGRES_DB=hansabit
DATABASE_URL=postgresql+psycopg://hansabit:change_me@db:5432/hansabit
REDIS_URL=redis://redis:6379/0
SECRET_KEY=change_me
JWT_EXPIRES_MINUTES=60
BACKEND_CORS_ORIGINS=["https://hansabit.de","http://localhost:3000"]
```
`SECRET_KEY` generieren:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## Migrationen & Seed
```bash
make migrate
make seed
```
Seed erstellt drei Beispiel-Cases und den Admin `admin@hansabit.de` mit Passwort `ChangeMe!123` (nur Entwicklung).

## Tests
```bash
make test
```

## Deployment
1. Server aufsetzen (z.B. Hetzner) und Docker installieren.
2. Repository klonen und `.env` setzen.
3. DNS A-Records für `hansabit.de` und `colabora.ge` auf Server-IP zeigen lassen.
4. `make up` ausführen. Caddy holt automatische TLS-Zertifikate von Let's Encrypt.

## Admin Login
Nach Seed: `admin@hansabit.de` / `ChangeMe!123`.

## Lighthouse
Für lokale Tests:
```bash
npm install -g lighthouse
lighthouse http://localhost --view
```
Zielscore ≥ 90 für Performance, Accessibility, Best Practices und SEO.

## Sicherheit & Datenschutz
- Argon2 Passwort-Hashing
- HTTPS via Caddy
- Keine Secrets im Repo
- Im Projekt enthaltene Seiten: Impressum und Datenschutz mit Platz für Angaben.

