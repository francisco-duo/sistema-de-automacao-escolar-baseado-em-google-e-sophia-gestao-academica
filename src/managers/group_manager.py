from src.config.base import BaseConfiguration

from src.utils.domain import get_domain_and_orgunit
from src.utils.domain import current_period
from src.utils.normalize_name import normalize_name


class GroupManager(BaseConfiguration):
    
    def create_groups(self):
        for classroom in self.sophia.get_classroom():
                
            if any(exclude in classroom["nome"] for exclude in self.exclude_descriptions):
                continue
            
            domain, _ = get_domain_and_orgunit(classroom_description=classroom["nome"])
            normalized_name = normalize_name(name=classroom['nome'])
            period = current_period(domain=domain)
            email = f"{normalized_name}_{period}@{domain}".lower()
            parent_group_email = f"responsaveis_{normalized_name}_{period}@{domain}".lower()
            
            # Create user groups to GOOGLE ADMIN SDK
            self.google.create_groups(
                email=email,
                name=classroom["nome"],
                description=f"Grupo de emails referente à turma: {classroom['nome']}"
            )
            
            if domain == "cciweb.com.br":
                # Create parent groups to GOOGLE ADMIN SDK
                self.google.create_groups(
                    email=parent_group_email,
                    name=classroom["nome"],
                    description=f"Grupo de emails referente à turma: {classroom['nome']}"
                )
    
    def insert_email_to_groups(self):
        """
        """
        """
        """
        for student in self.sophia.get_student():
            for student_classroom in student.get("turmas", []):
                classroom_description = student_classroom["descricao"]
                
                if any(exclude in classroom_description for exclude in self.exclude_descriptions):
                    continue
                
                domain, _ = get_domain_and_orgunit(classroom_description=classroom_description)
                normalized_name = normalize_name(name=classroom_description)
                period = current_period(domain=domain)
                email = f"{normalized_name}_{period}@{domain}".lower()
                
                try:
                    self.google.insert_members_group(
                                groupKey=email,
                                email=parent["email"],
                                role="MEMBER"
                            )
                except Exception as err:
                    ...

                if domain == "cciweb.com.br":
                    for parent in student.get("responsaveis", []):
                        try:
                            # Insert memeber
                            self.google.insert_members_group(
                                groupKey=f"responsaveis_{email}",
                                email=parent["email"],
                                role="MEMBER"
                            )
                        except Exception as err:
                            ...
    
    def insert_owner_email_to_groups(self):
        ...
    
    def remove_email_to_wrong_group(self):
        for student in self.sophia.get_student():
            for classroom in student.get("turmas", []):
                classroom_description = classroom["descricao"]
                
                if any(exclude in classroom_description for exclude in self.exclude_descriptions):
                    continue
                
                domain, _ = get_domain_and_orgunit(classroom_description=classroom_description)
                normalized_name = normalize_name(name=classroom_description)
                period = current_period(domain=domain)
                email = f"{normalized_name}_{period}@{domain}".lower()
                
                try:
                    members = self.google.list_members_group(groupKey=email)
                    member_email = [member["email"] for member in members]

                    if student["email"] not in member_email:
                        # google.remove_memeber()
                        
                        if domain == "cciweb.com.br":
                            for parent in student.get("responsaveis", []):
                                try:
                                    # google.remove_member()
                                    ...
                                except Exception as err:
                                    ...
                        ...
                except Exception as err:
                    ...