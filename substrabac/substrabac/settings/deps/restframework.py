REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.AdminRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'UNICODE_JSON': False,
    'DEFAULT_VERSIONING_CLASS': 'libs.versioning.AcceptHeaderVersioningRequired',
    'ALLOWED_VERSIONS': ('0.0',),
    'DEFAULT_VERSION': '0.0',
}
