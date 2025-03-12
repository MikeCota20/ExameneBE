from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Post

# ----------------- Vistas Basadas en Funciones (FBV) -----------------

@csrf_exempt  # Deshabilitar CSRF para pruebas (no recomendado en producción)
def get_posts(request):
    """Obtener todos los posts"""
    if request.method == "GET":
        posts = list(Post.objects.values())  # Convertir QuerySet a lista de diccionarios
        return JsonResponse(posts, safe=False)

@csrf_exempt
def create_post(request):
    """Crear un nuevo post"""
    if request.method == "POST":
        data = json.loads(request.body)
        post = Post.objects.create(title=data['title'], content=data['content'])
        return JsonResponse({"message": "Post creado", "id": post.id}, status=201)

@csrf_exempt
def update_post(request, post_id):
    """Actualizar un post existente"""
    if request.method == "PUT":
        data = json.loads(request.body)
        try:
            post = Post.objects.get(id=post_id)
            post.title = data['title']
            post.content = data['content']
            post.save()
            return JsonResponse({"message": "Post actualizado"})
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post no encontrado"}, status=404)

@csrf_exempt
def delete_post(request, post_id):
    """Eliminar un post"""
    if request.method == "DELETE":
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return JsonResponse({"message": "Post eliminado"})
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post no encontrado"}, status=404)

# ----------------- Vistas Basadas en Clases (CBV) -----------------

class PostListView(View):
    """Obtener todos los posts"""
    def get(self, request):
        posts = list(Post.objects.values())
        return JsonResponse(posts, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class PostCreateView(View):
    """Crear un nuevo post"""
    def post(self, request):
        data = json.loads(request.body)
        post = Post.objects.create(title=data['title'], content=data['content'])
        return JsonResponse({"message": "Post creado", "id": post.id}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class PostUpdateView(View):
    """Actualizar un post existente"""
    def put(self, request, post_id):
        data = json.loads(request.body)
        try:
            post = Post.objects.get(id=post_id)
            post.title = data['title']
            post.content = data['content']
            post.save()
            return JsonResponse({"message": "Post actualizado"})
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post no encontrado"}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class PostDeleteView(View):
    """Eliminar un post"""
    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return JsonResponse({"message": "Post eliminado"})
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post no encontrado"}, status=404)
