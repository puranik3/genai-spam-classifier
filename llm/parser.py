import os
from typing import List, Literal
from pydantic import BaseModel, Field, ValidationError
from langchain_core.output_parsers import PydanticOutputParser

# =====================
# 1. Define Schema
# =====================
class SpamClassification(BaseModel):
    label: Literal["Spam", "Not Spam", "Uncertain"]
    reasons: List[str]
    risk_score: int = Field(..., ge=0, le=100, description="0..100 risk score")
    red_flags: List[str]
    suggested_action: str

def get_parser():
    parser = PydanticOutputParser(pydantic_object=SpamClassification)
    format_instructions = parser.get_format_instructions()
    return parser, format_instructions