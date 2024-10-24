# Observability how-to guides

Step-by-step guides that cover key tasks and operations for adding observability to your LLM applications with LangSmith.

## Tracing configuration

Set up LangSmith tracing to get visibility into your production applications.

### Basic configuration

- [Set your tracing project](./how_to_guides/tracing/log_traces_to_project)
- [Enable or disable tracing](./how_to_guides/tracing/toggle_tracing)
- [Trace any Python or JS Code](./how_to_guides/tracing/annotate_code)
- [Trace using the LangSmith REST API](./how_to_guides/tracing/trace_with_api)

### Trace natively supported libraries

- [Trace with `LangChain`](./how_to_guides/tracing/trace_with_langchain)
- [Trace with `LangGraph`](./how_to_guides/tracing/trace_with_langgraph)
- [Trace the OpenAI API client](./how_to_guides/tracing/annotate_code#wrap-the-openai-client)
- [Trace with `Instructor` (Python only)](./how_to_guides/tracing/trace_with_instructor)
- [Trace with the Vercel `AI SDK` (JS only)](./how_to_guides/tracing/trace_with_vercel_ai_sdk)

### Advanced configuration

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

## Tracing projects UI & API

View and interact with your traces to debug your applications.

- [Filter traces in a project](./how_to_guides/monitoring/filter_traces_in_application)
- [Save a filter for your project](./how_to_guides/monitoring/filter_traces_in_application#saved-filters)
- [Export traces using the SDK (low volume)](./how_to_guides/tracing/export_traces)
- [Bulk exporting traces (high volume)](./how_to_guides/tracing/data_export)
- [Share or unshare a trace publicly](./how_to_guides/tracing/share_trace)
- [Compare traces](./how_to_guides/tracing/compare_traces)
- [View threads](./how_to_guides/monitoring/threads#view-threads)

## Dashboards

Use LangSmith custom and built-in dashboards to gain insight into your production systems.

- [Create and use custom dashboards](./how_to_guides/monitoring/dashboards)
- [Use built-in monitoring dashboards](./how_to_guides/monitoring/use_monitoring_charts)

## Automations

Leverage LangSmith's powerful monitoring and automations features to make sense of your production data.

- [Set up automation rules](./how_to_guides/monitoring/rules)
- [Set up webhook notifications for rules](./how_to_guides/monitoring/webhooks)
