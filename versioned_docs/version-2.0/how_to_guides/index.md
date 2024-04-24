# How-To Guides

Step-by-step guides that cover key tasks and operations in LangSmith.

## Setup

* [Create an account and API key](./how_to_guides/setup/create_account_api_key)
* [Create an organization](./how_to_guides/setup/create_organization)
* [ ] Set up a workspace
* [ ] Setup billing
* [ ] Assign roles (enterprise only)

## Tracing

* [Annotate code for tracing](./how_to_guides/tracing/annotate_code)
  * [Use `@traceable`/`traceable`](./how_to_guides/tracing/annotate_code#use-traceable--traceable)
  * [Wrap the OpenAI API client](./how_to_guides/tracing/annotate_code#wrap-the-openai-client)
  * [Use the RunTree API](./how_to_guides/tracing/annotate_code#use-the-runtree-api)
* [Toggle tracing on and off](./how_to_guides/tracing/toggle_tracing)
* [Log traces to specific project](./how_to_guides/tracing/log_traces_to_project)
  * [Set the destination project statically](./how_to_guides/tracing/log_traces_to_project#set-the-destination-project-statically)
  * [Set the destination project dynamically](./how_to_guides/tracing/log_traces_to_project#set-the-destination-project-dynamically)
* [Set a sampling rate for traces](./how_to_guides/tracing/sample_traces)
- [ ] Add metadata and tags to traces
- [ ] Get run_id and trace_id
- [ ] Mask inputs and outputs
- [ ] Log a trace using LangChain
- [ ] Log a trace using instructor
- [ ] Exporting traces
  - [ ] Link to data format in reference section
- [ ] Log multi-modal traces

### Datasets

- [ ] Create a dataset in the application
- [ ] Create a dataset using the API
- [ ] Export datasets
- [ ] Import datasets
- [ ] Version datasets
- [ ] Add metadata to examples
- [ ] Filter examples from a dataset
- [ ] Add a trace to a dataset

### Evaluation

- [ ] Run an evaluation
- [ ] Run an evaluation from the playground
- [ ] Run an evaluation on a particular version of dataset
- [ ] Run an evaluation on subset of dataset
- [ ] Use off-the-shelf LangChain evaluators
- [ ] Use custom evaluators
- [ ] Evaluate on intermediate steps
- [ ] Compare experiment results
- [ ] Track regressions and improvements
- [ ] Export experiment
- [ ] Unit test LLM applications
- [ ] View trace for an evaluation run
- [ ] Run a pairwise evaluation (coming soon)
- [ ] Audit evaluation scores (coming soon)

### Human Feedback

- [ ] Attach user feedback from your application to traces
- [ ] Annotate traces inline
- [ ] Add trace to annotation queue
- [ ] Annotate traces in the annotation queue

### Monitoring and Automations

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

### Prompt Hub

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
