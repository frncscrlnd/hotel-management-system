class Camera: 
    def __init__ (self, numero_camera, piano):
        self.numero_camera = numero_camera
        self.piano = piano

    def __str__ (self):
        return f"Numero camera: {self.numero_camera}, piano: {self.piano}"