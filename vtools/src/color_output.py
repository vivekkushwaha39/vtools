class ColorOutput:
    
    COLOR_BLUE = 34
    COLOR_RED = 31
    COLOR_GREEN = 32
    COLOR_BLACK = 30
    
    STYLE_NONE = 0
    STYLE_BOLD = 1
    STYLE_UNDERLINE = 2
    
    BG_COLOR_BLACK = 40
    
    @classmethod
    def getColorString( cls, color=COLOR_BLACK, bgcolor = BG_COLOR_BLACK, style=STYLE_NONE ):
        return "\033[" + str( style ) + ";" + str( color ) + ";" + str( bgcolor ) +"m"
    
    @classmethod
    def getReset( cls ):
        return "\033[00m"