
# Task 5.7
# Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
# Try to change x to a list `[1,2,3]`. Explain the result.
# Try to change import to `from x import *` where x - module names. Explain the result.

"""

1) something like this
******************************
already_loaded_modules =[]

get_all_import_modules(module): = [ list ]
    all_import_modules_if_exists = []
    ...
    ... check all available imports in the file => for example: [import mod_c, import mod_b]
    ... search in local dir => PYTHONPATH => usr/local/lib/pythonX => sys.path => Built-in modules => return ImportError !
    ... add to all_import_modules_if_exists
    return all_import_modules_if_exists


init_module(module): = bool
    global already_loaded_modules

    all_import_modules = get_all_import_modules(module)

    for import_module in all_import_modules:
            if not import_module in already_loaded_modules:
                    init_module(import_module)
                    already_loaded_modules.append(import_module)

    some_load_function(module)

if name == "__main__":
    init_module(self)
****************************

    1) Run the module `modules/mod_a.py`. Check its result. Explain why does this happen.
        start: mode_a (get mod_c.x=>6) <= mode_b (set mod_c.x=6) <= mod_c (set x=5)
        After importing a module, its name becomes a variable through which you can access the attributes of the module.

    2) Try to change x to a list `[1,2,3]`. Explain the result.
        mode_a (set mod_c.x = [1,2,3])
        mode_b (get mod_c.x=> [1,2,3])
        mode_c (get mod_c.x=> [1,2,3])

    3) Try to change import to `from x import *` where x - module names. Explain the result.
        after `from x import *`, we got { module 'builtins' (built-in) } and can use variables like global.
        from mod_c import *
            mode_a (get x => 5)
            mode_a (set x = [1,2,3])
            mode_a (get x => [1,2,3])
"""



