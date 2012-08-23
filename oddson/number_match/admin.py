from django.contrib import admin

from .models import Attempt, Contract


##
# Admin
##
class AttemptAdmin(admin.ModelAdmin):
    pass


class ContractAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('is_active', 'contract_id', ('start_date', 'end_date'), ('allowed_attempts', 'used_attempts'), ('min_value', 'max_value')),
        }),
    )
    list_display = ('contract_id', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    readonly_fields = ('used_attempts',)
    search_fields = ('contract_id',)


##
# Register
##
admin.site.register(Attempt, AttemptAdmin)
admin.site.register(Contract, ContractAdmin)
