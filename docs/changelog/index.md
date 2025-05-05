---
sidebar_position: 1
---

import { RegionalUrl } from "@site/src/components/RegionalUrls";

# Changelog

What's new in LangSmith — new features, enhancements, and bugs fixed — organized by release date and release version.

### 2025‑04‑28 - v0.10.31

#### LangSmith

- Directly [add example metadata](/evaluation/how_to_guides/manage_datasets_in_application#edit-example-metadata) when editing examples in the UI
- Prompt previews now render when [running an experiment in the UI](/evaluation/how_to_guides/run_evaluation_from_prompt_playground) or configuring an [online evaluator](/observability/how_to_guides/online_evaluations) with f-string prompts
- [Group by](/evaluation/how_to_guides/analyze_single_experiment#group-results-by-metadata) [dataset split](/evaluation/how_to_guides/manage_datasets_in_application#create-and-manage-dataset-splits) when analyzing experiment results

#### LangGraph Studio

- Improved layout when expanding [subgraphs](https://langchain-ai.github.io/langgraph/how-tos/subgraph/?h=subgraph)
- Render errors and [interrupts](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/?h=#interrupt) correctly in Studio Chat UI
