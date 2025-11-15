import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger("KnowledgeMate")

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)
