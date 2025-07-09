import streamlit as st
import random

st.title("빠른 메뉴 추천 서비스")

mood = st.selectbox("현재 기분을 선택해주세요", ["좋음", "안좋음", "그냥"])
time = st.selectbox("시간대를 선택해주세요", ["아침", "점심", "저녁", "야식"])
budget = st.number_input("예산을 입력해주세요 (원)", min_value=1000, step=500)

# 메뉴 생성 헬퍼 함수
def generate_menu(base_names, price_range, count=30):
    menus = []
    for i in range(count):
        name = random.choice(base_names)
        suffix = f" {i+1}" if i > 0 else ""
        price = random.randint(price_range[0], price_range[1])
        menus.append((f"{name}{suffix}", price))
    return menus

# 기본 메뉴명 예시 (아침, 점심, 저녁, 야식)
base_menus = {
    "아침": ["토스트", "스무디", "팬케이크", "에그 베네딕트", "오트밀", "베이글", "그릭 요거트", "프렌치 토스트", "과일 샐러드", "바나나", "삶은 달걀"],
    "점심": ["파스타", "샐러드", "스테이크", "비빔밥", "샌드위치", "된장찌개", "치킨 샐러드", "김밥", "칼국수", "떡볶이", "제육볶음"],
    "저녁": ["스테이크", "파에야", "치즈 퐁듀", "닭갈비", "피자", "버거", "라면", "짜장면", "돈까스", "볶음밥", "김치찌개"],
    "야식": ["떡볶이", "튀김", "치킨", "쫄면", "김치전", "컵밥", "군만두", "오뎅탕", "핫도그", "순대", "컵라면"]
}

# 가격 범위 (기분별로 약간 다르게)
price_ranges = {
    "좋음": (7000, 20000),
    "안좋음": (3000, 12000),
    "그냥": (3000, 15000)
}

menu_data = {}

for t in base_menus:
    menu_data[t] = {}
    for m in ["좋음", "안좋음", "그냥"]:
        # 메뉴 기본명 리스트
        base_list = base_menus[t]
        # 30개 생성
        menu_data[t][m] = generate_menu(base_list, price_ranges[m], count=30)

if st.button("추천받기"):
    possible_menus = menu_data.get(time, {}).get(mood, [])
    affordable_menus = [menu for menu in possible_menus if menu[1] <= budget]

    if not affordable_menus:
        st.write("예산에 맞는 메뉴가 없습니다. 예산을 늘려보세요!")
    else:
        choice = random.choice(affordable_menus)
        st.success(f"추천 메뉴: {choice[0]} (예상 가격: {choice[1]}원)")


