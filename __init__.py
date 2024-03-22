basicTypeList = [int, float, str, bool]
basicContainerList = [list, tuple]


def toDict(src):
    tarDict = {
        "_m_": src.__class__.__module__,
        "_n_": src.__class__.__name__,
    }
    srcDict = vars(src)
    for key in srcDict:
        value = srcDict[key]
        valueType = type(value)
        if valueType in basicTypeList:
            tarDict[key] = value
        elif valueType in basicContainerList:
            tarDict[key] = toListDict(value)
        else:
            tarDict[key] = toDict(value)
    return tarDict


def toListDict(oldList):
    newList = []
    for value in oldList:
        valueType = type(value)
        if valueType in basicTypeList:
            newList.append(value)
        elif valueType in basicContainerList:
            newList.append(toListDict(value))
        else:
            newList.append(toDict(value))
    if type(oldList) == tuple:
        return tuple(newList)
    return newList


def fromDict(srcDict):
    tarObj = getattr(__import__(srcDict["_m_"], fromlist=[""]), srcDict["_n_"])()
    for key in srcDict:
        if key not in ["_m_", "_n_"]:
            value = srcDict[key]
            valueType = type(value)
            if valueType in basicTypeList:
                setattr(tarObj, key, value)
            elif valueType in basicContainerList:
                setattr(tarObj, key, fromListDict(value))
            else:
                setattr(tarObj, key, fromDict(value))
    return tarObj


def fromListDict(oldList):
    newList = []
    for value in oldList:
        if type(value) in basicTypeList:
            newList.append(value)
        elif type(value) in basicContainerList:
            newList.append(fromListDict(value))
        else:
            newList.append(fromDict(value))
    if type(oldList) == tuple:
        return tuple(newList)
    return newList
