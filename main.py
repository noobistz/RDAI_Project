from model_server import LLMBot
from fastapi import FastAPI    # as before
from pydantic import BaseModel # as before

class Item(BaseModel):
    text: str

app = FastAPI()

# Initialise LLM Bot
llmbot = LLMBot()

@app.post("/generate/")
async def response_generator(data: Item):
  generated_text = llmbot.generate(data)
  return llmbot.parse_text(generated_text)

# # In browser : http://127.0.0.1:8000/docs
'''
curl -X 'POST' \
  'http://127.0.0.1:8000/generate/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "What is the capital of england?"
}'
'''