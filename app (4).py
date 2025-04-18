
import streamlit as st
import random
import time

st.set_page_config(page_title="象象蹭蹭小遊戲世界", page_icon="🐘", layout="centered")
st.title("🎮 象象蹭蹭小遊戲世界 v1.0")

st.markdown("選擇一款你喜歡的蹭蹭遊戲，開始療癒互動吧 🐘💖")

# 小遊戲選單
game = st.selectbox("選擇小遊戲", [
    "🐘 象鼻快閃蹭蹭王",
    "🫲 象掌養成計畫",
    "🧠 象象記憶訓練所",
    "🎯 象象蹭蹭彈珠台"
])

# 1. 象鼻快閃蹭蹭王
if game == "🐘 象鼻快閃蹭蹭王":
    st.subheader("🐘 象鼻快閃蹭蹭王")
    st.markdown("象象會在三秒內隨機出現，請搶先點擊正確的象象來觸發蹭蹭！")

    target = random.choice(["小索", "冰嘣", "小巧", "杜克", "波堤"])
    st.info(f"🎯 快閃目標象象是：**{target}**")
    time.sleep(1)

    with st.form("flash_form"):
        choice = st.radio("👆 點擊你看到的象象！", ["小索", "冰嘣", "小巧", "杜克", "波堤"])
        submitted = st.form_submit_button("蹭！")
        if submitted:
            if choice == target:
                st.success("🎉 你成功蹭到象象！他超開心地轉圈圈！")
            else:
                st.warning("😅 蹭錯象象啦～他害羞跑走了...")

# 2. 象掌養成計畫
elif game == "🫲 象掌養成計畫":
    st.subheader("🫲 象掌養成計畫")
    st.markdown("請幫象象按摩象掌～調整力度讓他最舒服！")

    pressure = st.slider("🧴 按摩力度", 0, 10, 5)
    if st.button("幫象象按摩！"):
        if pressure < 3:
            st.warning("👋 力道太小…象象癢癢的，笑到縮起來！")
        elif pressure > 8:
            st.error("🐘 啊啊太大力了～象象哞哞叫逃走了！")
        else:
            st.success("🥰 完美力道！象掌變得柔軟又香香～")
            st.balloons()

# 3. 記憶訓練所
elif game == "🧠 象象記憶訓練所":
    st.subheader("🧠 象象記憶訓練所")
    st.markdown("象象們說了話，請記住是誰說的！")

    sayings = {
        "小索": "我不只會蹭，我還會陪你～",
        "冰嘣": "香香的我來啦～",
        "杜克": "朕也需要被蹭。",
        "小巧": "來～吃點心再蹭～"
    }
    speaker, line = random.choice(list(sayings.items()))
    st.markdown(f"💬 有象象剛剛說了：「_{line}_」")
    guess = st.selectbox("請選擇誰說的", list(sayings.keys()))
    if st.button("提交答案"):
        if guess == speaker:
            st.success("💡 太棒了，你記得象象的心聲～親密度 +10！")
        else:
            st.error(f"🙈 錯了！剛剛是 **{speaker}** 在說話啦～")

# 4. 蹭蹭彈珠台
elif game == "🎯 象象蹭蹭彈珠台":
    st.subheader("🎯 象象蹭蹭彈珠台")
    st.markdown("放出一顆蹭蹭球，看看它掉進哪個蹭感洞口！")

    if st.button("放出蹭蹭球！🪀"):
        outcome = random.choice([
            "💗 親密洞！象象立刻黏過來～",
            "🥞 點心餵食口！你嘴巴被塞滿了象耳鬆餅！",
            "🛏 象掌抱緊處理槽～你現在被包起來了！",
            "🐘 象象懶得理你區…今天他想休息…"
        ])
        st.markdown(f"📣 結果：**{outcome}**")
