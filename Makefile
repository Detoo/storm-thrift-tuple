compile_thrift:
	thrift -r -out app/ --gen py:new_style message_services.thrift

build_topology:
	docker-compose run --rm pyleus-env pyleus -v build -s topology.yml

debug_topology:
	docker-compose run --rm pyleus-env pyleus local app.jar
