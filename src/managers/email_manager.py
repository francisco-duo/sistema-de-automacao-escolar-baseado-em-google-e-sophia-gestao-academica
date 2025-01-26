from src.config.base import BaseConfiguration
from src.utils.domain import get_domain_and_orgunit
from src.utils.insert_student_data import insert_student_data

class EmailManager(BaseConfiguration):
    
    def create_emails(self):
        # Iterate students data
        for student in self.sophia.get_student():

            # Verify if emails is none
            if student.get("email"):
                continue
            
            for classroom in student.get("turmas", []):
                classroom_description = classroom["descricao"]
                
                if any(exclude in classroom_description for exclude in self.exclude_descriptions):
                    continue
                
                domain, orgunit = get_domain_and_orgunit(classroom_description)
                first_name = student["nome"].split()[0]
                email = f"{first_name}{student['codigoExterno']}@{domain}".lower()
                
                try:
                    # Update student email
                    student_data = self.sophia.get_student(id=student['codigo'])
                    data = insert_student_data(data=student_data, email=email)
                    self.sophia.put_student(data=data, id=student['codigo'])
                except Exception as err:
                    print(err)
                
                try:
                    # Insert student email into goolge admin sdk
                    self.google.insert_user(
                        primaryEmail=email,
                        name={"givenName": first_name, "familyName": " ".join(student["nome"].split()[1:])},
                        password=f"cci{student['codigoExterno']}",
                        orgUnit=orgunit,
                        chagePasswordAtNextLogin=True
                    )
                    
                except Exception as err:
                    ...
