from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ProductViewSet, CustomerViewSet, CommentViewSet


router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('products', ProductViewSet, basename='products')
router.register('customer', CustomerViewSet, basename='customer')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = router.urls