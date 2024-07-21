from alphabet import *
from text_preprocessing import *


addsign('~')
text = """    aaaa   bbbb 1234~678
#       &?
"""

print(text_preprocessing(text))