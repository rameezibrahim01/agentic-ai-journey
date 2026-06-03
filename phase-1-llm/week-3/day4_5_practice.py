print("•	Define an LLMMessage model (role must be 'user', 'assistant', or 'system'; content min_length=1). Validate 5 instances.")

from pydantic import BaseModel, Field, field_validator, ValidationError

class Message(BaseModel):
    role: str
    content:str = Field(min_length=1)

    @field_validator("role")
    @classmethod
    def valid_role(cls, role: str) -> str:
        if role.lower() not in ["user", "assistant", "system"]:
            raise ValueError("Invalid role")
        return role


try:
    m = Message(role = "user", content = "hi")
    print(m)
except ValidationError as e:
    print(f"Error: {e}")


print("•	Define a ProductReview model (rating: int 1-5, text: str, reviewer: str). Try invalid rating — verify error.")

class ProductReview(BaseModel):
    rating: int = Field(ge = 1, le = 5)
    text: str
    reviewer: str

try:
    prod_review = ProductReview(rating = 1.4, text = "sample", reviewer = "me")
    print(prod_review)
except ValidationError as e:
    print(f"Error: {e}")


print("•	Refactor Phase 0 Contact model to use Field() validators.")

import datetime

class Contact(BaseModel):
    name: str = Field(min_length = 1)
    phone: str = Field(min_length = 6)
    email: str = Field(pattern = "^[^@\s]+@[^@\s]+$")
    last_modified: datetime

