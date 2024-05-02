---
sidebar_position: 1
---

# How-to guides

Step-by-step guides that cover key tasks and operations in LangSmith.

## Setup

- [Create an account and API key](./how_to_guides/setup/create_account_api_key)
- [Create an organization](./how_to_guides/setup/create_organization)
- [Set up a workspace](./how_to_guides/setup/set_up_workspace)
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

* [ ] Trace a generator function
* [ ] Trace with LangChain
* [ ] Trace using instructor

## Datasets

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
  - [Fetch datasets](./how_to_guides/datasets/manage_datasets_programmatically#fetch-datasets)
  - [Fetch examples](./how_to_guides/datasets/manage_datasets_programmatically#fetch-examples)
- [Version datasets](./how_to_guides/datasets/version_datasets)
  - [Create a new version of a dataset](./how_to_guides/datasets/version_datasets#create-a-new-version-of-a-dataset)
  - [Tag a version](./how_to_guides/datasets/version_datasets#tag-a-version)

## Evaluation

- [Evaluate an LLM application](./how_to_guides/evaluation/evaluate_llm_application)
  - [Run an evaluation](./how_to_guides/evaluation/evaluate_llm_application#run-an-evaluation)
  - [Use custom evaluators](./how_to_guides/evaluation/evaluate_llm_application#use-custom-evaluators)
  - [Evaluate on a particular version of a dataset](./how_to_guides/evaluation/evaluate_llm_application#evaluate-on-a-particular-version-of-a-dataset)
  - [Evaluate on a subset of a dataset](./how_to_guides/evaluation/evaluate_llm_application#evaluate-on-a-subset-of-a-dataset)
  - [Use a summary evaluator](./how_to_guides/evaluation/evaluate_llm_application#use-a-summary-evaluator)
  - [Evaluate a LangChain runnable](./how_to_guides/evaluation/evaluate_llm_application#evaluate-a-langchain-runnable)
- [Run an evaluation from the prompt playground](./how_to_guides/evaluation/run_evaluation_from_prompt_playground)
- [Evaluate on intermediate steps](./how_to_guides/evaluation/evaluate_on_intermediate_steps)
- [Use LangChain off-the-shelf evaluators (Python only)](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators)
  - [Use question and answer (correctness) evaluators](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-question-and-answer-correctness-evaluators)
  - [Use criteria evaluators](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-criteria-evaluators)
  - [Use labeled criteria evaluators](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-labeled-criteria-evaluators)
  - [Use string or embedding distance metrics](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-string-or-embedding-distance-metrics)
  - [Use a custom LLM in off-the-shelf evaluators](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-a-custom-llm-in-off-the-shelf-evaluators)
  - [Handle multiple input or output fields](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#handle-multiple-input-or-output-fields)
- [ ] Evaluate an existing experiment - will
- [ ] Compare experiment results
- [ ] Export experiment results - will
- [ ] Unit test LLM applications with `pytest` (Python only) - will

## Human feedback

- [ ] Attach user feedback from your application to traces
- [ ] Annotate traces inline
- [ ] Add trace to annotation queue
- [ ] Annotate traces in the annotation queue

## Monitoring and automations

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

## Prompt hub

- [ ] Create a prompt
- [ ] Update a prompt
- [ ] Pull prompts in code
- [ ] Open a prompt from a trace
- [ ] Open a prompt from an experiment

## Playground

- [ ] Run a prompt in the playground
- [ ] Run a prompt on a custom model

## Proxy

- [ ] Run proxy
- [ ] Make a request to the proxy
- [ ] Turn off caching
- [ ] Stream results
- [ ] Turn on tracing
