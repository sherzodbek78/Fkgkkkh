from direct.showbase.ShowBase import ShowBase
from panda3d.core import LPoint3f, LVector3f
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import CollisionTraverser, CollisionNode, CollisionSphere
from panda3d.core import CollisionHandlerPusher, CollisionHandlerQueue
from panda3d.core import NodePath

class MyGame(ShowBase):
    def __init__(self):
            ShowBase.__init__(self)
                    
                            # Kamera sozlamalari
                                    self.disableMouse()  # Sichqonchani o‘chirib qo‘yamiz
                                            self.camera.setPos(0, -10, 5)
                                                    self.camera.lookAt(0, 0, 0)

                                                            # Yorug‘lik
                                                                    self.setup_lighting()
                                                                            
                                                                                    # Kublar yaratish
                                                                                            self.create_cube(LPoint3f(0, 0, 0))
                                                                                                    self.create_cube(LPoint3f(2, 2, 0))
                                                                                                            self.create_cube(LPoint3f(-2, -2, 0))
                                                                                                                    
                                                                                                                            # Klaviatura harakatlarini sozlash
                                                                                                                                    self.accept("arrow_up", self.move_forward)
                                                                                                                                            self.accept("arrow_down", self.move_backward)
                                                                                                                                                    self.accept("arrow_left", self.move_left)
                                                                                                                                                            self.accept("arrow_right", self.move_right)

                                                                                                                                                                def create_cube(self, position):
                                                                                                                                                                        """ 3D kublarni yaratish """
                                                                                                                                                                                cube = self.loader.loadModel("models/box")  # Standart 3D model
                                                                                                                                                                                        cube.setScale(1)
                                                                                                                                                                                                cube.setPos(position)
                                                                                                                                                                                                        cube.reparentTo(self.render)

                                                                                                                                                                                                            def setup_lighting(self):
                                                                                                                                                                                                                    """ Yorug‘lik sozlamalari """
                                                                                                                                                                                                                            ambient_light = AmbientLight("ambient_light")
                                                                                                                                                                                                                                    ambient_light.setColor((0.5, 0.5, 0.5, 1))
                                                                                                                                                                                                                                            self.render.setLight(self.render.attachNewNode(ambient_light))
                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                            directional_light = DirectionalLight("directional_light")
                                                                                                                                                                                                                                                                    directional_light.setDirection(LVector3f(-1, -1, -1))
                                                                                                                                                                                                                                                                            directional_light.setColor((0.7, 0.7, 0.7, 1))
                                                                                                                                                                                                                                                                                    self.render.setLight(self.render.attachNewNode(directional_light))

                                                                                                                                                                                                                                                                                        def move_forward(self):
                                                                                                                                                                                                                                                                                                self.camera.setY(self.camera, 1)

                                                                                                                                                                                                                                                                                                    def move_backward(self):
                                                                                                                                                                                                                                                                                                            self.camera.setY(self.camera, -1)

                                                                                                                                                                                                                                                                                                                def move_left(self):
                                                                                                                                                                                                                                                                                                                        self.camera.setX(self.camera, -1)

                                                                                                                                                                                                                                                                                                                            def move_right(self):
                                                                                                                                                                                                                                                                                                                                    self.camera.setX(self.camera, 1)

                                                                                                                                                                                                                                                                                                                                    # O‘yinni ishga tushirish
                                                                                                                                                                                                                                                                                                                                    game = MyGame()
                                                                                                                                                                                                                                                                                                                                    game.run()
                                                                                                            self.create_cube(LPoint3f(-2, -2, 0))
                                                                                                                    
                                                                                                                            # Klaviatura harakatlarini sozlash
                                                                                                                                    self.accept("arrow_up", self.move_forward)
                                                                                                                                            self.accept("arrow_down", self.move_backward)
                                                                                                                                                    self.accept("arrow_left", self.move_left)
                                                                                                                                                            self.accept("arrow_right", self.move_right)

                                                                                                                                                                def create_cube(self, position):
                                                                                                                                                                        """ 3D kublarni yaratish """
                                                                                                                                                                                cube = self.loader.loadModel("models/box")  # Standart 3D model
                                                                                                                                                                                        cube.setScale(1)
                                                                                                                                                                                                cube.setPos(position)
                                                                                                                                                                                                        cube.reparentTo(self.render)

                                                                                                                                                                                                            def setup_lighting(self):
                                                                                                                                                                                                                    """ Yorug‘lik sozlamalari """
                                                                                                                                                                                                                            ambient_light = AmbientLight("ambient_light")
                                                                                                                                                                                                                                    ambient_light.setColor((0.5, 0.5, 0.5, 1))
                                                                                                                                                                                                                                            self.render.setLight(self.render.attachNewNode(ambient_light))
                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                            directional_light = DirectionalLight("directional_light")
                                                                                                                                                                                                                                                                    directional_light.setDirection(LVector3f(-1, -1, -1))
                                                                                                                                                                                                                                                                            directional_light.setColor((0.7, 0.7, 0.7, 1))
                                                                                                                                                                                                                                                                                    self.render.setLight(self.render.attachNewNode(directional_light))

                                                                                                                                                                                                                                                                                        def move_forward(self):
                                                                                                                                                                                                                                                                                                self.camera.setY(self.camera, 1)

                                                                                                                                                                                                                                                                                                    def move_backward(self):
                                                                                                                                                                                                                                                                                                            self.camera.setY(self.camera, -1)

                                                                                                                                                                                                                                                                                                                def move_left(self):
                                                                                                                                                                                                                                                                                                                        self.camera.setX(self.camera, -1)

                                                                                                                                                                                                                                                                                                                            def move_right(self):
                                                                                                                                                                                                                                                                                                                                ʼ                                                                                                                                                                     


                                                        ʼ 