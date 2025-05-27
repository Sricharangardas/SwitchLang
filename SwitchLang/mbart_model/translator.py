from transformers import MBart50TokenizerFast, MBartForConditionalGeneration

# Correct path to the model files
cache_dir = "C:/Users/YASH/.cache/huggingface/hub/models--facebook--mbart-large-50-many-to-many-mmt"

# Load the tokenizer and model from the local cache
tokenizer = MBart50TokenizerFast.from_pretrained(cache_dir)
model = MBartForConditionalGeneration.from_pretrained(cache_dir)

# In translator.py

def map_lang_code(detected_lang):
    # A dictionary to map language codes from langdetect to mBART's language format
    lang_mapping = {
        "en": "en_XX",
        "fr": "fr_XX",
        "de": "de_XX",
        "es": "es_XX",
        "it": "it_XX",
        "pt": "pt_XX",
        # Add more languages as needed
    }

    # Return the mapped language code or default to 'en_XX' if not found
    return lang_mapping.get(detected_lang, "en_XX")


# Example function for translation
def translate(text, src_lang, tgt_lang):
    tokenizer.src_lang = src_lang  # e.g., "en_XX"

    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512  # specify maximum length
    )

    generated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_lang),
        max_length=512
    )

    return tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

