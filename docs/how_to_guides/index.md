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
  - [Manage your organization using the API](./how_to_guides/setup/manage_organization_by_api)
- [Set up a workspace](./how_to_guides/setup/set_up_workspace)
  - [Create a workspace](./how_to_guides/setup/set_up_workspace#create-a-workspace)
  - [Manage users](./how_to_guides/setup/set_up_workspace#manage-users)
  - [Configure workspace settings](./how_to_guides/setup/set_up_workspace#configure-workspace-settings)
- [Set up billing](./how_to_guides/setup/set_up_billing)
- [Update invoice email, tax id and, business information](./how_to_guides/setup/update_business_info)
- [Set up access control (enterprise only)](./how_to_guides/setup/set_up_access_control)
  - [Create a role](./how_to_guides/setup/set_up_access_control#create-a-role)
  - [Assign a role to a user](./how_to_guides/setup/set_up_access_control#assign-a-role-to-a-user)
- [Set up resource tags](./how_to_guides/setup/set_up_resource_tags)
  - [Create a tag](./how_to_guides/setup/set_up_resource_tags#create-a-tag)
  - [Assign a tag to a resource](./how_to_guides/setup/set_up_resource_tags#assign-a-tag-to-a-resource)
  - [Delete a tag](./how_to_guides/setup/set_up_resource_tags#delete-a-tag)
  - [Filter resources by tags](./how_to_guides/setup/set_up_resource_tags#filter-resources-by-tags)

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
- [Compare traces](./how_to_guides/tracing/compare_traces)
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
  - [Trace without setting environment variables](./how_to_guides/tracing/trace_with_langchain#trace-without-setting-environment-variables)
  - [Distributed tracing with LangChain (Python)](./how_to_guides/tracing/trace_with_langchain#distributed-tracing-with-langchain-python)
  - [Interoperability between LangChain (Python) and LangSmith SDK](./how_to_guides/tracing/trace_with_langchain#interoperability-between-langchain-python-and-langsmith-sdk)
  - [Interoperability between LangChain.JS and LangSmith SDK](./how_to_guides/tracing/trace_with_langchain#interoperability-between-langchainjs-and-langsmith-sdk)
- [Trace with `LangGraph`](./how_to_guides/tracing/trace_with_langgraph)
  - [Interoperability between LangChain and LangGraph](./how_to_guides/tracing/trace_with_langgraph#with-langchain)
  - [Interoperability between `@traceable`/`traceable` and LangGraph](./how_to_guides/tracing/trace_with_langgraph#without-langchain)
- [Trace with `Instructor` (Python only)](./how_to_guides/tracing/trace_with_instructor)
- [Trace with the Vercel `AI SDK` (JS only)](./how_to_guides/tracing/trace_with_vercel_ai_sdk)
- [Trace without setting environment variables](./how_to_guides/tracing/trace_without_env_vars)
- [Trace using the LangSmith REST API](./how_to_guides/tracing/trace_with_api)
- [Calculate token-based costs for traces](./how_to_guides/tracing/calculate_token_based_costs)
- [Bulk Exporting Traces](./how_to_guides/tracing/data_export)

## Datasets

Manage datasets in LangSmith to evaluate and improve your LLM applications.

- [Manage datasets in the application](./how_to_guides/datasets/manage_datasets_in_application)
  - [Create a new dataset and add examples manually](./how_to_guides/datasets/manage_datasets_in_application#create-a-new-dataset-and-add-examples-manually)
  - [Dataset schema validation](./how_to_guides/datasets/manage_datasets_in_application#dataset-schema-validation)
  - [Add inputs and outputs from traces to datasets](./how_to_guides/datasets/manage_datasets_in_application#add-inputs-and-outputs-from-traces-to-datasets)
  - [Upload a CSV file to create a dataset](./how_to_guides/datasets/manage_datasets_in_application#upload-a-csv-file-to-create-a-dataset)
  - [Generate synthetic examples](./how_to_guides/datasets/manage_datasets_in_application#generate-synthetic-examples)
  - [Export a dataset](./how_to_guides/datasets/manage_datasets_in_application#export-a-dataset)
  - [Create and manage dataset splits](./how_to_guides/datasets/manage_datasets_in_application#create-and-manage-dataset-splits)
- [Manage datasets programmatically](./how_to_guides/datasets/manage_datasets_programmatically)
  - [Create a dataset from list of values](./how_to_guides/datasets/manage_datasets_programmatically#create-a-dataset-from-list-of-values)
  - [Create a dataset from traces](./how_to_guides/datasets/manage_datasets_programmatically#create-a-dataset-from-traces)
  - [Create a dataset from a CSV file](./how_to_guides/datasets/manage_datasets_programmatically#create-a-dataset-from-a-csv-file)
  - [Create a dataset from a pandas DataFrame](./how_to_guides/datasets/manage_datasets_programmatically#create-a-dataset-from-a-pandas-dataframe)
  - [Fetch datasets](./how_to_guides/datasets/manage_datasets_programmatically#fetch-datasets)
  - [Fetch examples](./how_to_guides/datasets/manage_datasets_programmatically#fetch-examples)
  - [Update examples](./how_to_guides/datasets/manage_datasets_programmatically#update-examples)
  - [Bulk update examples](./how_to_guides/datasets/manage_datasets_programmatically#bulk-update-examples)
- [Version datasets](./how_to_guides/datasets/version_datasets)
  - [Create a new version of a dataset](./how_to_guides/datasets/version_datasets#create-a-new-version-of-a-dataset)
  - [Tag a version](./how_to_guides/datasets/version_datasets#tag-a-version)
- [Share or unshare a dataset publicly](./how_to_guides/datasets/share_dataset)
- [Index a dataset for few shot example selection](./how_to_guides/datasets/index_datasets_for_dynamic_few_shot_example_selection)

## Monitoring and automations

Leverage LangSmith's powerful monitoring and automations features to make sense of your production data.

- [Filter traces in the application](./how_to_guides/monitoring/filter_traces_in_application)
  - [Create a filter](./how_to_guides/monitoring/filter_traces_in_application#create-a-filter)
  - [Filter for intermediate runs (spans)](./how_to_guides/monitoring/filter_traces_in_application#filter-for-intermediate-runs-spans)
  - [Advanced: filter for intermediate runs (spans) on properties of the root](./how_to_guides/monitoring/filter_traces_in_application#advanced-filter-for-intermediate-runs-spans-on-properties-of-the-root)
  - [Advanced: filter for runs (spans) whose child runs have some attribute](./how_to_guides/monitoring/filter_traces_in_application#advanced-filter-for-runs-spans-whose-child-runs-have-some-attribute)
  - [Filter based on inputs and outputs](./how_to_guides/monitoring/filter_traces_in_application#filter-based-on-inputs-and-outputs)
  - [Filter based on input / output key-value pairs](./how_to_guides/monitoring/filter_traces_in_application#filter-based-on-input--output-key-value-pairs)
  - [Copy the filter](./how_to_guides/monitoring/filter_traces_in_application#copy-the-filter)
  - [Manually specify a raw query in LangSmith query language](./how_to_guides/monitoring/filter_traces_in_application#manually-specify-a-raw-query-in-langsmith-query-language)
  - [Use an AI Query to auto-generate a query](./how_to_guides/monitoring/filter_traces_in_application#use-an-ai-query-to-auto-generate-a-query)
- [Use monitoring charts](./how_to_guides/monitoring/use_monitoring_charts)
  - [Change the time period](./how_to_guides/monitoring/use_monitoring_charts#change-the-time-period)
  - [Slice data by metadata or tag](./how_to_guides/monitoring/use_monitoring_charts#slice-data-by-metadata-or-tag)
  - [Drill down into specific subsets](./how_to_guides/monitoring/use_monitoring_charts#drill-down-into-specific-subsets)
- [Create dashboards](./how_to_guides/monitoring/dashboards)
  - [Creating a new dashboard](./how_to_guides/monitoring/dashboards#creating-a-new-dashboard)
  - [Adding charts to your dashboard](./how_to_guides/monitoring/dashboards#adding-charts-to-your-dashboard)
  - [Filtering traces in your chart](./how_to_guides/monitoring/dashboards#filtering-traces-in-your-chart)
  - [Comparing data within a chart](./how_to_guides/monitoring/dashboards#comparing-data-within-a-chart)
  - [Chart display options](./how_to_guides/monitoring/dashboards#chart-display-options)
  - [Saving and managing charts](./how_to_guides/monitoring/dashboards#saving-and-managing-charts)
  - [View a chart in full screen](./how_to_guides/monitoring/dashboards#view-a-chart-in-full-screen)
  - [User journeys](./how_to_guides/monitoring/dashboards#user-journeys)
- [Set up automation rules](./how_to_guides/monitoring/rules)
  - [Create a rule](./how_to_guides/monitoring/rules#create-a-rule)
  - [View logs for your automations](./how_to_guides/monitoring/rules#view-logs-for-your-automations)
- [Set up online evaluations](./how_to_guides/monitoring/online_evaluations)
  - [Configure online evaluations](./how_to_guides/monitoring/online_evaluations#configure-online-evaluations)
  - [Set API keys](./how_to_guides/monitoring/online_evaluations#set-api-keys)
- [Set up webhook notifications for rules](./how_to_guides/monitoring/webhooks)
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
- [Manage prompts programmatically](./how_to_guides/prompts/manage_prompts_programatically)
  - [Configure environment variables](./how_to_guides/prompts/manage_prompts_programatically#configure_environment_variables)
  - [Push a prompt](./how_to_guides/prompts/manage_prompts_programatically#push_a_prompt)
  - [Pull a prompt](./how_to_guides/prompts/manage_prompts_programatically#pull_a_prompt)
  - [Use a prompt without LangChain](./how_to_guides/prompts/manage_prompts_programatically#use_a_prompt_without_langchain)
  - [List, delete, and like prompts](./how_to_guides/prompts/manage_prompts_programatically#list_delete_and_like_prompts)
- [LangChain Hub](./how_to_guides/prompts/langchain_hub)

## Playground

Quickly iterate on prompts and models in the LangSmith Playground.

- [Use custom TLS certificates](./how_to_guides/playground/custom_tls_certificates)
- [Use a custom model](./how_to_guides/playground/custom_endpoint)
- [Save settings configuration](./how_to_guides/playground/save_model_configuration)
