# Observability how-to guides

Step-by-step guides that cover key tasks and operations for adding observability to your LLM applications with LangSmith.

## Tracing configuration

Set up LangSmith tracing to get visibility into your production applications.

### Basic configuration

- [Set your tracing project](./how_to_guides/log_traces_to_project)
- [Trace any Python or JS Code](./how_to_guides/annotate_code)
- [Trace using the LangSmith REST API](./how_to_guides/trace_with_api)
- [Trace without environment variables](./how_to_guides/trace_without_env_vars)

### Integrations

- [LangChain OSS libraries](./how_to_guides/trace_with_langchain)
- [LangGraph](./how_to_guides/trace_with_langgraph)
- [OpenAI](./how_to_guides/annotate_code#wrap-the-openai-client)
- [Instructor](./how_to_guides/trace_with_instructor)
- [Vercel AI SDK (JS only)](./how_to_guides/trace_with_vercel_ai_sdk)
- [OpenTelemetry](./how_to_guides/trace_with_opentelemetry)
- [OpenAI Agent SDK (Python only)](./how_to_guides/trace_with_openai_agents_sdk)

### Advanced configuration

- [Configure threads](./how_to_guides/threads)
- [Set a sampling rate for traces](./how_to_guides/sample_traces)
- [Add metadata and tags to traces](./how_to_guides/add_metadata_tags)
- [Implement distributed tracing](./how_to_guides/distributed_tracing)
- [Trace LangChain with OpenTelemetry (Python only)](./how_to_guides/trace_langchain_with_otel)
- [Access the current span within a traced function](./how_to_guides/access_current_span)
- [Log multimodal traces](./how_to_guides/log_multimodal_traces)
- [Log retriever traces](./how_to_guides/log_retriever_trace)
- [Log custom LLM traces / provide custom token counts](./how_to_guides/log_llm_trace)
- [Prevent logging of sensitive data in traces](./how_to_guides/mask_inputs_outputs)
- [Trace generator functions](./how_to_guides/trace_generator_functions)
- [Calculate token-based costs for traces](./how_to_guides/calculate_token_based_costs)
- [Trace JS functions in serverless environments](./how_to_guides/serverless_environments)
- [Troubleshoot trace testing](./how_to_guides/nest_traces)
- [Upload files with traces](./how_to_guides/upload_files_with_traces)
- [Print out logs from the LangSmith SDK (Python Only)](./how_to_guides/output_detailed_logs)
- [Troubleshooting: Missing or Misrouted Traces](./how_to_guides/toubleshooting_variable_caching)

## Tracing projects UI & API

View and interact with your traces to debug your applications.

- [Filter traces in a project](./how_to_guides/filter_traces_in_application)
- [Save a filter for your project](./how_to_guides/filter_traces_in_application#saved-filters)
- [Query / Export traces using the SDK (low volume)](./how_to_guides/export_traces)
- [Bulk exporting traces (high volume)](./how_to_guides/data_export)
- [Share or unshare a trace publicly](./how_to_guides/share_trace)
- [Compare traces](./how_to_guides/compare_traces)
- [View threads](./how_to_guides/threads#view-threads)
- [Set up alerts for your project (Private Beta)](./how_to_guides/alerts)

## Dashboards

Use LangSmith custom and built-in dashboards to gain insight into your production systems.

- [Create and use custom dashboards](./how_to_guides/dashboards)
- [Use built-in monitoring dashboards](./how_to_guides/use_monitoring_charts)

## Automations

Leverage LangSmith's powerful monitoring, automation, and online evaluation features to make sense of your production data.

- [Set up automation rules](./how_to_guides/rules)
- [Set up webhook notifications for rules](./how_to_guides/webhooks)
- [Perform online evaluations](./how_to_guides/online_evaluations)

## Human feedback

- [Log user feedback](../evaluation/how_to_guides/attach_user_feedback)
- [Set up a new feedback criteria](../evaluation/how_to_guides/set_up_feedback_criteria)
- [Annotate traces inline in the UI](../evaluation/how_to_guides/annotate_traces_inline)
