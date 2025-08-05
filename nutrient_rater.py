import pandas as pd

class NutrientRater:
    def __init__(self, nutrient_dict: dict, gender_input: str):
        self.gender_input = gender_input  # '남' or '여'
        self.gender = '남' if gender_input == '남' else '여'
        self.meal = self._parse_nutrients(nutrient_dict)
        self.rating_table = self._build_rating_table()

    def _parse_nutrients(self, nutrient_dict):
        parsed = {}
        for key, val in nutrient_dict.items():
            try:
                parsed[key] = float(val.split()[0])
            except:
                continue
        return pd.Series(parsed)

    def _build_rating_table(self):
        # 단위 생략, 순서: [부족, 보통하한, 좋음하한, 좋음상한, 보통상한, 과잉]
        if self.gender == '여':
            return {
                "열량(kcal)": [469, 603, 737, 871],
                "탄수화물(g)": [70.35, 90.45, 110.55, 130.65],
                "단백질(g)": [12.88, 16.56, 20.24, 23.92],
                "지방(g)": [15.12, 19.44, 23.76, 28.08],
                "비타민A(μg RE)": [151.9, 195.3, 238.7, 282.1],
                "티아민(mg)": [0.26, 0.33, 0.41, 0.48],
                "리보플라빈(mg)": [0.28, 0.36, 0.44, 0.52],
                "비타민C(mg)": [23.38, 30.06, 36.74, 43.42],
                "칼슘(mg)": [186.9, 240.3, 293.7, 347.1],
                "철분(mg)": [3.29, 4.23, 5.17, 6.11],
            }
        else:
            return {
                "열량(kcal)": [674.99, 810, 990, 1125],
                "탄수화물(g)": [97.86, 117.45, 143.55, 163.13],
                "단백질(g)": [16.26, 19.53, 23.87, 27.14],
                "지방(g)": [24.29, 29.16, 35.64, 40.51],
                "비타민A(μg RE)": [212.99, 255.6, 312.4, 355.01],
                "티아민(mg)": [0.32, 0.4, 0.48, 0.56],
                "리보플라빈(mg)": [0.42, 0.51, 0.63, 0.72],
                "비타민C(mg)": [25.04, 30.06, 36.74, 41.76],
                "칼슘(mg)": [224.99, 270, 330, 375.01],
                "철분(mg)": [3.52, 4.23, 5.17, 5.88],
            }

    def _rate_nutrient(self, name, value):
        if name not in self.rating_table:
            return '기준 없음'

        low, mid_low, mid_high, high = self.rating_table[name]

        if value < low:
            return '부족'
        elif low <= value < mid_low:
            return '약간부족'
        elif mid_low <= value <= mid_high:
            return '좋음'
        elif mid_high < value <= high:
            return '약간초과'
        else:  # value > high
            return '초과'

    def rate(self):
        return {nutrient: self._rate_nutrient(nutrient, value) for nutrient, value in self.meal.items()}

    def print_rating(self):
        print(f"\n[{self.gender_input}학생 급식 영양소 평가]")
        for nutrient, rating in self.rate().items():
            print(f"{nutrient}: {rating}")
