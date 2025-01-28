"""Define metadata for tags used in OpenAPI documentation."""
from typing import Optional
from backend.app.models.base import BaseSchema


class ExternalDocs(BaseSchema):

    description: Optional[str] = None
    url: str


class MetaDataTag(BaseSchema):

    name: str
    description: Optional[str] = None
    external_docs: Optional[ExternalDocs] = None

    class Config:

        allow_population_by_field_name = True
        fields = {"external_docs": {"alias": "externalDocs"}}


users_tag = MetaDataTag(
    name="user",
    description="Stuff that you would want to know about this endpoint."
)

products_tag = MetaDataTag(
    name="product",
    description="Stuff that you would want to know about this endpoint."
)

sellers_tag = MetaDataTag(
    name="seller",
    description="Stuff that you would want to know about this endpoint."
)

metadata_tags = [users_tag, products_tag, sellers_tag]
