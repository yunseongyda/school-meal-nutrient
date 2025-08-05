import pandas as pd
import matplotlib.pyplot as plt

recommended_nutrient = pd.read_csv('data/nutrient_recommendations.csv', encoding='cp949')
recommended_nutrient = recommended_nutrient.head(2)
recommended_nutrient = recommended_nutrient.rename(columns={'Unnamed: 0' : '성별(sex)'})

# set index as 성별(sex)
recommended_nutrient = recommended_nutrient.set_index('성별(sex)')


class BarplotVisualizer:
    def __init__(self, menu, nutrient, gender, gi):
        self.meal = pd.Series(menu)
        self.nutrient = pd.Series(nutrient)
        self.gender = gender
        self.gender_input = gi

    def drawPlot(self):
        recommended = recommended_nutrient.loc[self.gender]

        # Create bar plot
        plt.figure(figsize=(12,6))
        bar_width = 0.4
        index = range(len(recommended))

        # Recommended nutrient bar
        plt.bar(index, recommended, width=bar_width, label='권장 섭취량', color='skyblue')

        # Meal nutrient bar
        plt.bar([i + bar_width for i in index], self.nutrient, width=bar_width, label='오늘 급식', color='lightcoral')

        # Set labels and ticks
        plt.xlabel('영양소')
        plt.ylabel('섭취량')
        plt.title(f'{self.gender_input}학생 - 오늘 급식 권장 섭취량 비교')
        plt.xticks([i + bar_width / 2 for i in index], recommended.index, rotation=30)
        plt.legend()
        plt.tight_layout()
        plt.show()
        