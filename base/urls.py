from .views import *
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register("student", viewset=StudentViewSet)
router.register("event", viewset=EventViewSet)
event_router = routers.NestedSimpleRouter(router, r"event", lookup="event")
event_router.register(
    r"attendance", viewset=AttendanceViewSet, basename="event-attendance"
)
student_router = routers.NestedSimpleRouter(router, r"student", lookup="student")
student_router.register(
    r"attendance", viewset=AttendanceViewSet, basename="student-attendance"
)
urlpatterns = router.urls + student_router.urls + event_router.urls
