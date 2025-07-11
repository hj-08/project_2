import streamlit as st
import random

st.title("빠른 메뉴 추천 서비스")

# 1. 사용자 입력
mood = st.selectbox("현재 기분을 선택해주세요", ["좋음", "안좋음", "그냥"])
time = st.selectbox("시간대를 선택해주세요", ["아침", "점심", "저녁", "야식"])
budget = st.number_input("예산을 입력해주세요 (원)", min_value=1000, step=500)

# 2. 간결한 메뉴 데이터 (시간대별/기분별 10~15개씩)
menu_data = {
    "아침": {
        "좋음": [("아보카도 토스트", 5500), ("스무디 볼", 7000), ("에그 베네딕트", 12000),
                 ("프렌치 토스트", 8000), ("오트밀", 4000), ("팬케이크", 8500),
                 ("그릭 요거트", 4500), ("삶은 달걀", 3000), ("베이글", 6000), ("과일 샐러드", 6500)],
        "안좋음": [("토스트와 잼", 3500), ("삶은 달걀", 3000), ("블랙 커피", 2500),
                   ("베이컨과 계란", 10000), ("바나나", 2000), ("오트밀", 4000),
                   ("핫초코", 3500), ("요거트", 4500), ("시리얼", 3000), ("과일 샐러드", 6500)],
        "그냥": [("시리얼과 우유", 3500), ("베이글과 크림치즈", 6000), ("팬케이크", 8500),
                 ("그릭 요거트", 4500), ("토스트", 3000), ("삶은 달걀", 3000),
                 ("크로와상", 6500), ("오트밀", 4000), ("바나나", 2000), ("블랙 커피", 2500)]
    },
    "점심": {
        "좋음": [("파스타 카르보나라", 11000), ("그릴 치킨 샐러드", 9000), ("연어 스테이크", 15000),
                 ("비빔밥", 8000), ("샌드위치 세트", 7500), ("된장찌개 백반", 7000),
                 ("치킨 커리", 12000), ("참치 샐러드", 8500), ("우동", 9000), ("스테이크 덮밥", 13000)],
        "안좋음": [("치킨 너겟과 감자튀김", 8500), ("라면", 4000), ("칼국수", 7000),
                   ("김치찌개", 6500), ("떡국", 6000), ("김밥", 4000),
                   ("순두부찌개", 7000), ("제육볶음", 7500), ("떡볶이", 6500), ("부대찌개", 8000)],
        "그냥": [("김밥", 4000), ("참치 샌드위치", 7000), ("제육볶음 덮밥", 9000),
                 ("토마토 스파게티", 8000), ("야채 볶음밥", 7000), ("된장찌개", 7000),
                 ("오므라이스", 8000), ("닭갈비", 13000), ("비빔밥", 8000), ("라면", 4000)]
    },
    "저녁": {
        "좋음": [("스테이크", 20000), ("파에야", 18000), ("치즈 퐁듀", 15000),
                 ("닭갈비", 13000), ("피자", 12000), ("버거", 11000),
                 ("라면", 7000), ("짜장면", 7000), ("돈까스", 9000), ("볶음밥", 8500)],
        "안좋음": [("김치찌개", 6500), ("라면", 4000), ("떡볶이", 6500),
                   ("순두부찌개", 7000), ("제육볶음", 7500), ("닭볶음탕", 12000),
                   ("오징어 볶음", 8000), ("부대찌개", 8000), ("감자탕", 10000), ("칼국수", 7000)],
        "그냥": [("피자", 12000), ("버거", 11000), ("라면", 7000),
                 ("짜장면", 7000), ("돈까스", 9000), ("볶음밥", 8500),
                 ("스테이크", 20000), ("닭갈비", 13000), ("김치찌개", 6500), ("떡볶이", 6500)]
    },
    "야식": {
        "좋음": [("치킨", 15000), ("떡볶이", 8000), ("튀김", 7500),
                 ("쫄면", 7000), ("김치전", 6500), ("컵밥", 7000),
                 ("군만두", 6000), ("오뎅탕", 6500), ("핫도그", 7000), ("순대", 7000)],
        "안좋음": [("라면", 4000), ("컵라면", 3000), ("김밥", 4000),
                   ("떡볶이", 6500), ("오뎅", 3000), ("튀김", 7500),
                   ("순대", 7000), ("치킨너겟", 6000), ("핫도그", 7000), ("김치전", 6500)],
        "그냥": [("치킨", 15000), ("떡볶이", 8000), ("튀김", 7500),
                 ("컵밥", 7000), ("핫도그", 7000), ("순대", 7000),
                 ("오뎅탕", 6500), ("쫄면", 7000), ("군만두", 6000), ("김치전", 6500)]
    }
}

# 3. 추천 함수
def recommend_menu(time, mood, budget):
    menus = menu_data.get(time, {}).get(mood, [])
    affordable = [m for m in menus if m[1] <= budget]
    if not affordable:
        return None
    sample_size = min(30, len(affordable))
    sampled = random.sample(affordable, sample_size)
    choice = random.choice(sampled)
    return choice

# 4. 추천 받기 버튼 및 결과 출력
if st.button("추천받기"):
    result = recommend_menu(time, mood, budget)
    if result:
        st.success(f"추천 메뉴: {result[0]} (예상 가격: {result[1]}원)")
    else:
        st.warning("예산에 맞는 메뉴가 없습니다. 예산을 늘려주세요!")





