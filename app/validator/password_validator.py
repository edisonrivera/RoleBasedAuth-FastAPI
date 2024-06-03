import re


def is_valid_password(plain_password: str) -> bool:
    regex = (
        r'^(?=.*[a-z])'  # al menos una letra minúscula
        r'(?=.*[A-Z])'  # al menos una letra mayúscula
        r'(?=.*\d)'  # al menos un número
        r'(?=.*[@$!%*?&%#\.\,\$\(\)\]\[_\-+\'\"\{\}\\\^=\/<>=¿:; ~|`])'  # al menos un carácter especial
        r'[A-Za-z\d@$!%*?&%#\.\,\$\(\)\]\[_\-+\'\"\{\}\\\^=\/<>=¿:; ~|`]{8,}$'  # longitud mínima de 8 caracteres
    )

    return re.match(regex, plain_password) is not None


