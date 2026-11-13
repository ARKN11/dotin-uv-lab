"""Application entry point for the current learning-stage demo."""

import logging

from dotin_uv_lab.products.operations import create_sample_product
from dotin_uv_lab.services.order_service import build_order_summary
from dotin_uv_lab.settings import Settings
from dotin_uv_lab.customers.models import Customer
from dotin_uv_lab.products.models import Product

logger = logging.getLogger(__name__)


def configure_logging(debug: bool = False) -> None:
    """Configure application-wide logging once at the entry point."""
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def main() -> None:
    """Load configuration and run the small application demonstration."""
    settings = Settings()
    configure_logging(settings.debug)

    customer = Customer(customer_id=1, name="Amir")
    product = Product(product_id=1, name="Laptop", price=1200.00)
    sample_product = create_sample_product()

    logger.info("Application started: %s", settings.app_name)
    logger.info(
        "Database configuration loaded for host %s on port %s",
        settings.database_host,
        settings.database_port,
    )
    logger.info("Sample product created: %s", sample_product.name)
    logger.info("Order summary:\n%s", build_order_summary(customer, product))


if __name__ == "__main__":
    main()
