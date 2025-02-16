from transformers import pipeline
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Load the NLP model
nlp_model = pipeline("text-classification", model="xlm-roberta-base")

@api_view(["POST"])
def process_text(request):
    text = request.data.get("text", "")
    if not text:
        return Response({"error": "No text provided"}, status=400)
    
    result = nlp_model(text)
    return Response({"prediction": result})