.PHONY: help
help:  ## help
	@echo "Command list:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# TODO: .python-versionにインストールしていないバージョンがあったらインストールするコマンド追加
.PHONY: setup
setup:  ## Install python libraries and activate pre-commit.
	poetry install
	poetry run pre-commit install