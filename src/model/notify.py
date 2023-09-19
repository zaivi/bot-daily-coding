from config.config import Config

from pydantic import BaseModel, Field, ConfigDict



class Notify(BaseModel):
    cfg: Config = Field(..., description="Configuration for notify")
    statisticalDomain: str = Field(..., description="")


def NewNotify(cfg, statisticalDomain) -> Notify:
    return Notify(cfg=cfg, statisticalDomain=statisticalDomain)
