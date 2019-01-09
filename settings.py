import pymongo


MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DBNAME = "api_test"

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'users': {
        'schema': {
            'username': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 32,
                'required': True,
                'unique': True,
            },
            'firstname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 10,
                'required': True,
            },
            'lastname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
                'required': True,
            },
            'role': {

                'type': 'list',
                'allowed': ["author", "contributor"],
            },
            'location': {
                'type': 'dict',
                'schema': {
                    'address': {'type': 'string'},
                    'city': {'type': 'string'}
                },
            },
            'born': {
                'type': 'datetime',
            },
            'active': {
                'type': 'boolean',
                'default': True
            }
        }
    },
    'groups': {
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 32,
                'required': True,
                'unique': True
            },
            'users': {
                'type': 'list',
                'default': [],
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'users',
                        'field': '_id',
                        'embeddable': True
                    }
                }
            }
        }
    }
}
