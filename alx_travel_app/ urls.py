from drf_yasg.views import get_schema_view
from drf_yasg import openapi
...
path('swagger/', schema_view.with_ui('swagger', ...))
path('api/', include('listings.urls'))
