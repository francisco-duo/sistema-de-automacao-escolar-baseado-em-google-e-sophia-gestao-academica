import requests

import google.auth
import google.auth.exceptions
import googleapiclient.errors

from .environments import EnvironmentsConfiguration

from typing import Dict

from googleapiclient.discovery import build
from google.oauth2 import service_account


class Auth:
    sophia_enviroment = EnvironmentsConfiguration().sophia()
    google_enviroment = EnvironmentsConfiguration().google()
    
    def directory_service(self) -> build:
        """
        Return the necessery service to use google api.
        
        Raises:
            FileNotFoundError: Case the file of credentials not found.
            google.auth.exceptions.DefaultCredentialsError: Case have problems with credentials.
            HttpError: Case have any problem with the api.
            
        Returns:
            googleapiclient.discovery.Resource: Return the api service.
        """
        email = self.google_enviroment["service_email"]
        scopes = self.google_enviroment["scopes"]
        
        if not email or not scopes:
            raise Exception
        
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.google_enviroment["credentials"],
                scopes=self.google_enviroment["scopes"],
                subject=self.google_enviroment["service_email"]
            )
            service = build("admin", "directory_v1", credentials=credentials)
            return service
        except FileNotFoundError as e:
            raise Exception(f"credentials is notfound: {e}")
        except google.auth.exceptions.DefaultCredentialsError as e:
            raise Exception(f"Error to load credential: {e}")
        except googleapiclient.errors.HttpError as e:
            raise Exception(f"Error to comunicate whit google api: {e}")
        except Exception as e:
            raise Exception(f"Imprevible error: {e}")

    def sophia_connectioin(self) -> Dict:
        """
        Get the token to access sophia api.
        
        Raises:
            NameError: If requests or others imports is not importeds, the code returns a exception.
            KeyError: If the environments variables is not defined, the code will be fail to execute os,getenv().
            RequestException: Generc error. Will be start because connection errors, DNS and orthers errors.
        
        Returns:
            Dict: Return a dict with a token to request.
        """
        url = self.sophia_enviroment['auth']
        user = self.sophia_enviroment['user']
        password = self.sophia_enviroment['password']
        
        if not url or not user or not password:
            raise KeyError("The environments variables is not defined")

        try:
            response = requests.post(url, json={"usuario": user, "senha": password})
            response.raise_for_status()
            return {"token": response.text}
        except requests.exceptions.RequestException as e: 
            raise requests.exceptions.RequestException(f"Error when making the request: {e}")
        except KeyError as e:
            raise KeyError(f"Configuration error: {e}")
