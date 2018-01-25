from firstlove.helpers import file_manager


def export_to_csv(modeladmin, request, queryset):
    file_name = modeladmin.model.__name__
    
    return file_manager.download_as_csv(request, queryset, file_name)

export_to_csv.short_description = 'Export to csv'