from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('attendance_date', 'shift', 'in_time', 'out_time', 'duration', 'attendance_type', 'late_by_min', 'early_gone_by_min')
    search_fields = ('attendance_date', 'shift', 'attendance_type')
    list_filter = ('attendance_date', 'shift', 'attendance_type')
