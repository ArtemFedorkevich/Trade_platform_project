from rest_framework.views import exception_handler


def core_exception_handler(exc, context):
    # If an exception is thrown that we do not explicitly handle here, we
    # we want to pass it to the default exception handler offered by
    # DRF. And yet, if we are handling this type of exception, we need
    # access to the generated DRF - get it in advance here.
    response = exception_handler(exc, context)
    handlers = {'ValidationError': _handle_generic_error
                }
    # Determine the type of the current exception. We will use this immediately further,
    # to decide whether to do it yourself or give it the job to DRF.
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        # If this exception can be handled, handle it. Otherwise
        # case, return a response generated by standard means in advance
        return handlers[exception_class](exc, context, response)

    return response


def _handle_generic_error(exc, context, response):
    # This is the simplest exception handler we can create. We
    # take the response generated by DRF and enclose it in the 'errors' key.
    response.data = {
        'errors': response.data
    }
    return response
