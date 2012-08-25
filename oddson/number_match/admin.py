from django.contrib import admin

from .models import Attempt, Game


##
# Admin
##
class AttemptAdmin(admin.ModelAdmin):  # pragma: no cover
    pass


class GameAdmin(admin.ModelAdmin):  # pragma: no cover
    fieldsets = (
        (None, {
            'fields': ('is_active', ('start_date', 'end_date'), ('used_attempts', 'allowed_attempts'), ('min_value', 'max_value')),
        }),
    )
    list_display = ('id', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    readonly_fields = ('used_attempts',)


##
# Register
##
admin.site.register(Attempt, AttemptAdmin)  # pragma: no cover
admin.site.register(Game, GameAdmin)  # pragma: no cover
