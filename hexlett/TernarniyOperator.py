def normalize_url(original_url):
    original_http = original_url[:7]
    print(original_http)
    original_https = original_url[:8]

    if original_http == 'http://':
        return 'https://' + original_url[7:]
    elif original_https == 'https://':
        print(original_https)
        return 'https://' + original_url[8:]
    else:
        return 'https://' + original_url


print(normalize_url('yandex.ru'))
