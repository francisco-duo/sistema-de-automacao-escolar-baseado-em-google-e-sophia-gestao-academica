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

"""

import requests

from typing import Dict, Any

from src.config.authentication import Auth
from src.config.environments import EnvironmentsConfiguration


class SophiaRepository:
    
    connection = Auth().sophia_connectioin()
    environment = EnvironmentsConfiguration().sophia()

    def get_student(self, params: Dict | None = None, id: str = "") -> list:
        """
        Request to get all or one data of students.
        
        Args:
            params: Dict: A dict of paramethers. 
        
        Raises:
            NameError: If requests or os are not imported, the code will raise an exception.
            KeyError: If the environment variables are not set or are incorrect, the code may fail when trying to execute os.getenv().
            RequestException: Generic error that may occur during the request. This could be caused by connection issues, server failure, or DNS failure. 
        
        Returns:
            list: Returns a list of students. 
        """
        url = self.environment['students'] + str(id)
        
        if not url:
            raise KeyError("url is not defined")
        
        try:
            response = requests.get(url, params=params, headers=self.connection)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"Erro when making the request: {e}")
        except KeyError as e:
            raise KeyError(f"Configuration error: {e}")

    def put_student(self, data: Dict, id: str = "") -> Any:
        """
        Args:
            data: Dict:
            id: str
        
        Raises:
            RequestException:
            KeyError:
        
        Returns:
            Dict: Return a updated body student.
        """
        url = self.environment['students'] + str(id)
    
        if not url:
            raise KeyError("url is not defiend")

        try:
            response = requests.put(url, json=data, headers=self.connection)
            return response
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"Error when making the request: {e}")
        except KeyError as e:
            raise KeyError(f"Configuration error: {e}")
        except Exception as e:
            print(e)

    def get_classroom(self, params: Dict | None = None, id: str = "") -> list:
        """
        Request to get all or one data of classrooms.
        
        Args:
            params: Dict: A dict of paramethers. 
        
        Raises:
            NameError: If requests or os are not imported, the code will raise an exception.
            KeyError: If the environment variables are not set or are incorrect, the code may fail when trying to execute os.getenv().
            RequestException: Generic error that may occur during the request. This could be caused by connection issues, server failure, or DNS failure. 
        
        Returns:
            list: Returns a list of classrooms. 
        """
        url = self.environment['classrooms'] + str(id)
        
        if not url:
            raise KeyError("url is not defined")
        
        try:
            response = requests.get(url, params=params, headers=self.connection)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"Erro when making the request: {e}")
        except KeyError as e:
            raise KeyError(f"Configuration error: {e}")

    def get_period(self, params: Dict | None = None) -> Any:
        """
        Get the code of a year period
        
        Args:
            params: Dict | None: Insert a Dict to get especific year period.
        
        Raises:
        
        Return:

        """
        return requests.get(self.environment['period'], params=params, headers=self.connection).json()


if __name__ == "__main__":
    sophia = SophiaRepository()
    print(
        sophia.put_student(id="24125", data={'codigo': 24125, 'codigoExterno': '0008118', 'nome': 'Maria Fernanda Ferreira Medeiros do Nascimento', 'utilizaNomeSocial': False, 'nomeSocial': None, 'estadoCivil': {'codigo': 1, 'descricao': 'Solteiro(a)'}, 'certidaoNascimento': '02125301552016100577117026317171', 'cpf': '080.023.281-08', 'rg': None, 'dataExpedicaoRg': None, 'orgaoExpedidorRg': None, 'rgEscolar': None, 'sexo': 'F', 'religiao': {'codigo': 4, 'descricao': 'Evangélica'}, 'raca': {'codigo': 5, 'descricao': 'Parda'}, 'dataNascimento': '2016-09-11T00:00:00', 'localNascimento': {'codigo': 1580, 'descricao': ' Brasília'}, 'ufLocalNascimento': 'DF', 'nacionalidade': {'codigo': 668, 'descricao': 'Brasileira'}, 'numeroPassaporte': None, 'paisExpedidorPassaporte': None, 'dataExpedicaoPassaporte': None, 'dataValidadePassaporte': None, 'cep': '72306-605', 'logradouro': 'Qnl 10 conjunto B lote 08', 'numeroLogradouro': '403', 'complemento': 'Residencial Algarve', 'bairro': {'codigo': 940, 'descricao': 'Taguatinga Norte (Taguatinga)'}, 'cidade': {'codigo': 1580, 'descricao': ' Brasília'}, 'uf': 'DF', 'contaOffice365': None, 'contatos': [{'tipoContato': 1, 'contato': 'dfd'}, {'tipoContato': 2, 'contato': '61985370648'}, {'tipoContato': 2, 'contato': '61991273064'}, {'tipoContato': 4, 'contato': 'teste@teste.com'}]})
    )
