from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomAdministrationManager(UserManager):
    pass


# 내부 관리자 모델
# 실제 백엔드 조작에 관여하는 Admin 사용자
class AdministrationUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성일시")
    updated = models.DateTimeField(auto_now=True, verbose_name="수정일시")

    objects = CustomAdministrationManager()

    class Meta:
        verbose_name = '관리자'
        verbose_name_plural = '관리자'


class User(AbstractBaseUser):
    username = None
    last_login = None
    USERNAME_FIELD = 'internal_uuid'
    REQUIRED_FIELDS = []

    gender_choice = (
        ("F", "여자"),
        ("M", "남자")
    )
    user_type_choices = (
        # 본인인증을 진행한
        # 모든 행위가 가능한 계정
        ('main', '메인계정'),
        # 메인계정에 딸린
        # 멀티프로필 개념의 계정임
        ('sub', '서브계정'),
        # 게스트모드(클라이밋)
        ('guest', '게스트계정'),
    )
    # 고유식별 uuid(internal)
    # 사용할지 안할지 모르겠지만
    # 이 컬럼은 유저 기본 고유식별 키로서 기능을 할 예정
    internal_uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        editable=False
    )

    # 고유식별 uuid(external)
    # 외부에 노출될 용도의
    # 개인 식별키
    # 특정 본인인증시 클라이언트와 통신용도로
    # 사용할 예정이며 외부에 노출되더라도
    # 전혀 개인정보접근에 영향이 가지않게할 예정이다.
    external_uuid = models.UUIDField(
        default=uuid4,
        unique=True,
    )

    # 유저타입
    user_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=user_type_choices
    )

    # 이메일(id)
    # 이메일을 고유 ID처럼 쓰려고 했지만
    # 이메일은 조건부 유니크하게 구현해야한다.
    # 회원가입할 당시에 활성화된 이메일은 unique할 수 없으나,
    # 탈퇴계정의 email은 unique하지 않아도 된다.
    email = models.EmailField(
        _('email address'),
        blank=True,
        null=True,
        # unique=True,
    )

    # 비밀번호
    password = models.CharField(
        _('password'),
        max_length=128,
        blank=True,
        null=True,
    )

    # 폰번호
    # DB 제약조건으로 비어있을 수는 있지만
    # 실제 앱에서 API로 값을 받을때는
    # 반드시 받아야하는 데이터임
    # unique여야 하는 값이지만,
    # 실제 서비스운영중에 유니크할 필요는 없다.
    # 개인식별은 본인인증을통해 발급받은 unique_key를 통해 할것이기때문.
    phone = models.CharField(
        max_length=11,
        verbose_name="휴대전화번호",
        blank=True,
        null=True,
    )
