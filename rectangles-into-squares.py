def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    short, long = sorted((lng, wdth))
    result = []
    while short != long:
        result.append(short)
        long -= short
        short, long = sorted((short, long))
    result.append(short)
    return result
