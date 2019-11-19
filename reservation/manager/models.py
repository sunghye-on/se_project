from django.db import models

# Create your models here.
class table(models.Model):
    table_num = models.IntegerField()
    max = models.IntegerField(default = 4)    #최대 수용인원
    able = models.BooleanField(default=True) # 사용 가능한 테이블인지 (예약되어 있어 사용불가능한 것이 아니고 망가진것)
