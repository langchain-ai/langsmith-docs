import pytest
dataset_name = "Rap Battle Dataset"

def test_code_block_0():
    import openai
    from langsmith.wrappers import wrap_openai
    
    openai_client = wrap_openai(openai.Client())
    
    # You evaluate any arbitrary function over the dataset.
    # The input to the function will be the inputs dictionary for each example.
    def predict(inputs: dict) -> dict:
        messages = [{"role": "user", "content": inputs["question"]}]
        response = openai_client.chat.completions.create(messages=messages, model="gpt-4o-mini")
        return {"output": response}
    from langsmith.schemas import Run, Example
    
    from langsmith.evaluation import evaluate, LangChainStringEvaluator
    
    def must_mention(run: Run, example: Example) -> dict:
        prediction = run.outputs.get("output") or ""
        required = example.outputs.get("must_mention") or []
        score = all(phrase in prediction for phrase in required)
        return {"key":"must_mention", "score": score}
    
    evaluators = [
      must_mention,
      LangChainStringEvaluator(
        "criteria",
        config={"criteria":  "harmfulness"}
      ),
      LangChainStringEvaluator(
        "criteria",
        config={
          "criteria": {
            "cliche": "Are the lyrics cliche?"
            " Respond Y if they are, N if they're entirely unique."
          }
        },
      ),
    ]
    
    experiment_results = evaluate(
        predict,
        data=dataset_name,
        evaluators=evaluators,
        experiment_prefix="custom-rap-generator",
        # Any experiment metadata can be specified here
        metadata={
          "version": "1.0.0",
          "variant": "custom-function",
        },
    )


def test_code_block_1():
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = ChatPromptTemplate.from_messages([("human", "Spit some bars about {question}.")])
    chain = prompt | llm | StrOutputParser()
    def predict(inputs: dict) -> dict:
        return {"output": chain.invoke(inputs)}
    from langsmith.schemas import Run, Example
    
    from langsmith.evaluation import evaluate, LangChainStringEvaluator
    
    def must_mention(run: Run, example: Example) -> dict:
        prediction = run.outputs.get("output") or ""
        required = example.outputs.get("must_mention") or []
        score = all(phrase in prediction for phrase in required)
        return {"key":"must_mention", "score": score}
    
    evaluators = [
      must_mention,
      LangChainStringEvaluator(
        "criteria",
        config={"criteria":  "harmfulness"}
      ),
      LangChainStringEvaluator(
        "criteria",
        config={
          "criteria": {
            "cliche": "Are the lyrics cliche?"
            " Respond Y if they are, N if they're entirely unique."
          }
        },
      ),
    ]
    
    experiment_results = evaluate(
        predict,
        data=dataset_name,
        evaluators=evaluators,
        experiment_prefix="runnable-rap-generator",
        # Any experiment metadata can be specified here
        metadata={
          "version": "1.0.0",
          "variant": "runnable",
        },
    )


def test_code_block_2():
    from langchain.agents import AgentExecutor, create_openai_functions_agent
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Spit some bars about the topic\
    \
    {agent_scratchpad}"),
            ("user", "{question}"),
        ]
    )
    
    @tool
    def get_encouragement(request: str) -> str:
        """Get some encouragement."""
        return "You can do it!"
    
    tools = [get_encouragement]
    llm = ChatOpenAI(model="gpt-4o-mini")
    
    def predict(inputs: dict) -> dict:
        agent = create_openai_functions_agent(
            llm,
            tools=[get_encouragement],
            prompt=prompt,
        )
        executor = AgentExecutor(agent=agent, tools=tools)
        return executor.invoke(inputs)
    from langsmith.schemas import Run, Example
    
    from langsmith.evaluation import evaluate, LangChainStringEvaluator
    
    def must_mention(run: Run, example: Example) -> dict:
        prediction = run.outputs.get("output") or ""
        required = example.outputs.get("must_mention") or []
        score = all(phrase in prediction for phrase in required)
        return {"key":"must_mention", "score": score}
    
    evaluators = [
      must_mention,
      LangChainStringEvaluator(
        "criteria",
        config={"criteria":  "harmfulness"}
      ),
      LangChainStringEvaluator(
        "criteria",
        config={
          "criteria": {
            "cliche": "Are the lyrics cliche?"
            " Respond Y if they are, N if they're entirely unique."
          }
        },
      ),
    ]
    
    experiment_results = evaluate(
        predict,
        data=dataset_name,
        evaluators=evaluators,
        experiment_prefix="agent-rap-generator",
        # Any experiment metadata can be specified here
        metadata={
          "version": "1.0.0",
          "variant": "agent",
        },
    )


def test_code_block_3():
    from langchain_openai import ChatOpenAI
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    def predict(inputs: dict):
        return {"output": llm.invoke(inputs['question']).content}
    from langsmith.schemas import Run, Example
    
    from langsmith.evaluation import evaluate, LangChainStringEvaluator
    
    def must_mention(run: Run, example: Example) -> dict:
        prediction = run.outputs.get("output") or ""
        required = example.outputs.get("must_mention") or []
        score = all(phrase in prediction for phrase in required)
        return {"key":"must_mention", "score": score}
    
    evaluators = [
      must_mention,
      LangChainStringEvaluator(
        "criteria",
        config={"criteria":  "harmfulness"}
      ),
      LangChainStringEvaluator(
        "criteria",
        config={
          "criteria": {
            "cliche": "Are the lyrics cliche?"
            " Respond Y if they are, N if they're entirely unique."
          }
        },
      ),
    ]
    
    experiment_results = evaluate(
        predict,
        data=dataset_name,
        evaluators=evaluators,
        experiment_prefix="llm-rap-generator",
        # Any experiment metadata can be specified here
        metadata={
          "version": "1.0.0",
          "variant": "raw-llm",
        },
    )


def test_code_block_4():
    # If your predictor is stateful (e.g. it has memory),
    # You can create a new instance of the predictor for each row in the dataset.
    class MyPredictor:
        def __init__(self):
            self.state = 0
        
        def predict(self, input_: dict) -> dict:
            if self.state > 0:
                raise ValueError("This predictor is stateful and can only be called once.")
            self.state += 1
            return {"output": f"Bar Bar Bar {self.state}"}
    
    def predict(inputs: dict) -> dict:
        predictor = MyPredictor()
        # Return the function that will be called on the next row
        return predictor.predict(inputs)
    
    from langsmith.schemas import Run, Example
    
    from langsmith.evaluation import evaluate, LangChainStringEvaluator
    
    def must_mention(run: Run, example: Example) -> dict:
        prediction = run.outputs.get("output") or ""
        required = example.outputs.get("must_mention") or []
        score = all(phrase in prediction for phrase in required)
        return {"key":"must_mention", "score": score}
    
    evaluators = [
      must_mention,
      LangChainStringEvaluator(
        "criteria",
        config={"criteria":  "harmfulness"}
      ),
      LangChainStringEvaluator(
        "criteria",
        config={
          "criteria": {
            "cliche": "Are the lyrics cliche?"
            " Respond Y if they are, N if they're entirely unique."
          }
        },
      ),
    ]
    
    experiment_results = evaluate(
        predict,
        data=dataset_name,
        evaluators=evaluators,
        experiment_prefix="class-rap-generator",
        # Any experiment metadata can be specified here
        metadata={
          "version": "1.0.0",
          "variant": "custom-class",
        },
    )

