import time
from itertools import islice
import linecache
import math

lsteps=open("lsteps.txt","r")
rsteps=open("rsteps.txt","r")
open("lfinal.txt","w").close()
open("rfinal.txt","w").close()
delay=0.6
prev_llen = 0
prev_rlen = 0
curr_lstep = [None]*3
curr_rstep = [None]*3
prev_lstep = [0]*3
prev_rstep = [0]*3

def file_len(file):
	return sum(1 for line in file)	

def dist(prev_step, curr_step):
	step_len=0
	step_len+=(curr_step[0]-prev_step[0])**2
	step_len+=(curr_step[1]-prev_step[1])**2  
	step_len+=(curr_step[2]-prev_step[2])**2
	step_len = math.sqrt(step_len)
	return step_len	

def correct_step(ref_step, curr_step):
	step_len = dist(ref_step, curr_step)
	if step_len > 100:
		nx = ref_step[0] + (curr_step[0]-ref_step[0])*100/step_len
		ny = ref_step[1] + (curr_step[1]-ref_step[1])*100/step_len
		nz = ref_step[2] + (curr_step[2]-ref_step[2])*100/step_len
		return [nx,ny,nz]
	else:
		return curr_step	

while True:
	time.sleep(0.2)  #check for new input every some_time.
	lsteps=open("lsteps.txt","r")
	rsteps=open("rsteps.txt","r")
	curr_llen = file_len(lsteps)
	curr_rlen = file_len(rsteps)
	time.sleep(0.1)  #To wait before entire line is copied.
	
	if curr_llen > prev_llen:
		prev_llen = curr_llen
		lsteps=open("lsteps.txt","r")
		lfinal = open("lfinal.txt","a")
		for lline in islice(lsteps, curr_llen-1, curr_llen):
			ls=lline.split(", ")
			lpkt=float(ls[0])
			curr_lstep = [float(ls[1]),float(ls[2]),float(ls[3])]
			lang=float(ls[4])
			curr_lstep = correct_step(prev_rstep, curr_lstep)
			prev_lstep = curr_lstep
			lfinal.write(str(curr_lstep[0])+" "+str(curr_lstep[1])+"\n")
			print(str(curr_lstep[0])+" "+str(curr_lstep[1]))
			lfinal.close()
	
	if curr_rlen > prev_rlen:
		prev_rlen = curr_rlen
		rsteps=open("rsteps.txt","r")
		rfinal = open("rfinal.txt","a")
		for rline in islice(rsteps, curr_rlen-1, curr_rlen):
			rs=rline.split(", ")
			rpkt=float(rs[0])
			rang=float(rs[4])
			curr_rstep = [float(rs[1]),float(rs[2]),float(rs[3])]
			curr_rstep = correct_step(prev_lstep, curr_rstep)
			prev_rstep = curr_rstep
			rfinal.write(str(curr_rstep[0])+" "+str(curr_rstep[1])+"\n")
			print(str(curr_rstep[0])+" "+str(curr_rstep[1]))
			rfinal.close()
"""
t0 = time.time()
print(file_len(lsteps))
t1 = time.time()
print("Time taken: ", t1-t0)
"""
"""
lsteps=open("lsteps.txt","r")
for line in islice(lsteps, 6, 7):
	print(line)
	print(type(line))
"""