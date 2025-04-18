
import streamlit as st
import random
import time

st.set_page_config(page_title="象鼻快閃蹭蹭王 V3", page_icon="🐘", layout="centered")
st.title("🐘 象鼻快閃蹭蹭王 V3")

# 遊戲提示
st.markdown("🔊 請在 **30秒** 內狂點出現的象鼻！命中會得分，還有 Combo 語錄喔！")

# 資料夾路徑
img_path = "images/elephant_nose.png"

# 初始化 session state
if "game_start" not in st.session_state:
    st.session_state.game_start = False
    st.session_state.score = 0
    st.session_state.combo = 0
    st.session_state.start_time = 0

# 開始按鈕
if not st.session_state.game_start:
    if st.button("🎮 開始蹭蹭挑戰！"):
        st.session_state.game_start = True
        st.session_state.start_time = time.time()
        st.session_state.score = 0
        st.session_state.combo = 0
        st.rerun()

# 遊戲中
if st.session_state.game_start:
    elapsed = time.time() - st.session_state.start_time
    game_duration = 30
    if elapsed > game_duration:
        st.session_state.game_start = False
        st.markdown(f"## ⏱️ 時間到！你總共蹭中了 **{st.session_state.score} 次**！")
        if st.session_state.score >= 15:
            st.success("🏆 你是象鼻蹭蹭大師！")
        elif st.session_state.score >= 8:
            st.info("👏 蹭感熟練者，再接再厲！")
        else:
            st.warning("🐘 蹭感初學者，加油多練練象鼻定位！")
    else:
        st.markdown(f"⏱️ 剩餘時間：{int(game_duration - elapsed)} 秒")
        st.markdown(f"🎯 分數：{st.session_state.score} | Combo：{st.session_state.combo}")

        cols = st.columns(3)
        target_index = random.randint(0, 8)
        for i in range(9):
            with cols[i % 3]:
                if i == target_index:
                    if st.button("👃", key=f"nose_{i}"):
                        st.session_state.score += 1
                        st.session_state.combo += 1
                        if st.session_state.combo > 0 and st.session_state.combo % 3 == 0:
                            st.info(random.choice([
                                "象象：「你根本是鼻子魔術師！」",
                                "冰嘣：「哇～連續命中耶！」",
                                "小巧：「要不要加入蹭蹭隊？」"
                            ]))
                        st.rerun()
                else:
                    if st.button(" ", key=f"miss_{i}"):
                        st.session_state.combo = 0
                        st.rerun()
