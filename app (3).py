
import streamlit as st
import random

st.set_page_config(page_title="大象蹭蹭模擬器 V4 核心版", page_icon="🐘", layout="centered")
st.title("🐘 大象蹭蹭模擬器 V4：宇宙療癒核心版")

st.markdown("✨ 歡迎來到象象蹭蹭宇宙計畫核心模擬器 V4！")

# --- 角色資料庫（名稱、職業、技能、初始親密度） ---
characters = {
    "小索": {"職業": "蹭術師", "技能": "三連捲蹭擊", "親密度": 60, "語錄": "你要不要靠我近一點？"},
    "冰嘣": {"職業": "音療師", "技能": "雙鼻交響樂", "親密度": 80, "語錄": "來～我放點香香鼻風～"},
    "杜克": {"職業": "王政官", "技能": "全體蹭感強化", "親密度": 50, "語錄": "朕允你靠近。"},
    "小巧": {"職業": "點心師", "技能": "鬆餅大噴發", "親密度": 70, "語錄": "點心吃飽才有力氣被蹭呀～"},
    "拿鐵": {"職業": "睡眠師", "技能": "象掌搖籃波", "親密度": 75, "語錄": "來～睡一下吧～我幫你抱緊處理～"}
}

# --- 模式選擇 ---
mode = st.radio("🎮 選擇蹭蹭模式", ["🐘 角色蹭感互動", "🎉 派對亂鬥模式", "📅 每日任務", "🎁 贈禮收集"])

# --- 角色互動區 ---
if mode == "🐘 角色蹭感互動":
    selected = st.selectbox("選擇象象角色", list(characters.keys()))
    info = characters[selected]
    st.subheader(f"👑 {selected} | {info['職業']}")
    st.markdown(f"🧠 技能：{info['技能']}")
    st.markdown(f"💗 親密度：{info['親密度']} / 100")
    st.markdown(f"💬 語錄：_{info['語錄']}_")

    if st.button("進行互動 🐘💬"):
        gain = random.randint(5, 15)
        characters[selected]["親密度"] = min(100, info["親密度"] + gain)
        st.success(f"你和 {selected} 的親密度提升了 {gain} 點！")
        if characters[selected]["親密度"] >= 100:
            st.balloons()
            st.markdown(f"🎉 {selected}：「你現在是我最最最愛的蹭蹭夥伴了～」")

# --- 派對亂鬥模式 ---
elif mode == "🎉 派對亂鬥模式":
    st.subheader("🎲 派對加成事件轉盤")
    if st.button("轉轉轉～ GO！"):
        event = random.choice([
            "🐘 象鼻轉轉抽獎：獲得雙倍蹭感值！",
            "🛏 杜克啟動午睡模式，全體回血＋安撫！",
            "🫧 冰嘣泡泡療法！整場香香滿分！",
            "🫲 象掌連發：被十隻象掌同時蓋住！",
            "🥞 小巧餵你吃鬆餅，嘴巴被餅乾塞滿！"
        ])
        st.markdown(f"📣 派對事件觸發：**{event}**")
        st.toast("🎉 派對加成發動成功！")

# --- 每日任務 ---
elif mode == "📅 每日任務":
    st.subheader("📅 今日蹭蹭任務")
    tasks = [
        "✅ 完成一次角色互動",
        "✅ 啟動一次派對亂鬥模式",
        "✅ 提升任一象象親密度達 80",
        "✅ 收到 1 項象象贈禮"
    ]
    for t in tasks:
        st.write(t)
    st.success("🎁 任務完成！你獲得了『象掌徽章 ×1』")

# --- 贈禮收集系統 ---
elif mode == "🎁 贈禮收集":
    st.subheader("🎁 今日贈禮掉落")
    gifts = [
        "🧸 象掌造型暖寶寶",
        "🥞 象耳鬆餅片",
        "🫖 象奶茶加大杯",
        "🪄 杜克御用鼻梳",
        "🐘 冰嘣魔法鼻風器"
    ]
    gift = random.choice(gifts)
    st.markdown(f"你今天幸運地獲得了：**{gift}**")
    st.info("📦 小提醒：可把贈禮存進象象收藏冊（未來開放）")
