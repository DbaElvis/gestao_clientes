from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from vendas import urls as vendas_urls
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    path('vendas/', include(vendas_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    # path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

admin.site.site_header = 'Gestão de Clientes'                    # default: "Django Administration"
admin.site.index_title = 'Administração'                 # default: "Site administration"
admin.site.site_title = 'Seja Bem Vindo'
