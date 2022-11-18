run:
	python scripts/main.py

format:
	python -m black ./scripts/*
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports --recursive ./scripts