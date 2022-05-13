from unittest.mock import MagicMock

mock_obj = MagicMock()

print("\n", dir(mock_obj), "\b")

# Zero calls
try:
    mock_obj.assert_called_once()
except Exception as e:
    print("\n", e)

# One call
mock_obj()

try:
    mock_obj.assert_called_once()
except Exception as e:
    print("\n", e)

# Two calls
mock_obj()

try:
    mock_obj.assert_called_once()
except Exception as e:
    print("\n", e)

# called with
mock_obj(name="Pedro")
try:
    mock_obj.assert_called_with(name="Pedro")
    print("\nassert called once with success", "\n")
except Exception as e:
    print("\n", e)

# call args
print("\ncall args")
print(mock_obj.call_args)

print("\ncall args list")
print(mock_obj.call_args_list)


# return value
mock_obj_ret = MagicMock(return_value=42)
print("\nReturning value:", mock_obj_ret(), "\n")

# side effects
mock_obj_raise = MagicMock(side_effect=ValueError("mocked error"))
print("\nMocking raising error")
try:
    mock_obj_raise()
except Exception as e:
    print("\n", e)