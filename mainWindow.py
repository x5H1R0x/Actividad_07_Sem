from PySide2.QtWidgets import QMainWindow   
from ui_mainWindow import Ui_MainWindow
from particle import Particle
from particle_list import  Particle_List

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.particle_list = Particle_List()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addToStart_pushButton.clicked.connect(self.click_addStart)
        self.ui.addEnd_pushButton.clicked.connect(self.click_addEnd)
        self.ui.showListParticle_pushButton.clicked.connect(self.click_show)

    def click_addStart(self):
        self.particle_list.addFirst(self.make_particle())
        self.reset_spinBoxs()

    def click_addEnd(self):
        self.particle_list.addToEnd(self.make_particle())
        self.reset_spinBoxs()

    def click_show(self):
        self.ui.particle_PlainText.clear()
        self.ui.particle_PlainText.insertPlainText(str(self.particle_list))

    def make_particle(self)->Particle:
        id = self.ui.id_spinBox.value()
        x1 = self.ui.originX_spinBox.value()
        y1 = self.ui.originY_spinBox.value()
        x2 = self.ui.destX_spinBox.value()
        y2 = self.ui.destY_spinBox.value()
        speed = self.ui.speed_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        myParticle = Particle(id, x1, y1, x2, y2, speed, red, green, blue)
        return myParticle

    def reset_spinBoxs(self):
        self.ui.id_spinBox.setValue(0)
        self.ui.originX_spinBox.setValue(0)
        self.ui.originY_spinBox.setValue(0)
        self.ui.destX_spinBox.setValue(0)
        self.ui.destY_spinBox.setValue(0)
        self.ui.speed_spinBox.setValue(0)
        self.ui.red_spinBox.setValue(0)
        self.ui.green_spinBox.setValue(0)
        self.ui.blue_spinBox.setValue(0)
