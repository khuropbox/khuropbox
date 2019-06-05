import re
import json
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt

from .operations import *

"fetch the directories within the selected folder"
def isauth(path, request):
    path_user = path[1:path.find('/')]
    username = request.user.get_username()
    if path_user == username:
        return True
    else:
        return False

def get_folder_items(request, main_folder, sort_a_z):
    if isauth(main_folder, request):
        json_string = get_folder_with_items(main_folder, sort_a_z)
        return HttpResponse(json.dumps(json_string), content_type="application/json")
    else:
        raise PermissionDenied

@csrf_exempt
def upload(request):
    if isauth(request.POST['loc'], request):
        file = request.FILES.get('file')
        upload_file(request.POST['loc'], file)
        return HttpResponse(json.dumps(file.name), content_type="application/json", status=200)
    else:
        raise PermissionDenied

@csrf_exempt
def create_folder(request):
    if isauth(request.POST['loc'], request):
        create_folder_item(request.POST['loc'], request.POST['folder_name'])
        return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)
    else:
        raise PermissionDenied


@csrf_exempt
def download(request):
    if isauth(request.POST['loc'], request):
        file = request.GET.get('file')
        result = download_file(file)
        response = HttpResponse(result['Body'].read())
        response['Content-Type'] = result['ContentType']
        response['Content-Length'] = result['ContentLength']
        response['Content-Disposition'] = 'attachment; filename=' + file
        response['Accept-Ranges'] = 'bytes'
        return response
    else:
        raise PermissionDenied

@csrf_exempt
def paste_file(request):
    if isauth(request.POST['loc'], request):
        paste(request.POST['loc'], request.POST.getlist('file_list[]'))
        return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)
    else:
        raise PermissionDenied

@csrf_exempt
def delete_file(request):
    delete(request.POST.getlist('file_list[]'))
    return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)