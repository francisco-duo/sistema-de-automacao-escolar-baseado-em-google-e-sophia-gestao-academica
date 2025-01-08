# MIT License

# Copyright (c) [Year] [Company Name]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
google_repository.py
---------------------

This module provides a repository class for interacting with the Google Admin SDK Directory API.

Classes:
    - GoogleRepository: Contains methods to manage users in the Google Admin domain.

Dependencies:
    - google-auth: For authentication.
    - google-api-python-client: For interacting with the Google APIs.

License:
    MIT License. See LICENSE file for details.

Author:
    Francisco Duó (francisco.duo@portalcci.com.br | francisco.duo2000@gmail.com)

Date:
    January 3, 2025
"""


from src.config.authentication import Auth


class GoogleRepository:
    """
        A repository for interacting with the Google Admin SDK Directory API.
    """
    directory_admin_service = Auth().directory_service()
    
    def insert_user(self, **kwargs):
        """
        Inserts a new user into the Google Admin domain.

        This method creates a new user in the Google Admin directory using the 
        provided parameters. It requires valid authentication and authorization 
        to access the Google Admin SDK Directory API.

        Args:
            **kwargs: Arbitrary keyword arguments representing the body of the 
                      request. These parameters are passed directly to the API 
                      to define the user's attributes (e.g., name, email, password).

        Returns:
            dict: The API response as a dictionary, containing details of the 
                  created user.

        Raises:
            googleapiclient.errors.HttpError: If the API request fails due to an 
                                              HTTP error, such as invalid parameters 
                                              or insufficient permissions.
        """
        return self.directory_admin_service.users().inser(body=kwargs).execute()
    
    def create_groups(self, **kwargs):
        """
        Create a new group of emails in admin doamin
        
        Args:
            **kwargs:
        
        Raises:
        
        Returns:
        
        """
        return self.directory_admin_service.groups().insert(body=kwargs).execute()
    
    def insert_members_group(self, groupKey: str, **kwargs):
        """
        Insert a memeber into group
        
        Args:
        
        Raises:
        
        Returns:
        """
        return self.directory_admin_service.members().insert(groupKey=groupKey, body=kwargs)

    def remove_members_group(self):
        """
        Remove a wrong membert to group
        
        Args:
        
        Raises:
        
        Returns:
        
        """
        ...
    
    def list_members_group(self, groupKey: str): ...
    
    def insert_data_to_spreadsheet(self): ...