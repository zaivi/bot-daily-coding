from enum import Enum
from typing import Optional, List, Dict, Union
from pydantic import BaseModel, Field, ConfigDict, validator, computed_field

from model.slack import TextMessageDailyCodingChallenge, SlackEnum



class LeetCodeEnum(Enum):
    Body = "\n    query questionOfToday {\n  activeDailyCodingChallengeQuestion {\n    date\n    userStatus\n    link\n    question {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      hasVideoSolution\n      hasSolution\n      topicTags {\n        name\n        id\n        slug\n      }\n    }\n  }\n}\n    "
    Payload = '{"query": "\n    query questionOfToday {\n  activeDailyCodingChallengeQuestion {\n    date\n    userStatus\n    link\n    question {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      hasVideoSolution\n      hasSolution\n      topicTags {\n        name\n        id\n        slug\n      }\n    }\n  }\n}\n    ", "variables": {}}'
    URLGraphql = "https://leetcode.com/graphql"
    ArrayUserAgent = [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",
        "Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4",
        "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
        "Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16",
        "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4",
        "Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
        "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020b Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-N910T Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36"
    ]
    FormatLinkLeetCode    = "https://leetcode.com{}"
    FormatTextLeetCode    = "{}\n{}"
    FormatBoldTextLeetCode    = "*{}*\n{}"
    FormatLinkTagLeetCode = "https://leetcode.com/tag/{}"
     

class TopicTag(BaseModel):
    name: str = Field(..., descriptio="Topic name")
    id: str = Field(..., descriptio="Topic ID")
    slug: str = Field(..., descriptio="URL topic tag")


class ChallengeQuestion(BaseModel):
    acRate: float = Field(..., description="")
    difficulty: str = Field(..., description="Difficulty of question")
    freqBar: str = Field(..., description="")
    frontendQuestionId: str = Field(..., description="")
    isFavor: bool = Field(..., description="")
    paidOnly: bool = Field(..., description="")
    status: str = Field(..., description="")
    title: str = Field(..., description="")
    titleSlug: str = Field(..., description="")
    hasVideoSolution: bool = Field(..., description="")
    hasSolution: bool = Field(..., description="")
    topicTags: List[TopicTag] = Field(..., description="List of topic tags")
    
    @validator("*", pre=True)
    def replace_none(cls, v):
        if type(v) is bool:
            return v
        return v or "None"


class LeetCodeChallenge(BaseModel):
    date: str = Field(..., description="Creation challenge date")
    userStatus: str = Field(..., description="User status")
    link: str = Field(..., description="Challenge link")
    question: ChallengeQuestion = Field(..., description="Challenge question")


class ParamDailyCodingChallenge(BaseModel):
    Body: str

    @computed_field
    @property
    def Payload(cls) -> dict:
        return dict({"query": cls.Body, "variables": {}})


def ToTextMessageDailyCodingChallenge(d: LeetCodeChallenge) -> TextMessageDailyCodingChallenge:
    if d == None:
        return None

    textMsg = TextMessageDailyCodingChallenge(
        Title=d.question.frontendQuestionId + ". " + d.question.title,
        Date=d.date,
        Difficulty=d.question.difficulty,
        Link=LeetCodeEnum.FormatLinkLeetCode.value.format(d.link),
        TopicTags=""
    )
    
    topicTags = []

    for _, val in enumerate(d.question.topicTags):
        tagLink = LeetCodeEnum.FormatLinkTagLeetCode.value.format(val.slug)
        topicTags.append(SlackEnum.FormatTextLinkSlack.value.format(tagLink, val.name))

    textMsg.TopicTags = ", ".join(topicTags)

    return textMsg
