from unicodedata import normalize


def normalize_name(name: str):
    """"""
    name_sanitized = name.replace(" ", "")\
                                   .replace("ª", "")\
                                   .replace("º", "")\
                                   .replace("°", "")\
                                   .replace(".", "")\
                                   .replace("-", "")
    
    name_normalize =  normalize('NFKD', name_sanitized)\
            .encode('ASCII', 'ignore').decode('ASCII')
    
    
    return name_normalize


if __name__ == "__main__":
    print(normalize_name(name="1ºAm - profªFrancisca"))