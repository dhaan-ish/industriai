import os
import os
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-0.5B")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen1.5-0.5B")


generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
llm = HuggingFacePipeline(pipeline=generator)
response = llm.invoke("Generate 5 specific, open-ended questions about quantum mechanics that can be used to search for detailed answers on a search engine.")

questions = response.split('\n') 
questions = [q.strip() for q in questions if q.strip()]  

questions.pop(0)

import requests
import json

url = "https://google.serper.dev/search"


for i in questions:

    payload = json.dumps({
  "q": i
})
    headers = {
  'X-API-KEY': 'c2e459bb67bc16a20cf2aafc1fa977b524b2fe10',
  'Content-Type': 'application/json'
}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


