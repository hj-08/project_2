import streamlit as st
import random

st.title("빠른 메뉴 추천 서비스")

# 사용자 입력
mood = st.selectbox("현재 기분을 선택해주세요", ["좋음", "안좋음", "그냥"])
time = st.selectbox("시간대를 선택해주세요", ["아침", "점심", "저녁", "야식"])
budget = st.number_input("예산을 입력해주세요 (원)", min_value=1000, step=500)

# 기본 메뉴명 (시간대별)
base_menus = {
    "아침": ["토스트", "스무디", "팬케이크", "에그 베네딕트", "오트밀", "베이글", "그릭 요거트", "프렌치 토스트", "과일 샐러드", "바나나", "삶은 달걀"],
    "점심": ["파스타", "샐러드", "스테이크", "비빔밥", "샌드위치", "된장찌개", "치킨 샐러드", "김밥", "칼국수", "떡볶이", "제육볶음"],
    "저녁": ["스테이크", "파에야", "치즈 퐁듀", "닭갈비", "피자", "버거", "라면", "짜장면", "돈까스", "볶음밥", "김치찌개"],
    "야식": ["떡볶이", "튀김", "치킨", "쫄면", "김치전", "컵밥", "군만두", "오뎅탕", "핫도그", "순대", "컵라면"]
}

# 기분별 가격 범위
price_ranges = {
    "좋음": (7000, 20000),
    "안좋음": (3000, 12000),
    "그냥": (3000, 15000)
}

def generate_unique_menus(base_list, price_range, count=30):
    menus = []
    used_names = set()

    while len(menus) < count:
        base_name = random.choice(base_list)
        # 이름 중복을 피하기 위해 번호 붙이기
        suffix_num = 1
        name_candidate = base_name
        while name_candidate in used_names:
            name_candidate = f"{base_name} {suffix_num}"
            suffix_num += 1

        price = random.randint(price_range[0], price_range[1])
        menus.append((name_candidate, price))
        used_names.add(name_candidate)

    return menus

# 메뉴 데이터 생성
menu_data = {}
for t in base_menus:
    menu_data[t] = {}
    for m in ["좋음", "안좋음", "그냥"]:
        menu_data[t][m] = generate_unique_menus(base_menus[t], price_ranges[m], 30)

if st.button("추천받기"):
    possible_menus = menu_data.get(time, {}).get(mood, [])
    affordable_menus = [menu for menu in possible_menus if menu[1] <= budget]

    if not affordable_menus:
        st.warning("예산에 맞는 메뉴가 없습니다. 예산을 늘려보세요!")
    else:
        choice = random.choice(affordable_menus)
        st.success(f"추천 메뉴: {choice[0]} (예상 가격: {choice[1]}원)")



