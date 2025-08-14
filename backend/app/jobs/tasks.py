import structlog

logger = structlog.get_logger()


def handle_contact(contact_id: int) -> None:
    logger.info("contact.received", id=contact_id)
