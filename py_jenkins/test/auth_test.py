"""Unit test for the py_jenkins.authentcation module."""
from unittest import TestCase
from mock import patch
import py_jenkins.auth as auth

class StandAloneTests(TestCase):
    """Test the stand-alone module functions."""

    @patch('__builtin__.open')
    def test_login(self,mock_open):
        """auth.login方法的正确传参情况测试"""
        mock_open.return_value.read.return_value = "netease|password\n"
        self.assertTrue(auth.login('netease','password'))

    @patch('__builtin__.open')
    def test_login_bad_creds(self,mock_open):
        """auth.login方法错误传参情况测试"""
        mock_open.return_value.read.return_value = "netease|password"
        self.assertFalse(auth.login('netease','badpassword'))

    @patch('__builtin__.open')
    def test_login_error(self,mock_open):
        """auth.login方法的异常情况测试"""
        mock_open.side_effect = IOError()
        self.assertFalse(auth.login('netease','password'))
        
