from vllm import LLM, SamplingParams
import textwrap

class LLMBot:
  def __init__(self, model_name="TheBloke/TinyLlama-1.1B-Chat-v1.0-AWQ"):
      self.llm = LLM(model=model_name, quantization="awq", dtype="float16", gpu_memory_utilization=0.95)
      self.system_prompt = "You are a friendly chatbot who always responds in the style of a pirate."

  def get_prompt(self, human_prompt):
      prompt_template=f"<|system|>\n {self.system_prompt}</s>\n<|user|>\n{human_prompt}</s>\n<|assistant|>:\n"
      return prompt_template

  def cut_off_text(self, text, prompt):
      cutoff_phrase = prompt
      index = text.find(cutoff_phrase)
      if index != -1:
          return text[:index]
      else:
          return text

  def remove_substring(self, string, substring):
      return string.replace(substring, "")

  def generate(self, text):
      prompt = self.get_prompt(text)
      sampling_params = SamplingParams(
                                      max_tokens = 512,
                                      # do_sample=True,
                                      temperature = 0.1,
                                      top_p = 0.95,
                                      top_k = 50,
                                      )
      outputs = self.llm.generate([prompt], sampling_params)
      return outputs

  def parse_text(self, output):
          generated_text = output[0].outputs[0].text
          # wrapped_text = textwrap.fill(generated_text, width=100)
          # print(wrapped_text +'\n\n')
          return generated_text
      
if __name__ == '__main__':
  llmbot = LLMBot()
  # print("Created LLM Bot")
  # generated_text = llmbot.generate("What is the capital of England?")
  # print(llmbot.parse_text(generated_text))