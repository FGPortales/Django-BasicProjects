from django.views import View
from .models import Company
from django.http import JsonResponse
from django.forms.models import model_to_dict


class CompanyListView(View):
    def get(self, request):
        company_list = Company.objects.all()
        return JsonResponse(list(company_list.values()), safe=False)


class CompanyDetailView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        return JsonResponse(model_to_dict(company))
