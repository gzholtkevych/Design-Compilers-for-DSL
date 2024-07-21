from typing import List
from alphabet import *


def text_preprocessing(text: str) -> List[str]:
    """parts text into pieces such that
    1) each piece does not contain whitespaces
    2) if a piece contains a sign then it contains only signs
    3) after joining all the pieces, the obtained string equals 'text'
       without whitespaces.

    Args:
        text (str): the analized text

    Raises:
        ValueError: extraneous symbols been found in 'text'

    Returns:
        List[str]: list of pieces
    """    
    # find extraneous symbols in 'text'
    bad_symbols = " ".join(c for c in text if not issymbol(c))
    if bad_symbols:
        raise ValueError(
            f"the text contains extraneous symbols '{bad_symbols}'")
    # part 'text' into pieces
    text_rest, outcome = text, []
    while text_rest:
        text_rest = text_rest.lstrip(wsstr())
        if not text_rest:
            break
        if text_rest[0] in signs():
            for ic, c in enumerate(text_rest):
                if c not in signs():
                    break
                else:
                    continue
            outcome.append(text_rest[: ic])
            text_rest = text_rest[ic :]
            continue
        for ic, c in enumerate(text_rest):
            if c in signs() or c in whitespaces():
                break
            else:
                continue
        outcome.append(text_rest[: ic])
        text_rest = text_rest[ic :]
    return outcome