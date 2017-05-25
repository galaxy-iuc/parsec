rebuild:
	rsync -ar external/ parsec/commands/
	python scripts/autobuilder.py
	python scripts/commands_to_rst.py
