# MIT License

# Copyright (c) 2025 Francisco Duó

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

import os
import unittest
from unittest.mock import patch
from src.config.environments import EnvironmentsConfiguration


class TestEnvironmentsConfiguration(unittest.TestCase):
    """
    Test suite for the EnvironmentsConfiguration class.

    This test suite verifies the behavior of the `sophia` and `google` methods,
    ensuring they return the correct environment variable values as dictionaries.
    """

    @patch.dict(os.environ, {
        "SOPHIA_USERNAME": "test_user",
        "SOPHIA_PASSWORD": "test_password",
        "SOPHIA_STUDENTS": "test_students",
        "SOPHIA_CLASSROOMS": "test_classrooms",
        "SOPHIA_PERIOD": "test_period",
        "SOPHIA_AUTH": "test_auth",
        "GOOGLE_EMAIL": "google_service_email@test.com",
        "GOOGLE_SCOPES": "scope1 scope2 scope3",
        "GOOOGLE_CREDENTIALS_PATH": "/path/to/credentials.json"
    })
    def test_sophia_method(self):
        """
        Test the `sophia` method to ensure it correctly retrieves and returns
        the Sophia-related environment variables as a dictionary.
        """
        config = EnvironmentsConfiguration()
        expected_sophia = {
            "user": "test_user",
            "password": "test_password",
            "students": "test_students",
            "classrooms": "test_classrooms",
            "period": "test_period",
            "auth": "test_auth",
        }
        self.assertEqual(config.sophia(), expected_sophia)

    @patch.dict(os.environ, {
        "SOPHIA_USERNAME": "test_user",
        "SOPHIA_PASSWORD": "test_password",
        "SOPHIA_STUDENTS": "test_students",
        "SOPHIA_CLASSROOMS": "test_classrooms",
        "SOPHIA_PERIOD": "test_period",
        "SOPHIA_AUTH": "test_auth",
        "GOOGLE_EMAIL": "google_service_email@test.com",
        "GOOGLE_SCOPES": "scope1 scope2 scope3",
        "GOOOGLE_CREDENTIALS_PATH": "/path/to/credentials.json"
    })
    def test_google_method(self):
        """
        Test the `google` method to ensure it correctly retrieves and returns
        the Google-related environment variables as a dictionary.
        """
        config = EnvironmentsConfiguration()
        expected_google = {
            "service_email": "google_service_email@test.com",
            "scopes": ["scope1", "scope2", "scope3"],
            "credentials": "/path/to/credentials.json",
        }
        self.assertEqual(config.google(), expected_google)

if __name__ == "__main__":
    unittest.main()
