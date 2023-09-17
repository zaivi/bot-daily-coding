from typing import Optional, List, Dict, Union

from pydantic import BaseModel, Field, ConfigDict



class TopicTag(BaseModel):
	Name: str = Field(..., descriptio="Topic name")
	ID: str = Field(..., descriptio="Topic ID")
	Slug: str = Field(..., descriptio="URL topic tag")


class ChallengeQuestion(BaseModel):
    AcRate: float = Field(..., description="")
    Difficulty: str = Field(..., description="Difficulty of question")
    FreqBar: str = Field(..., description="")
    FrontendQuestionID: str = Field(..., description="")
    IsFavor: bool = Field(..., description="")
    PaidOnly: bool = Field(..., description="")
    Status: str = Field(..., description="")
    Title: str = Field(..., description="")
    TitleSlug: str = Field(..., description="")
    HasVideoSolution: bool = Field(..., description="")
    HasSolution: bool = Field(..., description="")
    HasSolution: bool = Field(..., description="")
    TopicTags: List[TopicTag] = Field(..., description="List of topic tags")


class LeetCodeChallenge(BaseModel):
    Date: str = Field(..., description="Creation challenge date")
    UserStatus: str = Field(..., description="User status")
    Link: str = Field(..., description="Challenge link")
    Question: ChallengeQuestion = Field(..., description="Challenge question")
