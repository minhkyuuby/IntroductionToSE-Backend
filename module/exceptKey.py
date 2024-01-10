def exceptKey(data, keys):
    if isinstance(data, list):
        return [exceptKey(d, keys) for d in data]
    elif isinstance(data, dict):
        r = data.copy()
        for k in keys:
            if k in r:
                del r[k]
        return r
    else:
        return data