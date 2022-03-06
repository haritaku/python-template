.PHONY: help setup
help:  ## help
	@echo "Command list:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup:  ## Install python libraries and activate pre-commit.
	@cat .python-version | xargs -n1 pyenv install -s 
	@poetry install
	@poetry run pre-commit install