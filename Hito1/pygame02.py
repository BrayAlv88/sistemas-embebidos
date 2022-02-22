class Figuras:
    def __init__(self,x,y,r,ancho,alto):
        self.x=x
        self.y=y
        self.ancho= 600
        self.alto= 500
        self.color=(255,0,0)
        self.centro=(x,y)
        self.radio=r
        self.incx=5
        self.incy=5
        print('se ha creado la figura')
    def actualizarx(self):
        if(self.x>=slef.ancho-self.r) or (self.x<self.r):
            self.incx= -self.incx
        x+=self.incx
    def actualizary(self):
        if(self.y>=self.alto-self.r) or (self.y<self.r):
            self.incy= -self.incy
        y+=self.incy
