LOC:
	PYTHONPATH=$(PWD) python3 scripts/update_loc_badge.py

conformance:
	PYTHONPATH=$(PWD) python3 scripts/conformance_harness.py

golden-check: conformance
	python3 scripts/check_golden.py

caps:
	PYTHONPATH=$(PWD) python3 scripts/dump_capabilities.py

publish-caps:
	PYTHONPATH=$(PWD) CSL_VERSION=$(shell git describe --tags --abbrev=0 2>/dev/null || echo v0.x) \
		python3 scripts/publish_capabilities.py

roundtrip:
	PYTHONPATH=$(PWD) python3 scripts/roundtrip_validation.py

query-fuzz:
	PYTHONPATH=$(PWD) python3 scripts/query_fuzz.py

perf:
	PYTHONPATH=$(PWD) python3 scripts/perf_baseline.py

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

aps-da-ensure-appbundle:
	# Usage: make aps-da-ensure-appbundle NAME=MyAppBundle ENGINE=Autodesk.Fusion+<ver> ZIP=path/to/zip
	python3 scripts/aps_da_stub.py ensure-appbundle "$(NAME)" "$(ENGINE)" "$(ZIP)"

aps-da-ensure-activity:
	# Usage: make aps-da-ensure-activity NAME=MyActivity ENGINE=Autodesk.Fusion+<ver> APPBUNDLE=<bundleId>
	python3 scripts/aps_da_stub.py ensure-activity "$(NAME)" "$(ENGINE)" "$(APPBUNDLE)"

aps-da-pipeline:
	# Required env: APS_ENGINE, APS_BUNDLE_ZIP; optional: APS_BUNDLE_NAME, APS_ACTIVITY_NAME, APS_INPUT_URL, APS_OUTPUT_URL
	PYTHONPATH=$(PWD) python3 scripts/aps_da_pipeline.py


