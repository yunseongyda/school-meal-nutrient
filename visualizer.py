import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Set the font to Malgun Gothic for Korean characters
plt.rcParams['font.family'] = 'Malgun Gothic'

plt.rcParams['axes.unicode_minus'] = False 

recommended_nutrient = pd.read_csv('data/nutrient_recommendations.csv', encoding='cp949')
recommended_nutrient = recommended_nutrient.head(2)
recommended_nutrient = recommended_nutrient.rename(columns={'Unnamed: 0' : '성별(sex)', '열량(kcal)' : '칼로리(kcal)', '비타민A(mg)' : '비타민A(R.E)'})


# set index as 성별(sex)
recommended_nutrient = recommended_nutrient.set_index('성별(sex)')


class BarplotVisualizer:
    def __init__(self, menu, nutrient, gender, gi):
        self.meal = pd.Series(menu)
        self.nutrient = pd.Series(nutrient, dtype=float)
        self.gender = gender
        self.gender_input = gi

    def drawPlot(self):
        recommended = recommended_nutrient.loc[self.gender]
        nutrient = self.nutrient[recommended.index]

        # major & minor 나누기
        major_nutrients = ['칼로리(kcal)', '탄수화물(g)', '단백질(g)', '지방(g)', '칼슘(mg)', '비타민C(mg)', '비타민A(R.E)']
        minor_nutrients = ['티아민(mg)', '리보플라빈(mg)', '철분(mg)']

        # 필요한 값 필터링
        rec_major = recommended[major_nutrients]
        meal_major = self.nutrient[major_nutrients].astype(float)

        rec_minor = recommended[minor_nutrients]
        meal_minor = self.nutrient[minor_nutrients].astype(float)

        bar_width = 0.35

        # -------- major nutrients plot --------
        plt.figure(figsize=(10, 5))
        index = range(len(rec_major))
        plt.bar(index, rec_major, width=bar_width, label='권장 섭취량', color='skyblue')
        plt.bar([i + bar_width for i in index], meal_major, width=bar_width, label='오늘 급식', color='lightcoral')

        # 차이값 표시
        for i in index:
            diff = abs(meal_major[i] - rec_major.iloc[i])
            max_height = max(rec_major[i], meal_major.iloc[i])
            plt.text(i + bar_width / 2, max_height + 5, f'{diff:.1f}', ha='center', va='bottom', fontsize=9, color='black')

        plt.xticks([i + bar_width / 2 for i in index], major_nutrients, rotation=30)
        plt.title(f'{self.gender_input}학생 - 주요 영양소 비교')
        plt.xlabel('영양소')
        plt.ylabel('섭취량')
        plt.legend()
        plt.tight_layout()
        plt.show()

        # -------- minor nutrients plot --------
        plt.figure(figsize=(10, 5))
        index = range(len(rec_minor))
        plt.bar(index, rec_minor, width=bar_width, label='권장 섭취량', color='skyblue')
        plt.bar([i + bar_width for i in index], meal_minor, width=bar_width, label='오늘 급식', color='lightcoral')

        # 차이값 표시
        for i in index:
            diff = abs(meal_minor[i] - rec_minor.iloc[i])
            max_height = max(meal_minor[i], rec_minor.iloc[i])
            plt.text(i + bar_width / 2, max_height + 0.1, f'{diff:.2f}', ha='center', va='bottom', fontsize=9, color='black')
        
        plt.xticks([i + bar_width / 2 for i in index], minor_nutrients, rotation=30)
        plt.title(f'{self.gender_input}학생 - 미량 영양소 비교')
        plt.xlabel('영양소')
        plt.ylabel('섭취량')
        plt.legend()
        plt.tight_layout()
        plt.show()