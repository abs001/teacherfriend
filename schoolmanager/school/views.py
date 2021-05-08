from django.http import HttpResponse
from django.shortcuts import render
from .models import GetResult
from datetime import datetime
import pandas as pd


def index(request):
    if request.method == "POST":
        result_object = GetResult()
        result_object.upload_date = datetime.now()
        result_object.raw_file = request.FILES['rawfile']
        result_object.save()

    uploaded_files = GetResult.objects.all().order_by('-upload_date')
    return render(request, 'school/home.html', {'uploaded_files': uploaded_files})


def generate_result(request, fileid):
    uploaded_files = GetResult.objects.all().order_by('-upload_date')
    excel_data = pd.read_excel(GetResult.objects.get(id=fileid).raw_file.path, engine='openpyxl')
    return render(request, 'school/result.html', {'data': uploaded_files})


def delete_record(request, id):
    GetResult.objects.filter(id=id).delete()
    uploaded_files = GetResult.objects.all().order_by('-upload_date')
    return render(request, 'school/home.html', {'uploaded_files': uploaded_files})
