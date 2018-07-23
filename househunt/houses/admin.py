from django.contrib import admin

# Register your models here.
from . models import House

class HouseModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	class Meta:
		model = House


admin.site.register(House, HouseModelAdmin)