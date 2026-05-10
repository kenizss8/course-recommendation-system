from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    title: str = Field(..., min_length=1)
    category: str = Field(..., min_length=1)
    level: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    skills: list[str] = Field(default_factory=list)


class CourseCreate(CourseBase):
    pass


class CourseUpdate(CourseBase):
    pass


class RecommendRequest(BaseModel):
    desired_category: str = ""
    desired_level: str = ""
    keywords: list[str] = Field(default_factory=list)
    description: str = ""
