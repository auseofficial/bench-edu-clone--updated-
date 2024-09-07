from django.db import models

class Attendance(models.Model):
    ATTENDANCE_TYPES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
        ('Half-day', 'Half-day'),
    ]
    
    SHIFT_TYPES =[
        ('Morning','Morning'),
        ('Day','Day'),
    ] 
     
    attendance_date = models.DateField()
    shift = models.CharField(max_length=50, choices=SHIFT_TYPES)
    in_time = models.TimeField()
    out_time = models.TimeField()
    duration = models.DurationField() 
    attendance_type = models.CharField(max_length=20, choices=ATTENDANCE_TYPES)
    late_by_min = models.IntegerField(null=True, blank=True)
    early_gone_by_min = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.attendance_date} - {self.shift}"
