LOC:
	PYTHONPATH=$(PWD) python3 scripts/update_loc_badge.py

conformance:
	PYTHONPATH=$(PWD) python3 scripts/conformance_harness.py

golden-check: conformance
	python3 scripts/check_golden.py


