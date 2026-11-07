from PySide6.QtCore import QSortFilterProxyModel, Qt

class AppsProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filter_mode = "all"

    def set_filter_mode(self, mode: str):
        if self.filter_mode != mode:
            self.filter_mode = mode
            self.invalidateFilter()

    def filterAcceptsRow(self, source_row: int, source_parent):
        text_accepts = super().filterAcceptsRow(source_row, source_parent)
        if not text_accepts:
            return False

        if self.filter_mode == "all":
            return True

        model = self.sourceModel()
        if not model:
            return True
            
        app = model._apps[source_row]

        if self.filter_mode == "system":
            return app.get("is_system", False)
        elif self.filter_mode == "user":
            return not app.get("is_system", False)
        elif self.filter_mode == "disabled":
            return app.get("is_disabled", False)

        return True