def bouncing_ball(h, bounce, window):
    if h > 0 and 1 > bounce > 0 and window < h:
        m = 1
        while h*bounce > window:
            h *= bounce
            m += 2
        return m
    else:
        return -1
