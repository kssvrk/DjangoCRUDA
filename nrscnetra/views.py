# Create your views here.
from django.shortcuts import render
from nrscnetra.forms import SystemForm,JobForm
from nrscnetra.models import System,Job
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import  reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages

#----------------------------------------SYSTEM VIEWS---------------------------------------------

class SystemCreate(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = System
    form_class = SystemForm
    success_message = "System succesfully registered"
    template_name = "nrscnetra/systems/create.html"
    success_url = reverse_lazy('netra:systemlist')
    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)
  
class SystemDetail(LoginRequiredMixin,DetailView):
    model=System
    template_name = "nrscnetra/systems/detail.html"

    def get_queryset(self):
        return System.objects.filter(added_by=self.request.user,pk=self.kwargs['pk'])

class SystemList(LoginRequiredMixin,SuccessMessageMixin,ListView):
    model=System
    template_name = "nrscnetra/systems/list.html"
    context_object_name='system_list'
    #--- paginate ---
    paginate_by = 5
    #----------------------------------------
    def get_queryset(self):
        return System.objects.filter(added_by=self.request.user)
    
class SystemUpdate(LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    model = System
    form_class = SystemForm
    success_message = "System succesfully updated"
    template_name = "nrscnetra/systems/update.html"

    def get_success_url(self):
        return self.request.path
    def get_object(self, queryset=None):
        return get_object_or_404(self.model, added_by=self.request.user,pk=self.kwargs['pk'])

class SystemDelete(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = System
    success_url = reverse_lazy('netra:systemlist')
    success_message = "System succesfully deleted"
    template_name = "nrscnetra/systems/delete.html"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, added_by=self.request.user,pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(SystemDelete, self).delete(request, *args, **kwargs)

#----------------------------------- JOB VIEWS----------------------------------------------------------
class JobCreate(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = Job
    form_class = JobForm
    success_message = "Job succesfully registered"
    template_name = "nrscnetra/jobs/create.html"
    success_url = reverse_lazy('netra:systemlist')

    def get_context_data(self, **kwargs):
        ctx = super(JobCreate, self).get_context_data(**kwargs)
        system=get_object_or_404(System, added_by=self.request.user,pk=self.kwargs['sysid'])
        ctx['system_ipaddress'] = system.ip_address
        #ctx['system_id']=system.system_id
        ctx['form'].fields['system'].initial=system.system_id
        return ctx
    
    def clean(self):
        cleaned_data = super(JobForm, self).clean()
        system_id=cleaned_data.get('system')
        count=System.objects.filter(added_by=self.request.user,pk=system_id).count()
        if(count==0):
            self.add_error(None, ValidationError('System does not belong to the loggedin User'))



    