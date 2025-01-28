from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from backend.app.db.models.base import Base, BaseDBModel


class Seller(Base, BaseDBModel):
    """
    Seller model
    """

    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    photo = image_attachment('SellerPicture')
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    owner = relationship('User', back_populates="sellers")


class SellerPicture(Base, Image):
    """
    Seller picture model
    """

    seller_id: Mapped[int] = mapped_column(Integer, ForeignKey('seller.id'), nullable=False)
    seller = relationship('Seller', back_populates="photoes")
