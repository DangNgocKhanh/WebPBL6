# views.py
from rest_framework import viewsets, pagination ,filters
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework.decorators import action, parser_classes
import random
import string

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    # try:
        user =  User_Serializer(request.user).data
        data = {'status': status.HTTP_200_OK,'user':user}
        return Response(data, status=status.HTTP_200_OK)
    # except:
    #     data = {'status': status.HTTP_400_BAD_REQUEST,'error_mesage':'Lấy thông tin thất bại'}
    #     return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_suggest(request):
    # try:
        id_user = request.data['id_user']
        user = User.objects.get(pk=int(id_user))

        latest_order = Oder.objects.filter(User=user).order_by('-id').first()

        oder_detail_list = Oder_detail.objects.filter(Oder=latest_order)

        code_ai_list = []
        for i in oder_detail_list:
             code_ai_list.append(i.Product.Category.Code_ai)

        print('Chjashd',code_ai_list)

        # Loại bỏ các phần tử trùng lặp từ danh sách Code_ai
        unique_code_ai_list = list(set(code_ai_list))

        print('Unique Code_ai List:', unique_code_ai_list)

        # Lấy danh sách Category từ các mã Code_ai duy nhất
        category_queryset = Category.objects.filter(Code_ai__in=unique_code_ai_list)

        print('Unique Code_ai List:',  category_queryset)

        # Lấy danh sách Product có Category trong danh sách Category đã lọc
        List_Product = Product.objects.filter(Category__in=category_queryset)
        List_Product = Product_Serializer(List_Product,many=True).data
        print('Unique Code_ai List:',  List_Product)
        # # data = List_Product
        data = List_Product
        return Response(data, status=status.HTTP_200_OK)
    # except:
    #     data = {'status': status.HTTP_400_BAD_REQUEST,'error_mesage':'Lấy thông tin thất bại'}
    #     return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_detail_cart(request):
    # # try:        
        id_cart = request.data['id_cart']
        cart = Cart.objects.get(pk=int(id_cart))
        id_product = request.data['id_cart_detail']
        product = Product.objects.get(pk=int( id_product))
        dk = Cart_detail.objects.filter(Cart=cart,Product=product)
        if dk:
            print('sdhdshf')
        else:
            Cart_detail.objects.create(Cart=cart,Product=product)

            Cart_detail_list = Cart_detail.objects.filter(Cart=cart)
            cart.Total_amount = sum(orderdetail.Amount for orderdetail in Cart_detail_list)
            cart.Total_money = sum(orderdetail.Amount*orderdetail.Product.Price_has_decreased for orderdetail in Cart_detail_list)
            cart.save()
        data = {'status': status.HTTP_200_OK,}
        return Response(data, status=status.HTTP_200_OK)
    # except:
    #     data = {'status': status.HTTP_400_BAD_REQUEST,'error_mesage':'Lấy thông tin thất bại'}
    #     return Response(data, status=status.HTTP_400_BAD_REQUEST)


def generate_random_code():
    characters = string.digits + string.ascii_uppercase
    code_length = 10
    random_code = ''.join(random.choice(characters) for i in range(code_length))
    return random_code

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_Oder(request):
    # # try: 
        print('hgajjsdjhjashd')
        code = generate_random_code()

        id_cart = request.data['id_cart']
        cart = Cart.objects.get(pk=int(id_cart))

        id_user = request.data['id_user']
        user = User.objects.get(pk=int(id_user))


        oder = Oder.objects.create(Code=code,User=user)

        print('hsaghsdag')


        Cart_detail_list = Cart_detail.objects.filter(Cart=cart)
        oder.Total_amount = sum(orderdetail.Amount for orderdetail in Cart_detail_list)
        oder.Total_money = sum(orderdetail.Amount*orderdetail.Product.Price_has_decreased for orderdetail in Cart_detail_list)
        oder.save()

        for i in Cart_detail_list:
            Oder_detail.objects.create(Oder=oder,Product=i.Product,Amount=i.Amount)

        data = {'status': status.HTTP_200_OK,}
        return Response(data, status=status.HTTP_200_OK)

    # except:
    #     data = {'status': status.HTTP_400_BAD_REQUEST,'error_mesage':'Lấy thông tin thất bại'}
    #     return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_amount(request):
    id_dk = request.data['id_dk']
    amount  = request.data['amount']
    id_cart = request.data['id_cart']
    cart = Cart.objects.get(pk=int(id_cart))
    if amount:
        dk = Cart_detail.objects.get(pk=int(id_dk))
        dk.Amount = amount
        dk.save()

        cart = Cart.objects.get(pk=int(id_cart))
        Cart_detail_list = Cart_detail.objects.filter(Cart=cart)
        cart.Total_amount = sum(orderdetail.Amount for orderdetail in Cart_detail_list)
        cart.Total_money = sum(orderdetail.Amount*orderdetail.Product.Price_has_decreased for orderdetail in Cart_detail_list)
        cart.save()

    data = {'status': status.HTTP_200_OK,}
    return Response(data, status=status.HTTP_200_OK)

