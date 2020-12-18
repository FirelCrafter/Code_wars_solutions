def validate_pin(pin):
    return True if pin.isdigit() and len(pin) in (4, 6) else False
