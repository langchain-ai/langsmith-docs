# Evaluation how-to guides

## Evaluation SDK & API

Write evaluations to test and improve your application.

- [Evaluate an LLM application in the SDK](./how_to_guides/evaluation/evaluate_llm_application)
- [Define a custom evaluator](./how_to_guides/evaluation/evaluate_llm_application#use-custom-evaluators)
- [Evaluate on intermediate steps](./how_to_guides/evaluation/evaluate_on_intermediate_steps)
- [Use LangChain off-the-shelf evaluators (Python only)](./how_to_guides/evaluation/use_langchain_off_the_shelf_evaluators)
- [Evaluate an existing experiment](./how_to_guides/evaluation/evaluate_existing_experiment)
- [Run a pairwise evaluation](./how_to_guides/evaluation/evaluate_pairwise)
- [Run evals using the API only](./how_to_guides/evaluation/run_evals_api_only)

## Unit testing
Run assertions and expectations designed to quickly identify obvious bugs and regressions in your AI system, natively in your favorite testing library.

- [Unit test LLM applications (Python only)](./how_to_guides/evaluation/unit_testing)

## Auto-evaluation

Set up auto-evaluators that LangSmith will automatically run on your experiments.

- [Set up an Auto-Evaluator to run on all experiments](./how_to_guides/evaluation/bind_evaluator_to_dataset)
- [Create few-shot evaluators](./how_to_guides/evaluation/create_few_shot_evaluators)

## Online evaluation

Set up evaluations to run on incoming traces to understand your application's behavior in production.

- [Set up online evaluations](./how_to_guides/monitoring/online_evaluations)
- [Create few-shot evaluators](./how_to_guides/evaluation/create_few_shot_evaluators)

## Experiments

Use the experiments UI & API to understand your evaluations.

- [Run an evaluation in the prompt playground](./how_to_guides/evaluation/run_evaluation_from_prompt_playground)
- [Compare experiments with the comparison view](./how_to_guides/evaluation/compare_experiment_results)
- [Filter experiments](./how_to_guides/evaluation/filter_experiments_ui)
- [View pairwise experiments](./how_to_guides/evaluation/evaluate_pairwise#view-pairwise-experiments)
- [Fetch experiment results in the SDK](./how_to_guides/evaluation/fetch_perf_metrics_experiment)
- [Upload experiments run outside of LangSmith with the REST API](./how_to_guides/evaluation/upload_existing_experiments)

## Datasets

Manage datasets in LangSmith used by your offline evaluations (as well as other downstream applications).

- [Manage datasets in the application](./how_to_guides/datasets/manage_datasets_in_application)
- [Manage datasets programmatically](./how_to_guides/datasets/manage_datasets_programmatically)
- [Version datasets](./how_to_guides/datasets/version_datasets)
- [Share or unshare a dataset publicly](./how_to_guides/datasets/share_dataset)

## Annotation Queues and Human Feedback

Collect feedback from subject matter experts and users to improve your LLM applications.

- [Use annotation queues](./how_to_guides/human_feedback/annotation_queues)
- [Capture user feedback from your application to traces](./how_to_guides/human_feedback/attach_user_feedback)
- [Set up a new feedback criteria](./how_to_guides/human_feedback/set_up_feedback_criteria)
- [Annotate traces inline](./how_to_guides/human_feedback/annotate_traces_inline)
- [Audit and correct evaluator scores](./how_to_guides/evaluation/audit_evaluator_scores)
