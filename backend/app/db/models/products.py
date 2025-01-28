from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy import String, Float, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from backend.app.db.models.base import Base, BaseDBModel


class ProductCategory(Base, BaseDBModel):
    """
    Product category model
    """

    name: Mapped[str] = mapped_column(String, unique=True)


class Product(Base, BaseDBModel):
    """
    Product model
    """

    name: Mapped[str] = mapped_column(String, nullable=False)
    cost: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    photo = image_attachment('ProductPicture')
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('category.id'), nullable=False)
    category = relationship('Category', back_populates="products")
    seller_id: Mapped[int] = mapped_column(Integer, ForeignKey('seller.id'), nullable=False)
    seller = relationship('Seller', back_populates="products")


class ProductPicture(Base, Image):
    """
    Product picture model
    """

    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates="photoes")


class ProductReview(Base, BaseDBModel):
    """
    Product review model
    """

    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship('Product', back_populates="reviews")
    photo = image_attachment('ProductReviewPicture')


class ProductReviewPicture(Base, Image):
    """
    Product picture model
    """

    product_review_id: Mapped[int] = mapped_column(Integer, ForeignKey('productreview.id'), nullable=False)
    product_review = relationship('ProductReview', back_populates="photoes")
