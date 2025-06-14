---
sidebar_label: Self-Hosted Observability
sidebar_position: 11
description: "Observability guides for LangSmith"
---

# Self-Hosted Observability

This section contains guides for accessing telemetry data for your self-hosted LangSmith deployments. 

:::warning Important
**This section is only applicable for Kubernetes deployments.**
:::

- [Export LangSmith Telemetry](./observability/export_backend): Export logs, metrics and traces to your collector/backend of choice.
- [Install a Collector for LangSmith Telemetry](./observability/langsmith_collector): How to use the LangSmith observability [helm chart](https://github.com/langchain-ai/helm) to deploy an OpenTelemetry Collector and export telemetry to your backend.