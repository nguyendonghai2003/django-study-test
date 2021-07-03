from django.db import models
from django.utils import timezone


# Create your models here.
class Machine(models.Model):
    machine_code = models.CharField(verbose_name="Mã máy", max_length=20)
    location = models.CharField(verbose_name="Nhà máy", max_length=50)
    machine_name = models.CharField(verbose_name="Tên Máy", max_length=200)
    clamping_force = models.IntegerField(verbose_name="Số Tấn", null=False)
    robot = models.CharField(verbose_name="Tay Robot", max_length=200, blank = True)
    dry_machine = models.CharField(verbose_name="Máy Sấy Nhựa", max_length=200, blank = True)
    hot_water = models.CharField(verbose_name="Máy Nước Nóng", max_length=200, blank = True)
    covey_bell = models.CharField(verbose_name="Băng Tải", max_length=100, blank = True)
    update_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return (self.location + " - " + self.machine_code)


class Mold(models.Model):
    mold_code = models.CharField(verbose_name="Mã Khuôn", max_length=200)
    check_machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    mold_weight = models.IntegerField(verbose_name="Trọng Lượng Khuôn")
    cavity = models.IntegerField(verbose_name="Số Cavity Nghiệm thu")

    def __str__(self):
        return (self.mold_code)


class Product(models.Model):
    product_code = models.CharField(verbose_name="Mã Sản Phẩm", max_length=200)
    product_name = models.CharField(verbose_name="Tên Sản Phẩm Đầy Đủ", max_length=200)
    customer = models.CharField(verbose_name="Khách Hàng", max_length=200)
    mold_code = models.ForeignKey(Mold,verbose_name="Mã Khuôn",  on_delete=models.CASCADE)
    shot_weight = models.FloatField(verbose_name="Trọng Lượng Shot")
    product_weight = models.FloatField(verbose_name="Trọng Lượng Sản Phẩm")
    NG_rate = models.FloatField(verbose_name='Tỷ lệ NG cho phép', default=0.03)
    max_day = models.IntegerField(verbose_name="SL Max day", blank = False, null = False)
    production_cycle = models.FloatField(verbose_name="Chu kỳ Chuẩn")
    
    def __str__(self):
        return (self.product_code + " - " + self.product_name)

class Dailyproduction(models.Model):
    production_date = models.DateField(default = timezone.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    cavity = models.IntegerField(verbose_name="Số Cavity SX", null = False)
    production_time = models.IntegerField(verbose_name="Thời gian SX")
    product_cycle = models.FloatField(verbose_name="Chu kỳ sản xuất")
    good_quantity = models.IntegerField(verbose_name="Số lượng OK", null = False)
    NG_quantity = models.IntegerField(verbose_name="Số lượng hàng NG")

    def __str__(self):
        return (self.production_date + " - " + self.product.product_code)
