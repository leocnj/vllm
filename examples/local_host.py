import openai
from typing import Iterable, List

# Modify OpenAI's API key and API base to use vLLM's API server.
openai.api_key = "EMPTY"
# openai.api_base = "http://localhost:8000/v1"
# self-hosted vLLM openAI style server
openai.api_base = "https://h273c2bf060bb2192-proj-tango-hpc-2.hpc.jpw1a.r-local.net/v1"

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

#vLLM="https://hd01e324754ce48f5-proj-tango-hpc-2.hpc.jpw1a.r-local.net"

vLLM = openai.api_base
import requests as _requests
import json

json_body = {
    "model" : model,
    "prompt": "A robot may not injure a human being",
    "n" : 1,
    "use_beam_search" : False,
    "logprobs" : 3,
    }

completion2 = _requests.post(
    vLLM + "/completions",
    json = json_body
    )

def get_response(response: _requests.Response) -> List[str]:
    data = json.loads(response.content)
    out_str = json.dumps(data, indent=4)
    return out_str

print("\n\nCompletion2 results:")
if stream:
    for c in completion2:
        print(c)
else:
    print(get_response(completion2))
