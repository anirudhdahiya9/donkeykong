from bard import *
from boarditems import *
from donkey import *
from ball import *
class player(boarditems):
	def __init__(self):
		boarditems.__init__(self,1,24)
		self.score=0
		self.lives=3

	def getcoin(self,brd):
		if brd.getitem(self.x,self.y)=='C':
			brd.updateitem(self.x,self.y,' ')
			self.score+=5
	
	def checkdeath(self):
		from time import sleep
		if self.lives<=0:	
			print 'GAME OVER!!!!!!!!'
			sleep(2)
			exit()
	def initpos(self):
		self.x=2
		self.y=24

	def checkqueen(self):
		from time import sleep
		if self.x==13 and self.y==1:
			print 'You win!','Wanna play again? (y/n):'
			ans=getchar()
			if ans.lower()=='y':
				main()
			print 'Bye! Have fun with that princess!!'
			sleep(4)
			exit()

	def checkdonkey(self,don,fl):
		import os
		from time import sleep
		if self.x==don.x and self.y==don.y:
			os.system('clear')
			print 'Oops!! That Hurt!'
			self.lives-=1
			sleep(1)
			self.score=0
			fl=1
			return fl
		if self.x==don.x+1 and self.y==don.y:
			if self.direction==1 and don.direction==0:
				os.system('clear')
				print 'Oops!! That Hurt!'
				self.lives-=1
				sleep(1)
				self.score=0
				fl=1
				return fl
		if self.x==don.x-1 and self.y==don.y:
			if self.direction==0 and don.direction==1:
				os.system('clear')
				print 'Oops!! That Hurt!'
				self.lives-=1
				sleep(1)
				self.score=0
				fl=1
				return fl

	def checkball(self,b1,fl):
		import os
		from time import sleep
		for i in b1:
			if i.x==self.x and i.y==self.y:
				os.system('clear')
				print 'Oops!! That Hurt!'
				self.lives-=1
				sleep(1)
				self.score=0
				fl=2
				break
			if i.x==self.x+1 and i.y==self.y:
				if i.direction==1 and self.direction==0:
					os.system('clear')
					print 'Oops!! That Hurt!'
					self.lives-=1
					sleep(1)
					self.score=0
					fl=2
					break
			if i.x==self.x-1 and i.y==self.y:
				if i.direction==0 and self.direction==1:
					os.system('clear')
					print 'Oops!! That Hurt!'
					self.lives-=1
					sleep(1)
					self.score=0
					fl=2
					break
		if fl==2:
			fl=1
			return fl

	def getdir(self,mv):
		if mv.lower()=='a':
			self.direction=1
		elif mv.lower()=='d':
			self.direction=0
		return self
			

# 0 means right diredwction, 1 means left
	def move(self,plr,brd,mode=0,mv=''):
		if mv=='':
			pass
		elif mv.lower()=='d':
			if brd.checkwall(plr,mv):
				return plr
			else:
				self.getcoin(brd)
				plr.x+=1
				return plr
		elif mv.lower()=='a':
			if brd.checkwall(plr,mv):
				return plr
			else:
				self.getcoin(brd)
				plr.x-=1
				return plr
		elif mv.lower()=='w':
		  	if mode==0:
				if not brd.getitem(self.x,self.y)=='H':
					return plr
				if brd.checkwall(plr,mv):
					return plr
				else:
					self.getcoin(brd)
					plr.y-=1
					return plr
			elif mode==1:
				if brd.checkwall(plr,mv):
					return plr
				else:
					self.getcoin(brd)
					plr.y-=1
					return plr
				
		elif mv.lower()=='s':
			if brd.checkwall(plr,mv):
				return plr
			else:
				self.getcoin(brd)
				plr.y+=1
				return plr
		elif mv.lower()=='q':
			exit()
		else:
			return plr
	
	def checkfall(self,brd,don,b1):
		from time import sleep
		while not brd.checkfloor(self):
			sleep(0.12)
			self=self.move(self,brd,0,'s')
			brd.printboard(self,don,b1)
		return self
	
	def jump(self,brd,don,b1):
		if self.direction==0:
			if brd.getitem(y=self.y-1,x=self.x+1)!='X':
				self=self.move(self,brd,0,'d')
				self=self.move(self,brd,1,'w')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
					
			if brd.getitem(y=self.y-1,x=self.x+1)!='X':
				self=self.move(self,brd,0,'d')
				self=self.move(self,brd,1,'w')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
			if brd.getitem(y=self.y+1,x=self.x+1)!='X':
				self=self.move(self,brd,0,'d')
				self=self.move(self,brd,1,'s')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
		
			if brd.getitem(y=self.y+1,x=self.x+1)!='X':
				self=self.move(self,brd,0,'d')
				self=self.move(self,brd,1,'s')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
		elif self.direction==1:
			if brd.getitem(y=self.y-1,x=self.x-1)!='X':
				self=self.move(self,brd,0,'a')
				self=self.move(self,brd,1,'w')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
					
			if brd.getitem(y=self.y-1,x=self.x-1)!='X':
				self=self.move(self,brd,0,'a')
				self=self.move(self,brd,1,'w')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
			if brd.getitem(y=self.y+1,x=self.x-1)!='X':
				self=self.move(self,brd,0,'a')
				self=self.move(self,brd,1,'s')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
		
			if brd.getitem(y=self.y+1,x=self.x-1)!='X':
				self=self.move(self,brd,0,'a')
				self=self.move(self,brd,1,'s')
				brd.printboard(self,don,b1)
			else:
				self=self.checkfall(brd,don,b1)
		return self
