"""Product-related application operations."""

import logging

from .models import Product

logger = logging.getLogger(__name__)


def create_sample_product(
    product_id: int = 101,
    name: str = "Keyboard",
    price: float = 75.50,
) -> Product:
    """Create and return a sample product for the learning demo."""
    try:
        product = Product(product_id, name, price)
    except (TypeError, ValueError):
        logger.exception("Product creation failed")
        raise

    logger.info("Product created: %s", product.name)
    return product
