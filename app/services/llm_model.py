from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "google/gemma-3-4b-it"

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    local_files_only=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
    local_files_only=True
)

prompt = f"""
You are a professional editor.

Summarize the text below clearly and accurately.
Do not add extra information.

TEXT:
{context}
"""

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

output = model.generate(
    **inputs,
    max_new_tokens=200,
    temperature=0.3,
    top_p=0.9
)

summary = tokenizer.decode(output[0], skip_special_tokens=True)
print(summary)