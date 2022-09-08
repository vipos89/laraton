import os, pkgutil, ast
import sys


def get_command_list(search_path: str):
    all_modules = [x[1] for x in pkgutil.iter_modules(path=[search_path])]
    namespace = search_path.replace(os.sep, '.')
    commands = {}
    for module in all_modules:
        code = open(os.path.join(os.path.join(search_path, module + '.py')), 'rb').read()
        tree = ast.parse(code)
        classes = [i.name for i in tree.body]

        mod = __import__(namespace + '.' + module, fromlist=classes)
        for class_name in classes:
            obj = getattr(mod, class_name)
            commands[obj.name.lower()] = {
                'description': obj.description,
                'obj': obj()
            }

    return commands


if __name__ == "__main__":
    commands = get_command_list(str(os.path.join('laraton', 'console')))
    arguments = sys.argv[1:]
    try:
        if len(arguments) == 0:
            [print("\033[31m {} \033[32m {}".format(command, commands[command]['description'])) for command in commands]
        else:
            command_name = arguments[0].lower()
            if command_name == 'help':
                [print("\033[31m {} \033[32m {}".format(command, commands[command]['description'])) for command in
                 commands]
            else:
                if command_name in commands:
                    commands[command_name]['obj'].handle()
                else:
                    raise Exception('command not found')
    except Exception as error:
        print("\033[31m {} ".format(error))
