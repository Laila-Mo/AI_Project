import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui

from GUICode1 import Ui_mainWindow
import networkx as nx
import matplotlib.pyplot as plt
import Algos

arr = []


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    EXIT_CODE_REBOOT = -12345678

    def checkb(self):
        if self.checkBox.isChecked():
            return True
        else:
            return False

    heuristicSet = dict()

    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        Ui_mainWindow.__init__(self)

        self.setupUi(self)
        self.initwigets()
        self.AddEdge_button.pressed.connect(self.AddEdge)
        self.AddHeuristic_button.pressed.connect(self.AddHeuristic)
        self.submitEnd_button.pressed.connect(self.SubmitGoal)
        self.comboBox.currentIndexChanged.connect(self.cb)
        self.radioButton.toggled.connect(self.rb)
        self.checkBox.pressed.connect(self.checkb)
        self.pushButton.pressed.connect(self.add_H)
        self.clearButton.pressed.connect(self.reset)

    def add_H(self):
        a = self.End_input.toPlainText()
        arr.append(a)
        self.End_input.clear()

    def initwigets(self):
        self.Hnode_label.setEnabled(False)
        self.Hnode_Input.setEnabled(False)
        self.Heuristic_Input.setEnabled(False)
        self.Heuristic_label.setEnabled(False)
        self.AddHeuristic_button.setEnabled(False)
        self.Start_label.setEnabled(False)
        self.Start_input.setEnabled(False)
        self.End_label.setEnabled(False)
        self.End_input.setEnabled(False)
        self.submitEnd_button.setEnabled(False)
        self.WeightInput.setHidden(True)
        self.Weight_label.setHidden(True)
        self.AddEdge_button.setEnabled(False)
        self.Draw_button.setEnabled(False)
        self.radioButton.setChecked(False)
        self.checkBox.setEnabled(False)
        self.radioButton.setEnabled(False)

    def cb(self):
        selected = self.comboBox.currentIndex()
        self.State = self.checkb()
        if selected == 0:
            self.Hnode_label.setEnabled(False)
            self.Hnode_Input.setEnabled(False)
            self.Heuristic_Input.setEnabled(False)
            self.Heuristic_label.setEnabled(False)
            self.AddHeuristic_button.setEnabled(False)
            self.Start_label.setEnabled(False)
            self.Start_input.setEnabled(False)
            self.End_label.setEnabled(False)
            self.End_input.setEnabled(False)
            self.submitEnd_button.setEnabled(False)
            self.AddEdge_button.setEnabled(False)
            self.Draw_button.setEnabled(False)
            self.WeightInput.setHidden(True)
            self.Weight_label.setHidden(True)
            self.checkBox.setEnabled(False)
            self.radioButton.setEnabled(False)
        else:
            self.Start_label.setEnabled(True)
            self.Start_input.setEnabled(True)
            self.End_label.setEnabled(True)
            self.End_input.setEnabled(True)
            self.submitEnd_button.setEnabled(True)
            self.AddEdge_button.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.radioButton.setEnabled(True)
            if selected == 1:
                self.Hnode_label.setEnabled(False)
                self.Hnode_Input.setEnabled(False)
                self.Heuristic_Input.setEnabled(False)
                self.Heuristic_label.setEnabled(False)
                self.AddHeuristic_button.setEnabled(False)
                self.WeightInput.setHidden(True)
                self.Weight_label.setHidden(True)
            elif selected == 2:
                self.Hnode_label.setEnabled(False)
                self.Hnode_Input.setEnabled(False)
                self.Heuristic_Input.setEnabled(False)
                self.Heuristic_label.setEnabled(False)
                self.AddHeuristic_button.setEnabled(False)
                self.WeightInput.setHidden(True)
                self.Weight_label.setHidden(True)
            elif selected == 3:
                self.Hnode_label.setEnabled(False)
                self.Hnode_Input.setEnabled(False)
                self.Heuristic_Input.setEnabled(False)
                self.Heuristic_label.setEnabled(False)
                self.AddHeuristic_button.setEnabled(False)
                self.WeightInput.setHidden(False)
                self.Weight_label.setHidden(False)
            elif selected == 4:
                self.Hnode_label.setEnabled(True)
                self.Hnode_Input.setEnabled(True)
                self.Heuristic_Input.setEnabled(True)
                self.Heuristic_label.setEnabled(True)
                self.AddHeuristic_button.setEnabled(True)
                self.WeightInput.setHidden(True)
                self.Weight_label.setHidden(True)
            elif selected == 5:
                self.Hnode_label.setEnabled(True)
                self.Hnode_Input.setEnabled(True)
                self.Heuristic_Input.setEnabled(True)
                self.Heuristic_label.setEnabled(True)
                self.AddHeuristic_button.setEnabled(True)
                self.WeightInput.setHidden(False)
                self.Weight_label.setHidden(False)

    G = nx.DiGraph()
    graphid = Algos.Graph(directed=True)
    graphi = Algos.Graph(directed=False)

    def rb(self):
        if self.radioButton.isChecked:
            self.Draw_button.setEnabled(True)
            self.Draw()
            self.AddEdge_button.setEnabled(False)
        else:
            self.Draw_button.setEnabled(False)

    def AddEdge(self):
        if self.checkb():
            self.G.add_edge(self.Node1Input.toPlainText(), self.Node2Input.toPlainText(),
                            weight=self.WeightInput.toPlainText())
            selected = self.comboBox.currentIndex()
            if selected == 1:
                self.graphid.add_edge(self.Node1Input.toPlainText(), self.Node2Input.toPlainText())
            elif selected == 2:
                self.graphid.add_edge(self.Node1Input.toPlainText(), self.Node2Input.toPlainText())
            elif selected == 3:
                self.graphid.add_edge_ucs(self.Node1Input.toPlainText(), self.Node2Input.toPlainText(),
                                          int(self.WeightInput.toPlainText()))
            elif selected == 4:
                self.graphid.add_edge_g_A(self.Node1Input.toPlainText(), self.Node2Input.toPlainText(), 1)
            elif selected == 5:
                self.graphid.add_edge_g_A(self.Node1Input.toPlainText(), self.Node2Input.toPlainText(),
                                          int(self.WeightInput.toPlainText()))
            self.Node1Input.clear()
            self.Node2Input.clear()
            self.WeightInput.clear()
        else:
            self.G.add_edge(self.Node1Input.toPlainText(), self.Node2Input.toPlainText(),
                            weight=self.WeightInput.toPlainText())
            selected = self.comboBox.currentIndex()
            if selected == 1:
                self.graphi.add_edge(self.Node1Input.toPlainText(), self.Node2Input.toPlainText())
            elif selected == 2:
                self.graphi.add_edge(self.Node1Input.toPlainText(), self.Node2Input.toPlainText())
            elif selected == 3:
                self.graphi.add_edge_ucs(self.Node1Input.toPlainText(), self.Node2Input.toPlainText(),
                                         int(self.WeightInput.toPlainText()))
            elif selected == 4:
                self.graphi.add_edge_g_A(self.Node1Input.toPlainText(), self.Node2Input.toPlainText(), 1)
            elif selected == 5:
                self.graphi.add_edge_g_A(self.Node1Input.toPlainText(), self.Node2Input.toPlainText(),
                                         int(self.WeightInput.toPlainText()))
            self.Node1Input.clear()
            self.Node2Input.clear()
            self.WeightInput.clear()

    def AddHeuristic(self):
        s = int(self.Heuristic_Input.toPlainText())
        e = self.Hnode_Input.toPlainText()
        self.heuristicSet.update({e: s})
        if self.checkb():
            self.graphid.set_huristics(self.heuristicSet)
        else:
            self.graphi.set_huristics(self.heuristicSet)
        self.Heuristic_Input.clear()
        self.Hnode_Input.clear()

    def Create_path(self, came_from, goal):
        parent = came_from[goal]
        if parent:
            self.Create_path(came_from, parent)
        else:
            self.Path_output.insertPlainText(goal);
            return
        self.Path_output.insertPlainText(' => ')
        self.Path_output.insertPlainText(goal)

    def SubmitGoal(self):
        s = self.Start_input.toPlainText()
        a = self.End_input.toPlainText()
        arr.append(a)
        selected = self.comboBox.currentIndex()
        if self.checkb():
            if selected == 1:
                traced_path, bk = self.graphid.breadth_first_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, bk);
            elif selected == 2:
                traced_path, bk = self.graphid.deapth_first_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, bk);
            elif selected == 3:
                traced_path, cost, bk = self.graphid.uniform_cost_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,
                                                                                 bk); self.Path_output.insertPlainText(
                    ' cost: ' + str(cost))
            elif selected == 4:
                traced_path, cost, bk = self.graphid.greedy_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,
                                                                                 bk); self.Path_output.insertPlainText(
                    ' cost: ' + str(cost))
            elif selected == 5:
                traced_path, cost, bk = self.graphid.aStarSearch(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,
                                                                                 bk); self.Path_output.insertPlainText(
                    ' cost: ' + str(cost))
        else:
            if selected == 1:
                traced_path, bk = self.graphi.breadth_first_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, bk);
            elif selected == 2:
                traced_path, bk = self.graphi.deapth_first_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, bk);
            elif selected == 3:
                traced_path, cost, bk = self.graphi.uniform_cost_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,
                                                                                 bk); self.Path_output.insertPlainText(
                    ' cost: ' + str(cost))
            elif selected == 4:
                traced_path, cost, bk = self.graphi.greedy_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,
                                                                                 bk); self.Path_output.insertPlainText(
                    ' cost: ' + str(cost))
            elif selected == 5:
                traced_path, cost, bk = self.graphi.aStarSearch(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,
                                                                                 bk); self.Path_output.insertPlainText(
                    ' cost: ' + str(cost))

    def Draw(self):
        selected = self.comboBox.currentIndex()
        if selected == 1:
            self.State = self.checkb()
            nx.draw_circular(self.G, with_labels=True, arrows=self.State)
            # plt.show()
            plt.savefig("fig.png")

        elif selected == 2:
            self.State = self.checkb()
            nx.draw_circular(self.G, with_labels=True, arrows=self.State)
            # plt.show()
            plt.savefig("fig.png")

        elif selected == 3:
            self.State = self.checkb()
            pos = nx.spring_layout(self.G)
            weights = nx.get_edge_attributes(self.G, "weight")
            nx.draw_networkx(self.G, pos, with_labels=True, arrows=self.State)
            nx.draw_networkx_edge_labels(self.G, pos, edge_labels=weights)
            plt.savefig("fig.png")

        elif selected == 4:
            self.State = self.checkb()
            nx.draw_circular(self.G, with_labels=True, arrows=self.State)
            plt.savefig("fig.png")
        elif selected == 5:
            self.State = self.checkb()
            pos = nx.spring_layout(self.G)
            weights = nx.get_edge_attributes(self.G, "weight")
            nx.draw_networkx(self.G, pos, with_labels=True, arrows=self.State)
            nx.draw_networkx_edge_labels(self.G, pos, edge_labels=weights)
            plt.savefig("fig.png")

    def reset(self):
        self.G.clear()
        self.G.clear_edges()
        os.system('python3 "Main.py"')
        QtWidgets.qApp.exit(MainWindow.EXIT_CODE_REBOOT)


if __name__ == "__main__":
    currentExitCode = MainWindow.EXIT_CODE_REBOOT
    while currentExitCode == MainWindow.EXIT_CODE_REBOOT:
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        #    app.exec_()
        currentExitCode = app.exec_()
        app = None
