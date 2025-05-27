from transformers import MBartTokenizer, MBartForConditionalGeneration

# Correct path to the model files
cache_dir = "C:/Users/YASH/.cache/huggingface/hub/models--facebook--mbart-large-cc25/"

# Load the tokenizer and model from the local cache
tokenizer = MBartTokenizer.from_pretrained(cache_dir)
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
    # Encode the text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Generate translation (using the model)
    translated_tokens = model.generate(
        inputs["input_ids"], 
        decoder_start_token_id=model.config.pad_token_id,
        forced_bos_token_id=model.config.lang2id[tgt_lang],
        max_length=512
    )

    # Decode the translated tokens
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return translated_text
