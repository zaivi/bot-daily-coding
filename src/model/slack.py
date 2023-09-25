from enum import Enum
from typing import Optional, List, Dict, Union
from pydantic import BaseModel, Field, ConfigDict



class SlackEnum(Enum):
    FormatTextLinkSlack = "<{}|{}>"


class MessField(BaseModel):
    Short: bool = Field(..., description="")
    Title: str = Field(..., description="")
    Value: str = Field(..., description="")
    

class Attachment(BaseModel):
    Fields: List[MessField] = Field(..., description="")
    ImageUrl: str = Field("None", description="")


class TextMessageDailyCodingChallenge(BaseModel):
    Title: str = Field(..., description="Challenge Title")
    Date: str = Field(..., description="Challenge creation date")
    Difficulty: str = Field(..., description="Challenge Difficulty")
    Link: str = Field(..., description="Challenge URL resource")
    TopicTags: Optional[str] = Field(..., description="Challenge list of topic tags")


class SlackMessage(BaseModel):
    text: str = Field(..., description="")
    iconEmoji: str = Field("None", description="")
    attachments: Attachment = Field(..., description="")


def toAttachment(s: TextMessageDailyCodingChallenge) -> Attachment:
    fields = list()
    fields.append(MessField(
        Short=True,
        Title="Title",
        Value=s.Title
    ))
    fields.append(MessField(
        Short=True,
        Title="Date",
        Value=s.Date
    ))
    fields.append(MessField(
        Short=True,
        Title="Difficulty",
        Value=s.Difficulty
    ))
    fields.append(MessField(
        Short=True,
        Title="Link",
        Value=SlackEnum.FormatTextLinkSlack.value.format(s.Link, s.Title)
    ))
    fields.append(MessField(
        Short=True,
        Title="Topic Tags",
        Value=s.TopicTags
    ))

    return Attachment(Fields=fields)
