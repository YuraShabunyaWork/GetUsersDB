build:
	docker compose build

up:
	docker compose up -d

restart:
	docker compose restart

down:
	docker compose down

delete:
	docker system prune -a
