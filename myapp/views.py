from django.shortcuts import render

from itertools import chain
from django.views.generic import ListView

#Models
from myapp.models import Model_1
from myapp_2.models import Model_2
from myapp_3.models import Model_3


#Search Class
class SearchView(ListView):
    template_name = 'index.html'
    count = 0
    all_data = ''
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['all_data'] = self.all_data or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        all_data_chain = chain(
            Model_1.objects.all(),
            Model_2.objects.all(),
            Model_3.objects.all()
        )
        self.all_data = sorted(all_data_chain, key=lambda instance: instance.pk,reverse=True)
        
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            model_1_results        = Model_1.objects.search(query)
            model_2_results      = Model_2.objects.search(query)
            model_3_results     = Model_3.objects.search(query)
            
            queryset_chain = chain(
                    model_1_results,
                    model_2_results,
                    model_3_results
            )        
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            self.count = len(qs) 
            return qs 
        return Model_1.objects.none()