import os
from django.http import HttpResponse

file_path = os.path.abspath(__file__)
pro_dir = os.path.dirname(file_path)

def home(request):
    file_addr=os.path.join(pro_dir,'home.html')
    fp = open(file_addr,'r')
    data1 = fp.read()
    return HttpResponse(data1)