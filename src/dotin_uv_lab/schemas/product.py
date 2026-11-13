"""Pydantic schemas for product input data."""

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    """Validated data required to request creation of a catalog product."""

    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    name: str = Field(min_length=1, max_length=120)
    price: float = Field(ge=0, allow_inf_nan=False)
    stock: int = Field(ge=0)
    category: str = Field(min_length=1, max_length=60)
    description: str | None = Field(default=None, max_length=500)
    tags: list[str] = Field(default_factory=list)
    is_active: bool = True
