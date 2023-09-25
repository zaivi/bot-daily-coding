import os
from loguru import logger

from model import notify
from config.config import Config
from utils.notify import notify_fn
from constants.base import TaskErrorMessage



"""Main module."""
if __name__ == "__main__":
    b = notify.NewNotify(
        cfg=Config(
            WebhookSlackLeetCode=os.environ["WEBHOOK_SLACK_LEETCODE"],
            TagsSlackLeetCode="<@channel>"
        ), 
        statisticalDomain="test"
    )
    err = notify_fn.ProcessNotifyDailyLeetCodingChallenge(b=b)

    if err is not None:
        logger.warning(TaskErrorMessage.format("ProcessNotifyDailyLeetCodingChallenge", err))
