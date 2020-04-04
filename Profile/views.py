from django.shortcuts import render,redirect
from django.views.generic import View

#IMPORTAR METODO DE AUTENTICACION
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
 #LLEGA A LA VISTA Y LA EJECUTA

class ProfileClass(LoginRequiredMixin,View):
    templates_okidoki = 'profile.html'
    def get (self,request,*args,**kwargs):
        #printn("GET DE DASHBOARD")
        return render(request,self.templates_okidoki,{})
# class DashboardClass(View):
#     templates='dashboard.html'
#     def get(self,request,*args,**kwargs):
#         return render(request,self.templates,{})
