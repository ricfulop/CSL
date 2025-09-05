LOC:
	PYTHONPATH=$(PWD) python3 scripts/update_loc_badge.py

conformance:
	PYTHONPATH=$(PWD) python3 scripts/conformance_harness.py

golden-check: conformance
	python3 scripts/check_golden.py

caps:
	PYTHONPATH=$(PWD) python3 scripts/dump_capabilities.py

aps-auth:
	python3 scripts/aps_auth_test.py

aps-orchestrate-example:
	PYTHONPATH=$(PWD) python3 scripts/run_fusion_example.py

aps-da-list-engines:
	python3 scripts/aps_da_stub.py list-engines

aps-da-create-appbundle:
	# Usage: make aps-da-create-appbundle NAME=MyAppBundle ENGINE=Autodesk.Fusion+<ver> ZIP=path/to/zip
	python3 scripts/aps_da_stub.py create-appbundle "$(NAME)" "$(ENGINE)" "$(ZIP)"

aps-da-create-activity:
	# Usage: make aps-da-create-activity NAME=MyActivity ENGINE=Autodesk.Fusion+<ver> APPBUNDLE=<bundleId>
	python3 scripts/aps_da_stub.py create-activity "$(NAME)" "$(ENGINE)" "$(APPBUNDLE)"

aps-da-submit-workitem:
	# Usage: make aps-da-submit-workitem ACTIVITY=<activityId> ARGS=workitem_args.json
	python3 scripts/aps_da_stub.py submit-workitem "$(ACTIVITY)" "$(ARGS)"

aps-da-bootstrap:
	# Idempotent helper: list engines as a sanity check
	python3 scripts/aps_da_stub.py list-engines

aps-da-clean:
	# Placeholder for future cleanup operations
	@echo "Nothing to clean yet for APS DA"


