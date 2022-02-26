from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
#
#####
# 유저 매니저 클래스
# 유저와 수퍼유저 생성시 호출된다. create_user()와 create_superuser()
#####
class UserManager(BaseUserManager):    
    
    use_in_migrations = True        

    def create_user(self, email, name, phone='', password=None):        
        
        user = self.model(            
            email = self.normalize_email(email),            
            name = name,
            phone = phone
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user     

    def create_superuser(self, email, name, password, phone='',  ):        
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            name = name,            
            password = password,
            phone = phone
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 

#####
# 새로운 유저 클래스
#####
class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()

		# 새롭게 추가할 필드들
    email = models.EmailField(max_length=255, null=False,unique=True)
    name = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=15, null=False)

    # 필수로 추가해야 할 필드들 (기본 유저 필드)
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)

		# 유저 생성 시 필수 입력 사항
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone']
