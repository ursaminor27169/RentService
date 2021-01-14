from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Cars
from .models import Transmissions
from .models import Marks
from .models import Ranks


class InlineCars(admin.TabularInline):
    model = Cars


class CarsAdmin(ImportExportModelAdmin):
    list_filter = ('transmission', 'rank', 'reservation')
    list_display = ('stamp', 'transmission', 'price', 'litre', 'reservation', 'description')
    list_display_links = ('stamp',)
    search_fields = ('stamp', 'description', 'price')


class RanksAdmin(ImportExportModelAdmin):
    inlines = [InlineCars, ]
    list_display = ('rank',)
    list_display_links = ('rank',)
    search_fields = ('rank',)


class TransmissionsAdmin(ImportExportModelAdmin):
    inlines = [InlineCars,]
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


class MarksAdmin(ImportExportModelAdmin):
    inlines = [InlineCars, ]
    list_filter = ('mark',)
    list_display = ('mark', 'model')
    list_display_links = ('mark', 'model')
    search_fields = ('mark', 'model')


admin.site.register(Transmissions, TransmissionsAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(Ranks, RanksAdmin)
