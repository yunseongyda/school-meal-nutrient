import pandas as pd
import matplotlib.pyplot as plt

class BarplotVisualizer:
    def __init__(self, menu, nutrient):
        self.menu = pd.Series(menu)
        self.nutrient = pd.DataFrame([nutrient])

    def drawPlot(self):
        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Create a bar plot for each nutrient
        for nutrient in self.nutrient.columns:
            plt.bar(self.menu, self.nutrient[nutrient], label=nutrient)


        