from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from langdetect import detect
from mbart_model.translator import translate_code_switched_to_target, map_lang_code
import json

@csrf_exempt
def process_text(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            target_lang = data.get('target_lang', 'en_XX')

            if not text:
                return JsonResponse({'error': 'No text provided'}, status=400)

            detected_lang = detect(text)
            src_lang = map_lang_code(detected_lang)
            translated = translate_code_switched_to_target(text, target_lang)

            return JsonResponse({
                'input': text,
                'source_lang': src_lang,
                'target_lang': target_lang,
                'translation': translated
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
