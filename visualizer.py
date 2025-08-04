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
        plt.xlabel('Menu Items')
        plt.ylabel('Nutrient Values')
        plt.title('Nutrient Values by Menu Item')
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        plt.show()


        