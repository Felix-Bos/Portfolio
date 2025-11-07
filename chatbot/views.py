
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat_api(request):
    from chatbot.rag.llm_interface import ask_rag  # Lazy import to avoid heavy RAG deps during startup
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            query = data.get("query")
            if not query:
                return JsonResponse({"error": "Query not provided"}, status=400)
            
            answer = ask_rag(query)
            print(f"Final Answer: {answer}")
            return JsonResponse({"answer": answer})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            print(f"An error occurred in chat_api: {e}")
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def chat_view(request):
    return render(request, 'chatbot/widget.html')
