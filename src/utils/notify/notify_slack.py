import ast
import json
import requests
from http import HTTPStatus

from loguru import logger

from model import slack, leetcode
from exceptions import base
from utils.notify.config import ssi_headers



def sendMessage(webhook: str, slackMessage: slack.SlackMessage) -> base.CustomException:
    logger.info("Send message to webhook ", webhook)
    
    try:
        slack_dict = slackMessage.model_dump()

        slack_msg = json.dumps(slack_dict)

        logger.debug(slack_msg)

        slack_text = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": slack_dict["text"]
                    }
                },
                {
                    "type": "section",
                    "block_id": "section789",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": leetcode.LeetCodeEnum.FormatBoldTextLeetCode.value.format(slack_dict["attachments"]["Fields"][1]["Title"], slack_dict["attachments"]["Fields"][1]["Value"])
                        },
                        {
                            "type": "mrkdwn",
                            "text": leetcode.LeetCodeEnum.FormatBoldTextLeetCode.value.format(slack_dict["attachments"]["Fields"][2]["Title"], slack_dict["attachments"]["Fields"][2]["Value"])
                        },
                        {
                            "type": "mrkdwn",
                            "text": leetcode.LeetCodeEnum.FormatBoldTextLeetCode.value.format(slack_dict["attachments"]["Fields"][4]["Title"], slack_dict["attachments"]["Fields"][4]["Value"])
                        },
                        {
                            "type": "mrkdwn",
                            "text": leetcode.LeetCodeEnum.FormatBoldTextLeetCode.value.format(slack_dict["attachments"]["Fields"][3]["Title"], slack_dict["attachments"]["Fields"][3]["Value"])
                        }
                    ]
                }
            ]
        }

        response = requests.post(webhook, headers=ssi_headers, json=slack_text)

        logger.debug(response.request.body)

        if response.status_code == HTTPStatus.OK:
            response_data = response.content

        else:
            logger.debug(response.request.body)
            logger.debug(response.content)
            logger.error(base.BadRequestException(message="Notification failure").message)

        logger.info("Successfully sent notification...", webhook)

        return None
        
    except Exception as e:
        return base.NotFoundException(message=str(e)).message


def sendSlackMessage(webhook: str, slackMessage: slack.SlackMessage) -> base.CustomException:
    if webhook is None:
        return base.NotFoundException(message="Missing channel url")
    
    for i in range(5):
        err = sendMessage(webhook, slackMessage)
        
        logger.error(err)

        if err is None:
            return
        
    return err
