from django.contrib import admin
from zoomgrid.models import Grid
from zoomgrid.models import GridColumn
from zoomgrid.models import GridRow
from zoomgrid.models import GridCell
from zoomgrid.models import GridCellEntry

admin.site.register(Grid)
admin.site.register(GridColumn)
admin.site.register(GridRow)
admin.site.register(GridCell)
admin.site.register(GridCellEntry)