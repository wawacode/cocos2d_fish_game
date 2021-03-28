import cocos
import pyglet
import random
class Fish(cocos.sprite.Sprite):
    def __init__(self,index):
        index = "0" + str(index) if index < 10 else str(index)
        textures=[]
        for i in range(1,11):
            name_i="0"+str(i) if i<10 else str(i)
            fish_name_i="textures/fish"+index+"_"+name_i+".png"
            texture=pyglet.resource.image(fish_name_i)
            textures.append(texture)
        animation=pyglet.image.Animation.from_image_sequence(textures,0.1)
        super(Fish, self).__init__(animation)
        self.y=random.randint(10,480)
        self.position = 800,self.y
        self.swim()
    def swim(self):
        self.y=random.randint(10,480)
        self.position=800,self.y
        minutes=random.randint(2,8)
        self.do(cocos.actions.MoveTo((-20,self.y),minutes)+ cocos.actions.CallFunc(self.swim))
    def on_enter(self):
        super(Fish, self).on_enter()
        cocos.director.director.window.push_handlers(self.on_mouse_press)
    def on_mouse_press(self,x,y,button,modifier):
        if x > self.x - self.width * 1 / 2 and x < self.x + self.width * 1 / 2 and y > self.y - self.height * 1 / 2 and y < self.y + self.height * 1 / 2:
            self.explode()
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
        for i in range(2,11):
            fish=Fish(i)
            self.add(fish)
if __name__=="__main__":
    cocos.director.director.init(width=800,height=480);
    background=Background();
    main_scene=cocos.scene.Scene(background)
    cocos.director.director.run(main_scene)