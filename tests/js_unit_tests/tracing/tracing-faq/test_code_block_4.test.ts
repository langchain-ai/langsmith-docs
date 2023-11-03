
test('test_code_block_4', async () => {
    const configuredChain = chain.withConfig({ runName: "MyCustomChain" });
    await configuredChain.invoke({query: "What is the meaning of life?"});
});
