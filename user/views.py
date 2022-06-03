from django.shortcuts import render
from .models import User,Policy,Page,Visit,Queries
from django.http import HttpResponse
from django.db.models import Count
import simplejson as json
from django.core import serializers
from urllib import parse
from django.shortcuts import render
from django.views import View
from datetime import date
from datetime import timedelta
# Create your views here.Queries



class IndexView(View):
    template_name = 'user_visit.html'

    def get(self, request):
        #displaying last 7 days data
        day=date.today()-timedelta(days=7)
        visit_query= list(Visit.objects.filter(policy_id__start_date__gte=day).values('page_id__name','policy_id__user_id__name').annotate(dcount=Count('page_id')).order_by('page_id__name'))
        jsonList = json.dumps(visit_query)
        #convert python obj to string
        Queries.objects.create(query_set=jsonList)
        # fetch data from Queries table
        try:
            jsonQueries=  Queries.objects.all().values().last()
            #convert string to python obj
            queryobj= json.loads(jsonQueries['query_set'])
            status=True
        except Exception:
            status=False
            queryobj=''
        return render(request, self.template_name, {
                'queryobj': queryobj,'status':status
                })
