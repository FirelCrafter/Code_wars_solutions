def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        t = g * 3600 / (v2-v1)
        return [int(t / 3600), int((t % 3600)/60), int(t % 60)]
