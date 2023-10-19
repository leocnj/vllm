import openai

# Modify OpenAI's API key and API base to use vLLM's API server.
openai.api_key = "EMPTY"
# openai.api_base = "http://localhost:8000/v1"

# self-hosted vLLM openAI style server
openai.api_base = "https://h503711e54cdad8aa-proj-tango-hpc-2.hpc.jpw1a.r-local.net/v1"
# List models API
models = openai.Model.list()
print("Models:", models)

model = models["data"][0]["id"]

# Completion API
stream = False
completion = openai.Completion.create(
    model=model,
    prompt="A robot may not injure a human being",
    echo=False,
    n=1,
    stream=stream,
    logprobs=3)

print("Completion results:")
if stream:
    for c in completion:
        print(c)
else:
    print(completion)
