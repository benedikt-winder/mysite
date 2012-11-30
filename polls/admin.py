from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    # Bestimmte Reihenfolge
    #fields = ['pub_date', 'question']
    
    # Welche Elemente in der Uebersicht angezeigt werden
    list_display = ('question', 'pub_date', 'was_published_recently')
    
    # Fuegt eine Filterbox rechts hinzu
    list_filter = ['pub_date']
    
    # Suche ermoeglichen
    search_fields = ['question']
    
    # Auswahl des Jahres / Monats ...
    date_hierarchy = 'pub_date'
    
    # Mehre "Choices" gleichzeitig eingeben
    class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 3
    
    # Bereiche mit bestimmten Feldern
    fieldsets = [
        ('Ask the question', {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
