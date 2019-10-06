#!make

rebuild: clean | build

build:
	@echo "+\n++ Building images ...\n+"
	@docker-compose build --parallel

run:
	@echo "+\n++ Running client and server ...\n+"
	@docker-compose up

clean:
	@echo "+\n++ Removing any running/stopped containers, images etc...\n+"
	@docker-compose rm -f -v -s
	@docker rmi -f react-python-starter_client