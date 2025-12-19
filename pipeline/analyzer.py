from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class GrammarAnalyzer:
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32
        )

        self.model.eval()
