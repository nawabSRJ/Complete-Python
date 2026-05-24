# Custom Exceptions in Python
# Custom exception classes let you define meaningful error types for your application.

# 1) Basic custom exception class
class MyCustomError(Exception):
    """A simple custom exception."""
    pass

# 2) Custom exception with an initializer and custom attributes
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f'Validation failed for {field}: {message}')

# 3) Raise and handle a custom exception

def validate_name(name):
    if not name:
        raise ValidationError('name', 'Name must not be empty')
    if len(name) < 3:
        raise ValidationError('name', 'Name must have at least 3 characters')
    return True

try:
    validate_name('')
except ValidationError as err:
    print('Custom exception caught:')
    print(' field ->', err.field)
    print(' message ->', err.message)
    print(' full ->', err)

# 4) Inheritance from built-in exception classes
#    Prefer subclassing a built-in exception when it makes sense.
#    Example: subclass ValueError if your exception is a kind of invalid value.

class AgeError(ValueError):
    pass

age = -10
if age < 0:
    raise AgeError('Age must be zero or positive')

# 5) Exception chaining and "from"
#    "raise NewException(...) from original_exception" preserves the original cause.

try:
    int('abc')
except ValueError as original:
    raise ValidationError('age', 'Invalid numeric value') from original

# 6) Using custom exceptions to simplify exception handling
#    Catching a domain-specific exception is clearer than catching many built-in exceptions.
class AuthenticationError(Exception):
    pass

class AuthorizationError(Exception):
    pass

try:
    raise AuthorizationError('User does not have permission')
except AuthenticationError:
    print('Authentication failed')
except AuthorizationError as err:
    print('Authorization failed:', err)

# 7) Best practices for custom exceptions
# - Give the class a clear name ending in "Error".
# - Inherit from a built-in exception class when appropriate.
# - Add custom attributes only when they provide useful error context.
# - Keep exception logic simple and lightweight.
# - Document the exception in the class docstring.

# 8) When to use custom exceptions
# - When the error is specific to your application domain.
# - When you want a single exception type to represent many low-level error conditions.
# - When you need to attach structured metadata to an error.

# 9) Example of custom exception for business logic
class OrderProcessingError(Exception):
    def __init__(self, order_id, reason):
        self.order_id = order_id
        self.reason = reason
        super().__init__(f'Order {order_id} failed: {reason}')

try:
    raise OrderProcessingError(1234, 'Payment authorization failed')
except OrderProcessingError as err:
    print('Order Error:', err)
    print('Order ID:', err.order_id)
    print('Reason:', err.reason)
