import re


def is_valid_phone(phone_number: str) -> bool:
    return bool(re.fullmatch(r"\+380\d{9}", phone_number))


def normalize_phone(phone_number: str) -> str:
    phone_number = re.sub(r"\D", "", phone_number)

    if phone_number.startswith("380"):
        return "+" + phone_number

    if phone_number.startswith("0"):
        return "+38" + phone_number

    return "+" + phone_number


def prepare_phone(phone_number: str) -> str:
    if is_valid_phone(phone_number):
        return phone_number

    return normalize_phone(phone_number)