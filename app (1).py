
import streamlit as st
import random

st.set_page_config(page_title="大象舒適度蹭蹭模擬器 v3", page_icon="🐘", layout="centered")
st.title("🐘 大象舒適度蹭蹭模擬器 v3 - 大風車模式上線！")

mode = st.radio("🎡 選擇模式", ["一般模式", "蹭蹭大風車模式（極限蹭感）"])

if mode == "蹭蹭大風車模式（極限蹭感）":
    # 預設極限參數
    elephant_count = 10
    elephant_weight = 3500
    head_taste_index = 9.9
    foot_softness = 10.0
    trunk_length = 180
    trunk_flexibility = 10.0
    skin_score = 10.0
    belly_temp = 37.8
    ear_flap = 5
    rumble_volume = 9.5
    huddle_tightness = 10.0
    palm_wrap = 10.0
    belly_wave = 8.0
    emotion_sync = 100.0
    sound_type = "雙頻交響"
else:
    elephant_count = st.slider("🐘 大象數量", 1, 10, 3)
    elephant_weight = st.slider("⚖️ 大象體重 (kg)", 1000, 4000, 2500)
    head_taste_index = st.slider("🍭 頭頂好吃程度", 0.0, 10.0, 7.0)
    foot_softness = st.slider("🦶 腳掌柔軟舒適度", 0.0, 10.0, 8.0)
    trunk_length = st.slider("👃 象鼻長度 (cm)", 50, 200, 120)
    trunk_flexibility = st.slider("🐍 象鼻靈活度", 1.0, 10.0, 7.0)
    skin_score = st.slider("🧴 皮膚好蹭程度", 0.0, 10.0, 9.0)
    belly_temp = st.slider("🌡️ 肚肚溫度 (°C)", 30.0, 40.0, 37.5)
    ear_flap = st.slider("👂 搧耳頻率 (次/分鐘)", 0, 10, 3)
    rumble_volume = st.slider("🎶 咕嚕聲療癒度", 0.0, 10.0, 6.5)
    huddle_tightness = st.slider("🤗 群聚緊密程度", 0.0, 10.0, 8.0)
    palm_wrap = st.slider("🫲 象掌包覆感", 0.0, 10.0, 8.0)
    belly_wave = st.slider("🌊 象肚波動頻率 (次/分鐘)", 4.0, 12.0, 7.0)
    emotion_sync = st.slider("🧠 象象情緒同步指數 (%)", 0.0, 100.0, 80.0)
    sound_type = st.selectbox("🎵 象鳴音頻舒適度", ["低頻嗚鳴", "溫柔鼻哼", "撒嬌鼻音"])

elephant_names = ["小索", "小巧", "冰嘣", "波堤", "杜克", "拿鐵", "歐姆", "小札", "早吉", "大嫂"]
random.shuffle(elephant_names)
selected_names = elephant_names[:elephant_count]

if st.button("開始模擬 🧪"):
    comfort = round(
        elephant_count * 2 +
        foot_softness * 2.5 +
        skin_score * 2 +
        belly_temp +
        huddle_tightness * 2 +
        rumble_volume * 1.5 +
        palm_wrap * 2.5 +
        belly_wave * 2 +
        trunk_flexibility * 2 +
        emotion_sync / 10, 2
    )

    thermal = round(belly_temp * 2 + elephant_count * 1.5, 2)
    social = round(trunk_length / 20 + ear_flap * 1.2 + huddle_tightness + trunk_flexibility / 2, 2)
    rubbing = round(skin_score * 3 + foot_softness * 2 + palm_wrap * 2, 2)
    edibility = round(head_taste_index * 5, 2)

    st.subheader("🎯 模擬結果")
    st.write(f"🐘 蹭蹭舒適指數: **{comfort}/100**")
    st.write(f"🌡️ 熱感療癒指數: **{thermal}**")
    st.write(f"🧡 互動潛力指數: **{social}**")
    st.write(f"🧴 皮膚摩擦適配性: **{rubbing}**")
    st.write(f"🍭 好吃誘蹭程度: **{edibility}**")
    st.write(f"🎵 象鳴音頻：**{sound_type}**")

    st.subheader("🐘 今天參與蹭蹭的大象有：")
    for name in selected_names:
        st.markdown(f"- {name} 正在開心地蹭蹭～")

    if mode == "蹭蹭大風車模式（極限蹭感）":
        st.markdown("---")
        st.header("🌀 蹭蹭大風車模式已啟動！")
        st.markdown("""
> 十隻象象自動進入同步蹭蹭陣型，每隻象鼻高速靈活交錯，宛如巨型按摩風車。

> - 🐘 小索從你耳後溫柔地輕蹭進來。
> - 🐘 冰嘣皇后親自用象鼻捲住你的手幫你擦鼻涕。
> - 🐘 杜克國王坐鎮核心，掌控群象陣法節奏，象掌同步拍打大地。

> 🧁 你一邊旋轉、一邊被餵入象耳鬆餅與象鼻吉拿棒，嘴裡喊著：

> **「還要還要～再轉五圈！！」**

> 同步啟動《象象奶茶暖流注入》系統，直接灌進靈魂最深處……
        """)