class User_ViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer
    # parser_classes = [MultiPartParser,FormParser]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['Name']
    ordering_fields = ['Name']  # Các trường bạn muốn cho phép sắp xếp
    search_fields = ['Name']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang

    def perform_create(self, serializer):
        # Mã hóa mật khẩu trước khi lưu vào cơ sở dữ liệu
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = hashed_password

        # Gọi perform_create của lớp cha để hoàn thành quá trình tạo bản ghi
        super().perform_create(serializer)
        user_instance = serializer.data
        print(user_instance['id'])
        user = User.objects.get(pk=2)
        print(user)
        # Tạo giỏ hàng cho người dùng mới
        Cart.objects.create(User=User.objects.get(pk=int(user_instance['id'])))

        return user_instance

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        # Tạo serializer với partial=True để cập nhật các trường có sẵn trong dữ liệu mới
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Lấy mật khẩu và avatar từ dữ liệu mới
        new_password = data.get('password', None)
        new_avatar = data.get('Avatar', None)

        # Kiểm tra xem mật khẩu có tồn tại trong dữ liệu mới hay không
        if new_password:
            hashed_password = make_password(new_password)
            instance.password = hashed_password

        # Kiểm tra xem avatar có tồn tại trong dữ liệu mới hay không
        if new_avatar:
            instance.Avatar = new_avatar

        # Lưu các thay đổi vào cơ sở dữ liệu
        instance.save()

        # Tiếp tục thực hiện các bước khác của phương thức cập nhật mặc định
        return super().partial_update(request, *args, **kwargs)

class Category_ViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['Name']
    ordering_fields = ['Name']  # Các trường bạn muốn cho phép sắp xếp
    search_fields = ['Name']
    # pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    # page_size = 15  # Số lượng mục trên mỗi trang

class Trademark_ViewSet(viewsets.ModelViewSet):
    queryset = Trademark.objects.all()
    serializer_class = Trademark_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['Name']
    ordering_fields = ['Name']  # Các trường bạn muốn cho phép sắp xếp
    search_fields = ['Name']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang

class Made_ViewSet(viewsets.ModelViewSet):
    queryset = Made.objects.all()
    serializer_class = Made_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['Name']
    ordering_fields = ['Name']  # Các trường bạn muốn cho phép sắp xếp
    search_fields = ['Name']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang

class Product_ViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['Category__Name','Trademark__Name','Made__Name']
    ordering_fields = ['Name']  # Các trường bạn muốn cho phép sắp xếp
    search_fields = ['Name']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang

class Stock_ViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = Stock_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['Product__Name']
    ordering_fields = ['Product__Name']  # Các trường bạn muốn cho phép sắp xếp
    search_fields = ['Product__Name']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang

class Goods_received_note_ViewSet(viewsets.ModelViewSet):
    queryset = Goods_received_note.objects.all()
    serializer_class = Goods_received_note_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['Product__Name']
    ordering_fields = ['Product__Name']  # Các trường bạn muốn cho phép sắp xếp
    search_fields = ['Product__Name']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang


class Cart_ViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = Cart_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    # filterset_fields = ['User__Name']
    # ordering_fields = ['User__Name']  # Các trường bạn muốn cho phép sắp xếp
    # search_fields = ['User__Name']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang

class Cart_detail_ViewSet(viewsets.ModelViewSet):
    queryset = Cart_detail.objects.all()
    serializer_class = Cart_detail_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    # filterset_fields = ['Product__Name']
    # ordering_fields = ['Product__Name']  # Các trường bạn muốn cho phép sắp xếp
    # search_fields = ['Product__Name']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang

class Oder_ViewSet(viewsets.ModelViewSet):
    queryset = Oder.objects.all()
    serializer_class = Oder_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['Code']
    ordering_fields = ['Code']  # Các trường bạn muốn cho phép sắp xếp
    search_fields = ['Code']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang

class Oder_detail_ViewSet(viewsets.ModelViewSet):
    queryset = Oder_detail.objects.all()
    serializer_class = Oder_detail_Serializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['Oder__Code']
    ordering_fields = ['Oder__Code']  # Các trường bạn muốn cho phép sắp xếp
    search_fields = ['Oder__Code']
    pagination_class = pagination.PageNumberPagination  # Chọn loại phân trang
    page_size = 15  # Số lượng mục trên mỗi trang
