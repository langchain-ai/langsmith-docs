---
sidebar_position: 1
---

import { RegionalUrl } from "@site/src/components/RegionalUrls";

# Changelog

What's new in LangSmith — new features, enhancements, and bugs fixed — organized by release date and release version. Looking for just the major product updates & highlights? [Check out our website feed.](https://changelog.langchain.com/?categories=cat_FvjDMlZoyaKkX)

## 2025‑05‑19

#### LangSmith v0.10.60

- Updated usage charts to show month-over-month usage by workspace for SaaS customers
- Added automatic cost tracking for OpenAI's `o3` and `o4-mini` models
- Added ability to sync prompts tracked in LangSmith with external systems using [webhook notifications on prompt commit](prompt_engineering/how_to_guides/trigger_webhook)

## 2025‑05‑12

#### LangSmith v0.10.52

- [Agent Observability: Gain Insights into Tool Calls & Run Stats](https://changelog.langchain.com/announcements/agent-observability-gain-insights-into-tool-calls-run-stats)
- Customize the number of groups when using [group by](/observability/how_to_guides/dashboards#split-the-data) in custom charts

## 2025‑05‑05

#### LangSmith v0.10.40

- Added ability to re-sync [few shot dataset](/evaluation/how_to_guides/index_datasets_for_dynamic_few_shot_example_selection) indices via the [Python SDK's `sync_indexed_dataset()` method](https://docs.smith.langchain.com/reference/python/async_client/langsmith.async_client.AsyncClient#langsmith.async_client.AsyncClient.sync_indexed_dataset)
- Added up/down hotkey navigation for output traces when [viewing experiment results](/evaluation/how_to_guides/analyze_single_experiment#view-experiment-results)
- Added ability to run `evaluate()` on existing experiments to add more feedback to the experiment
- [Improved multimodal support](https://changelog.langchain.com/announcements/multimodal-support-in-langsmith)
- Improved configuration for [few-shot examples](/evaluation/how_to_guides/create_few_shot_evaluators) when creating [LLM-as-a-judge evaluators](/evaluation/how_to_guides/llm_as_judge)

## 2025‑04‑28

#### LangSmith v0.10.31

- Directly [add example metadata](/evaluation/how_to_guides/manage_datasets_in_application#edit-example-metadata) when editing examples in the UI
- Prompt previews now render when [running an experiment in the UI](/evaluation/how_to_guides/run_evaluation_from_prompt_playground) or configuring an [online evaluator](/observability/how_to_guides/online_evaluations) with f-string prompts
- [Group by](/evaluation/how_to_guides/analyze_single_experiment#group-results-by-metadata) [dataset split](/evaluation/how_to_guides/manage_datasets_in_application#create-and-manage-dataset-splits) when analyzing experiment results
