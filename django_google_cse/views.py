from django.views.generic import TemplateView
from django.conf import settings


class Search(TemplateView):
    template_name = "django_google_cse/default.html"

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        #context['TEMPLATE'] = getattr(settings, 'CSE_TEMPLATE', 'django_google_cse/default.html')
        context['CX_CODE'] = getattr(settings, 'CX_CODE', '')
        context['q'] = self.request.GET.get('q', '')
        return context