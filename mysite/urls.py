from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^step/', include("step.urls" , namespace="step")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

