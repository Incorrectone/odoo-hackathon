from functools import wraps
from flask import abort
from flask_login import current_user

def permission_required(whois):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.Role_ID == whois and not current_user.is_admin():
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator