def dict_creator(list_values):
    temps = {}

    for val in list_values:
        if '=' in val:
            args = val.split('=')
            key = args[0]
            vals = args[1]
            temps.update({key: vals})
    return actual(temps)


def actual(values):
    temp = {}

    for key, val in values.items():
        if val.startswith('"'):
            temp[key] = val.strip('"').replace("_", " ")
        elif val.isdigit():
            temp[key] = int(val)
        elif val.count(".") == 1:
            try:
                temp[key] = float(val)
            except Exception:
                pass
    return (temp)
