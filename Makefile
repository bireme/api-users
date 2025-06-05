default: build

COMPOSE_FILE_DEV=docker-compose-dev.yml
IMAGE_NAME=bireme/api-gateway-users
export APP_VER?=$(shell git describe --tags --long --always | sed 's/-g[a-z0-9]\{7\}//' | sed 's/-/\./')
TAG_LATEST=$(IMAGE_NAME):latest

## variable used in docker-compose for tag the build image
export IMAGE_TAG=$(IMAGE_NAME):$(APP_VER)

tag:
	@echo "IMAGE TAG:" $(IMAGE_TAG)

## DEV shortcuts
dev_build:
	@docker compose -f $(COMPOSE_FILE_DEV) build

dev_build_no_cache:
	@docker compose -f $(COMPOSE_FILE_DEV) build --no-cache

dev_run:
	@docker compose -f $(COMPOSE_FILE_DEV) up

dev_start:
	@docker compose -f $(COMPOSE_FILE_DEV) up -d

dev_rm:
	@docker compose -f $(COMPOSE_FILE_DEV) rm -f

dev_logs:
	@docker compose -f $(COMPOSE_FILE_DEV) logs -f

dev_stop:
	@docker compose -f $(COMPOSE_FILE_DEV) stop

dev_down:
	@docker compose -f $(COMPOSE_FILE_DEV) down

dev_sh:
	@docker compose -f $(COMPOSE_FILE_DEV) exec api_gateway_users bash

dev_cache_sh:
	@docker compose -f $(COMPOSE_FILE_DEV) exec api_gateway_users bash


## PROD shortcuts
build:
	@docker compose build

build_no_cache:
	@docker compose build --no-cache

run:
	@docker compose up

start:
	@docker compose up -d

rm:
	@docker compose rm -f

logs:
	@docker compose logs -f

stop:
	@docker compose stop

down:
	@docker compose down

sh:
	@docker compose exec api_users sh

collectstatic:
	@docker compose exec -T api_users uv run manage.py collectstatic --noinput

migrate:
	@docker compose exec -T api_users uv run manage.py migrate


