from django.views import generic
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from . import models
from . import forms


class HomeView(auth_mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'


class WorkView(generic.View, auth_mixins.LoginRequiredMixin):
    context = {}
    model = models.Work
    form = forms.NewWorkForm

    def get_form(self):
        return self.form

    def get_model(self):
        return self.model

    def get(self, request):
        self.compare_context(request)

        return render(request, 'works.html', self.context)

    def compare_context(self, request, **kwargs):
        self.context['worklist'] = self.get_model(
        ).objects.filter(user=request.user)
        self.context['form'] = self.get_form()

        for k, v in kwargs:
            self.context[k] = v

    def post(self, request):
        form = self.get_form()(request.POST)
        self.compare_context(request)

        if form.is_valid():
            instance = self.get_model()(**form.cleaned_data)
            instance.user = self.request.user
            instance.save()

        return redirect('works')


class ReportsView(generic.View, auth_mixins.LoginRequiredMixin):

    def get(self, request):
        return render(request, template_name='reports.html')