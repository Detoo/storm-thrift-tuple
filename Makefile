compile_thrift:
	thrift -r -out ./ --gen py:new_style app_services.thrift
