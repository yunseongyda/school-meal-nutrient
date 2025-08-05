from data_collector import DataCollector
from visualizer import BarplotVisualizer
from nutrient_rater import NutrientRater

def get_whole(data):
    # '요리명' ~ '원산지' 사이의 문자열 추출
    menu_block = data.split("요리명")[1].split("원산지")[0].strip()
    
    # 각 줄을 리스트로 변환
    menu_list = menu_block.split("\n")

    # 각 항목 strip
    menu = [item.strip() for item in menu_list if item.strip()]

    return menu

def get_nutrient(data, cal):
    nutrient_dict = {}

    # Parsing Kcal
    try:
        cal = cal.split(" ")[1].strip()
        nutrient_dict['칼로리(kcal)'] = float(cal)
    except Exception as e:
        print(f"[ERROR - Parsing Kcal]: {e}")
        nutrient_dict['칼로리(kcal)'] = 0.0

    # 영양소 부분의 문자열 추출
    nutrient_block = data.split("영양소")[1].strip()

    # 각 줄을 리스트로 변환
    nutrient_list = nutrient_block.split("\n")

    # 각 항목 strip
    nutrient_list = [item.strip() for item in nutrient_list if item.strip()]

    for nutrient in nutrient_list:
        sep = nutrient.split(" : ")
        nutrient_dict[sep[0]] = sep[1]

    return nutrient_dict

if __name__ == "__main__":
    url = "https://swjb-h.goesw.kr/subList/31000019471"
    collector = DataCollector(url)
    data = collector.collect_data()
    print(data)

    whole = get_whole(data)
    print(whole)
    for i in range(len(whole)):
        print(f"{i}: {whole[i]}")
    nutrient = get_nutrient(data, whole[7])
    print("whole:", whole)
    print("Nutrient:", nutrient)
    # set sex
    gender_input = input("성별을 입력하세요 (남/여): ")
    gender = 'Male' if gender_input == '남' else 'Female'

    # visualizing
    barplot = BarplotVisualizer(whole[0:7], nutrient, gender, gender_input)
    barplot.drawPlot()

    # print meal
    for i in whole[0:7]:
        print(f"{i}")

    # rating
    rater = NutrientRater(nutrient, gender_input)
    rater.print_rating()