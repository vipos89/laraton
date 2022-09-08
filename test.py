import inspect


class Ololo:
    def __init__(self, a=1):
        self.a = 1

    def test(self, b=1):
        self.a = b
        return 123


# def resolve(alias, method):
#     if method == '__init__':
#         constructor_signature = inspect.signature(alias.__init__).parameters
#     else:
#         fun = getattr(alias, method)
#         constructor_signature = inspect.signature(fun).parameters
#     entries = get_entries(constructor_signature, alias)
#
#     return entries
#
#
# def get_entries(constructor_signature, obj):
#     entries = []
#     print(constructor_signature)
#     for param in constructor_signature:
#         if param == 'self' or param == 'cls':
#             entries = [obj]
#             continue
#
#         if constructor_signature[param].default is not inspect.Parameter.empty:
#             entries.append(constructor_signature[param].default)
#
#         if constructor_signature[param].default is inspect.Parameter.empty:
#             if isinstance(inspect.isclass(constructor_signature[param].annotation),
#                           (float, int, str, tuple, set, dict, bool, list, inspect._empty)):
#                 pass
#     return entries


# attrs = resolve(Ololo, '__init__')
# obj = Ololo(attrs)
# attrs2 = resolve(obj, 'test')
# res= getattr(obj, 'test')(resolve(obj, 'test'))
# print(res)
