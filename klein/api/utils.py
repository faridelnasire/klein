from django.conf import settings


'''
These 2 functions convert the Base10 Hyperlink.id value to a Base62 short url.
Inspired by the PHP base_convert function and this implementation:
https://www.php2python.com/wiki/function.base-convert/
'''


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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
