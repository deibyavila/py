"""importo modelo de de clente para poder
 adminsitrar al data delsde el admin"""
 
from django.contrib import admin
from clientes.models import Tercero
# Register your models here.

#forma trdicionañ de mostrar el admin de perfil
#admin.site.register(Tercero)

#creo nueva foram de mosrtar perfil
@admin.register(Tercero)
class TerceroAdmin(admin.ModelAdmin):
    list_display = ('pk','nit', 'primer_nombre','foto','email','activo')
    list_display_links = ('pk','nit','primer_nombre')
    search_fields = ('email','nit')
    list_filter = ('fecha_creacion','fecha_modificacion')

    fieldsets = (
        ('Datos Basicos',{
            'fields': ('nit',('primer_nombre','segundo_nombre'),('primer_apellido','segundo_apellido'),)
        }),
        ('Datos Extra',{
            'fields': (('activo','sexo'),'foto')
        }),
        ('MetaData',{
            'fields': (('fecha_creacion','fecha_modificacion'),)
        })
        
    )
    readonly_fields = ('fecha_creacion','fecha_modificacion',)