PROJECT_NAME = netatmo

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	rm -rf .cache .config .ipython .jupyter .local
	rm -rf $(PROJECT_NAME).egg-info

.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: test
test:
	flake8 $(PROJECT_NAME)
	pytest $(PROJECT_NAME)
