""" Boilerplate init code for setting up celery"""
from .celery import app as celery_app

__all__ = ("celery_app",)
