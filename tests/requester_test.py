from future.standard_library import install_aliases
install_aliases()

from mock import patch, Mock
from maclookup import Requester
from maclookup.exceptions import *

import unittest
from urllib.error import HTTPError
import logging
import io

class RequesterTest(unittest.TestCase):
    def setUp(self):
        pass

    @patch('maclookup.requester.urlopen')
    def test_200_code(self, mock_urlopen):
        result = Mock()
        result.code = 200
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['response']
        mock_urlopen.return_value = result

        requester = Requester('test', 'Test/0.1')

        res = requester.request('https://test.test', {})
        self.assertEqual(res, 'response')

    @patch('maclookup.requester.urlopen')
    def test_299_code(self, mock_urlopen):
        result = Mock()
        result.code = 299
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['response']
        mock_urlopen.return_value = result

        requester = Requester('test', 'Test/0.1')
        res = requester.request('https://test.test', {})
        self.assertEqual(res, 'response')

    @patch('maclookup.requester.urlopen')
    def test_deprecation_warning(self, mock_urlopen):
        result = Mock()
        result.code = 200
        result.getheaders.return_value = [(u'Content-Type', u'text/plain'),
                                          (u'Warning', u'299 Test Warning: deprecated API version')]

        result.read.side_effect = ['response']
        mock_urlopen.return_value = result

        log_capture_buffer = io.StringIO()
        logging.basicConfig(stream=log_capture_buffer, level=logging.WARNING)

        requester = Requester('test', 'Test/0.1')

        requester.request('https://test.test', {})

        self.assertEqual(log_capture_buffer.getvalue(),
                         u'WARNING:maclookup-requester:299 Test Warning: deprecated API version\n')

        log_capture_buffer.close()

    @patch('maclookup.requester.urlopen')
    def test_199_code(self, mock_urlopen):
        result = Mock()
        result.code = 199
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['response']
        mock_urlopen.return_value = result

        requester = Requester('test', 'Test/0.1')
        with self.assertRaises(ServerErrorException):
            res = requester.request('https://test.test', {})
            pass

    @patch('maclookup.requester.urlopen')
    def test_300_code(self, mock_urlopen):
        result = Mock()
        result.code = 300
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['response']
        mock_urlopen.return_value = result

        requester = Requester('test', 'Test/0.1')
        with self.assertRaises(ServerErrorException):
            res = requester.request('https://test.test', {})
            pass

    @patch('maclookup.requester.urlopen')
    def test_500_code(self, mock_urlopen):
        result = Mock()
        result.code = 500
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['error']
        mock_urlopen.return_value = result
        mock_urlopen.side_effect = HTTPError("https://test.test", 500, 'Internal Server Error', None, None)

        requester = Requester('test', 'Test/0.1')
        with self.assertRaises(ServerErrorException):
            res = requester.request('https://test.test', {})
            pass

    @patch('maclookup.requester.urlopen')
    def test_400_code(self, mock_urlopen):
        result = Mock()
        result.code = 400
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['error']
        mock_urlopen.return_value = result
        mock_urlopen.side_effect = HTTPError("https://test.test", 400, 'Bad Request', None, None)

        requester = Requester('test', 'Test/0.1')
        with self.assertRaises(UnknownOutputFormatException):
            res = requester.request('https://test.test', {})
            pass

    @patch('maclookup.requester.urlopen')
    def test_401_code(self, mock_urlopen):
        result = Mock()
        result.code = 401
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['error']
        mock_urlopen.return_value = result
        mock_urlopen.side_effect = HTTPError("https://test.test", 401, 'Auth Required', None, None)

        requester = Requester('test', 'Test/0.1')
        with self.assertRaises(AuthorizationRequiredException):
            res = requester.request('https://test.test', {})
            pass

    @patch('maclookup.requester.urlopen')
    def test_402_code(self, mock_urlopen):
        result = Mock()
        result.code = 402
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['error']
        mock_urlopen.return_value = result
        mock_urlopen.side_effect = HTTPError("https://test.test", 402, 'Payment Required', None, None)

        requester = Requester('test', 'Test/0.1')
        with self.assertRaises(NotEnoughCreditsException):
            res = requester.request('https://test.test', {})
            pass

    @patch('maclookup.requester.urlopen')
    def test_403_code(self, mock_urlopen):
        result = Mock()
        result.code = 403
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['error']
        mock_urlopen.return_value = result
        mock_urlopen.side_effect = HTTPError("https://test.test", 403, 'Access Denied', None, None)

        requester = Requester('test', 'Test/0.1')
        with self.assertRaises(AccessDeniedException):
            res = requester.request('https://test.test', {})
            pass

    @patch('maclookup.requester.urlopen')
    def test_422_code(self, mock_urlopen):
        result = Mock()
        result.code = 422
        result.getheaders.return_value = [(u'Content-Type', u'text/plain')]
        result.read.side_effect = ['error']
        mock_urlopen.return_value = result
        mock_urlopen.side_effect = HTTPError("https://test.test", 422, 'Unprocessable Entity', None, None)

        requester = Requester('test', 'Test/0.1')
        with self.assertRaises(InvalidMacOrOuiException):
            res = requester.request('https://test.test', {})
            pass

    def tearDown(self):
        pass
