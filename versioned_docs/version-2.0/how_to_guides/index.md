---
sidebar_label: How-to guides
sidebar_position: 0
---

# How-to guides

Step-by-step guides that cover key tasks and operations in LangSmith.

## Setup

See the following guides to set up your LangSmith account.

- [Create an account and API key](./how_to_guides/setup/create_account_api_key)
- [Set up an organization](./how_to_guides/setup/set_up_organization)
  - [Create an organization](./how_to_guides/setup/set_up_organization#create-an-organization)
  - [Manage and navigate workspaces](./how_to_guides/setup/set_up_organization#manage-and-navigate-workspaces)
  - [Manage users](./how_to_guides/setup/set_up_organization#manage-users)
- [Set up a workspace](./how_to_guides/setup/set_up_workspace)
  - [Create a workspace](./how_to_guides/setup/set_up_workspace#create-a-workspace)
  - [Manage users](./how_to_guides/setup/set_up_workspace#manage-users)
  - [Configure workspace settings](./how_to_guides/setup/set_up_workspace#configure-workspace-settings)
- [Set up billing](./how_to_guides/setup/set_up_billing)
- [Set up access control (enterprise only)](./how_to_guides/setup/set_up_access_control)
  - [Create a role](./how_to_guides/setup/set_up_access_control#create-a-role)
  - [Assign a role to a user](./how_to_guides/setup/set_up_access_control#assign-a-role-to-a-user)

## Tracing

Get started with LangSmith's tracing features to start adding observability to your LLM applications.

- [Annotate code for tracing](./how_to_guides/tracing/annotate_code)
  - [Use `@traceable`/`traceable`](./how_to_guides/tracing/annotate_code#use-traceable--traceable)
  - [Wrap the OpenAI API client](./how_to_guides/tracing/annotate_code#wrap-the-openai-client)
  - [Use the RunTree API](./how_to_guides/tracing/annotate_code#use-the-runtree-api)
  - [Use the `trace` context manager (Python only)](./how_to_guides/tracing/annotate_code#use-the-trace-context-manager-python-only)
- [Toggle tracing on and off](./how_to_guides/tracing/toggle_tracing)
- [Log traces to specific project](./how_to_guides/tracing/log_traces_to_project)
  - [Set the destination project statically](./how_to_guides/tracing/log_traces_to_project#set-the-destination-project-statically)
  - [Set the destination project dynamically](./how_to_guides/tracing/log_traces_to_project#set-the-destination-project-dynamically)
- [Set a sampling rate for traces](./how_to_guides/tracing/sample_traces)
- [Add metadata and tags to traces](./how_to_guides/tracing/add_metadata_tags)
- [Implement distributed tracing](./how_to_guides/tracing/distributed_tracing)
  - [Distributed tracing in Python](./how_to_guides/tracing/distributed_tracing#distributed-tracing-in-python)
  - [Distributed tracing in TypeScript](./how_to_guides/tracing/distributed_tracing#distributed-tracing-in-typescript)
- [Access the current span within a traced function](./how_to_guides/tracing/access_current_span)
- [Log multimodal traces](./how_to_guides/tracing/log_multimodal_traces)
- [Log retriever traces](./how_to_guides/tracing/log_retriever_trace)
- [Log custom LLM traces](./how_to_guides/tracing/log_llm_trace)
  - [Chat-style models](./how_to_guides/tracing/log_llm_trace#chat-style-models)
  - [Specify model name](./how_to_guides/tracing/log_llm_trace#specify-model-name)
  - [Stream outputs](./how_to_guides/tracing/log_llm_trace#stream-outputs)
  - [Manually provide token counts](./how_to_guides/tracing/log_llm_trace#manually-provide-token-counts)
  - [Instruct-style models](./how_to_guides/tracing/log_llm_trace#instruct-style-models)
- [Prevent logging of sensitive data in traces](./how_to_guides/tracing/mask_inputs_outputs)
  - [Rule-based masking of inputs and outputs](./how_to_guides/tracing/mask_inputs_outputs#rule-based-masking-of-inputs-and-outputs)
- [Export traces](./how_to_guides/tracing/export_traces)
  - [Use filter arguments](./how_to_guides/tracing/export_traces#use-filter-arguments)
  - [Use filter query language](./how_to_guides/tracing/export_traces#use-filter-query-language)
- [Share or unshare a trace publicly](./how_to_guides/tracing/share_trace)
- [Trace generator functions](./how_to_guides/tracing/trace_generator_functions)
- [Trace with `LangChain`](./how_to_guides/tracing/trace_with_langchain)
  - [Installation](./how_to_guides/tracing/trace_with_langchain#installation)
  - [Quick start](./how_to_guides/tracing/trace_with_langchain#quick-start)
  - [Trace selectively](./how_to_guides/tracing/trace_with_langchain#trace-selectively)
  - [Log to specific project](./how_to_guides/tracing/trace_with_langchain#log-to-specific-project)
  - [Add metadata and tags to traces](./how_to_guides/tracing/trace_with_langchain#add-metadata-and-tags-to-traces)
  - [Customize run name](./how_to_guides/tracing/trace_with_langchain#customize-run-name)
  - [Access run (span) ID for LangChain invocations](./how_to_guides/tracing/trace_with_langchain#access-run-span-id-for-langchain-invocations)
  - [Ensure all traces are submitted before exiting](./how_to_guides/tracing/trace_with_langchain#ensure-all-traces-are-submitted-before-exiting)
  - [Trace withouth setting environment variables](./how_to_guides/tracing/trace_with_langchain#trace-without-setting-environment-variables)
- [Trace with `Instructor` (Python only)](./how_to_guides/tracing/trace_with_instructor)
- [Trace without setting environment variables](./how_to_guides/tracing/trace_without_env_vars)
- [Trace using the LangSmith REST API](./how_to_guides/tracing/trace_with_api)

## Datasets

Manage datasets in LangSmith to evaluate and improve your LLM applications.

- [Manage datasets in the application](./how_to_guides/datasets/manage_datasets_in_application)
  - [Create a new dataset and add examples manually](./how_to_guides/datasets/manage_datasets_in_application#create-a-new-dataset-and-add-examples-manually)
  - [Add inputs and outputs from traces to datasets](./how_to_guides/datasets/manage_datasets_in_application#add-inputs-and-outputs-from-traces-to-datasets)
  - [Upload a CSV file to create a dataset](./how_to_guides/datasets/manage_datasets_in_application#upload-a-csv-file-to-create-a-dataset)
  - [Export a dataset](./how_to_guides/datasets/manage_datasets_in_application#export-a-dataset)
  - [Create and manage dataset splits](./how_to_guides/datasets/manage_datasets_in_application#create-and-manage-dataset-splits)
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
- [Share or unshare a dataset publicly](./how_to_guides/datasets/share_dataset)

## Evaluation

Evaluate your LLM applications to measure their performance over time.

- [Evaluate an LLM application](./how_to_guides/evaluation/evaluate_llm_application)
  - [Run an evaluation](./how_to_guides/evaluation/evaluate_llm_application#run-an-evaluation)
  - [Use custom evaluators](./how_to_guides/evaluation/evaluate_llm_application#use-custom-evaluators)
  - [Evaluate on a particular version of a dataset](./how_to_guides/evaluation/evaluate_llm_application#evaluate-on-a-particular-version-of-a-dataset)
  - [Evaluate on a subset of a dataset](./how_to_guides/evaluation/evaluate_llm_application#evaluate-on-a-subset-of-a-dataset)
  - [Evaluate on a dataset split](./how_to_guides/evaluation/evaluate_llm_application#evaluate-on-a-dataset-split)
  - [Evaluate on a dataset with repetitions](./how_to_guides/evaluation/evaluate_llm_application#evaluate-on-a-dataset-with-repetitions)
  - [Use a summary evaluator](./how_to_guides/evaluation/evaluate_llm_application#use-a-summary-evaluator)
  - [Evaluate a LangChain runnable](./how_to_guides/evaluation/evaluate_llm_application#evaluate-a-langchain-runnable)
  - [Return multiple scores](./how_to_guides/evaluation/evaluate_llm_application#return-multiple-scores)
- [Bind an evaluator to a dataset in the UI](./how_to_guides/evaluation/bind_evaluator_to_dataset)
- [Run an evaluation from the prompt playground](./how_to_guides/evaluation/run_evaluation_from_prompt_playground)
- [Evaluate on intermediate steps](./how_to_guides/evaluation/evaluate_on_intermediate_steps)
- [Use LangChain off-the-shelf evaluators (Python only)](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators)
  - [Use question and answer (correctness) evaluators](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-question-and-answer-correctness-evaluators)
  - [Use criteria evaluators](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-criteria-evaluators)
  - [Use labeled criteria evaluators](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-labeled-criteria-evaluators)
  - [Use string or embedding distance metrics](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-string-or-embedding-distance-metrics)
  - [Use a custom LLM in off-the-shelf evaluators](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#use-a-custom-llm-in-off-the-shelf-evaluators)
  - [Handle multiple input or output fields](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators#handle-multiple-input-or-output-fields)
- [Compare experiment results](./how_to_guides/evaluation/compare_experiment_results)
  - [Open the comparison view](./how_to_guides/evaluation/compare_experiment_results#open-the-comparison-view)
  - [View regressions and improvements](./how_to_guides/evaluation/compare_experiment_results#view-regressions-and-improvements)
  - [Filter on regressions or improvements](./how_to_guides/evaluation/compare_experiment_results#filter-on-regressions-or-improvements)
  - [Update baseline experiment](./how_to_guides/evaluation/compare_experiment_results#update-baseline-experiment)
  - [Select feedback key](./how_to_guides/evaluation/compare_experiment_results#select-feedback-key)
  - [Open a trace](./how_to_guides/evaluation/compare_experiment_results#open-a-trace)
  - [Expand detailed view](./how_to_guides/evaluation/compare_experiment_results#expand-detailed-view)
  - [Update display settings](./how_to_guides/evaluation/compare_experiment_results#update-display-settings)
- [Evaluate an existing experiment](./how_to_guides/evaluation/evaluate_existing_experiment)
- [Unit test LLM applications (Python only)](./how_to_guides/evaluation/unit_testing)
- [Run pairwise evaluations](./how_to_guides/evaluation/evaluate_pairwise)
  - [Use the `evaluate_comparative` function](./how_to_guides/evaluation/evaluate_pairwise#use-the-evaluate_comparative-function)
  - [Configure inputs and outputs for pairwise evaluators](./how_to_guides/evaluation/evaluate_pairwise#configure-inputs-and-outputs-for-pairwise-evaluators)
  - [Compare two experiments with LLM-based pairwise evaluators](./how_to_guides/evaluation/evaluate_pairwise#compare-two-experiments-with-llm-based-pairwise-evaluators)
  - [View pairwise experiments](./how_to_guides/evaluation/evaluate_pairwise#view-pairwise-experiments)
- [Audit evaluator scores](./how_to_guides/evaluation/audit_evaluator_scores)
  - [In the comparison view](./how_to_guides/evaluation/audit_evaluator_scores#in-the-comparison-view)
  - [In the runs table](./how_to_guides/evaluation/audit_evaluator_scores#in-the-runs-table)
  - [In the SDK](./how_to_guides/evaluation/audit_evaluator_scores#in-the-sdk)
- [Create few-shot evaluators](./how_to_guides/evaluation/create_few_shot_evaluators)
  - [Create your evaluator](./how_to_guides/evaluation/create_few_shot_evaluators#create-your-evaluator)
  - [View your corrections dataset](./how_to_guides/evaluation/create_few_shot_evaluators#view-your-corrections-dataset)
  - [Making corrections](./how_to_guides/evaluation/create_few_shot_evaluators#making-corrections)
- [Fetch performance metrics for an experiment](./how_to_guides/evaluation/fetch_perf_metrics_experiment)

## Human feedback

Collect human feedback to improve your LLM applications.

- [Capture user feedback from your application to traces](./how_to_guides/human_feedback/attach_user_feedback)
- [Set up a new feedback criteria](./how_to_guides/human_feedback/set_up_feedback_criteria)
- [Annotate traces inline](./how_to_guides/human_feedback/annotate_traces_inline)
- [Use annotation queues](./how_to_guides/human_feedback/annotation_queues)
  - [Create an annotation queue](./how_to_guides/human_feedback/annotation_queues#create-an-annotation-queue)
  - [Assign runs to an annotation queue](./how_to_guides/human_feedback/annotation_queues#assign-runs-to-an-annotation-queue)
  - [Review runs in an annotation queue](./how_to_guides/human_feedback/annotation_queues#review-runs-in-an-annotation-queue)

## Monitoring and automations

Leverage LangSmith's powerful monitoring and automations features to make sense of your production data.

- [Filter traces in the application](./how_to_guides/monitoring/filter_traces_in_application)
  - [Create a filter](./how_to_guides/monitoring/filter_traces_in_application#create-a-filter)
  - [Filter for intermediate runs (spans)](./how_to_guides/monitoring/filter_traces_in_application#filter-for-intermediate-runs-spans)
  - [Advanced: filter for intermediate runs (spans) on properties of the root](./how_to_guides/monitoring/filter_traces_in_application#advanced-filter-for-intermediate-runs-spans-on-properties-of-the-root)
  - [Advanced: filter for runs (spans) whose child runs have some attribute](./how_to_guides/monitoring/filter_traces_in_application#advanced-filter-for-runs-spans-whose-child-runs-have-some-attribute)
  - [Filter based on inputs and outputs](./how_to_guides/monitoring/filter_traces_in_application#filter-based-on-inputs-and-outputs)
  - [Copy the filter](./how_to_guides/monitoring/filter_traces_in_application#copy-the-filter)
  - [Manually specify a raw query in LangSmith query language](./how_to_guides/monitoring/filter_traces_in_application#manually-specify-a-raw-query-in-langsmith-query-language)
  - [Use an AI Query to auto-generate a query](./how_to_guides/monitoring/filter_traces_in_application#use-an-ai-query-to-auto-generate-a-query)
- [Use monitoring charts](./how_to_guides/monitoring/use_monitoring_charts)
  - [Change the time period](./how_to_guides/monitoring/use_monitoring_charts#change-the-time-period)
  - [Slice data by metadata or tag](./how_to_guides/monitoring/use_monitoring_charts#slice-data-by-metadata-or-tag)
  - [Drill down into specific subsets](./how_to_guides/monitoring/use_monitoring_charts#drill-down-into-specific-subsets)
- [Set up automation rules](./how_to_guides/monitoring/rules)
  - [Create a rule](./how_to_guides/monitoring/rules#create-a-rule)
  - [View logs for your automations](./how_to_guides/monitoring/rules#view-logs-for-your-automations)
- [Set up online evaluations](./how_to_guides/monitoring/online_evaluations)
  - [Configure online evaluations](./how_to_guides/monitoring/online_evaluations#configure-online-evaluations)
  - [Set API keys](./how_to_guides/monitoring/online_evaluations#set-api-keys)
- [Set up webhook notifications for rules (beta)](./how_to_guides/monitoring/webhooks)
  - [Webhook payload](./how_to_guides/monitoring/webhooks#webhook-payload)
  - [Example with Modal](./how_to_guides/monitoring/webhooks#example-with-modal)
- [Set up threads](./how_to_guides/monitoring/threads)
  - [Group traces into threads](./how_to_guides/monitoring/threads#group-traces-into-threads)
  - [View threads](./how_to_guides/monitoring/threads#view-threads)

## Prompts

Organize and manage prompts in LangSmith to streamline your LLM development workflow.

- [Create a prompt](./how_to_guides/prompts/create_a_prompt)
  - [Compose your prompt](./how_to_guides/prompts/create_a_prompt#compose-your-prompt)
  - [Save your prompt](./how_to_guides/prompts/create_a_prompt#save-your-prompt)
  - [View your prompts](./how_to_guides/prompts/create_a_prompt#view-your-prompts)
  - [Add metadata](./how_to_guides/prompts/create_a_prompt#add-metadata)
- [Update a prompt](./how_to_guides/prompts/update_a_prompt)
  - [Update metadata](./how_to_guides/prompts/update_a_prompt#update-metadata)
  - [Update the prompt content](./how_to_guides/prompts/update_a_prompt#update-the-prompt-content)
  - [Version a prompt](./how_to_guides/prompts/update_a_prompt#versioning)
- [Pull/push a prompt](./how_to_guides/prompts/pull_push_a_prompt)
  - [Install packages](./how_to_guides/prompts/pull_push_a_prompt#install_packages)
  - [Configure environment variables](./how_to_guides/prompts/pull_push_a_prompt#configure_environment_variables)
  - [Pull a prompt and use it](./how_to_guides/prompts/pull_push_a_prompt#pull_a_prompt_and_use_it)
  - [Push a prompt to your personal organization](./how_to_guides/prompts/pull_push_a_prompt#push_a_prompt_to_your_personal_organization)
- [LangChain Hub](./how_to_guides/prompts/langchain_hub)

## Playground

Quickly iterate on prompts and models in the LangSmith Playground.

- [Use custom TLS certificates](./how_to_guides/playground/custom_tls_certificates)
- [Use a custom model](./how_to_guides/playground/custom_endpoint)
