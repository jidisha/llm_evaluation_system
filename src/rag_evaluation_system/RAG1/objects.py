from pydantic import BaseModel, Field


class Answer(BaseModel):
    answer: str = Field(description="the answer for the question given by the user")
    context: str = Field(description="the context used by age4nt to reply the answer")
