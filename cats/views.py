# views.py
from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


# Если бы пользователи могли оставлять комментарии к котикам,
# то эндпоинт для работы с комментариями выглядел бы примерно так:
# cats/{cat_id}/comments/

# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
# queryset во вьюсете не указываем
# Нам тут нужны не все комментарии, а только связанные с котом с id=cat_id
# Поэтому нужно переопределить метод get_queryset и применить фильтр
#     def get_queryset(self):
#         # Получаем id котика из эндпоинта
#         cat_id = self.kwargs.get("cat_id")
#         # И отбираем только нужные комментарии
#         new_queryset = Comment.objects.filter(cat=cat_id)
#         return new_queryset
# в таком случае создаем basename, name автоматически не получиться
# router.register('cats', CatViewSet, basename='kitty')
