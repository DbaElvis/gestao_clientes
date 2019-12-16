from django.contrib import admin
from .models import Person, Documento

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados Complementares', {'fields': (('age', 'salary'),)}),
        ('Dados Opcionais', {'classes': ('collapse',),'fields': ('bio', 'photo')})
    )
    list_filter = ('age', 'salary')
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto')
    search_fields = ('id', 'first_name')
    autocomplete_fields = ('doc',)


    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_foto.short_description= 'Possui foto'


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']
