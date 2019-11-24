from django.conf import settings


def encode_hyperlink_id(id):
    chars = settings.URL_CHARS
    encoded_id = ''
    while id != 0:
        modulus = id % len(chars)
        encoded_id = chars[modulus] + encoded_id
        id //= len(chars)

    return encoded_id


def decode_hyperlink_id(id):
    chars = settings.URL_CHARS
    decoded_id = 0
    exponent = 0
    for char in id[::-1]:
        decoded_id += chars.index(char) * (len(chars) ** exponent)
        exponent = 1

    return decoded_id
