from maclookup.requester import Requester


class MockRequester(Requester):

    def __init__(self, data):
        self.data = data

    def request(self, url, parameters):
        return self.data
