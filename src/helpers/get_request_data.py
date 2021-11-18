
from functools import wraps
from flask import g



class RequestContentType ():

    @staticmethod
    def get_data(request):
        def get_data_decorator(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                if request.args:
                    g.params = request.args.to_dict(flat=True)

                if request.is_json:
                    if request.headers['Content-Type'].find('application/json') != -1:
                        g.body = request.get_json()
                        return function(*args, **kwargs)

                elif request.headers['Content-Type'].find('multipart/form-data') != -1:
                        form_values = request.form.to_dict(flat=False)
                        result = {
                                    key: form_values[key][0] if len(form_values[key]) == 1 else form_values[key]
                                    for key in form_values
                                }
                        g.body = dict(**result)
                        return function(*args, **kwargs)

            return wrapper

        return get_data_decorator



get_data = RequestContentType.get_data