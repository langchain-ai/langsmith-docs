import pytest
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

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
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    
    chat_model = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful AI."),
      ("human", "{input}")
    ])
    chain = prompt | chat_model
    
    chain.invoke({"input": "What is the meaning of life?"}, {"metadata": {"my_key": "My Value"}})

@pytest.mark.asyncio
async def test_code_block_3():
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import PromptTemplate
    
    llm = ChatOpenAI(temperature=0, tags=["my-llm-tag"])
    prompt = PromptTemplate.from_template("Say {input}")
    chain = (prompt | llm).with_config({"tags": ["my-bash-tag", "another-tag"]})
    
    chain.invoke({"input": "Hello, World!"}, {"tags": ["shared-tags"]})

@pytest.mark.asyncio
async def test_code_block_4():
    from langchain_core.messages import AIMessage, HumanMessage
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_openai import ChatOpenAI
    
    chain = (
        ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful AI."),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{message}"),
            ]
        )
        | ChatOpenAI(model="gpt-3.5-turbo")
        | StrOutputParser()
    )
    
    conversation_id = "101e8e66-9c68-4858-a1b4-3b0e3c51a933"
    
    chat_history = []
    message = HumanMessage(content="Hi there")
    response = ""
    for chunk in chain.stream(
        {
            "message": message,
            "chat_history": chat_history,
            "conversation_id": conversation_id,
        }
    ):
        print(chunk, end="")
        response += chunk
    print()
    chat_history.extend(
        [
            message,
            AIMessage(content=response),
        ]
    )
    
    # ... Next message comes in
    next_message = HumanMessage(content="I don't need much assistance, actually.")
    for chunk in chain.stream(
        {
            "message": next_message,
            "chat_history": chat_history,
            "conversation_id": conversation_id,
        }
    ):
        print(chunk, end="")
        response += chunk
    

@pytest.mark.asyncio
async def test_code_block_5():
    configured_chain = chain.with_config({"run_name": "MyCustomChain"})
    configured_chain.invoke({"query": "What is the meaning of life?"})

@pytest.mark.asyncio
async def test_code_block_6():
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    chat_model = ChatOpenAI()
    prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful AI."),
      ("human", "{input}")
    ])
    chain = prompt | chat_model
    
    chain.invoke({"input": "What is the meaning of life?"}, {"metadata": {"variant": "abc123"}})

@pytest.mark.asyncio
async def test_code_block_7():
    from langchain.callbacks import LangChainTracer
    from langchain_openai import ChatOpenAI
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
    from langchain_openai import ChatOpenAI
    from langchain.callbacks.tracers.langchain import wait_for_all_tracers
    
    llm = ChatOpenAI()
    try:
        llm.invoke("Hello, World!")
    finally:
        # highlight-next-line
        wait_for_all_tracers()
    

@pytest.mark.asyncio
async def test_code_block_9():
    from langchain_core.tracers.context import tracing_v2_enabled
    
    with tracing_v2_enabled(project_name="My Project"):
        chain.invoke({"query": "How many people live in canada as of 2023?"})
