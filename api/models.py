from django.db import models

# Create your models here.

#For each printer
class Printer(models.Model):
    printer_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)

    def __unicode__(self):
	   return str(self.description)	    
    
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=40)
    user_total_counter = models.IntegerField()
    user_counter_print_bw = models.IntegerField()
    user_counter_print_color = models.IntegerField()
    user_counter_copy_bw = models.IntegerField()
    user_counter_copy_color = models.IntegerField()
    printers = models.ManyToManyField(Printer)

    def __unicode__(self):
    	return str(self.user_name)

class PrinterLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    global_counter = models.IntegerField()
    counter_print_bw = models.IntegerField()
    counter_print_color = models.IntegerField()
    counter_copy_bw = models.IntegerField()
    counter_copy_color = models.IntegerField()
    fk_printer = models.ForeignKey(Printer)

    def __unicode__(self):
        return str(self.fk_printer)