from app1.models import Student
from app1.forms import StudentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# Create your views here.
class studentView(CreateView):
    model = Student
    fields = '__all__'

class showStudent_View(ListView):
    model = Student

class showupdate_View(UpdateView):
    model = Student
    fields = '__all__'
    success_url ="/"

class std_deleteView(DeleteView):
    model = Student
    success_url ="/"
