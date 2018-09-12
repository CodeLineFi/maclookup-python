from future.standard_library import install_aliases
install_aliases()

from urllib.error import HTTPError



class MockResponse():
    def __init__(self, data, code=200, msg='OK', headers=None, error=False):
        if error:
            raise HTTPError('http://test.dev', code, msg, headers, None)

        if headers is None:
            headers = [(u'Content-Type', u'text/plain')]
        self.headers = headers
        self.code = code
        self.resp_data = data
        self.msg = msg

    def read(self):
        return self.resp_data

    def getheaders(self):
        return self.headers

