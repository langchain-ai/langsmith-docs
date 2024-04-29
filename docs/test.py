from langsmith import Client

example_inputs = [
    ("What is the largest mammal?", "The blue whale"),
    ("What do mammals and birds have in common?", "They are both warm-blooded"),
    ("What are reptiles known for?", "Having scales"),
    (
        "What's the main characteristic of amphibians?",
        "They live both in water and on land",
    ),
]

client = Client()
dataset_name = "Elementary Animal Questions"

# Storing inputs in a dataset lets us
# run chains and LLMs over a shared set of examples.
dataset = client.create_dataset(
    dataset_name=dataset_name,
    description="Questions and answers about animal phylogenetics.",
)
for input_prompt, output_answer in example_inputs:
    client.create_example(
        inputs={"question": input_prompt},
        outputs={"answer": output_answer},
        metadata={"source": "Wikipedia"},
        dataset_id=dataset.id,
    )