---
sidebar_position: 1
---

# How-to guides

Step-by-step guides that cover key tasks and operations in LangSmith.

## Setup

- [Create an account and API key](./how_to_guides/setup/create_account_api_key)
- [Create an organization](./how_to_guides/setup/create_organization)
- [ ] Set up a workspace
- [ ] Setup billing
- [ ] Assign roles (enterprise only)

## Tracing

- [Annotate code for tracing](./how_to_guides/tracing/annotate_code)
  - [Use `@traceable`/`traceable`](./how_to_guides/tracing/annotate_code#use-traceable--traceable)
  - [Wrap the OpenAI API client](./how_to_guides/tracing/annotate_code#wrap-the-openai-client)
  - [Use the RunTree API](./how_to_guides/tracing/annotate_code#use-the-runtree-api)
- [Toggle tracing on and off](./how_to_guides/tracing/toggle_tracing)
- [Log traces to specific project](./how_to_guides/tracing/log_traces_to_project)
  - [Set the destination project statically](./how_to_guides/tracing/log_traces_to_project#set-the-destination-project-statically)
  - [Set the destination project dynamically](./how_to_guides/tracing/log_traces_to_project#set-the-destination-project-dynamically)
- [Set a sampling rate for traces](./how_to_guides/tracing/sample_traces)
- [Add metadata and tags to traces](./how_to_guides/tracing/add_metadata_tags)
- [Implement distributed tracing](./how_to_guides/tracing/distributed_tracing)
- [Access the current span within a traced function](./how_to_guides/tracing/access_current_span)
- [Log multimodal traces](./how_to_guides/tracing/log_multimodal_traces)
- [Log retriever traces](./how_to_guides/tracing/log_retriever_trace)
- [Log custom LLM traces](./how_to_guides/tracing/log_llm_trace)
  - [Chat-style models](./how_to_guides/tracing/log_llm_trace#chat-style-models)
  - [Specify model name](./how_to_guides/tracing/log_llm_trace#specify-model-name)
  - [Stream outputs](./how_to_guides/tracing/log_llm_trace#stream-outputs)
  - [Manually provide token counts](./how_to_guides/tracing/log_llm_trace#manually-provide-token-counts)
  - [Instruct-style models](./how_to_guides/tracing/log_llm_trace#instruct-style-models)
- [Prevent logging of inputs and outputs in traces](./how_to_guides/tracing/mask_inputs_outputs)
- [Export traces](./how_to_guides/tracing/export_traces)
  - [Use filter arguments](./how_to_guides/tracing/export_traces#use-filter-arguments)
  - [Use filter query language](./how_to_guides/tracing/export_traces#use-filter-query-language)

* [ ] Decorating a generator function
* [ ] Log a trace using LangChain
* [ ] Log a trace using instructor

### Datasets

- [Manage datasets in the application](./how_to_guides/datasets/manage_datasets_in_application)
  - [Create a new dataset and add examples manually](./how_to_guides/datasets/manage_datasets_in_application#create-a-new-dataset-and-add-examples-manually)
  - [Add inputs and outputs from traces to datasets](./how_to_guides/datasets/manage_datasets_in_application#add-inputs-and-outputs-from-traces-to-datasets)
  - [Upload a CSV file to create a dataset](./how_to_guides/datasets/manage_datasets_in_application#upload-a-csv-file-to-create-a-dataset)
  - [Export a dataset](./how_to_guides/datasets/manage_datasets_in_application#export-a-dataset)
- [Manage datasets programmatically](./how_to_guides/datasets/manage_datasets_programmatically)
  - [Create a dataset from list of values](./how_to_guides/datasets/manage_datasets_programmatically#create-a-dataset-from-list-of-values)
  - [Create a dataset from traces](./how_to_guides/datasets/manage_datasets_programmatically#create-a-dataset-from-traces)
  - [Create a dataset from a CSV file](./how_to_guides/datasets/manage_datasets_programmatically#create-a-dataset-from-a-csv-file)
  - [Create a dataset from a pandas DataFrame](./how_to_guides/datasets/manage_datasets_programmatically#create-a-dataset-from-a-pandas-dataframe)
- [ ] Version datasets
- [ ] Filter examples from a dataset

### Evaluation

- [ ] Run an evaluation
- [Run an evaluation from the prompt playground](./how_to_guides/evaluation/run_evaluation_from_prompt_playground)
- [ ] Run an evaluation on a particular version of dataset
- [ ] Run an evaluation on subset of dataset
- [ ] Use off-the-shelf LangChain evaluators
- [ ] Use custom evaluators
- [Evaluate on intermediate steps](./how_to_guides/evaluation/evaluate_on_intermediate_steps)
- [ ] Compare experiment results
- [ ] Track regressions and improvements
- [ ] Export experiment
- [ ] Unit test LLM applications
- [ ] View trace for an evaluation run
- [ ] Run a pairwise evaluation (coming soon)
- [ ] Audit evaluation scores (coming soon)

### Human feedback

- [ ] Attach user feedback from your application to traces
- [ ] Annotate traces inline
- [ ] Add trace to annotation queue
- [ ] Annotate traces in the annotation queue

### Monitoring and automations

- [ ] Filter for runs
- [ ] Use a trace filter
- [ ] View the monitor charts
- [ ] Slice chart by metadata and tag
- [ ] Set up a rule
  - [ ] Online evaluation
  - [ ] Annotation Queue addition
  - [ ] Dataset addition
  - [ ] Webhook action
- [ ] Group traces as threads
- [ ] View threads

### Prompt hub

- [ ] Create a prompt
- [ ] Update a prompt
- [ ] Pull prompts in code
- [ ] Open a prompt from a trace
- [ ] Open a prompt from an experiment

### Playground

- [ ] Run a prompt in the playground
- [ ] Run a prompt on a custom model

### Proxy

- [ ] Run proxy
- [ ] Make a request to the proxy
- [ ] Turn off caching
- [ ] Stream results
- [ ] Turn on tracing
