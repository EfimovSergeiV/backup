from django.shortcuts import render
from django.http import JsonResponse
from service.models import BackupModel
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse



def list_files(request):
    """ Возвращает список доступных файлов """

    bkps = BackupModel.objects.filter(file__isnull=False)

    data = [
        {
            'id': bkp.id,
            'service': bkp.service,
            'created_at': bkp.created_at.strftime('%d.%m.%Y %H:%M'),
            'file': bkp.file.url
        }
        for bkp in bkps        
    ]

    return JsonResponse(data, safe=False)
    
    

def get_file(request, uuid):
    """ Возвращает файл по его ID """

    print(f'UUID: { uuid }')

    return HttpResponse(f'Get file { uuid }')