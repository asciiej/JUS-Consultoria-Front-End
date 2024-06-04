from dotenv import load_dotenv
import os

# Carregando .env
load_dotenv()

# Variaveis
DATABASE_URL = os.getenv('DATABASE_URL')
DEBUG = os.getenv('DEBUG', False)