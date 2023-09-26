import random
import requests

from loguru import logger
from typing import Tuple
from http import HTTPStatus
from exceptions import base

from model import leetcode
from utils.leetcode import config



# Debug logging
# import logging
# import http.client as httplib
# httplib.HTTPConnection.debuglevel = 1
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# req_log = logging.getLogger('requests.packages.urllib3')
# req_log.setLevel(logging.DEBUG)
# req_log.propagate = True



def getDailyCodingChallenge(url: str, params: leetcode.ParamDailyCodingChallenge) -> Tuple[leetcode.LeetCodeChallenge, base.CustomException]:
    logger.info("Get daily leetcoding challenge")

    headers = config.ssi_headers
    headers["user-agent"] = leetcode.LeetCodeEnum.ArrayUserAgent.value[random.randint(0,len(leetcode.LeetCodeEnum.ArrayUserAgent.value)-1)]

    try:
        response = requests.request("POST", url, headers=headers, json=params.Payload)
        
        if response.status_code == HTTPStatus.OK:
            response_data = response.json()

        elif response.status_code == HTTPStatus.BAD_REQUEST:
            logger.debug(response)
            logger.error("Error in API response")
            logger.error(base.BadRequestException.message)

            return None, base.BadRequestException
        elif response.status_code == HTTPStatus.NOT_FOUND:
            logger.debug(response)
            logger.error("Error in API response")
            logger.error(base.NotFoundException.message)

            return None, base.NotFoundException
        else:
            logger.debug(response)
            logger.error("Error in API response")
            logger.error(base.CustomException.message)

            return None, base.CustomException
        
        codeChallenge = leetcode.LeetCodeChallenge(**response_data["data"]["activeDailyCodingChallengeQuestion"])
        logger.debug(codeChallenge)
        
    except Exception as e:
        logger.error(str(e))
        return None, e

    logger.info("Successfully get daily leetcoding challenge information...")

    return codeChallenge, None
        