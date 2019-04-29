rebuild:
	rm parsec/commands/*/*.py
	python scripts/autobuilder.py
	python scripts/autobuilder.py --config .command-engine-ts.yml
	python scripts/commands_to_rst.py
	find parsec/commands -type d -empty -exec rmdir '{}' +
