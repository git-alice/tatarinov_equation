from IPython.display import display, Markdown
from typing import List, Any

def display_list(l: List[Any], spaces: bool = False):
    for x in l:
        if spaces:
            display(Markdown('---'))
            # print('@@@'.center('_', 50))
        display(x)
