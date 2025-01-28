from pydantic import BaseModel


class BaseSchema(BaseModel):
    """Base pydantic schema for domain models.

    Share common logic here.
    """
    pass


class IDSchemaMixin(BaseModel):
    """Base pydantic schema to be inherited from by database schemata."""
    id: int

    class Config(BaseModel.Config):
        # allow database schematas mapping to ORM objects
        orm_mode = True