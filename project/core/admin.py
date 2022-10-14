from django.contrib import admin

from core.models import Truck, TruckModel

admin.site.register(TruckModel)


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    search_fields = ["side_number__icontains"]
    list_display = ["id", "side_number", "current_cargo_weight", "model"]
    exclude = ["deleted_at"]
