from django.db import models


class Organization(models.Model):
	name = models.CharField(max_length=16)


class Groupo(models.Model):
	name = models.CharField(max_length=16)


class User(models.Model):
	name = models.CharField(max_length=16)
	local_id = models.CharField(max_length=128)
	password = models.CharField(max_length=16)
	groups = models.ForeignKey(Groupo, on_delete=models.CASCADE)
	organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Printer(models.Model):
	name = models.CharField(max_length=16)
	owner = models.CharField(max_length=16)
	driver_name = models.CharField(max_length=64)
	port_name = models.CharField(max_length=64)
	organization = models.CharField(max_length=16)
	registered_in = models.DateTimeField('date published')
	last_seen = models.CharField(max_length=16)


class PrinterOuts(models.Model):
	registered_in = models.DateTimeField('date published')
	#File Props
	document_name = models.CharField(max_length=256)
	job_status = models.IntegerField(default=0)
	size = models.IntegerField(default=0)
	total_pages = models.IntegerField(default=0)
	local_user_name = models.CharField(max_length=32)
	printer_name = models.CharField(max_length=64)
	upload_by = models.ForeignKey(User, on_delete=models.CASCADE)

