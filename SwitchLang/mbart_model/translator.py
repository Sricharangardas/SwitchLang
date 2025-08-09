from transformers import MBart50TokenizerFast, MBartForConditionalGeneration
import nltk
from nltk import sent_tokenize
from langdetect import detect

# Correct path to the model files
cache_dir = "C:/Users/91934/.cache/huggingface/hub/models--facebook--mbart-large-50-many-to-many-mmt"

# Load the tokenizer and model from the local cache
tokenizer = MBart50TokenizerFast.from_pretrained(cache_dir)
model = MBartForConditionalGeneration.from_pretrained(cache_dir)

# In translator.py

def map_lang_code(detected_lang):
    # Mapping from ISO 639-1 to mBART-50 codes
    lang_mapping = {
    "af": "af_ZA",
    "ar": "ar_AR",
    "az": "az_AZ",
    "bn": "bn_IN",
    "my": "my_MM",
    "zh": "zh_CN",
    "hr": "hr_HR",
    "cs": "cs_CZ",
    "nl": "nl_XX",
    "en": "en_XX",
    "et": "et_EE",
    "fi": "fi_FI",
    "fr": "fr_XX",
    "gl": "gl_ES",
    "ka": "ka_GE",
    "de": "de_DE",
    "gu": "gu_IN",
    "he": "he_IL",
    "hi": "hi_IN",
    "id": "id_ID",
    "it": "it_IT",
    "ja": "ja_XX",
    "kk": "kk_KZ",
    "km": "km_KH",
    "ko": "ko_KR",
    "lv": "lv_LV",
    "lt": "lt_LT",
    "mk": "mk_MK",
    "ml": "ml_IN",
    "mr": "mr_IN",
    "mn": "mn_MN",
    "ne": "ne_NP",
    "fa": "fa_IR",
    "pl": "pl_PL",
    "ps": "ps_AF",
    "pt": "pt_XX",
    "ro": "ro_RO",
    "ru": "ru_RU",
    "si": "si_LK",
    "sl": "sl_SI",
    "es": "es_XX",
    "sw": "sw_KE",
    "sv": "sv_SE",
    "ta": "ta_IN",
    "te": "te_IN",
    "th": "th_TH",
    "tr": "tr_TR",
    "uk": "uk_UA",
    "ur": "ur_PK",
    "vi": "vi_VN",
    "xh": "xh_ZA"
    }
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

def translate_code_switched_to_target(text, target_lang):
    sentences = sent_tokenize(text)
    english_segments = []
    for sentence in sentences:
        try:
            detected_lang = detect(sentence)
        except:
            detected_lang = "en"
        src_lang = map_lang_code(detected_lang)
        english = translate(sentence, src_lang, "en_XX")
        english_segments.append(english)
    combined_english = ' '.join(english_segments)
    # If the target language is English, return the combined English directly
    if target_lang == "en_XX":
        return combined_english
    final_translation = translate(combined_english, "en_XX", target_lang)
    return final_translation