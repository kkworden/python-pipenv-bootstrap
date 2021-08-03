from unittest import mock
import unittest

import pytest

from .main import some_func


class TestMain(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _setup_service(self):
        self.mock_object = mock.MagicMock()

    def test_some_func(self):
        assert some_func() == 3

    # def test_mock(self):
    #     assert self.mock_object.some_method.called