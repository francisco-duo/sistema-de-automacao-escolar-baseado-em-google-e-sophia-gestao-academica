from src.repository.google_repository import GoogleRepository
from src.repository.sophia_repository import SophiaRepository
from src.config.environments import EnvironmentsConfiguration


class BaseConfiguration:
    def __init__(self):
        self.environments = EnvironmentsConfiguration()
        self.sophia = SophiaRepository()
        self.google = GoogleRepository()
        
        self.exclude_descriptions = [
            "PEC", "AQUA", "Preparatório", "Período", "Acampamento", "Oficina", "Curso", "Cursinho", "PI",
            "Proj", "Projeto", "Resgate", "Complementação Pedagógica", "Exercício", "Ballet", "Colônia",
            "Extensão", "Serviço"
        ]
