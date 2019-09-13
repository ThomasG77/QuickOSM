"""
/***************************************************************************
 QuickOSM
 A QGIS plugin
 OSM Overpass API frontend
                             -------------------
        begin                : 2014-06-11
        copyright            : (C) 2014 by 3Liz
        email                : info at 3liz dot com
        contributor          : Etienne Trimaille
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtWidgets import (
    QStyledItemDelegate, QComboBox, QCompleter, QTableView, QLineEdit)
from qgis.PyQt.QtCore import QStringListModel


class TableKeyValue(QTableView):
    def __init__(self, parent):
        super(TableKeyValue, self).__init__(parent)
        self.osm_keys = None

    def set_osm_keys(self, keys):
        self.osm_keys = keys

    def add_new_row(self):
        row = self.model().rowCount()

        keys = list(self.osm_keys.keys())
        keys.append('')  # All keys request #118
        keys.sort()
        keys_completer = QCompleter(keys)

        key_editor = QComboBox()
        key_editor.setEditable(True)
        key_editor.addItems(keys)
        key_editor.setCompleter(keys_completer)
        key_editor.completer().setCompletionMode(
            QCompleter.PopupCompletion)
        key_editor.lineEdit().setPlaceholderText(
            self.tr('Query on all keys'))

        self.model().setItem(row, 0, key_editor)
        self.model().setItem(row, 1, QComboBox())

    def dataChanged(self, top_left, bottom_right, roles):
        print(top_left.data())
        if top_left.data() == 'a':
            widget = QLineEdit()
            widget.setPlaceholderText('ahhhhhhhh')
            self.setIndexWidget(top_left, widget)
        else:
            self.setIndexWidget(top_left, None)



class QueryItemDelegate(QStyledItemDelegate):

    def __init__(self, osm_keys):
        super(QueryItemDelegate, self).__init__()
        self.osm_keys = osm_keys

    def createEditor(self, parent, option, index):
        if index.column() == 0:
            keys = list(self.osm_keys.keys())
            keys.append('')  # All keys request #118
            keys.sort()
            keys_completer = QCompleter(keys)

            key_editor = QComboBox(parent)
            key_editor.setEditable(True)
            key_editor.addItems(keys)
            key_editor.setCompleter(keys_completer)
            key_editor.completer().setCompletionMode(
                QCompleter.PopupCompletion)
            key_editor.lineEdit().setPlaceholderText(
                self.tr('Query on all keys'))
            return key_editor

        elif index.column() == 1:
            model = QStringListModel(parent)
            model.setStringList(['11111', '22222', '33333'])

            value_editor = QComboBox(parent)
            value_editor.setEditable(True)
            value_editor.setModel(model)
            value_editor.lineEdit().setPlaceholderText(
                self.tr('Query on all values'))
            return value_editor
