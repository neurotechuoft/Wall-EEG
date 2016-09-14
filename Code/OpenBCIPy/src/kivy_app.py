import random
import threading
from kivy import garden
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from kivy.properties import ObjectProperty, NumericProperty, Clock
from math import sin

from user.User import User
from view.PointsCollection import PointsCollection
from graph import Graph, MeshLinePlot


# class InSenseView(Widget):
# grid_layout = GridLayout()


class WallEEGApp(App):
    def __init__(self):
        super(WallEEGApp, self).__init__()
        self.user = User()
        self.graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                           x_ticks_major=25, y_ticks_major=0.001,
                           y_grid_label=True, x_grid_label=True, padding=5,
                           x_grid=True, y_grid=True, xmin=-0, xmax=100,
                           ymin=-0.1,
                           ymax=0.1)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.counter = 0

    # def build(self):
    #     return InSenseView()



    # def build(self):
    #     g = Gui()
    #     point_collection = PointsCollection(1000, 1000, 0, 100, 0, 100)
    #
    #     for i in range(100):
    #         x_coord = random.randint(
    #             point_collection.x_min, point_collection.x_max)
    #         y_coord = random.randint(
    #             point_collection.y_min, point_collection.y_max)
    #
    #         point_collection.add_point_vals(x_coord, y_coord)
    #
    #     for point in point_collection.points_list:
    #         g.grid.add_widget(point)
    #     # for i in range(24):
    #     #     g.grid.add_widget(Button(text='test'))
    #
    #     return g

    def build(self):
        self.plot.points = [(point[0], point[1]) for point in
                            self.user.userECG.ecgListFFT]
        # self.plot.points = [(x, sin(x / 100.)) for x in range(self.counter,
        #                                                       self.counter + 10)]
        self.graph.add_plot(self.plot)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

        return self.graph

    def update(self, dt):
        self.counter += 1
        # self.plot.points = [(x, sin(x / 100.)) for x in range(self.counter,
        #                                                       self.counter + 10)]
        self.plot.points = [(point[0], point[1]) for point in
                            self.user.userECG.ecgListFFT]



class Gui(FloatLayout):
    grid = ObjectProperty(None)


if __name__ == '__main__':
    app = WallEEGApp()


    def run():
        app.run()


    run()


    # kivy_thread = threading.Thread(target=run)
    # try:
    #     kivy_thread.start()
    # except:
    #     pass
