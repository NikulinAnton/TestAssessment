from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from core.forms import FindTrucksForm
from core.models import Truck


class TrucksView(View):
    def get(self, request):
        context = dict(heading="Список самосвалов")

        if request.GET.get("submitted"):
            form = FindTrucksForm(request.GET)
            if form.is_valid():
                filters = dict()
                if form.cleaned_data["model"]:
                    filters["model"] = form.cleaned_data["model"]
                trucks = Truck.objects.filter(**filters)
                paginator = Paginator(trucks, 10)
                page_number = request.GET.get("page", 1)
                page_obj = paginator.get_page(page_number)
                context["page_obj"] = page_obj
        else:
            form = FindTrucksForm()
            trucks = Truck.objects.all()

            paginator = Paginator(trucks, 10)
            page_number = request.GET.get("page", 1)
            page_obj = paginator.get_page(page_number)
            context["page_obj"] = page_obj

        context["form"] = form

        return render(request, "core/core-trucks.html", context)
