class SampleClass():
    """
    This is the starting line of the class' docstring.
    
    Newlines are preserved, apparently. It looks as though it keeps wrapping a
    paragraph until two newlines are detected, but I'm going to keep writing until
    it seems excessive just to find out. Blah blah blah.
    
    This formatting is called reStructuredText -- `reST`_.
    It is supported natively by Python and is quite handy for new developers coming into the
    codebase. It really makes learning the codebase quite simple. It uses the `:` symbol to signify parameters,
    return type, and exceptions that could be raised. The **`** is used to signify code.
    Now let's get into the parameters.
    
    :param param1: Some explanation on param1. It is an int and can be nothing else,
    and is not an optional argument.
    
    :param param2: This is an optional argument and expects a string.
    
    :raises ValueError: If you try to instantiate with only a string, I think
    a ValueError is raised. Or maybe it's a TypeError. I don't know. Try it and find out.
    
    .. _reST: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer
    """
    
    def __init__(self,
        param1: int,
        param2: str = ""
    ):
        """
        Specific information for initializing the class.
        
        :param param1: It should be an int (probably).
        :param (optional) param2: Not required, and should be a string.
        """
    
    
    def __privateMethod(self):
        """
        Some other formatting is also possible, like Epytext, which is a javadoc style of formatting.
        It appears to work almost the same way, but with ``@``'s instead of ``:``'s. I honestly kind
        of like this one more because the symbol stands out more when writing it, but it looks like it
        only works with parameters and not the return or raises.
        
        @param none:
        
        @return broken: There's probably a different way to format these but I can't be bothered to look.
        :return str: Returns a string. (Not really, don't test that -- it's just an empty method).
        """
        
        
    def listsAndLink(self, param: str):
        """
        It is possible to make **lists**. 
        
        * List item 1
        * List item 2
        
        1. Numbered list
        2. Another one
        
        1. A different kind of numbered list
        2. The numbering is somewhat automatic
        3. And will continue the numbering from above (this is numbered 3, but shows as 5)
        
        :param param: Accepts a string to do... something. Here's an inline `link <https://google.com>`_.
        
        Or an explicit one: https://google.com
        """
        
        
    def linksAndCodeBlocks(self) -> None:
        """
        A link with a seperate `reference`_.
        .. _reference: https://google.com
        
        Here's a code block::
        
            print("Some text", "goes here.")
            print()
            
        And we're back.
        
        :param none:
        :return none:
        """
        
    
    def directives(self):
        """
        .. ATTENTION::
            some damn thing
            
            :Stuff: a thing
            
        .. options::
            * -m: Run a module as a script
            * -n: Some thing or another
        """
    
    
    def __repr__(self):
        return "This is the sample class' representation method. It is intended for use "\
            "by the programmer, and as such usually contains very detailed "\
            "information. Often, it can be used to instantiate an identical instance of that class by providing "\
            "itself as a the intializer argument. It is viewable by running just the object from a python terminal."
    
    
    def __str__(self):
        return "This is the sample class' string method. It is intended for use by users, so "\
            "tends to contain brief, easy to digest information."
    
    
test = SampleClass(5)
print(test)