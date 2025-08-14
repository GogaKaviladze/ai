import structlog
from rq import Connection, Worker
import redis

from app.core.config import settings

logger = structlog.get_logger()


def run() -> None:
    redis_conn = redis.from_url(settings.redis_url)
    with Connection(redis_conn):
        worker = Worker(['default'])
        logger.info("worker.start")
        worker.work()


if __name__ == "__main__":
    run()
