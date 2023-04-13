#!/usr/bin/python3
"""create variable for insatnce of Blueprint"""
from flask import Blueprint

app_views = Blueprint('first_view', __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.states import *