
import streamlit as st
import random
import time
import numpy as np
import pandas as pd

st.set_page_config(page_title="大象舒適度蹭蹭模擬器 v3.5", page_icon="🐘", layout="centered")
st.title("🐘 大象舒適度蹭蹭模擬器 v3.5 - 🌀 蹭蹭大風車再進化！")

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

    # 計算結果
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

    # 模擬事件
    if mode == "蹭蹭大風車模式（極限蹭感）":
        st.markdown("---")
        st.header("🌀 蹭蹭大風車事件模擬")
        event = random.choice([
            "🧀 小巧丟出一顆起司球，你被砸中嘴巴，不小心吃掉了整塊。",
            "🧻 小索把象鼻當衛生紙，幫你擦了一下鼻子。",
            "🫧 冰嘣放出香香泡泡，你被包圍其中，香香地打了個噴嚏。",
            "🛏 杜克進入睡眠模式，大家集體進入療癒抖抖抱抱狀態～",
            "🐘 群象發動『象掌抱緊處理』，你整個人被抱住不能動…但超級舒服。"
        ])
        st.write(f"📣 事件觸發：{event}")

        # 象象語錄
        st.markdown("### 💬 象象語錄")
        quotes = [
            "小索：「你要不要靠我近一點…我這邊超暖的～」",
            "冰嘣：「肚子空空的嗎？餵你吃餅餅！」",
            "杜克：「朕允許你現在蹭朕。」",
            "拿鐵：「來～這裡躺著，象掌幫你包緊處理～」",
            "小札：「你剛剛是不是偷吸我頭頂？」"
        ]
        st.write(random.choice(quotes))

        # 贈禮系統
        st.markdown("### 🎁 獲得象象贈禮")
        gift = random.choice([
            "🧸 象掌造型暖寶寶：增加蹭蹭耐久度 10%",
            "🥞 象耳鬆餅片：恢復快樂值",
            "🫖 無熱量象奶茶：可再轉五圈不會暈",
            "🪄 杜克御用鼻梳：象鼻靈活度提升至 MAX",
            "🐘 冰嘣魔法鼻風器：產生飄浮狀態與旋轉特效"
        ])
        st.success(f"你獲得了：{gift}")

        # 模擬蹭蹭值波動圖
        st.markdown("### 📈 蹭蹭值波動圖")
        values = np.abs(np.sin(np.linspace(0, 3.5, 30)) * 100 + np.random.randn(30) * 5)
        df = pd.DataFrame({"蹭蹭值": values})
        st.line_chart(df)

        # 結語
        st.markdown("### 🧠 象象總結評語")
        if comfort > 90:
            st.info("你已經變成象象大家庭的一部分了，象象們愛你無限延伸～")
        elif comfort > 70:
            st.info("這場蹭蹭十分成功，你現在是象象認證的療癒朋友！")
        else:
            st.info("象象還需要更多時間認識你，但已經在默默靠近囉～")
