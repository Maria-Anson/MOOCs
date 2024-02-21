# Objects and Classes
> 
> Total points 3
> 
>  1.Question 1
> 
> Consider the class Rectangle, what are the data attributes:
> 
> <pre contenteditable="false" data-language="python" style="opacity: 1;" tabindex="0">
> 
> 
> class Rectangle(object):
> 
>     def __init__(self,width=2,height =3,color='r'):
> 
>         self.height=height 
> 
>         self.width=width
> 
>         self.color=color
> 
>     def drawRectangle(self):
> 
>         import matplotlib.pyplot as plt
> 
>         plt.gca().add_patch(plt.Rectangle((0, 0),self.width, self.height ,fc
> 
>           =self.color))
> 
>         plt.axis('scaled')
> 
>         plt.show()
> 
> XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
> 
> </pre>
> 
> 1 point 
> 

      self.height, self.width,self.color 
> 
>  drawRectangle 
> 
>  __init__ 
> 
>  2.Question 2
> 
> What is the result of running the following lines of code ?
> 
> <pre contenteditable="false" data-language="python" style="opacity: 1;" tabindex="0">
> 
> class Points(object):
> 
>   def __init__(self,x,y):
> 
>     self.x=x
> 
>     self.y=y
> 
>   def print_point(self):
> 
>     print('x=',self.x,' y=',self.y)
> 
> p1=Points("A","B")
> 
> p1.print_point()
> 
> XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
> 
> </pre>
> 
> 1 point 
> 
>  x= A 
> 
>  y= B 
> 

      x= A y= B 
> 
>  3.Question 3
> 
> What is the result of running the following lines of code ?
> 
> <pre contenteditable="false" data-language="python" style="opacity: 1;" tabindex="0">
> 
> class Points(object):
> 
>   def __init__(self,x,y):
> 
>     self.x=x
> 
>     self.y=y
> 
>   def print_point(self):
> 
>     print('x=',self.x,' y=',self.y)
> 
> p2=Points(1,2)
> 
> p2.x=2
> 
> p2.print_point()
> 
> XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
> 
> </pre>
> 
> 1 point 
> 

      x=2 y=2 
> 
>  x=1 y=2 
> 
>  x=1 y=1
>
> -- https://www.coursera.org/learn/python-for-applied-data-science-ai/exam/uZyXe/objects-and-classes/attempt#Tunnel Vision Close
