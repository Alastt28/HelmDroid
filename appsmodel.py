from PySide6 import QtCore, QtGui

class AppsModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._apps = []

    def set_apps(self, apps_data):
        self.beginResetModel()
        self._apps = apps_data
        self.endResetModel()

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._apps)

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags

        return (
            QtCore.Qt.ItemIsEnabled
            | QtCore.Qt.ItemIsSelectable
            | QtCore.Qt.ItemIsUserCheckable
        )

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self._apps)):
            return None

        app = self._apps[index.row()]

        if role == QtCore.Qt.DisplayRole:
            name = app.get("name", "")
            pkg = app.get("package", "")
            return f"{name}\n{pkg}"

        elif role == QtCore.Qt.DecorationRole:
            icon_path = app.get("icon_path", "")
            if icon_path:
                return QtGui.QIcon(icon_path)
            return QtGui.QIcon.fromTheme("application-x-executable")

        elif role == QtCore.Qt.SizeHintRole:
            return QtCore.QSize(0, 56)

        elif role == QtCore.Qt.CheckStateRole:
            return (
                QtCore.Qt.Checked
                if app.get("is_checked", False)
                else QtCore.Qt.Unchecked
            )

        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid() or not (0 <= index.row() < len(self._apps)):
            return False

        if role == QtCore.Qt.CheckStateRole:
            self._apps[index.row()]["is_checked"] = (value == QtCore.Qt.CheckState.Checked.value)
            self.dataChanged.emit(index, index, [role])
            return True

        return False