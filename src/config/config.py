from pydantic import BaseModel, Field, ConfigDict



class Config(BaseModel):
    DBDriver: str = Field(default="", description="")
    DBSource: str = Field(default="", description="")
    Port: str = Field(default="", description="")
    AppID: str = Field(default="", description="")
    WebhookSlack: str = Field(default="", description="")
    WebhookSlackLeetCode: str = Field(default="", description="")
    TagsSlackLeetCode: str = Field(default="Test", description="")
    ClientId: str = Field(default="", description="")
    ClientSecret: str = Field(default="", description="")
    RefreshToken: str = Field(default="", description="")
    GrantType: str = Field(default="", description="")
    Env: str = Field(default="", description="")
    CronNotifyRun: str = Field(default="", description="")
    CronNotifySummary: str = Field(default="", description="")
    CronNotifyStatistical: str = Field(default="", description="")
    ApiKeyUploadImage: str = Field(default="", description="")
    DistanceGoal: str = Field(default="", description="")
    