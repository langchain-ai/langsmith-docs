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
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import PromptTemplate
    
    llm = ChatOpenAI(temperature=0, tags=["my-llm-tag"])
    prompt = PromptTemplate.from_template("Say {input}")
    chain = (prompt | llm).with_config({"tags": ["my-bash-tag", "another-tag"]})
    
    chain.invoke("Hello, World!", {"tags": ["shared-tags"]})

@pytest.mark.asyncio
async def test_code_block_3():
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    
    chat_model = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful AI."),
      ("human", "{input}")
    ])
    chain = prompt | chat_model
    
    chain.invoke({"input": "What is the meaning of life?"}, {"metadata": {"my_key": "My Value"}})

@pytest.mark.asyncio
async def test_code_block_4():
    configured_chain = chain.with_config({"run_name": "MyCustomChain"})
    configured_chain.invoke({"query": "What is the meaning of life?"})

@pytest.mark.asyncio
async def test_code_block_5():
    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    chat_model = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful AI."),
      ("human", "{input}")
    ])
    chain = prompt | chat_model
    
    chain.invoke({"input": "What is the meaning of life?"}, {"metadata": {"variant": "abc123"}})

@pytest.mark.asyncio
async def test_code_block_6():
    from langchain.callbacks.manager import (
        trace_as_chain_group,
        atrace_as_chain_group,
    )
    
    with trace_as_chain_group("my_group_name", inputs={"input": "My Input"}) as group_manager:
        """Pass the group_manager as a callback to group all runs
        within this context"""
    
        # ...
        group_manager.on_chain_end({"output": "Final output"})
    # Or for async code
    async with atrace_as_chain_group("my_group_name", inputs={"input": "My Input"}) as async_group_manager:
        """Async applications are better suited with the async callback manager"""
        # ...
        await async_group_manager.on_chain_end({"output": "Final output"})
    
    # Example usage:
    from langchain.chat_models.anthropic import ChatAnthropic
    from langchain.prompts import ChatPromptTemplate
    
    llm = ChatAnthropic()
    prompt = ChatPromptTemplate.from_messages(
      [
        ("system", "You are a helpful AI."),
        ("human", "{question}")
      ]
    )
    chain = prompt | llm
    
    question = "What is your name?"
    with trace_as_chain_group("my_group", inputs={"question": question}) as group_manager:
        res1 = chain.invoke({"question": question}, config={"callbacks": group_manager})
        res2 = chain.invoke({"question": "What is your quest?"}, config={"callbacks": group_manager})
        group_manager.on_chain_end({"output": res2})

@pytest.mark.asyncio
async def test_code_block_7():
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
    
    llm = ChatOpenAI()
    llm.invoke("Hello, world!", config={"callbacks": callbacks})
    

@pytest.mark.asyncio
async def test_code_block_8():
    from langchain.chat_models import ChatOpenAI
    from langchain.callbacks.tracers.langchain import wait_for_all_tracers
    
    llm = ChatOpenAI()
    try:
        llm.invoke("Hello, World!")
    finally:
        # highlight-next-line
        wait_for_all_tracers()
    

@pytest.mark.asyncio
async def test_code_block_9():
    from langchain.callbacks import tracing_v2_enabled
    
    with tracing_v2_enabled(project_name="My Project"):
        chain.invoke({"query": "How many people live in canada as of 2023?"})
