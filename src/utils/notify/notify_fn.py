from loguru import logger

from typing import Optional, List, Dict, Union
from pydantic import BaseModel, Field, ConfigDict, validator

from exceptions import base
from model import leetcode, slack, notify
from constants.base import BeginningTaskMessage
from utils.leetcode.leetcode_fn import getDailyCodingChallenge
from utils.notify import notify_slack


def ProcessNotifyDailyLeetCodingChallenge(b: notify.Notify) -> base.CustomException:
    logger.info(BeginningTaskMessage, "ProcessNotifyDailyLeetCodingChallenge")

    dailyCodingChallenge, err = getDailyCodingChallenge(url=leetcode.LeetCodeEnum.URLGraphql.value, params=leetcode.ParamDailyCodingChallenge(
        Body=str(leetcode.LeetCodeEnum.Body.value)
    ))

    if err is not None:
        logger.error("Get daily leetcoding challenge information from leetcode.com fail {}".format(err))
        return err

    textMsgDailyCodingChallenge = leetcode.ToTextMessageDailyCodingChallenge(dailyCodingChallenge)

    message = slack.SlackMessage(
        text=leetcode.LeetCodeEnum.FormatTextLeetCode.value.format(
            b.cfg.TagsSlackLeetCode, 
            "This is the leetcoding challenge for today: " + "*" + dailyCodingChallenge.question.title + "*"
        ),
        attachments=slack.toAttachment(textMsgDailyCodingChallenge)
    )
    
    # logger.debug(message)

    return notify_slack.sendSlackMessage(b.cfg.WebhookSlackLeetCode, message)
