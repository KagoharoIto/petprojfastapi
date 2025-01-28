from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from backend.app.db.models.base import Base, BaseDBModel


class User(Base, BaseDBModel):
    """
    User model
    """

    nickname: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    second_name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    photo = image_attachment('UserPicture')


class UserPicture(Base, Image):
    """
    User picture model
    """

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates="photoes")
