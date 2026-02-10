# API reference build disabled - docs now redirect to reference.langchain.com/python/langsmith
# build-api-ref:
# 	git clone --depth=1 https://github.com/langchain-ai/langsmith-sdk.git
# 	...

vercel-build:
	NODE_OPTIONS="--max-old-space-size=5000" yarn run docusaurus build
