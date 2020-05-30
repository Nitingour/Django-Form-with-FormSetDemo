from django.forms import formset_factory
from FApp.forms import FamilyMemberForm
from django.views import View
from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from FApp.models import *
from django.views.generic import *
from FApp.forms import *
from django.db import transaction

class ProfileList(ListView):
    model = Profile
    def get_success_url(self):
            return reverse('profile-list')



class ProfileFamilyMemberCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileFamilyMemberCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['familymembers'] = FamilyMemberFormSet(self.request.POST)
        else:
            data['familymembers'] = FamilyMemberFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['familymembers']
        with transaction.atomic():
            self.object = form.save()

            if familymembers.is_valid():
                familymembers.instance = self.object
                familymembers.save()
        return super(ProfileFamilyMemberCreate, self).form_valid(form)

class ProfileCreate(CreateView):
    model = Profile
    fields = ['first_name', 'last_name']
