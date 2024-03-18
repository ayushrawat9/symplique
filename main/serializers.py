from rest_framework import serializers
from main.models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['date', 'time', 'message', 'reminder_type']
        # read_only_fields = [
        #     'date', 'time', 'message', 'reminder_type'
        # ]