import sys
sys.path.append('../../test')
from test.steps.login_steps import attemptLoginAsBadUser, attemptLoginAsTestUser, attemptloginAs, loadLoginPage, goToSignUpPage, verifyLoginFailure, verifyLoginSuccess
from test.steps.setup_steps import closeDriver, createDriver
from test.context import Context

# test that the test user can log in successfully
with Context() as context:
    createDriver(context=context)
    try:
        loadLoginPage(context)
        attemptLoginAsTestUser(context)
        verifyLoginSuccess(context)
    finally:
        closeDriver(context)

# test that the bad user credetials fail to login
with Context() as context:
    createDriver(context=context)
    try:
        loadLoginPage(context)
        attemptLoginAsBadUser(context)
        verifyLoginFailure(context)
    finally:
        closeDriver(context)