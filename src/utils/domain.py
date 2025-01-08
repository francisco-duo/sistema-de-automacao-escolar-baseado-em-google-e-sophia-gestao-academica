from datetime import date


def get_domain_and_orgunit(classroom_description: str):
    """"""
    if not isinstance(classroom_description, str):
        raise TypeError("The description does not a string")
    
    classroom_description = classroom_description.upper()
    
    mappings = {
        ("ENF", "PED", "ADM", "ADS", "PSI", "PIS", "DIR"): ("faculdadecci.com.br", "/Faculdade/Turmas Fac"),
        ("TÉC.",): ("tecscci.com.br", "/Escola Técnica/2024"),
        ("Maternal", "Jardim", "Período"): ("cciweb.com.br", "/Turmas 2025/Educação Infantil"),
        ("1º", "2º", "3º", "4º"): ("cciweb.com.br", "/Turmas 2025/Ensino Fundamental I"),
        ("5º", "6º", "7º", "8º"): ("cciweb.com.br", "/Turmas 2025/Ensino Fundamental II"),
        ("9º", "1ª", "2ª", "3ª"): ("cciweb.com.br", "/Turmas 2025/Ensino Médio"),
    }

    for keywords, (domain, orgunit) in mappings.items():
        if any(keyword in classroom_description for keyword in keywords):
            return domain, orgunit
    
    return "cciweb.com.br", "/Turmas 2024"


def current_period(domain: str):
    domain, _ = get_domain_and_orgunit(classroom_description=domain)
    current_date = str(date.today()).split("-")
    
    if domain != "cciweb.com.br":
        if int(current_date[1]) >= 7:
            return f"{current_date[0]}.2"
        return f"{current_date[0]}.1"
    
    return current_date[0]


if __name__ == "__main__":
    print(current_period("1ª"))
