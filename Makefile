#!make

rebuild: build | run

build:
	@echo "+\n++ Building images ...\n+"
	@docker-compose build --parallel

run:
	@echo "+\n++ Running client and server ...\n+"
	@docker-compose up

