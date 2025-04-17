
import streamlit as st
import random

st.set_page_config(page_title="大象舒適度蹭蹭模擬器 v1", page_icon="🐘", layout="centered")
st.title("🐘 大象舒適度蹭蹭模擬器 v1")

st.markdown("和小索、小巧、冰嘣、波堤一起來感受大象們的療癒蹭蹭時光！")

elephant_count = st.slider("🐘 大象數量", 1, 10, 3)
elephant_weight = st.slider("⚖️ 大象體重 (kg)", 1000, 4000, 2500)
head_taste_index = st.slider("🍭 頭頂好吃程度", 0.0, 10.0, 7.0)
foot_softness = st.slider("🦶 腳掌柔軟舒適度", 0.0, 10.0, 8.0)
trunk_length = st.slider("👃 象鼻長度 (cm)", 50, 200, 120)
skin_score = st.slider("🧴 皮膚好蹭程度", 0.0, 10.0, 9.0)
belly_temp = st.slider("🌡️ 肚肚溫度 (°C)", 30.0, 40.0, 37.5)
ear_flap = st.slider("👂 搧耳頻率 (次/分鐘)", 0, 10, 3)
rumble_volume = st.slider("🎶 咕嚕聲療癒度", 0.0, 10.0, 6.5)
huddle_tightness = st.slider("🤗 群聚緊密程度", 0.0, 10.0, 8.0)

elephant_names = ["小索", "小巧", "冰嘣", "波堤", "杜克", "拿鐵", "歐姆"]
random.shuffle(elephant_names)
selected_names = elephant_names[:elephant_count]

if st.button("開始模擬 🧪"):
    comfort = round(
        elephant_count * 2 +
        foot_softness * 3 +
        skin_score * 3 +
        belly_temp +
        huddle_tightness * 2 +
        rumble_volume * 2, 2
    )

    thermal = round(belly_temp * 2 + elephant_count * 1.5, 2)
    social = round(trunk_length / 20 + ear_flap * 1.2 + huddle_tightness, 2)
    rubbing = round(skin_score * 3 + foot_softness * 2, 2)
    edibility = round(head_taste_index * 5, 2)

    st.subheader("🎯 模擬結果")
    st.write(f"🐘 蹭蹭舒適指數: **{comfort}/100**")
    st.write(f"🌡️ 熱感療癒指數: **{thermal}**")
    st.write(f"🧡 互動潛力指數: **{social}**")
    st.write(f"🧴 皮膚摩擦適配性: **{rubbing}**")
    st.write(f"🍭 好吃誘蹭程度: **{edibility}**")

    st.subheader("🐘 今天參與蹭蹭的大象有：")
    for name in selected_names:
        st.markdown(f"- {name} 正在開心地蹭蹭～")
