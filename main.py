import math,time,os
from color import cprint

block = "█"
mdot = "·"

lup = "\u001b[1E"
ldown = "\u001b[1F"


class determinate:
  def __init__(self,format="%bar",char="=",l=50,fill=" ",lead=">",fg=(255,255,255),bg=(0,0,0)):
    self.format = format
    self.char = char
    self.fill = fill
    self.len = l
    self.lead = lead
    self.fg = fg
    
    self.bg = bg
    self.init = 0
    if self.len <= 0:
      raise ValueError("bar must have length")
  def update(self,pd=-1,done=-1,total=-1):
    print('\033[?25l', end="")

    global cchar
    if pd==-1:
      pd = done//total

    csx = math.floor(pd * self.len)
    if csx>1:
      cstr = ""
      for i in range(csx-1):
        cstr += self.char
      cstr += self.lead
      for i in range(self.len - csx):
        cstr += self.fill
    else:
      cstr = self.fill * self.len
    print("\r", end="", flush=True)
    
    perc = f"{round(pd*100)}%"
    res = self.format.replace("%bar",cstr).replace("%perc",perc).replace("%frac",f"{done}/{total} ")
    cprint(res,self.fg,self.bg,end="\r")
    print('\033[?25h', end="")
  def stop(self,msg="Done!"):
    print('\033[?25h', end="") 
    cprint(f"\r{msg}" + " " * (self.len+len(self.format)+2),self.fg,self.bg)
  def error(self,msg,fg=(255,0,0),bg=(0,0,0)):
    print('\033[?25h', end="") 
    print(end="\x1b[2K")
    cprint(f"\r{msg}",fg,bg,flush=True)
    os._exit(1)
indeterminate_modes = {
  "classic":["|","/","-","\\"],
  "arrow":[ "▹▹▹▹▹","▸▹▹▹▹","▹▸▹▹▹","▹▹▸▹▹","▹▹▹▸▹","▹▹▹▹▸"
],
  "dots": ["   ",".  ",".. ","..."],
  "x+": ["×","+","×","+"],
  "spindots":["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"],
  "spindots2":["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"],
  "spindots3":["⠁","⠂","⠄","⡀","⢀","⠠","⠐","⠈"],
  "hamburger":["☱","☲","☴"],
  "vdots": [".",":"," ",],
}

class indeterminate_spin:
  def __init__(self,mode="classic",pre="",post="",fg=(255,255,255),bg=(0,0,0)):
    if type(mode) == str:
      self.mode = mode
      self.arr = indeterminate_modes[self.mode]
    elif type(mode) == list:
      self.mode = "custom"
      self.arr = mode


    self.ind = 0

    self.pre = pre
    self.post = post
    self.fg = fg
    self.bg = bg
  def update(self,rate=0.1):
    print('\033[?25l', end="") 
    cprint(self.pre+self.arr[self.ind]+self.post,self.fg,self.bg,end="\r",flush=True)
    self.ind += 1 
    self.ind %= len(self.arr)
    time.sleep(rate*(4/len(self.arr)))
    
  def stop(self,msg = "DONE!"):
    print(end="\x1b[2K")
    print(end="\x1b[2K")

    cprint("\r"+msg,self.fg,self.bg)
    print('\033[?25h', end="") 
  def error(self,msg,fg=(255,0,0),bg=(0,0,0)):
      print('\033[?25h', end="") 
      print(end="\x1b[2K")
      cprint(f"\r{msg}",fg,bg,flush=True)

      os._exit(1)
class indeterminate_bar:
  def __init__(self,format="%bar",l=50,bar="<-->",fill=mdot,fg=(255,255,255),bg=(0,0,0)):
    self.len = l
    self.bar = bar
    self.fill = fill
    self.prog = 0
    self.format = format
    self.add = +1
    self.fg = fg
    self.bg = bg
    if len(self.bar) > self.len:
      raise ValueError("moving bar must not be longer than big bar")
    if len(self.bar) <= 0 or self.len <= 0:
      raise ValueError("both bars must have length")
  def update(self,rate=0.1):
    print('\033[?25l', end="") 
    s = [self.fill for _ in range(self.len)]
    for n in range(len(self.bar)):
      try:
        s[n+self.prog] = self.bar[n]
      except:
        pass
    self.prog += self.add
    if self.prog > self.len-len(self.bar)-1:
      self.add = -1
    if self.prog<1:
      self.add = +1
    s = ''.join(s)
    
    cprint(self.format.replace("%bar",s),self.fg,self.bg,end="\r",flush=True)
    time.sleep(rate)
  def stop(self,msg="Done!"):
    print('\033[?25h', end="") 
    print(end="\x1b[2K")

    cprint(f"\r{msg}",self.fg,self.bg)
  def error(self,msg,fg=(255,0,0),bg=(0,0,0)):
      print('\033[?25h', end="") 
      print(end="\x1b[2K")
      cprint(f"\r{msg}",fg,bg,flush=True)
      os._exit(1)


  
