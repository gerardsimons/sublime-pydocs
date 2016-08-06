import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World!")

        # window = self.window
        view = self.view
        sel = view.sel()

        pos = sel[0]
        selectionText = view.substr(pos)
        self.view.insert(edit, pos, "Helloooooo, World!")

        print("selectionText=",selectionText)

        # print("Done")

