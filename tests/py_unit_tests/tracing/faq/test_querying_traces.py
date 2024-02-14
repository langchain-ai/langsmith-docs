import pytest
from langsmith import Client
    
client = Client()

@pytest.mark.asyncio
async def test_code_block_0():
    from langsmith import Client
    client = Client()

@pytest.mark.asyncio
async def test_code_block_1():
    run_ids = ['a36092d2-4ad5-4fb4-9c0d-0dba9a2ed836', '9398e6be-964f-4aa4-8ae9-ad78cd4b7074']
    selected_runs = list(client.list_runs(id=run_ids))

@pytest.mark.asyncio
async def test_code_block_2():
    import json
    to_search = {'user_id': '4070f233-f61e-44eb-bff1-da3c163895a3'}
    list(client.list_runs(project_name='default', filter=f"has(metadata, '{json.dumps(to_search)}')"))

@pytest.mark.asyncio
async def test_code_block_3():
    import json
    to_search = {'environment': 'production'}
    list(client.list_runs(project_name='default', filter=f"has(metadata, '{json.dumps(to_search)}')"))

@pytest.mark.asyncio
async def test_code_block_4():
    import json
    to_search = {'conversation_id': 'a1b2c3d4-e5f6-7890'}
    list(client.list_runs(project_name='default', filter=f"has(metadata, '{json.dumps(to_search)}')"))

@pytest.mark.asyncio
async def test_code_block_5():
    import json
    to_search = {'conversation_id': '69b12c91-b1e2-46ce-91de-794c077e8151'}
    list(client.list_runs(project_name='default', filter=f"and(has(metadata, '{json.dumps(to_search)}'), eq(name, 'ChatOpenAI'))"))
