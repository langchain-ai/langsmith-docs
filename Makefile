install-vercel-deps:
	yum -y update
	yum install gcc bzip2-devel libffi-devel zlib-devel wget tar gzip rsync -y

PYTHON = .venv/bin/python

build-api-ref:
	git clone --depth=1 https://github.com/langchain-ai/langsmith-sdk.git
	python3 -m venv .venv
	. .venv/bin/activate
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install --upgrade uv
	cd langsmith-sdk && ../$(PYTHON) -m uv pip install -r python/docs/requirements.txt
	$(PYTHON) langsmith-sdk/python/docs/create_api_rst.py
	LC_ALL=C $(PYTHON) -m sphinx -T -E -b html -d langsmith-sdk/python/docs/_build/doctrees -c langsmith-sdk/python/docs langsmith-sdk/python/docs langsmith-sdk/python/docs/_build/html -j auto
	$(PYTHON) langsmith-sdk/python/docs/scripts/custom_formatter.py langsmith-sdk/docs/_build/html/
	cd langsmith-sdk/js && yarn && yarn run build:typedoc

vercel-build: install-vercel-deps build-api-ref 
	mkdir -p static/reference/python
	mv langsmith-sdk/python/docs/_build/html/* static/reference/python/
	mkdir -p static/reference/js
	mv langsmith-sdk/js/_build/api_refs/* static/reference/js/
	rm -rf langsmith-sdk
	NODE_OPTIONS="--max-old-space-size=5000" yarn run docusaurus build

