import os



class Config(object):
      BOT_TOKEN = "5129094585:AAGtanL9aOYPA9RROmXm2y25p4OLopxrfSw"
      API_ID = "7620015"
      API_HASH = "8b9cbac6c4e37afe61f472ab3deafcd9
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Ts_Bots")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 123476535 )) 
      DB_URL = os.environ.get("DATABASE_URL", "postgres://srdgvjhebnluum:fc41da72fc4a4fccebeff6ae823edb935f899ad1ea844103e8d11ad8a54f8a2f@ec2-54-158-247-210.compute-1.amazonaws.com:5432/d8jkid11otob0i")
