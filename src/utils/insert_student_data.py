from typing import Dict

from src.repository.sophia_repository import SophiaRepository

sophia = SophiaRepository()


def insert_student_data(data: Dict, email):
    
    contacts = data.get("contatos")
    
    for contact in contacts:
        if contact["tipoContato"] == 4:
            contact["contato"] = email
    
    print(data)
    # sophia.put_student(data=data)