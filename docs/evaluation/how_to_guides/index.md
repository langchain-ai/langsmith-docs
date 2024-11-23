# Evaluation how-to guides

These guides answer “How do I….?” format questions.
They are goal-oriented and concrete, and are meant to help you complete a specific task.
For conceptual explanations see the [Conceptual guide](./concepts).
For end-to-end walkthroughs see [Tutorials](./tutorials).
For comprehensive descriptions of every class and function see the [API reference](https://langsmith-sdk.readthedocs.io/en/latest/evaluation.html).

## Offline evaluation

Evaluate and improve your application before deploying it.

### Run an evaluation

- [Run an evaluation](./how_to_guides/evaluation/evaluate_llm_application)
- [Run an evaluation asynchronously](./how_to_guides/evaluation/async)
- [Run an evaluation comparing two experiments](./how_to_guides/evaluation/evaluate_pairwise)
- [Evaluate a `langchain` runnable](./how_to_guides/evaluation/langchain_runnable)
- [Evaluate a `langgraph` graph](./how_to_guides/evaluation/langgraph)
- [Run an evaluation of an existing experiment](./how_to_guides/evaluation/evaluate_existing_experiment)
- [Run an evaluation via the REST API](./how_to_guides/evaluation/run_evals_api_only)
- [Run an evaluation from the UI](./how_to_guides/evaluation/run_evaluation_from_prompt_playground)

### Define an evaluator

- [Define a custom evaluator](./how_to_guides/evaluation/custom_evaluator)
- [Define an LLM-as-a-judge evaluator](./how_to_guides/evaluation/llm_as_judge)
- [Define a pairwise evaluator](./how_to_guides/evaluation/evaluate_pairwise)
- [Define a summary evaluator](./how_to_guides/evaluation/summary)
- [Use an off-the-shelf evaluator via the SDK (Python only)](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators)
- [Evaluate intermediate steps](./how_to_guides/evaluation/evaluate_on_intermediate_steps)
- [Return multiple metrics in one evaluator](./how_to_guides/evaluation/multiple_scores)
- [Return categorical vs numerical metrics](./how_to_guides/evaluation/metric_type)
- [Check your evaluator setup](./how_to_guides/evaluation/check_evaluator)

### Configure the evaluation data

- [Evaluate on a split / filtered view of a dataset](./how_to_guides/evaluation/dataset_subset)
- [Evaluate on a specific dataset version](./how_to_guides/evaluation/dataset_version)

### Configure an evaluation job

- [Evaluate with repetitions](./how_to_guides/evaluation/repetition)
- [Handle model rate limits](./how_to_guides/evaluation/rate_limiting)

## Unit testing

Unit test your system to identify bugs and regressions.

- [Unit test applications (Python only)](./how_to_guides/evaluation/unit_testing)

## Online evaluation

Evaluate and monitor your system's live performance on production data.

- [Set up an online evaluator](../../observability/how_to_guides/monitoring/online_evaluations)
- [Create a few-shot evaluator](./how_to_guides/evaluation/create_few_shot_evaluators)

## Automatic evaluation

Set up evaluators that automatically run for all experiments against a dataset.

- [Set up an auto-evaluator](./how_to_guides/evaluation/bind_evaluator_to_dataset)
- [Create a few-shot evaluator](./how_to_guides/evaluation/create_few_shot_evaluators)

## Analyzing experiment results

Use the UI & API to understand your experiment results.

- [Compare experiments with the comparison view](./how_to_guides/evaluation/compare_experiment_results)
- [Filter experiments](./how_to_guides/evaluation/filter_experiments_ui)
- [View pairwise experiments](./how_to_guides/evaluation/evaluate_pairwise#view-pairwise-experiments)
- [Fetch experiment results in the SDK](./how_to_guides/evaluation/fetch_perf_metrics_experiment)
- [Upload experiments run outside of LangSmith with the REST API](./how_to_guides/evaluation/upload_existing_experiments)

## Dataset management

Manage datasets in LangSmith used by your evaluations.

- [Manage datasets from the UI](./how_to_guides/datasets/manage_datasets_in_application)
- [Manage datasets programmatically](./how_to_guides/datasets/manage_datasets_programmatically)
- [Version datasets](./how_to_guides/datasets/version_datasets)
- [Share or unshare a dataset publicly](./how_to_guides/datasets/share_dataset)
- [Export filtered traces from an experiment to a dataset](./how_to_guides/datasets/export_filtered_traces_to_dataset)

## Annotation queues and human feedback

Collect feedback from subject matter experts and users to improve your applications.

- [Use annotation queues](./how_to_guides/human_feedback/annotation_queues)
- [Capture user feedback from your application to traces](./how_to_guides/human_feedback/attach_user_feedback)
- [Set up a new feedback criteria](./how_to_guides/human_feedback/set_up_feedback_criteria)
- [Annotate traces inline](./how_to_guides/human_feedback/annotate_traces_inline)
- [Audit and correct evaluator scores](./how_to_guides/evaluation/audit_evaluator_scores)
