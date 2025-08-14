.PHONY: up down logs migrate seed test fmt lint

up:
docker-compose up -d --build

down:
docker-compose down

logs:
docker-compose logs -f

migrate:
docker-compose run --rm backend alembic upgrade head

seed:
docker-compose run --rm backend python app/db/init_db.py

test:
docker-compose run --rm backend pytest && docker-compose run --rm frontend npm test

fmt:
docker-compose run --rm backend black app && docker-compose run --rm frontend npm run fmt

lint:
docker-compose run --rm backend ruff app && docker-compose run --rm frontend npm run lint
