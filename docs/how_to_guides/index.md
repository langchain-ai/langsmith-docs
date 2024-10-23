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
<<<<<<< HEAD

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
- [Prompt tags](./how_to_guides/prompts/prompt_tags)
  - [Create a tag](./how_to_guides/prompts/prompt_tags#create_a_tag)
  - [Move a tag](./how_to_guides/prompts/prompt_tags#move_a_tag)
  - [Delete a tag](./how_to_guides/prompts/prompt_tags#delete_a_tag)
  - [Using tags in code](./how_to_guides/prompts/prompt_tags#using_tags_in_code)
  - [Common use cases](./how_to_guides/prompts/prompt_tags#common_use_cases)
- [LangChain Hub](./how_to_guides/prompts/langchain_hub)

## Playground

Quickly iterate on prompts and models in the LangSmith Playground.

- [Use custom TLS certificates](./how_to_guides/playground/custom_tls_certificates)
- [Use a custom model](./how_to_guides/playground/custom_endpoint)
- [Save settings configuration](./how_to_guides/playground/save_model_configuration)
=======
>>>>>>> e685220 (prompt engineering complete)
