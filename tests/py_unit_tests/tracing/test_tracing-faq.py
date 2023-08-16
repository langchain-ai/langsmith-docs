import pytest
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

chain = ChatPromptTemplate.from_messages([("human", "{query}")]) | ChatOpenAI()

@pytest.mark.asyncio
async def test_code_block_0():
    from langchain.chat_models import ChatAnthropic
    llm = ChatAnthropic()
    
    llm.invoke("Hello, World!")

@pytest.mark.asyncio
async def test_code_block_1():
    from langchain.callbacks.tracers import LangChainTracer
    tracer = LangChainTracer(project_name="My Project")
    chain.invoke({"query": "How many people live in canada as of 2023?"}, config={"callbacks": [tracer]})
    

@pytest.mark.asyncio
async def test_code_block_2():
    from langchain.chains import LLMChain
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import PromptTemplate
    
    llm = ChatOpenAI(temperature=0, tags=["my-llm-tag"])
    prompt = PromptTemplate.from_template("Say {input}")
    chain = LLMChain(llm=llm, prompt=prompt, tags=["my-bash-tag", "another-tag"])
    
    chain("Hello, World!", tags=["shared-tags"])
    

@pytest.mark.asyncio
async def test_code_block_3():
    from langchain.chat_models import ChatOpenAI
    from langchain.chains import LLMChain
    
    chat_model = ChatOpenAI()
    chain = LLMChain.from_string(llm=chat_model, template="What's the answer to {input}?")
    
    chain({"input": "What is the meaning of life?"}, metadata={"my_key": "My Value"})

@pytest.mark.asyncio
async def test_code_block_4():
    from langchain.chat_models import ChatOpenAI
    from langchain.chains import LLMChain
    
    chat_model = ChatOpenAI()
    chain = LLMChain.from_string(llm=chat_model, template="What's the answer to {input}?")
    
    chain({"input": "What is the meaning of life?"}, metadata={"variant": "abc123"})

@pytest.mark.asyncio
async def test_code_block_5():
    from langsmith import Client
    
    client = Client()
    runs = list(client.list_runs(
        filter='has(metadata, \'{"variant": "abc123"}\')',
    ))

@pytest.mark.asyncio
async def test_code_block_6():
    from langchain.callbacks.manager import (
        trace_as_chain_group, 
        atrace_as_chain_group,
    )
    
    with trace_as_chain_group("my_group_name") as group_manager:
        """Pass the group_manager as a callback to group all runs
        within this context"""
    
    # Or for async code
    async with atrace_as_chain_group("my_group_name") as async_group_manager:
        """Async applications are better suited with the async callback manager"""
    
    # Example usage:
    from langchain.chat_models import ChatOpenAI
    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate
    
    llm = ChatOpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["question"],
        template="What is the answer to {question}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    with trace_as_chain_group("my_group") as group_manager:
        chain.invoke({"question": "What is your name?"}, config={"callbacks": group_manager})
        chain.invoke({"question": "What is your quest?"}, config={"callbacks": group_manager})
        chain.invoke({"question": "What is your favorite color?"}, config={"callbacks": group_manager})

@pytest.mark.asyncio
async def test_code_block_7():
    from langchain.chat_models import ChatOpenAI
    from langchain.chains import LLMChain
    
    chain = LLMChain.from_string(ChatOpenAI(), "Say hi to {name}")
    def main():
        response = chain("Clara", include_run_info=True)
        run_id = response["__run"].run_id
        print(run_id)
    main()
    

@pytest.mark.asyncio
async def test_code_block_8():
    from langchain.callbacks import LangChainTracer
    from langchain.chat_models import ChatOpenAI
    from langsmith import Client
    
    callbacks = [
      LangChainTracer(
        project_name="YOUR_PROJECT_NAME_HERE",
        client=Client(
          api_url="https://api.smith.langchain.com",
          api_key="YOUR_API_KEY_HERE"
        )
      )
    ]
    
    llm = ChatOpenAI(callbacks=callbacks)
    llm.invoke("Hello, world!")
    

@pytest.mark.asyncio
async def test_code_block_9():
    from langchain.chat_models import ChatOpenAI
    from langchain.callbacks.tracers.langchain import wait_for_all_tracers
    
    llm = ChatOpenAI()
    try:
        llm.invoke("Hello, World!")
    finally:
        # highlight-next-line
        wait_for_all_tracers()
    

@pytest.mark.asyncio
async def test_code_block_10():
    from langchain.callbacks import tracing_v2_enabled
    
    with tracing_v2_enabled(project_name="My Project"):
        chain.invoke({"query": "How many people live in canada as of 2023?"})

@pytest.mark.asyncio
async def test_code_block_11():
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    
    chat_model = ChatOpenAI()
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a cat"),
            ("human", "Hi"),
        ]
    )
    res = chat_model.generate(messages=[prompt.format_messages()])
    res.run[0].run_id

@pytest.mark.asyncio
async def test_code_block_12():
    from langchain.llms import OpenAI
    
    openai = OpenAI()
    res = openai.generate(["You are a good bot"])
    print(res.run[0].run_id)
