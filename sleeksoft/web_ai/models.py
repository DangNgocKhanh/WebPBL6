from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.

class User(AbstractUser):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Quản lý tài khoản Đăng nhập"
	AbstractUser._meta.get_field('email').blank = False
	AbstractUser._meta.get_field('email').null = False
	AbstractUser._meta.get_field('username').blank = False
	AbstractUser._meta.get_field('username').null = False
	AbstractUser._meta.get_field('password').blank = False
	AbstractUser._meta.get_field('password').null = False

	Name = models.CharField('Tên khách hàng',max_length=255,default='',blank=True, null=True)
	Phone = models.CharField('Số điện thoại khách hàng',default='',max_length=15, blank=True, null=True)
	Address = models.CharField('Địa chỉ khách hàng',default='',max_length=255, blank=True, null=True)
	Birthday = models.DateField('Ngày sinh khách hàng',blank=True, null=True)
	Avatar = models.ImageField(upload_to='User_image',null=True,blank=True)
	update_time = models.DateTimeField(auto_now=True)
	
class Category(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "1 - Danh mục sản phẩm"

	Name = models.CharField('Tên danh mục',max_length=100, null=True, blank=True)
	Code_ai = models.CharField('Mã thông minh',max_length=100, null=True, blank=True)
	Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.Name)
	
class Trademark(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "2 - Thương hiệu"
	Avatar = models.ImageField('Ảnh đại diện',upload_to='Trademark_image',null=True,blank=True)
	Name = models.CharField('Tên thương hiệu',max_length=100, null=True, blank=True)
	Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.Name)
	
class Made(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "3 - Quốc gia sản xuất"
	Avatar = models.ImageField('Ảnh đại diện',upload_to='Made_image',null=True,blank=True)
	Name = models.CharField('Tên quốc gia',max_length=100, null=True, blank=True)
	Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.Name)
	

class Product(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "4 - Sản phẩm bán"

	Avatar = models.ImageField('Ảnh đại diện',upload_to='Product_image',null=True,blank=True)
	Name = models.CharField('Tên sản phẩm',max_length=100, null=True, blank=True)
	Code = models.CharField('Mã sản phẩm',max_length=100, null=True, blank=True)
	Category  = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Product_Category')
	Trademark = models.ForeignKey(Trademark, on_delete=models.CASCADE, related_name='Product_Trademark')
	Made = models.ForeignKey(Made, on_delete=models.CASCADE, related_name='Products_Made')
	Price = models.IntegerField('Giá sản phẩm', null=True, blank=True)
	Percent_discount = models.IntegerField('Phần trăm giảm giá (%)',default=10, null=True, blank=True)
	Price_has_decreased = models.IntegerField('Giá sau khi giảm',default=10, null=True, blank=True)
	Describe = models.TextField('Mô tả',null=True, blank=True)
	Guarantee = models.CharField('Bảo hành',max_length=100, null=True, blank=True)
	Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.Name)
	
class Stock(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "5 - Kho hàng"

	Product = models.OneToOneField(Product,on_delete=models.CASCADE)
	Amount = models.CharField('Số lượng',max_length=100, null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.product_id)
	
class Goods_received_note(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "6 - Phiếu nhập hàng"

	Stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='Goods_received_note_Stock')
	Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Goods_received_note_Product')
	Code = models.CharField('Mã phiếu',max_length=100, null=True, blank=True)
	input = models.IntegerField('Số lượng nhập', null=True, blank=True)
	Total = models.IntegerField('Giá trị đơn nhập', null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.stock_id)

class Cart(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "7 - Giỏ hàng của khách hàng"

	User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Cart_User')
	Total_amount = models.CharField('Tổng số lượng',max_length=100, null=True, blank=True)
	Total_money = models.CharField('Tổng giá trị',max_length=100, null=True, blank=True)
	Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.User.username)
	
class Cart_detail(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "8 - Các đơn hàng được thêm vào giỏ hàng"

	Cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='Cart_detail_Cart')
	Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Cart_detail_Product')
	Amount = models.IntegerField('Số lượng mua',default=1,null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.Amount)
	
class Oder(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "9 - Đơn hàng hàng của khách hàng"

	Code = models.CharField('Mã đơn hàng',max_length=100, null=True, blank=True)
	User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Oder_User')
	Total_amount = models.CharField('Tổng số lượng',max_length=100, null=True, blank=True)
	Total_money = models.CharField('Tổng giá trị',max_length=100, null=True, blank=True)
	Status = models.CharField('Trạng thái',default='Đang chờ xác nhận',max_length=100, null=True, blank=True)
	Url = models.CharField('Đường dẫn',max_length=100, null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.Code)
	
class Oder_detail(models.Model):
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "91 - Chi tiết các mặt hàng trong đơn hàng"

	Oder = models.ForeignKey(Oder, on_delete=models.CASCADE, related_name='Oder_detail_Oder')
	Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Oder_detail_Product')
	Amount = models.IntegerField('Số lượng mua',null=True, blank=True)
	Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
	Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

	def __str__(self):	
		return str(self.Oder.Code)