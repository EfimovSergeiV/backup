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
            'uuid': bkp.uuid,
            'service': bkp.service,
            'created_at': bkp.created_at.strftime('%d.%m.%Y %H:%M'),
            # 'file': bkp.file.url
        }
        for bkp in bkps        
    ]

    return JsonResponse(data, safe=False)
    
    

def get_file(request, uuid):
    """ Возвращает файл по его ID """

    qs = BackupModel.objects.get(uuid = uuid)

    ext = qs.file.name.split('.')[-1]
    file_name = f"{qs.service} {qs.created_at.strftime('%d.%m.%y')}.{ ext }"

    with open(qs.file.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=f"application/{ ext }")
        # response = HttpResponse(f.read(), content_type="application/octet-stream")
        # response['Content-Disposition'] = f'attachment; filename={file_name}'
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response




