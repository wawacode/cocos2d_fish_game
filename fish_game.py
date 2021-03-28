import cocos
import pyglet
import random
class Net(cocos.sprite.Sprite):
    def __init__(self):
        super(Net,self).__init__("textures/net_2.png")
        self.position=100,100
class Fish(cocos.sprite.Sprite):
    def __init__(self,width,height,index):
        index="0"+str(index) if index<10 else str(index)
        textures=[]
        for i in range(1,11):
            name_i="0"+str(i) if i<10 else str(i)
            fish_name_i="textures/fish"+index+"_"+name_i+".png"
            texture=pyglet.resource.image(fish_name_i)
            textures.append(texture)
        animation=pyglet.image.Animation.from_image_sequence(textures,0.1)
        super(Fish, self).__init__(animation)
        self.totaly=height
        self.totalw=width
        self.y = random.randint(0,self.totaly)
        self.x=width
        self.position=self.x,self.y
        self.swim()
    def swim(self):
        self.y=random.randint(0,self.totaly)
        self.x=self.totalw
        self.position=self.x,self.y
        minutes=random.randint(5,10)
        self.do(cocos.actions.MoveTo((-20,self.y),minutes)+ cocos.actions.CallFunc(self.swim))
    def on_mouse_press(self,x,y,button,modifier):
        if x>self.x-self.width*1/2 and x<self.x+self.width*1/2 and y>self.y-self.height*1/2 and y<self.y+self.height*1/2:
            self.explode()

    #def on_mouse_press(self,x,y,buttons,modifiers):
    #    self.explode()
    def explode(self):
        self.stop()
        self.kill()

class Background(cocos.layer.Layer):
    def __init__(self):
        super(Background,self).__init__()
        self.width,self.height=cocos.director.director.get_window_size()
        sprite=cocos.sprite.Sprite("textures/bg.jpg")
        sprite.position=self.width//2,self.height//2
        self.add(sprite)
        #self.fishes=[]
        #for i in range(2,11):
        self.fishes=[]
        for i in range(2,11):
            fish=Fish(self.width,self.height,i)
            self.add(fish)
            self.fishes.append(fish)
        self.net=Net()
        self.add(self.net)

    def on_enter(self):
        super(Background, self).on_enter()
        cocos.director.director.window.push_handlers(self.on_mouse_press)
    def on_mouse_press(self,x,y,button,modifier):
        fish_len=len(self.fishes)-1
        for index in range(fish_len,0,-1):
            print(index)
            if x>self.fishes[index].x and x<self.fishes[index].x+self.fishes[index].totalw and y>self.fishes[index].y and y<self.fishes[index].y+self.fishes[index].totaly:
                self.fishes[index].explode()
                self.fishes.remove(self.fishes[index])
    def on_exit(self):
        cocos.director.director.window.pop_handlers()
        super(Background, self).on_exit()

if __name__=="__main__":
    cocos.director.director.init(width=800,height=480);
    background=Background();
    main_scene=cocos.scene.Scene(background);
    cocos.director.director.run(main_scene);