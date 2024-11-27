install-vercel-deps:
	yum -y update
	yum install gcc bzip2-devel libffi-devel zlib-devel wget tar gzip rsync -y

PYTHON = .venv/bin/python

build-api-ref:
	git clone -b bagatur/update_py_api_ref --depth=1 https://github.com/langchain-ai/langsmith-sdk.git
	cd langsmith-sdk/python
	python3 -m venv .venv
	source .venv/bin/activate
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install --upgrade uv
	$(PYTHON) -m uv pip install -r docs/requirements.txt
	$(PYTHON) docs/create_api_rst.py
	cd docs && make html
	$(PYTHON) docs/scripts/custom_formatter.py docs/_build/html/
	cp docs/_build/html/{reference,index}.html


vercel-build: install-vercel-deps build-api-ref 
	mkdir static/api_reference
	mv langsmith-sdk/python/docs/_build/html/* static/api_reference/
	rm -rf langsmith-sdk
	NODE_OPTIONS="--max-old-space-size=5000" yarn run docusaurus build
