from typing import List


alphabet = {}
alphabet['chars'] = {chr(i) for i in range(ord('a'), ord('z') + 1)}.union(
    {chr(i) for i in range(ord('A'), ord('Z') + 1)})
alphabet['digits'] = {chr(i) for i in range(ord('0'), ord('9') + 1)}


def issymbol(x) -> bool:
	return isinstance(x, str) and len(x) == 1


def ischar(x) -> bool:
	return issymbol(x) and (ord('a') <= ord(x) <= ord('z') or
	                        ord('A') <= ord(x) <= ord('Z'))


def isdigit(x) -> bool:
	return issymbol(x) and (ord('0') <= ord(x) <= ord('9'))


def iswhitespace(x) -> bool:
	whitespaces = " \n\t"  # this item can be changed
	return issymbol(x) and x in whitespaces


def issign(x) -> bool:
	signs = "+-*/><="  # this item can be changed
	return issymbol(x) and x in signs


def isother(x) -> bool:
	return issymbol(x) and not (ischar(x) or
								isdigit(x) or
								iswhitespace(x) or
								issign(x))


def remove_whitespaces(text: str, whitespaces: str=" \n\t") -> List[str]:
    # trim whitespaces from head and tail
    text_for_preprocessing, result = text.strip(whitespaces), []
    # first positions of whitespaces
    trials = list(filter(lambda x: x >= 0,
                         [text_for_preprocessing.find(c) for
                          c in whitespaces]))
    while trials:  # break if there is no whitespace
        index = min(trials)  # position of the first whitespace
        result.append(text_for_preprocessing[: index])
        text_for_preprocessing = text_for_preprocessing[index : ]
        text_for_preprocessing = text_for_preprocessing.lstrip(whitespaces)
        trials = list(filter(lambda x: x >= 0,
                             [text_for_preprocessing.find(c) for
                              c in whitespaces]))
    result.append(text_for_preprocessing)
    return result


def split_operators(text: str, signs: str="+-*/^%") -> List[str]:
    if text:
        if issign(text[0])
        pass
    else:
        return []