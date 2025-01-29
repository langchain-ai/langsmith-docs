# Evaluation how-to guides

These guides answer “How do I…?” format questions.
They are goal-oriented and concrete, and are meant to help you complete a specific task.
For conceptual explanations see the [Conceptual guide](./concepts).
For end-to-end walkthroughs see [Tutorials](./tutorials).
For comprehensive descriptions of every class and function see the [API reference](https://langsmith-sdk.readthedocs.io/en/latest/evaluation.html).

## Offline evaluation

Evaluate and improve your application before deploying it.

### Run an evaluation

- [Run an evaluation with the SDK](./how_to_guides/evaluate_llm_application)
- [Run an evaluation asynchronously](./how_to_guides/async)
- [Run an evaluation comparing two experiments](./how_to_guides/evaluate_pairwise)
- [Evaluate a `langchain` runnable](./how_to_guides/langchain_runnable)
- [Evaluate a `langgraph` graph](./how_to_guides/langgraph)
- [Evaluate an existing experiment (Python only)](./how_to_guides/evaluate_existing_experiment)
- [Run an evaluation from the UI](./how_to_guides/run_evaluation_from_prompt_playground)
- [Run an evaluation via the REST API](./how_to_guides/run_evals_api_only)
- [Run an evaluation with large file inputs](./how_to_guides/evaluate_with_attachments)

### Define an evaluator

- [Define a custom evaluator](./how_to_guides/custom_evaluator)
- [Define an LLM-as-a-judge evaluator](./how_to_guides/llm_as_judge)
- [Define a pairwise evaluator](./how_to_guides/evaluate_pairwise)
- [Define a summary evaluator](./how_to_guides/summary)
- [Use an off-the-shelf evaluator via the SDK (Python only)](./how_to_guides/use_langchain_off_the_shelf_evaluators)
- [Evaluate an application's intermediate steps](./how_to_guides/evaluate_on_intermediate_steps)
- [Return multiple metrics in one evaluator](./how_to_guides/multiple_scores)
- [Return categorical vs numerical metrics](./how_to_guides/metric_type)

### Configure the evaluation data

- [Evaluate on a split / filtered view of a dataset](./how_to_guides/dataset_subset)
- [Evaluate on a specific dataset version](./how_to_guides/dataset_version)

### Configure an evaluation job

- [Evaluate with repetitions](./how_to_guides/repetition)
- [Handle model rate limits](./how_to_guides/rate_limiting)
- [Print detailed logs (Python only)](../../observability/how_to_guides/tracing/output_detailed_logs)
- [Run an evaluation locally (beta, Python only)](./how_to_guides/local)

## Testing integrations

Run evals using your favorite testing tools:

- [Run evals with pytest (beta)](./how_to_guides/pytest)
- [Run evals with Vitest/Jest (beta)](./how_to_guides/vitest_jest)

## Online evaluation

Evaluate and monitor your system's live performance on production data.

- [Set up an LLM-as-judge online evaluator](../../observability/how_to_guides/monitoring/online_evaluations#configure-llm-as-judge-evaluators)
- [Set up a custom code online evaluator](../../observability/how_to_guides/monitoring/online_evaluations#configure-custom-code-evaluators)
- [Create a few-shot evaluator](./how_to_guides/create_few_shot_evaluators)

## Automatic evaluation

Set up evaluators that automatically run for all experiments against a dataset.

- [Set up an auto-evaluator](./how_to_guides/bind_evaluator_to_dataset)
- [Create a few-shot evaluator](./how_to_guides/create_few_shot_evaluators)

## Analyzing experiment results

Use the UI & API to understand your experiment results.

- [Compare experiments with the comparison view](./how_to_guides/compare_experiment_results)
- [Filter experiments](./how_to_guides/filter_experiments_ui)
- [View pairwise experiments](./how_to_guides/evaluate_pairwise#view-pairwise-experiments)
- [Fetch experiment results in the SDK](./how_to_guides/fetch_perf_metrics_experiment)
- [Upload experiments run outside of LangSmith with the REST API](./how_to_guides/upload_existing_experiments)

## Dataset management

Manage datasets in LangSmith used by your evaluations.

- [Create a dataset from the UI](./how_to_guides/manage_datasets_in_application#set-up-your-dataset)
- [Export a dataset from the UI](./how_to_guides/manage_datasets_in_application#export-a-dataset)
- [Create a dataset split from the UI](./how_to_guides/manage_datasets_in_application#create-and-manage-dataset-splits)
- [Filter examples from the UI](./how_to_guides/manage_datasets_in_application#filter-examples)
- [Create a dataset with the SDK](./how_to_guides/manage_datasets_programmatically#create-a-dataset)
- [Fetch a dataset with the SDK](./how_to_guides/manage_datasets_programmatically#fetch-datasets)
- [Update a dataset with the SDK](./how_to_guides/manage_datasets_programmatically#update-examples)
- [Version a dataset](./how_to_guides/version_datasets)
- [Share/unshare a dataset publicly](./how_to_guides/share_dataset)
- [Export filtered traces from an experiment to a dataset](./how_to_guides/export_filtered_traces_to_dataset)

## Annotation queues and human feedback

Collect feedback from subject matter experts and users to improve your applications.

- [Use annotation queues](./how_to_guides/annotation_queues)
- [Capture user feedback from your application to traces](./how_to_guides/attach_user_feedback)
- [Set up a new feedback criteria](./how_to_guides/set_up_feedback_criteria)
- [Annotate traces inline](./how_to_guides/annotate_traces_inline)
- [Audit and correct evaluator scores](./how_to_guides/audit_evaluator_scores)
