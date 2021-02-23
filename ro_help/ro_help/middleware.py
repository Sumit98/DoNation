def force_default_language_middleware(get_response):
    def middleware(request):
        if request.META.get('en'):
            del request.META['en']

        response = get_response(request)

        return response

    return middleware