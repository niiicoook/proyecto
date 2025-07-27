from fastapi.testclient import TestClient
from rutas import *

client = TestClient()

def test_movie_add():
    