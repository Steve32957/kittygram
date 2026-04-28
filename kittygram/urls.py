# urls.py
from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet, basename='kitty')
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]

'''
DefaultRouter — это расширенная версия SimpleRouter: он умеет всё то же,
что и SimpleRouter,
а в дополнение ко всему генерирует корневой эндпоинт /,
GET-запрос к которому вернёт список ссылок на все ресурсы, доcтупные в API.
Работа с DefaultRouter не отличается от SimpleRouter.
'''
