from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, Vec3

class Panda3DGame:
    def __init__(self):
        self.panda3d_app = ShowBase()
        self.camera_control = self.panda3d_app.trackball.node()

    def setup_camera(self, distance=10, elevation=45, azimuth=45):
        self.camera_control.setPos(0, -distance, elevation)
        self.camera_control.lookAt(0, 0, elevation)
        self.camera_control.setHpr(azimuth, -elevation, 0)

    def create_3d_object(self, model_path, pos=(0, 0, 0), scale=1):
        model = self.panda3d_app.loader.loadModel(model_path)
        model.reparentTo(self.panda3d_app.render)
        model.setScale(scale)
        model.setPos(pos)
        return model

    def apply_physics(self, obj, mass=1, friction=0.2):
        physics_obj = self.panda3d_app.loader.loadModel("models/box.egg")
        obj.setFluid(physics_obj)
        obj.setMass(mass)
        obj.setFriction(friction)

    def setup_mouse_camera_control(self, speed=0.2):
        self.panda3d_app.accept("mouse1", self.panda3d_app.startDrag, [self.panda3d_app.mouseWatcherNode])
        self.panda3d_app.accept("mouse1-up", self.panda3d_app.stopDrag)

        def update_camera(task):
            self.camera_control.setPos(self.panda3d_app.mouseWatcherNode.getMouseX() * 10,
                                        -self.panda3d_app.mouseWatcherNode.getMouseY() * 10, 0)
            return task.cont

        self.panda3d_app.taskMgr.add(update_camera, "update_camera")

    def run_game(self):
        self.panda3d_app.run()

