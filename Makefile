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

# Fusion Automation API (GA) helpers
fusion-auto-hello:
	# Requires APS_CLIENT_ID/APS_CLIENT_SECRET or out/token_3l.json; uses DA (Automation v3)
	python3 scripts/fusion_auto_submit.py

fusion-auto-status:
	# Requires DA_WORKITEM_ID (or out/fusion_auto_submit.json) and uses DA (Automation v3)
	python3 scripts/fusion_auto_status.py

fusion-auto-hello-msg:
	# Usage: make fusion-auto-hello-msg MSG="adsk.log('hi')"
	# Env: FUSION_TASK_SCRIPT overrides inline script, FUSION_PAT required
	FUSION_TASK_SCRIPT="$(MSG)" python3 scripts/fusion_auto_submit.py

fusion-auto-status-logs:
	# Poll and download report; DA_FETCH_REPORT=1 to fetch logs
	DA_FETCH_REPORT=1 python3 scripts/fusion_auto_status.py

# Compute Fusion feature coverage and update badge in FUSION_FEATURE_COVERAGE.md
fusion-cov:
	PYTHONPATH=$(PWD) python3 scripts/compute_fusion_coverage.py

fusion-auto-unfold-test:
	# Runs the TS script that creates a sheet base, unfolds, then refolds
	FUSION_SCRIPT_FILE=scripts/fusion_auto_unfold_test.ts python3 scripts/fusion_auto_submit.py

fusion-auto-unfold-status:
	# Poll and download report/logs for the last unfold/refold run
	DA_FETCH_REPORT=1 python3 scripts/fusion_auto_status.py

# Fillet transition/setback test
fusion-auto-fillet-test:
	FUSION_SCRIPT_FILE=scripts/fusion_auto_fillet_test.ts python3 scripts/fusion_auto_submit.py

# Chamfer variants test
fusion-auto-chamfer-test:
	FUSION_SCRIPT_FILE=scripts/fusion_auto_chamfer_test.ts python3 scripts/fusion_auto_submit.py

# Loft and Sweep tests
fusion-auto-loft-test:
	FUSION_SCRIPT_FILE=scripts/fusion_auto_loft_test.ts python3 scripts/fusion_auto_submit.py

fusion-auto-sweep-test:
	FUSION_SCRIPT_FILE=scripts/fusion_auto_sweep_test.ts python3 scripts/fusion_auto_submit.py

# Wrap/Project tests (Automation ScriptJob)
fusion-auto-wrap-project-test:
	FUSION_SCRIPT_FILE=scripts/fusion_auto_wrap_project_test.ts python3 scripts/fusion_auto_submit.py

# Remote validation orchestrator: runs multiple tests
automation-remote-validate:
	PYTHONPATH=$(PWD) python3 scripts/automation_remote_validation.py

# 3-legged OAuth helper for Fusion Automation (uses Traditional Web App creds)
oauth3l-login:
	# Set APS_CLIENT_ID/APS_CLIENT_SECRET (Traditional Web App) and optional APS_REDIRECT_URI; saves out/token_3l.json
	python3 scripts/oauth3l_login.py

oauth3l-exchange:
	# Usage: make oauth3l-exchange URL='<redirected_url_with_code>'
	python3 scripts/oauth3l_exchange.py "$(URL)"

# Design Automation (DA) v3 helpers (US-East)
da-submit:
	# Set DA_ACTIVITY_ID (e.g., MyActivity+v1) and FUSION_PAT (Fusion Personal Access Token)
	python3 scripts/da_submit_workitem.py

da-status:
	# Set DA_WORKITEM_ID or ensure out/da_workitem_submit.json is present
	python3 scripts/da_workitem_status.py
