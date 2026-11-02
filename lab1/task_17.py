def merge_dicts(dict_a , dict_b):
    for key in dict_b:
        if key in dict_a:
            val_a=dict_a[key]
            val_b=dict_b[key]
            if type(val_a)==dict and type(val_b)==dict:
                merge_dicts(val_a, val_b)
            else:
                dict_a[key] = val_b
        else:
            dict_a[key] = dict_b[key]


a = {"a": 1, "b": {"c": 1, "f": 4}}
b = {"d": 1, "b": {"c": 2, "e": 3}}
merge_dicts(a, b)
print("Результат :", a)
