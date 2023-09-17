from typing import Optional, List, Dict, Union

from pydantic import BaseModel, Field, ConfigDict



class Field(BaseModel):
    Short: bool = Field(..., description="")
    Title: str = Field(..., description="")
    Value: str = Field(..., description="")
    

class Attachment(BaseModel):
    Fields: List[Field] = Field(..., description="")
    ImageUrl: str = Field(..., description="")


class TextMessageDailyCodingChallenge(BaseModel):
    Title: str = Field(..., description="Challenge Title")
    Date: str = Field(..., description="Challenge creation date")
    Difficulty: str = Field(..., description="Challenge Difficulty")
    Link: str = Field(..., description="Challenge URL resource")
    TopicTags: str = Field(..., description="Challenge list of topic tags")


def toAttachment(s: TextMessageDailyCodingChallenge) -> List[Attachment]:
    fields = list()
    fields.append(Field(
        Short=True,
        Title="Title",
        Value=s.Title
    ))
    fields.append(Field(
        Short=True,
        Title="Date",
        Value=s.Date
    ))
    fields.append(Field(
        Short=True,
        Title="Difficulty",
        Value=s.Difficulty
    ))
    fields.append(Field(
        Short=True,
        Title="Link",
        Value=s.Link
    ))
    fields.append(Field(
        Short=True,
        Title="Topic Tags",
        Value=s.TopicTags
    ))
