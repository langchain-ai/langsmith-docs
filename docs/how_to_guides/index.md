---
sidebar_label: How-to guides
sidebar_position: 0
---

# How-to guides

Step-by-step guides that cover key tasks and operations in LangSmith.

## Observability

### Tracing Configuration

Set up LangSmith tracing to get visibility into your production applications.

#### Basic Configuration

- [Trace any Python or JS Code](./how_to_guides/tracing/annotate_code)
- [Trace with `LangChain`](./how_to_guides/tracing/trace_with_langchain)
- [Trace with `LangGraph`](./how_to_guides/tracing/trace_with_langgraph)
- [Trace using the LangSmith REST API](./how_to_guides/tracing/trace_with_api)
- [Set your tracing project](./how_to_guides/tracing/log_traces_to_project)
- [Enable or disable tracing](./how_to_guides/tracing/toggle_tracing)

#### Trace Supported 3rd Party Libraries

- [Trace the OpenAI API client](./how_to_guides/tracing/annotate_code#wrap-the-openai-client)
- [Trace with `Instructor` (Python only)](./how_to_guides/tracing/trace_with_instructor)
- [Trace with the Vercel `AI SDK` (JS only)](./how_to_guides/tracing/trace_with_vercel_ai_sdk)

#### Advanced Configuration

- [Configure threads](./how_to_guides/monitoring/threads)
- [Set a sampling rate for traces](./how_to_guides/tracing/sample_traces)
- [Add metadata and tags to traces](./how_to_guides/tracing/add_metadata_tags)
- [Implement distributed tracing](./how_to_guides/tracing/distributed_tracing)
- [Access the current span within a traced function](./how_to_guides/tracing/access_current_span)
- [Log multimodal traces](./how_to_guides/tracing/log_multimodal_traces)
- [Log retriever traces](./how_to_guides/tracing/log_retriever_trace)
- [Log custom LLM traces / provide custom token counts](./how_to_guides/tracing/log_llm_trace)
- [Prevent logging of sensitive data in traces](./how_to_guides/tracing/mask_inputs_outputs)
- [Trace generator functions](./how_to_guides/tracing/trace_generator_functions)
- [Calculate token-based costs for traces](./how_to_guides/tracing/calculate_token_based_costs)

### Tracing Projects UI & API

View and interact with your traces to debug your applications.

- [Filter traces in a project](./how_to_guides/monitoring/filter_traces_in_application)
- [Save a filter for your project](./how_to_guides/monitoring/filter_traces_in_application#saved-filters)
- [Export traces using the SDK (low volume)](./how_to_guides/tracing/export_traces)
- [Bulk exporting traces (high volume)](./how_to_guides/tracing/data_export)
- [Share or unshare a trace publicly](./how_to_guides/tracing/share_trace)
- [Compare traces](./how_to_guides/tracing/compare_traces)
- [View threads](./how_to_guides/monitoring/threads#view-threads)

### Dashboards

Use LangSmith custom and built-in dashboards to gain insight into your production systems.

- [Create and use custom dashboards](./how_to_guides/monitoring/dashboards)
- [Use built-in monitoring dashboards](./how_to_guides/monitoring/use_monitoring_charts)

### Automations

Leverage LangSmith's powerful monitoring and automations features to make sense of your production data.

- [Set up automation rules](./how_to_guides/monitoring/rules)
- [Set up webhook notifications for rules](./how_to_guides/monitoring/webhooks)

## Evaluation

### Evaluation SDK & API

Write evaluations to test and improve your application.

- [Evaluate an LLM application in the SDK](./how_to_guides/evaluation/evaluate_llm_application)
- [Define a custom evaluator](./how_to_guides/evaluation/evaluate_llm_application#use-custom-evaluators)
- [Evaluate on intermediate steps](./how_to_guides/evaluation/evaluate_on_intermediate_steps)
- [Use LangChain off-the-shelf evaluators (Python only)](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators)
- [Evaluate an existing experiment](./how_to_guides/evaluation/evaluate_existing_experiment)
- [Unit test LLM applications (Python only)](./how_to_guides/evaluation/unit_testing)
- [Run a pairwise evaluation](./how_to_guides/evaluation/evaluate_pairwise)
- [Run evals using the API only](./how_to_guides/evaluation/run_evals_api_only)

### Auto Evaluation

Set up auto-evaluators that LangSmith will automatically run on your experiments.

- [Set up an Auto-Evaluator to run on all experiments](./how_to_guides/evaluation/bind_evaluator_to_dataset)
- [Create few-shot evaluators](./how_to_guides/evaluation/create_few_shot_evaluators)

### Online Evaluation

Set up evaluations to run on incoming traces to understand your application's behavior in production.

- [Set up online evaluations](./how_to_guides/monitoring/online_evaluations)
- [Create few-shot evaluators](./how_to_guides/evaluation/create_few_shot_evaluators)

### Experiments

Use the experiments UI & API to understand your evaluations.

- [Run an evaluation in the prompt playground](./how_to_guides/evaluation/run_evaluation_from_prompt_playground)
- [Compare experiments with the comparison view](./how_to_guides/evaluation/compare_experiment_results)
- [Filter experiments](./how_to_guides/evaluation/filter_experiments_ui)
- [View pairwise experiments](./how_to_guides/evaluation/evaluate_pairwise#view-pairwise-experiments)
- [Fetch experiment results in the SDK](./how_to_guides/evaluation/fetch_perf_metrics_experiment)
- [Upload experiments run outside of LangSmith with the REST API](./how_to_guides/evaluation/upload_existing_experiments)

### Datasets

Manage datasets in LangSmith used by your offline evaluations (as well as other downstream applications).

- [Manage datasets in the application](./how_to_guides/datasets/manage_datasets_in_application)
- [Manage datasets programmatically](./how_to_guides/datasets/manage_datasets_programmatically)
- [Version datasets](./how_to_guides/datasets/version_datasets)
- [Share or unshare a dataset publicly](./how_to_guides/datasets/share_dataset)

### Annotatio Queues and Human Feedback

Collect human feedback to improve your LLM applications.

- [Use annotation queues](./how_to_guides/human_feedback/annotation_queues)
- [Capture user feedback from your application to traces](./how_to_guides/human_feedback/attach_user_feedback)
- [Set up a new feedback criteria](./how_to_guides/human_feedback/set_up_feedback_criteria)
- [Annotate traces inline](./how_to_guides/human_feedback/annotate_traces_inline)
- [Audit and correct evaluator scores](./how_to_guides/evaluation/audit_evaluator_scores)

## Prompt Engineering

### Prompt Hub

Organize and manage prompts in LangSmith to streamline your LLM development workflow.

- [Create a prompt](./how_to_guides/prompts/create_a_prompt)
- [Update a prompt](./how_to_guides/prompts/update_a_prompt)
- [Manage prompts programmatically](./how_to_guides/prompts/manage_prompts_programatically)
- [Use prompt tags](./how_to_guides/prompts/prompt_tags)
- [LangChain Hub](./how_to_guides/prompts/langchain_hub)

### Playground

Quickly iterate on prompts and models in the LangSmith Playground.

- [Use custom TLS certificates](./how_to_guides/playground/custom_tls_certificates)
- [Use a custom model](./how_to_guides/playground/custom_endpoint)
- [Save settings configuration](./how_to_guides/playground/save_model_configuration)

### Few shot prompting

Use LangSmith datasets to serve few shot examples to your application

- [Index a dataset for few shot example selection](./how_to_guides/datasets/index_datasets_for_dynamic_few_shot_example_selection)

## Administration

See the following guides to set up your LangSmith account.

- [Create an account and API key](./how_to_guides/setup/create_account_api_key)
- [Set up an organization](./how_to_guides/setup/set_up_organization)
- [Set up a workspace](./how_to_guides/setup/set_up_workspace)
- [Set up billing](./how_to_guides/setup/set_up_billing)
- [Update invoice email, tax id and, business information](./how_to_guides/setup/update_business_info)
- [Set up access control (enterprise only)](./how_to_guides/setup/set_up_access_control)
- [Set up resource tags](./how_to_guides/setup/set_up_resource_tags)
