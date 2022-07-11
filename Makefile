.DEFAULT_GOAL := help

.PHONY: help
help: ## Print the help message
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%s\033[0m : %s\n", $$1, $$2}' $(MAKEFILE_LIST) | \
		sort | \
		column -s ':' -t

.PHONY: test
test: ## Run python tests
	docker-compose run --rm app python -m pytest -vv tests

.PHONY: bandit
bandit:
	docker-compose run --rm app bandit -r app

.PHONY: build
build: ## Build the app
	docker build -t example/example:latest -f Dockerfile.prod .

.PHONY: ci
ci: test bandit build ## Run CI tests
