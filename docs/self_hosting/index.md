---
sidebar_label: Self-hosting
sidebar_position: 0
---

# Self-Hosting LangSmith

Step-by-step guides that cover the installation, configuration, and scaling of your Self-Hosted LangSmith instance.

- [Architectural overview](./self_hosting/architectural_overview): A high-level overview of the LangSmith architecture.
  - [Storage services](./self_hosting/architectural_overview#datastores): The storage services used by LangSmith.
  - [Services](./self_hosting/architectural_overview#services): The services that make up LangSmith.
- [Installation](./self_hosting/installation): How to install LangSmith on your own infrastructure.
  - [Kubernetes](./self_hosting/installation/kubernetes): Deploy LangSmith on Kubernetes.
  - [Docker](./self_hosting/installation/docker): Deploy LangSmith using Docker.
- [Configuration](./self_hosting/configuration): How to configure your self-hosted instance of LangSmith.
  - [SSO with OAuth2.0 and OIDC](./self_hosting/configuration/sso): Configure LangSmith to use OAuth2.0 and OIDC for SSO.
  - [Connect to an external ClickHouse database](./self_hosting/configuration/external_clickhouse): Configure LangSmith to use an external ClickHouse database.
  - [Connect to an external Postgres database](./self_hosting/configuration/external_postgres): Configure LangSmith to use an external Postgres database.
  - [Connect to an external Redis instance](./self_hosting/configuration/external_redis): Configure LangSmith to use an external Redis instance.
  - [Email/password a.k.a. basic auth (beta)](./self_hosting/configuration/basic_auth): Configure LangSmith to use email/password authentication.
  - [Blob storage](./self_hosting/configuration/blob_storage): Configure LangSmith to use blob storage.
  - [TTLs](./self_hosting/configuration/ttl): Configure LangSmith to use TTLs.
- [Usage](./self_hosting/usage): How to use your self-hosted instance of LangSmith.
- [Organization Charts](./self_hosting/organization_charts): View trace counts for your organization and workspaces.
- [Upgrades](./self_hosting/upgrades): How to upgrade your self-hosted instance of LangSmith.
- [Egress for Subscription Metrics and Operational Metadata](./self_hosting/egress): Egress requirements for Subscription Metrics and Operational Metadata.
- [Release notes](./self_hosting/release_notes): The latest release notes for LangSmith.
- - [Week of August 26, 2024 - LangSmith v0.7](./self_hosting/release_notes#week-of-august-26-2024---langsmith-v07): Release notes for version 0.7 of LangSmith.
  - [Week of June 17, 2024 - LangSmith v0.6](./self_hosting/release_notes#week-of-june-17-2024---langsmith-v05): Release notes for version 0.6 of LangSmith.
  - [Week of May 13, 2024 - LangSmith v0.5](./self_hosting/release_notes#week-of-may-13-2024---langsmith-v05): Release notes for version 0.5 of LangSmith.
  - [Week of March 25, 2024 - LangSmith v0.4](./self_hosting/release_notes#week-of-march-25-2024---langsmith-v04): Release notes for version 0.4 of LangSmith.
  - [Week of Februrary 21, 2024 - LangSmith v0.3](./self_hosting/release_notes#week-of-february-21-2024---langsmith-v03): Release notes for version 0.3 of LangSmith.
  - [Week of January 29, 2024 - LangSmith v0.2](./self_hosting/release_notes#week-of-january-29-2024---langsmith-v02): Release notes for version 0.2 of LangSmith.
- [FAQ](./self_hosting/faq): Frequently asked questions about LangSmith.
- [Troubleshooting](./self_hosting/troubleshooting): Troubleshooting common issues with your Self-Hosted LangSmith instance.
- [Observability](./self_hosting/observability): How to access telemetry data for your self-hosted LangSmith instance.
  - [Export LangSmith telemetry to your backend](./self_hosting/observability/export_backend): How to export telemetry data from LangSmith to your observability backend.
