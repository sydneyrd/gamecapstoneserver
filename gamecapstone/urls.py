from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from gamecapstoneapi.views import register_user, login_user, SlotUserView, QuestionView, SolutionView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', SlotUserView, 'users'),
router.register(r'questions', QuestionView, 'questions'),
router.register(r'solutions', SolutionView, 'solutions')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

