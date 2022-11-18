run:
	python scripts/main.py

format:
	python -m black ./scripts/*
	autoflake --in-place --remove-unused-variables --recursive ./scripts