import inspect


class Container:
    __entries = {}

    def get(self, id: str):
        if not self.has(id):
            self.set(id)

        return self.resolve(id)

    def has(self, id: str):
        return id in self.__entries[id]

    def set(self, abstract, concrete=None):
        if concrete is None:
            concrete = abstract
        self.__entries[abstract] = concrete

    def resolve(self, alias):
        return self.get_entries(inspect.signature(alias.__init__).parameters, alias)

    def get_entries(self, constructor_signature, alias):
        entries = {}
        for param in constructor_signature:
            if param == 'self' or param == 'cls':
                entries[str(param)] = alias
                continue

            if constructor_signature[param].default is not inspect.Parameter.empty:
                entries[str(param)] = constructor_signature[param].default

            if constructor_signature[param].default is inspect.Parameter.empty:
                if isinstance(inspect.isclass(constructor_signature[param].annotation),
                              (float, int, str, tuple, set, dict, bool, list, inspect._empty)):
                    pass
        return entries
