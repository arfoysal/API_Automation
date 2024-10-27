from os.path import dirname, join


class AppConstant:

    PROJECT_ROOT = dirname(dirname(__file__))
    RESOURCE_FOLDER = join(PROJECT_ROOT, 'resources')
    REQUEST_DATA_FOLDER = join(RESOURCE_FOLDER, 'request_data')
    RESPONSE_SCHEMA = join(RESOURCE_FOLDER, 'response_schema')


