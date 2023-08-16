import { Client, Run } from "langsmith";

test('test_code_block_5', async () => {
    const client = new Client();
    const runs: Run[] = [];
    for await (const run of client.listRuns({
      filter: 'has(metadata, \'{"variant": "abc123"}\')',
    })) {
      runs.push(run);
    }
});
