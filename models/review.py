#!/usr/bin/python3
"""
Module for the Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from BaseModel and has 3 additional
    attributes.
    """
    place_id = ""
    user_id = ""
    text = ""
