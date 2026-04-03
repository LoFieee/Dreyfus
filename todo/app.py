import streamlit as st
import streamlit.components.v1 as components
import json
import time

# ================= STYLE =================
st.set_page_config(page_title="TRAVAIL POUR LA NATION", layout="wide")

st.markdown("""
<style>
.main {
    background-color: #4d4582;
    color: white;
}

.card {
    background-color: #4d4582;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

#================= BOUTONS =================

st.markdown("""
<style>

/* Container du radio */
div[role="radiogroup"] {
    display: flex;
    justify-content: center;
    gap: 10px;
}

/* Chaque bouton */
div[role="radiogroup"] label {
    background-color: #1e293b;
    padding: 10px 20px;
    border-radius: 10px;
    cursor: pointer;
    transition: 0.3s;
    border: 1px solid transparent;
}

/* Hover */
div[role="radiogroup"] label:hover {
    background-color: #334155;
}

</style>
""", unsafe_allow_html=True)


#================= BANNER =================

st.markdown("""
<style>
.marquee {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    box-sizing: border-box;
}

.marquee span {
    display: inline-block;
    padding-left: 100%;
    animation: scroll 10s linear infinite;
    font-size: 40px;
    font-weight: bold;
    color: #38bdf8;
}

@keyframes scroll {
    0% { transform: translateX(0%); }
    100% { transform: translateX(-100%); }
}
</style>

<div class="marquee">
    <span>TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     TRAVAIL POUR LE PEUPLE ☭☭☭☭☭☭      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL     TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL      TRAVAIL     </span>
</div>
""", unsafe_allow_html=True)


# ================= LOFI GIRL =================

st.markdown("""
<div style="
position: fixed;
bottom: 610px;
right: 20px;
width: 300px;
background: #1e293b;
border-radius: 10px;
padding: 10px;
z-index: 9999;
box-shadow: 0 0 10px rgba(0,0,0,0.5);
">

<!-- Bouton fermer -->
<div style="text-align:right;">
    <button onclick="this.parentElement.parentElement.style.display='none'" 
    style="background:none;border:none;color:white;font-size:16px;cursor:pointer;">
        ✖
    </button>
</div>

<!-- Player -->
<iframe width="100%" height="150"
src="https://www.youtube.com/embed/jfKfPfyJRdk"
frameborder="0"
allow="autoplay; encrypted-media"
</iframe>

</div>
""", unsafe_allow_html=True)

# ================= DATA =================

    
FILE = "data.json"

def load():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"tasks": [], "notes": []}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

data = load()



# ================= MENU =================


menu = st.radio(
    "",
    ["📋 To-Do", "⏱ Timer", "🍅 Pomodoro", "📝 Notes", "📊 Stats"],
    horizontal=True
)



# ================= MOTIVATION IMAGE =================


total = len(data["tasks"])
done = sum(1 for t in data["tasks"] if t["done"])


if total < 0 and done == total:
    st.image("win.png", width=200)
    st.success("Tout est terminé")
else:
    st.image("motivation.jpg", width=200)
    st.warning("☭ Au boulot ☭")



# ================= TO DO =================


if menu == "📋 To-Do":
    st.markdown("## To-Do List")

    col1, col2 = st.columns([1,1])
    with col1:
        new_task = st.text_input("Nouvelle tâche")
    with col2:
        if st.button("Ajouter"):
            if new_task:
                data["tasks"].append({"titre": new_task, "done": False})
                save(data)
                st.rerun()

    for i, t in enumerate(data["tasks"]):
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([6,1,1])

        with col1:
            checked = st.checkbox(t["titre"], value=t["done"], key=i)
            data["tasks"][i]["done"] = checked

        with col2:
            if st.button("❌", key=f"del{i}"):
                data["tasks"].pop(i)
                save(data)
                st.rerun()

        with col3:
            st.write("Fait ✔️" if t["done"] else "❌")

        st.markdown("</div>", unsafe_allow_html=True)

    save(data)

# ================= TIMER =================


elif menu == "⏱ Timer":
    st.markdown("## Timer")

    minutes_input = st.slider("Durée (minutes)", 1, 60, 1)
    sec = minutes_input * 60

    if "timer_end" not in st.session_state:
        st.session_state.timer_end = None

    if st.button("Lancer"):
        st.session_state.timer_end = time.time() + sec

    if st.session_state.timer_end:
        remaining = int(st.session_state.timer_end - time.time())

        if remaining > 0:
            minutes = remaining // 60
            seconds = remaining % 60

            st.markdown(f"## ⏳ {minutes:02d}:{seconds:02d}")

            progress = 1 - (remaining / sec)
            st.progress(progress)

            time.sleep(1)
            st.rerun()
        else:
            st.success("Temps écoulé 🎉")
            st.balloons()
            st.session_state.timer_end = None
            st.markdown("""
            <audio autoplay>
            <source src="alarm.mp3" type="audio/mpeg">
            </audio>
            """, unsafe_allow_html=True)
        

# ================= POMODORO =================

elif menu == "🍅 Pomodoro":
    st.markdown("## 🍅 Pomodoro")

    work = st.number_input("Travail (minutes)", 1, 60, 25)
    break_time = st.number_input("Pause (minutes)", 1, 30, 5)

    if "end_time" not in st.session_state:
        st.session_state.end_time = None
        st.session_state.mode = "work"

    if st.button("Start"):
        st.session_state.mode = "work"
        st.session_state.end_time = time.time() + work * 60

    if st.session_state.end_time:
        remaining = int(st.session_state.end_time - time.time())

        if remaining > 0:
            minutes = remaining // 60
            seconds = remaining % 60

            st.markdown(f"## ⏳ {minutes:02d}:{seconds:02d}")
            st.write(f"Mode : {st.session_state.mode}")

            time.sleep(1)
            st.rerun()
        else:
            if st.session_state.mode == "work":
                st.session_state.mode = "break"
                st.session_state.end_time = time.time() + break_time * 60
                st.rerun()
            else:
                st.success("Pomodoro fini 🎉")
                st.session_state.end_time = None
                st.markdown("""
                <audio autoplay>
                <source src="https://www.soundjay.com/buttons/beep-07.mp3" type="audio/mpeg">
                </audio>
                """, unsafe_allow_html=True)


# ================= NOTES =================
elif menu == "📝 Notes":
    st.markdown("## Notes")

    note = st.text_area("Écrire une note")
    if st.button("Ajouter note"):
        if note:
            data["notes"].append(note)
            save(data)
            st.rerun()

    for n in data["notes"]:
        st.markdown(f"<div class='card'>{n}</div>", unsafe_allow_html=True)

# ================= STATS =================
elif menu == "📊 Stats":
    st.markdown("## Statistiques")

    total = len(data["tasks"])
    done = sum(1 for t in data["tasks"] if t["done"])

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Tâches totales", total)

    with col2:
        st.metric("Terminées", done)

    if total > 0:
        st.progress(done / total)
