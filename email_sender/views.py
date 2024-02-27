from typing import Any
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View
from django.http import HttpResponse
from .models import MyModle
from .forms import MyModelForm

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name-field']
        email = request.POST['email-field']
        message = request.POST['message-field']
        send_mail('Hi, I am ' + name,
                  message,
                  email,
                  ['akromabdumannopov802@gmail.com'])
        return render(request, 'contact.html', {})

    return render(request, 'contact.html')


class CRUD_In_Generic_View(View):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            try:
                instance = MyModle.objects.get(pk=kwargs['pk'])
                data = {'id': instance.id, 'field1': instance.field1, 'field2': instance.field2}
                return HttpResponse(data)
            except MyModle.DoesNotExist:
                return HttpResponse({'error': 'Object not found'}, status=404)
        else:
            queryset = MyModle.objects.all()
            data = [{'id': obj.id, 'field1': obj.field1, 'field2': obj.field2} for obj in queryset]
            return HttpResponse(data)

    def post(self, request, *args, **kwargs):
        form = MyModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponse({'id': instance.id, 'message': 'Object created successfully'})
        else:
            return HttpResponse({'errors': form.errors}, status=400)

    def put(self, request, *args, **kwargs):
        try:
            instance = MyModle.objects.get(pk=kwargs['pk'])
            form = MyModelForm(request.POST, instance=instance)
            if form.is_valid():
                instance = form.save()
                return HttpResponse({'id': instance.id, 'message': 'Object updated successfully'})
            else:
                return HttpResponse({'errors': form.errors}, status=400)
        except MyModle.DoesNotExist:
            return HttpResponse({'error': 'Object not found'}, status=404)

    def delete(self, request, *args, **kwargs):
        try:
            instance = MyModle.objects.get(pk=kwargs['pk'])
            instance.delete()
            return HttpResponse({'message': 'Object deleted successfully'})
        except MyModle.DoesNotExist:
            return HttpResponse({'error': 'Object not found'}, status=404)


# class CRUD(View):
#     def get(self, request, *args, **kvargs):
#         if request.method == 'GET':
#             data_obj = MyModle.objects.all()
#             return render(request, 'get.html', {'data':data_obj})
    
#     def post(self, request, *args, **kvargs):
#         if request.method == "POST":  
#             form = MyModelForm(request.POST)  
#             if form.is_valid():  
#                 try:  
#                     form.save() 
#                     model = form.instance
#                 except:  
#                     pass  
#         else:  
#             form = MyModelForm()  
#         return render(request,'book-create.html',{'form':form}) 
    
#     def put(self, request, *args, **kvargs):
#         if request.method == 'PUT':
#             return render(request, 'put.html', {})
        
#     def delete(self, request, *args, **kvargs):
#         if request.method == 'DELETE':
#             return render(request, 'delete.html', {})
        