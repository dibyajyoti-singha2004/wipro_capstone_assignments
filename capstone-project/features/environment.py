"""Behave hooks — run before/after features, scenarios, and steps."""

from datetime import datetime
from framework.logger import get_logger

logger = get_logger()


def before_all(context):
    logger.info("=" * 60)
    logger.info("CAPSTONE — API AUTOMATION FRAMEWORK")
    logger.info(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 60)


def before_scenario(context, scenario):
    logger.info(f"▶ Scenario: {scenario.name}")
    context.response = None


def after_scenario(context, scenario):
    logger.info(f"  [{scenario.status.name.upper()}] {scenario.name}")


def after_all(context):
    logger.info("=" * 60)
    logger.info(f"Finished: {datetime.now().strftime('%H:%M:%S')}")
    logger.info("=" * 60)