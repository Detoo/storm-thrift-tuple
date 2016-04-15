compile_thrift:
	thrift -r -out app/ --gen py:new_style message_services.thrift

build_topology:
	docker-compose run storm-pyleus pyleus -v build topology.yml

debug_topology:
	docker-compose run storm-pyleus pyleus local app.jar
