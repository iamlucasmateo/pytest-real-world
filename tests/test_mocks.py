# Stub / Fakes: test return values / check state change (using a public API)
# Mock is a Stub, additionally verifying interactions
# Mock / Spy: test method calls
# The "spy" listens to interactions between a function / class and another one being called / used
# Difference between Spy and Mock: the mock fails the test if the expected thing doesn't happen
# right away. The Spy "spies" the interaction and then checks what went on at the end of the test

# to see these tests fail, change the implementation of the method

import pytest
from unittest.mock import Mock

from logic.my_service import MyService
from logic.single_sign_on import *

class TestMyService:
    def test_invalid_token(self):
        registry = FakeSingleSignOnRegistry()
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=None)
        assert "please enter your login details" in response
        
    def test_valid_token(self):
        registry = FakeSingleSignOnRegistry()
        token = registry.register("valid credentials")
        my_service = MyService(registry)
    
        response = my_service.handle_request("do stuff", token)
        assert "hello world" in response
        
    def test_invalid_token_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=False)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        assert registry.is_valid_was_called

    def test_valid_token_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=True)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token)
        assert registry.is_valid_was_called

    def test_invalid_token_with_spy(self):
        token = SSOToken()
        registry = SpySingleSignOnRegistry(accept_all_tokens=False)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        assert token in registry.checked_tokens

    def test_valid_token_with_spy(self):
        token = SSOToken()
        registry = SpySingleSignOnRegistry(accept_all_tokens=True)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token)
        assert token in registry.checked_tokens

    def test_invalid_token_with_mocking_fw_as_spy(self):
        token = SSOToken()
        registry = Mock(SingleSignOnRegistry)
        registry.is_valid = Mock(return_value=False)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        registry.is_valid.assert_called_with(token)

    def test_valid_token_with_mocking_fw_as_spy(self):
        token = SSOToken()
        registry = Mock(SingleSignOnRegistry)
        registry.is_valid = Mock(return_value=True)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token)
        registry.is_valid.assert_called_with(token)

    def test_invalid_token_with_mocking_fw_as_mock(self):
        invalid_token = SSOToken()
        registry = Mock(SingleSignOnRegistry)
        def is_valid(token):
            if not token == invalid_token:
                raise Exception("Got the wrong token")
            return False
        registry.is_valid = Mock(side_effect=is_valid)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=invalid_token)
        registry.is_valid.assert_called_with(invalid_token)

    def test_valid_token_with_mocking_fw_as_mock(self):
        valid_token = SSOToken()
        registry = Mock(SingleSignOnRegistry)
        def is_valid(token):
            if not token == valid_token:
                raise Exception("Got the wrong token")
            return True
        registry.is_valid = Mock(side_effect=is_valid)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=valid_token)
        registry.is_valid.assert_called_with(valid_token)