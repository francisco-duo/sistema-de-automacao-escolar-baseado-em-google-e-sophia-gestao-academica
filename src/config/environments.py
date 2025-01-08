import os

from dotenv import load_dotenv

load_dotenv()


class EnvironmentsConfiguration:
    
    def sophia(self):
        environments = {
            "user": os.getenv("SOPHIA_USERNAME"),
            "password": os.getenv("SOPHIA_PASSWORD"),
            "students": os.getenv("SOPHIA_STUDENTS"),
            "classrooms": os.getenv("SOPHIA_CLASSROOMS"),
            "period": os.getenv("SOPHIA_PERIOD"),
            "auth": os.getenv("SOPHIA_AUTH"),
        }
        return environments
    
    def google(self):
        environments = {
            "service_email": os.getenv("GOOGLE_EMAIL"),
            "scopes": os.getenv("GOOGLE_SCOPES").split(" "),
            "credentials": os.getenv("GOOOGLE_CREDENTIALS_PATH")
        }
        return environments
