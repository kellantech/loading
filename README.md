# loadingstuff


### A fully customizable library for loading bars, spinners, and animations


#### install

```
pip install loadingstuff
```


### determinate


bar = loadingstuff.determinate(format="[%bar]",char=loadingstuff.block,l=50,lead=None,fg=(255,255,255),bg=None)  
paramaters:  
format: format of the loader. options:
- %bar: progress bar
- %perc: percent done
- %frac: fraction. only applicable in some cases
- %log: log message

char: bar charictar  
fill: charictar to fill blank space  
lead: leading charictar of bar
fg: forground color
bg: background color

methods:  
`bar.update(pd=-1,done=-1,total=-1)`

pd: percent done (0-1)

OR

done: steps done  
and  
total: total steps 

(done and total used to compute %frac)

--- 

update %log  
`bar.log(msg)`  
msg: logging message  

---

print an ending message  
`bar.stop(msg="Done!")`  
msg: message  

---

exit the program,and display an error  
`bar.error(msg,fg=(255,0,0),bg=None)`

msg: message  
fg: forground color  
bg: background color  

---

example:

```python
#import
import time,threading
import loadingstuff 

pd = 0


#slow function
def slow():
  global pd
  while pd<=100:
    time.sleep(.05)
    pd += 1

loadingstuff.init() # initalize 
ml = loadingstuff.determinate("[%bar] %perc",l="full",fg=loadingstuff.color.green) # create bar
def load(): # update 
  while pd<101:
    ml.update(pd/100)

  ml.stop()
# start threads
s=threading.Thread(target=slow)
u=threading.Thread(target=load)
s.start()
u.start()

s.join()
u.join()

```

### indeterminate spinner 

spinner = loadingstuff.indeterminate_spin(mode="classic",pre="",post="",fg=(255,255,255),bg=None)  
paramaters:  
mode: mode of the spinner. options:
- classic
- arrow
- dots
- x+
- spindots
- spindots2
- spindots3
- hamburger
- vdots
- c2in
- c2out
- c2s
- letter
- rundots
- expand
- missing
- cycle


pre: text before spinner  
post: text after spinner  
fg: forground color  
bg: background color  

methods:  
`spinner.update(rate=0.1)`  
rate: time between updated

---

print an ending message  
`spinner.stop(msg="Done!")`  
msg: message  

---

exit the program,and display an error  
`spinner.error(msg,fg=(255,0,0),bg=None)`

msg: message  
fg: forground color  
bg: background color  

---

example:

```python
#import
import time,threading
import loadingstuff 

pd = 0


#slow function
def slow():
  global pd
  while pd<=100:
    time.sleep(.05)
    pd += 1

loadingstuff.init() # initalize 
ml = loadingstuff.determinate('classic',fg=loadingstuff.color.green)# create spinner
def load(): # update 
  while pd<101:
    ml.update()

  ml.stop()
# start threads
s=threading.Thread(target=slow)
u=threading.Thread(target=load)
s.start()
u.start()

s.join()
u.join()

```
