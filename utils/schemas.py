from pydantic import BaseModel, Field


class UserInput(BaseModel):

    a : int
    b : int
    choice : str