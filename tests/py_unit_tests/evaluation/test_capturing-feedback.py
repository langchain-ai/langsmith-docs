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
    with callbacks.collect_runs() as cb:
        for tok in chain.stream({"input": "Hi, I'm Clara"}):
            print(tok, end="", flush=True)
        run_id = cb.traced_runs[0].id
    # ... User copies the generated response
    client.create_feedback(run_id, "did_copy", score=True)
    # ... User clicks a thumbs up button
    client.create_feedback(run_id, "thumbs_up", score=True)
    # You can also add the expected output and comments, for human-in-the-loop evaluation
    client.create_feedback(
        run_id, 
        "manual_review",
        correction={"output": "Hello, Clara!"},
        comment="The output should have been more concise and enthusiastic."
    )
    
