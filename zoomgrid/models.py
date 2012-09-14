from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GridElement(models.Model):
	label = models.CharField(max_length=50)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.label

	class Meta:
		abstract = True


class Grid(GridElement):
	owner = models.ForeignKey(User, null=True, blank=True)

class GridColumn(GridElement):
	grid = models.ForeignKey(Grid, blank=False, null=False)
	ordinal = models.IntegerField(blank=False, null=False)

class GridRow(GridElement):
	grid = models.ForeignKey(Grid, blank=False, null=False)
	ordinal = models.IntegerField(blank=False, null=False)

class GridCell(GridElement):
	grid = models.ForeignKey(Grid, blank=False, null=False)
	grid_column = models.ForeignKey(GridColumn, blank=False, null=False)
	grid_row = models.ForeignKey(GridRow, blank=False, null=False)

class GridCellEntry(models.Model):
	grid_cell = models.ForeignKey(GridCell, blank=False, null=False)
	ordinal = models.IntegerField(blank=False, null=False)
	content = models.TextField(blank=True)