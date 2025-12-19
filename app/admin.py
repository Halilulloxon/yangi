from django.contrib import admin
from .models import Foydalanuvchilar, Kafedralar, oquvIshlari, ilmiy_ishlari, Dekanatlar

# --- Inlines ---
class oquvIshlariInline(admin.TabularInline):
    model = oquvIshlari
    extra = 1
    autocomplete_fields = ('muallif',)

class ilmiy_ishlariInline(admin.TabularInline):
    model = ilmiy_ishlari
    extra = 1
    autocomplete_fields = ('muallif',)

# --- Admin Classes ---
class FoydalanuvchilarAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'familiya', 'sharifi', 'tugulgan_sana', 'kafedra')
    search_fields = ('ism', 'familiya', 'sharifi')
    list_filter = ('tugulgan_sana', 'kafedra')
    inlines = [oquvIshlariInline, ilmiy_ishlariInline]

class KafedralarAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'mudir')
    search_fields = ('nomi', 'mudir__ism', 'mudir__familiya')
    list_filter = ('nomi',)

class DekanatlarAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'dekan')
    search_fields = ('nomi', 'dekan__ism', 'dekan__familiya')
    list_filter = ('nomi',)

# --- Register ---
admin.site.register(Foydalanuvchilar, FoydalanuvchilarAdmin)
admin.site.register(Kafedralar, KafedralarAdmin)
admin.site.register(oquvIshlari)
admin.site.register(ilmiy_ishlari)
admin.site.register(Dekanatlar, DekanatlarAdmin)
