LOC:
	PYTHONPATH=$(PWD) python3 scripts/update_loc_badge.py

conformance:
	PYTHONPATH=$(PWD) python3 scripts/conformance_harness.py

golden-check: conformance
	python3 scripts/check_golden.py

aps-auth:
	python3 scripts/aps_auth_test.py

aps-orchestrate-example:
	PYTHONPATH=$(PWD) python3 scripts/run_fusion_example.py

aps-da-list-engines:
	python3 scripts/aps_da_stub.py list-engines


