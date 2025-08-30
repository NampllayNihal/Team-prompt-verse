import os
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN", "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")
os.environ["HF_HOME"] = HF_TOKEN

ner_pipeline = pipeline(
    task="ner",
    model="dslim/bert-base-NER",
    tokenizer="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

def extract_entities(text: str):
    entities = ner_pipeline(text)
    return [{"word": e["word"], "entity_group": e["entity_group"], "score": float(e["score"])} for e in entities]
