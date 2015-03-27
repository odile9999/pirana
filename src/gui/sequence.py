# -*- coding: utf-8 -*-
"""
Created on 6 janv. 2015
@author: Odile

gui.sequence
"""

from PyQt4 import QtGui
from gui.sequence_qt import Ui_DockWidget_Sequence


class SequenceGUI(QtGui.QDockWidget):

    """
    classdocs
    """

    def __init__(self, parent=None):
        super(SequenceGUI, self).__init__(parent)
        self.ui = Ui_DockWidget_Sequence()
        self.ui.setupUi(self)

    def setup(self):
        self.model = QtGui.QStandardItemModel(2, 5)
        self.ui.tableView_Sequence.setModel(self.model)


if __name__ == '__main__':
    pass
else:
    print("\nImporting... ", __name__)
