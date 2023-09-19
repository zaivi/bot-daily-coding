from pydantic import BaseModel, Field, ConfigDict, validator, computed_field



class TimestampMixin:
    pass

class SoftDeleteMixin:
    pass

class Notification(TimestampMixin, SoftDeleteMixin):
    a: str
    b: str
    pass


class EmailNotification(Notification, BaseModel):
    c: str
    d: str
    pass

class SlackNotification(Notification, BaseModel):
    c: str
    e: str
    pass
