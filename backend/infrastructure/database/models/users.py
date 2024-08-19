import enum
from datetime import datetime
from decimal import Decimal
from typing import Optional
from sqlalchemy import (
    VARCHAR,
    BIGINT,
    false,
    true,
    TIMESTAMP,
    ForeignKey,
    DECIMAL,
)
from sqlalchemy.orm import Mapped, mapped_column

from .base import (
    Base,
    TableNameMixin,
    str_128,
    str_255,
    str_500,
    timestamp_now,
)


class User(Base, TableNameMixin):
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    full_name: Mapped[str_128]
    username: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    email: Mapped[Optional[str_255]] = mapped_column(unique=True)
    password_hash: Mapped[Optional[str_255]]
    is_premium: Mapped[bool] = mapped_column(server_default=false())

    created_at: Mapped[timestamp_now]
    last_login: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP)


class FreelancerProfession(enum.Enum):
    FULL_STACK_DEVELOPER = 'FULL_STACK_DEVELOPER'
    FRONTEND_DEVELOPER = 'FRONTEND_DEVELOPER'
    BACKEND_DEVELOPER = 'BACKEND_DEVELOPER'
    UI_DESIGNER = 'UI_DESIGNER'
    UX_DESIGNER = 'UX_DESIGNER'
    WEB_DESIGNER = 'WEB_DESIGNER'
    GRAPHIC_DESIGER = 'GRAPHIC_DESIGER'
    DATABASE_ADMINISTRATOR = 'DATABASE_ADMINISTRATOR'
    DEVOPS_ENGINEER = 'DEVOPS_ENGENEER'
    CLOUD_ARCHITECT = 'CLOUD_ARCHITECT'
    SYSTEM_ADMINISTRATOR = 'SYSTEM_ADMINISTRATOR'
    QA_ENGINEER = 'QA_ENGENEER'
    TEST_AUTOMATION_ENGEER = 'TEST_AUTOMATION_ENGEER'
    SECURITY_SPECIALIST = 'SECURITY_SPECIALIST'
    PERFOMANCE_ENGINEER = 'PERFOMANCE_ENGINEER'
    PROJECT_MANAGER = 'PROJECT_MANAGER'
    PRODUCT_MANAGER = 'PRODUCT_MANAGER'
    BUSINESS_ANALYST = 'BUSINESS_ANALYST'
    SEO_SPECIALIST = 'SEO_SPECIALIST'
    CONTENT_STRATEGIST = 'CONTENT_STRATEGIST'
    TECHNICAL_WRITER = 'TECHNICAL_WRITER'
    MOBILE_APP_DEVELOPER = 'MOBILE_APP_DEVELOPER'
    API_DEVELOPER = 'API_DEVELOPER'
    DATA_SCIENTIST = 'DATA_SCIENTIST'
    MACHINE_LEARNING_ENGINEER = 'MACHINE_LEARNING_ENGINEER'
    BLOCKCHEIN_DEVELOPER = 'BLOCKCHEIN_DEVELOPER'
    AR_VR_DEVELOPER = 'AR_VR_DEVELOPER'
    GAME_DEVELOPER = 'GAME_DEVELOPER'
    E_COMMERCE_SPECIALIST = 'E_COMMERCE_SPECIALIST'
    CMS_DEVELOPER = 'CMS_DEVELOPER'


class FreelancerProfile(Base, TableNameMixin):
    profile_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.user_id))
    portfolio_link: Mapped[str_255]
    profession: Mapped[FreelancerProfession]
    bio: Mapped[Optional[str_500]]
    hourly_rate: Mapped[Optional[Decimal]] = mapped_column(DECIMAL(10, 2))
    is_verified: Mapped[bool] = mapped_column(server_default=false())
    is_avaible: Mapped[bool] = mapped_column(server_default=true())

