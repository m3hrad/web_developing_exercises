def keyword_usage(str, lst):
    words = str.split();
    resultList = [];
    for eachList in lst:
        if (eachList in words):
             resultList.append(True);
        else:
             resultList.append(False);
    result = tuple(resultList);
    return result;
