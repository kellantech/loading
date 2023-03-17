def rgbf(r, g, b): 
	return f"\u001b[38;2;{r};{g};{b}m"

def rgbb(r, g, b): 
	return f"\u001b[48;2;{r};{g};{b}m"

RESET = "\u001b[0m"

def cprint(text,fg=(255,255,255),bg=(0,0,0),**kwargs):
	print(rgbf(*fg)+rgbb(*bg)+text+RESET,**kwargs)
