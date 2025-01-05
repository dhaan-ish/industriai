from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "Pinkstack/PARM-V2-QwQ-Qwen-2.5-o1-3B-GGUF"
filename = "Parm2-Qwen2.5-3B.Q8_0.gguf"

tokenizer = AutoTokenizer.from_pretrained(model_id, gguf_file=filename)
model = AutoModelForCausalLM.from_pretrained(model_id, gguf_file=filename)
