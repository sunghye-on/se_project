from django.db import models 
    
# Create your models here.
class Table(models.Model):
    table_num = models.IntegerField(blank = False)
    table_name= models.CharField(max_length = 15, default = "??번 테이블")
    max = models.IntegerField(default = 4)    #최대 수용인원
    able = models.BooleanField(default=True) # 사용 가능한 테이블인지 (예약되어 있어 사용불가능한 것이 아니고 망가진것)
    def __str__(self):
        return self.table_name
    
    
    

    