from . import mixins
from .camera import Camera
import warnings

class Scene(object):

    def __init__(self, meshes=[], camera=None, light=None, bgColor=(0., 0., 0., 1.)):
        """Returns a Scene object.  Scenes manage rendering of Meshes, Lights, and Cameras."""

        # Initialize List of all Meshes to draw
        self.meshes = list(meshes)
        if len(set(mesh.data.name for mesh in self.meshes)) != len(self.meshes):
            warnings.warn('Warning: Mesh.data.names not all unique--log data will overwrite some meshes!')
        self.camera = Camera() if not camera else camera # create a default Camera object
        self.light = mixins.Physical() if not light else light
        self.bgColor = mixins.Color(*bgColor)



