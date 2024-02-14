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
    to_search = {'user_id': ''}
    list(client.list_runs(project_name='default', filter="eq(metadata_key, 'user_id')"))
    list(client.list_runs(project_name='default', filter="and(eq(metadata_key, 'user_id'), eq(metadata_value, '4070f233-f61e-44eb-bff1-da3c163895a3'))"))

@pytest.mark.asyncio
async def test_code_block_3():
    list(client.list_runs(project_name='default', filter="and(eq(metadata_key, 'environment'), eq(metadata_value, 'production'))"))

@pytest.mark.asyncio
async def test_code_block_4():
    list(client.list_runs(project_name='default', filter="and(eq(metadata_key, 'conversation_id'), eq(metadata_value, 'a1b2c3d4-e5f6-7890'))"))

@pytest.mark.asyncio
async def test_code_block_5():
    list(client.list_runs(project_name='default', filter="and(eq(name, 'ChatOpenAI'), eq(metadata_key, 'conversation_id'), eq(metadata_value, '69b12c91-b1e2-46ce-91de-794c077e8151'))"))
