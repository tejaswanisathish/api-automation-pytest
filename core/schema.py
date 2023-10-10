# This file contains Pydantic schemas that allow validation of the API responses.


from pydantic import BaseModel, HttpUrl


class SuccessfulRegistrationResponse(BaseModel):
    """This class contains the schema for a successful registration response"""
    id: int
    token: str

class SuccessfulLoginResponse(BaseModel):
    """This class contains the schema for a successful login response"""
    token: str

class ResourceMetadata(BaseModel):
    """This class contains the schema for a resource metadata"""
    id:int
    name:str
    year:int
    color:str
    pantone_value:str

class SupportMetadata(BaseModel):
    """This class contains the schema for a support metadata"""
    url:HttpUrl
    text:str

class ListResourceResponse(BaseModel):
    """This class contains the schema for a list resource response"""
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[ResourceMetadata]
    support: SupportMetadata

