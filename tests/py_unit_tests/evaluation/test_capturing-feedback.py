import pytest
import uuid
from langsmith import Client, schemas
runs = [schemas.Run(
    name="my_run",
    inputs={"prompt": "Hello world!"},
    execution_order=1,
    run_type="llm",
    outputs={"generation": "Hi!"},
    start_time=0,
    id=uuid.uuid4(),
    end_time=100,
)]
client = Client()

@pytest.mark.asyncio
async def test_code_block_0():
    import os
    from langchain import chat_models, prompts, callbacks
    from langchain.schema import output_parser
    from langsmith import Client
    
    chain = (
      prompts.ChatPromptTemplate.from_messages(
        [
          ("system", "You are a conversational bot."),
          ("user", "{input}"),
        ]
      )
      | chat_models.ChatOpenAI()
      | output_parser.StrOutputParser()
    ) 
    client = Client()
    def main():
      with callbacks.collect_runs() as cb:
        for tok in chain.stream({"input": "Hi, I'm Clara"}):
          print(tok, end="", flush=True)
          run_id = cb.traced_runs[0].ids
      # ... User copies the generated response
      client.create_feedback(run_id, "did_copy", score=True)
      # ... User clicks a thumbs up button
      client.create_feedback(run_id, "thumbs_up", score=True)
    

@pytest.mark.asyncio
async def test_code_block_1():
    dataset = client.create_dataset(
      "Thumbs Up Runs",
      description="Runs that received a thumbs up from the user",
    )
    for run in runs:
        client.create_example_from_run(
          run=run,
          dataset_id=dataset.id,
        )
