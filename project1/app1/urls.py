from django.urls import path
from app1.views import studentView, showStudent_View, showupdate_View, std_deleteView
from app1.models import Student

urlpatterns = [
    path('std/', studentView.as_view(model=Student, success_url ="/a1/ss/"), name="student_url"),
    path('ss/', showStudent_View.as_view(), name="showstudent_url"),
    path('<pk>/update/', showupdate_View.as_view(model=Student, success_url ="/a1/ss/"), name='update_url'),
    path('<pk>/delete/', std_deleteView.as_view(model=Student, success_url ="/a1/ss/"), name='delete_url'),
]