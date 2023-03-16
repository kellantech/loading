import math,time

block = "█"

class determinate:
  def __init__(self,format,char="=",le=10,fill=" ",lead=">"):
    self.format = format
    self.char = char
    self.fill = fill
    self.len = le
    self.lead = lead
  def update(self,pd=-1,done=-1,total=-1):
    
    print('\033[?25l', end="")
    global cchar
    if pd==-1:
      pd = done/total
    csx = math.floor(pd * self.len)
    cstr = ""
    for i in range(csx-1):
      cstr += self.char
    cstr += self.lead
    for i in range(self.len - csx):
      cstr += self.fill
    print("\r", end="", flush=True)
    
    cstr = f"[{cstr}]"
    perc = f"{round(pd*100)}%"

    res = self.format.replace("%bar",cstr).replace("%perc",perc).replace("%frac",f"{done}/{total}")
    print(res,end="\r")
    print('\033[?25h', end="")
  def stop(self,msg="Done!"):
    print('\033[?25h', end="") 
    print(f"\r{msg}" + " " * (self.len+len(self.format)+2))


indeterminate_modes = {
  "classic":["|","/","-","\\"],
  "arrow":["˅","<","˄",">"],
  "dots": ["   ",".  ",".. ","..."],
  "x+": ["×","+","×","+"],
  "spindots":["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"],
  "spindots2":["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"],
  "spindots3":["⠁","⠂","⠄","⡀","⢀","⠠","⠐","⠈"],
  "hamburger":["☱","☲","☴"]
}

class indeterminate_spin:
  def __init__(self,mode="classic",pre="",post=""):
    self.mode = mode
    self.arr = indeterminate_modes[self.mode]
    self.ind = 0
    self.pre = pre
    self.post = post
  def spin(self,rate=0.1):
    print('\033[?25l', end="") 
    print(self.pre+self.arr[self.ind]+self.post,end="\r",flush=True)
    self.ind += 1 
    self.ind %= len(self.arr)
    time.sleep(rate*(4/len(self.arr)))
    
  def stop(self,msg = "DONE!"):
    print("\r"+msg+" "*(len(msg)+len(self.pre)+len(self.post)+1))
    print('\033[?25h', end="") 

class indeterminate_bar:
  def __init__(self,l=10,bar="<-->",fill="·"):
    self.len = l
    self.bar = bar
    self.fill = fill
    self.prog = 0
  def update(self,rate):
    print('\033[?25l', end="") 
    s = [self.fill for _ in range(self.len)]
    for n in range(len(self.bar)):
      try:
        s[n+self.prog] = self.bar[n]
      except:
        pass
    self.prog += 1
    self.prog %= self.len
    print(''.join(s),end="\r",flush=True)
    time.sleep(rate)
