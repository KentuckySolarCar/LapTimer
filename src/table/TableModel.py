

from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from src.log.Log import getInfoLog, getCriticalLog, getDebugLog, getErrorLog, getWarningLog



class TableModel(QAbstractTableModel):

    def __init__(self):
        super().__init__()