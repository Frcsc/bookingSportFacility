from facilities.mixin import FacilitiesBaseModel
from kansala_sports.mixin import BaseModel


class FutsalCourt(BaseModel, FacilitiesBaseModel):
    pass


class TennisCourt(BaseModel, FacilitiesBaseModel):
    pass


class BadmintonCourt(BaseModel, FacilitiesBaseModel):
    pass
