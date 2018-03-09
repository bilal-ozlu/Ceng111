def cm(lst):
	return cmhelp(lst,0,0.0,0.0,0.0)
def cmhelp(lst,n,total,cmx,cmy): #n number of the shape; total total area; cmx x-coordinates; cmy y-coordinates

	if n != len(lst) and len(lst[n])==4: #it's a circle
		total = total + (lst[n][0])*3.1415926535897932*((lst[n][3])**2.0) #(area of a circle)

		cmx = cmx + (lst[n][0])*3.1415926535897932*((lst[n][3])**2.0)*(lst[n][1]) #(area * x-coordinate of the circle) 

		cmy = cmy + (lst[n][0])*3.1415926535897932*((lst[n][3])**2.0)*(lst[n][2]) #(area * y-coordinate of the circle)

		n=n+1
		
		return cmhelp(lst,n,total,cmx,cmy)

	elif n != len(lst) and len(lst[n])==7: #it's a triangle
		total = total + (lst[n])[0]*(0.5)*abs(1.0*lst[n][1]*lst[n][4]+1.0*lst[n][3]*lst[n][6]+1.0*lst[n][5]*lst[n][2]-1.0*lst[n][2]*lst[n][3]-1.0*lst[n][4]*lst[n][5]-1.0*lst[n][6]*lst[n][1]) #(area of a triangle)

		cmx = cmx + ((lst[n])[0]*(0.5)*abs(1.0*lst[n][1]*lst[n][4]+1.0*lst[n][3]*lst[n][6]+1.0*lst[n][5]*lst[n][2]-1.0*lst[n][2]*lst[n][3]-1.0*lst[n][4]*lst[n][5]-1.0*lst[n][6]*lst[n][1]))*((lst[n][1]+lst[n][3]+lst[n][5])/3.0) #(area * x-coordinate of the triangle)

		cmy = cmy + ((lst[n])[0]*(0.5)*abs(1.0*lst[n][1]*lst[n][4]+1.0*lst[n][3]*lst[n][6]+1.0*lst[n][5]*lst[n][2]-1.0*lst[n][2]*lst[n][3]-1.0*lst[n][4]*lst[n][5]-1.0*lst[n][6]*lst[n][1]))*((lst[n][2]+lst[n][4]+lst[n][6])/3.0) #(area * y-coordinate of the triangle)

		n=n+1

		return cmhelp(lst,n,total,cmx,cmy)

	elif n != len(lst) and len(lst[n])==9: #it's a rectangle
		total = total + lst[n][0]*(1.0)*abs(1.0*lst[n][1]*lst[n][4]+1.0*lst[n][3]*lst[n][6]+1.0*lst[n][5]*lst[n][2]-1.0*lst[n][2]*lst[n][3]-1.0*lst[n][4]*lst[n][5]-1.0*lst[n][6]*lst[n][1]) #(area of a rectangle)

		cmx = cmx + lst[n][0]*(1.0)*abs(1.0*lst[n][1]*lst[n][4]+1.0*lst[n][3]*lst[n][6]+1.0*lst[n][5]*lst[n][2]-1.0*lst[n][2]*lst[n][3]-1.0*lst[n][4]*lst[n][5]-1.0*lst[n][6]*lst[n][1])*((lst[n][1]+lst[n][3]+lst[n][5]+lst[n][7])/4.0) #(area * x-coordinate of the rectangle) 

		cmy = cmy + lst[n][0]*(1.0)*abs(1.0*lst[n][1]*lst[n][4]+1.0*lst[n][3]*lst[n][6]+1.0*lst[n][5]*lst[n][2]-1.0*lst[n][2]*lst[n][3]-1.0*lst[n][4]*lst[n][5]-1.0*lst[n][6]*lst[n][1])*((lst[n][2]+lst[n][4]+lst[n][6]+lst[n][8])/4.0) #(area * y-coordinate of the rectangle)

		n=n+1

		return cmhelp(lst,n,total,cmx,cmy)
	elif n == len(lst):
		return [cmx/float(total) , cmy/float(total) , float(total)] #[CM in x-coordinate , CM in y-coordinate , total mass]
