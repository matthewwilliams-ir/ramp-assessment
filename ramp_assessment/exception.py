
class InvalidInputArray(Exception):
    status_code = 400
    name = "Bad Request"

    def __init__(self, message, name=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if name is not None:
            self.name = name
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['code'] = self.status_code
        rv['name'] = self.name
        rv['message'] = self.message
        return rv
