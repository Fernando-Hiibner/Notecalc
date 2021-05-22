class Edit():
    def copy(self):
        self.root.clipboard_clear()
        textToBeCopied = self.text.get("sel.first", "sel.last")
        self.root.clipboard_append(textToBeCopied)

    def cut(self):
        self.copy()
        self.text.delete("sel.first", "sel.last")

    def paste(self):
        self.text.insert("insert", self.root.clipboard_get())

    def undo(self):
        self.text.edit_undo()

    def redo(self):
        self.text.edit_redo()

    def selectAll(self):
        self.text.tag_add("sel", "1.0", "end")
        self.text.mark_set(0.0, "end")
        self.text.see("insert")

    def clearSelection(self):
        self.text.tag_remove("sel", "1.0", "end")

    def find(self):
        self.text.tag_remove("found", "1.0", "end")
        # Criar um menu de busca

    def __init__(self, root, text):
        self.text = text
        self.root = root
        self.root.bind("<Control-Z>", lambda event: self.redo())
        self.root.bind("<Control-f>", lambda event: self.find())

