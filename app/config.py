class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:9TCs896eGqzGxPB2O9X042p6@illegally-right-tapir-iad.a1.pgedge.io:5432/wolnelektury'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'sslmode': 'disable'
        }
    }
