import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 02 · The Five Senses", layout="wide", initial_sidebar_state="expanded")

# ─── Global CSS (Applied early to prevent flicker) ───────────────────────────
st.markdown("""
<style>
    /* Hide default Streamlit MainMenu and Footer */
    #MainMenu, footer {display: none;}

    /* Hide default sidebar navigation list */
    div[data-testid="stSidebarNav"] {display: none;}

    /* Smooth font */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d2b5e 0%, #1565c0 50%, #0d47a1 100%);
    }
    section[data-testid="stSidebar"] * {
        color: #e3f2fd !important;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffffff !important;
    }

    /* Button hover glow */
    div.stButton > button {
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:0.5rem 0;">
        <div style="font-size:2.5rem;">🔬</div>
        <div style="font-weight:700; font-size:1.1rem; color:#fff;">Science for Little Stars</div>
        <div style="font-size:0.8rem; color:#90caf9;">Grades 1–3 · Ages 5–8</div>
    </div>
    <hr style="border:2px solid lightblue;">
    """, unsafe_allow_html=True)
    
    st.markdown("### 🗺️ Navigation")
    st.page_link("Home.py", label="🏠 Home", icon="🏠")
    st.page_link("pages/01_chapter_our_body-01.py", label="Ch 01 · Our Amazing Body", icon="🦴")
    st.page_link("pages/02_chapter_senses-02.py", label="Ch 02 · The Five Senses", icon="👁️")
    st.page_link("pages/03_chapter_plants-03.py", label="Ch 03 · Plants and Growth", icon="🌱")
    st.page_link("pages/04_chapter_animals-04.py", label="Ch 04 · Animals and Habitats", icon="🐾")
    st.page_link("pages/05_chapter_magnets-05.py", label="Ch 05 · Marvelous Magnets", icon="🧲")
    st.page_link("pages/06_chapter_weather-06.py", label="Ch 06 · Water and Weather", icon="☁️")
    st.page_link("pages/07_chapter_simple_machines-07.py", label="Ch 07 · Simple Machines", icon="🛠️")
    st.page_link("pages/08_chapter_saving_our_planet-08.py", label="Ch 08 · Saving Our Planet", icon="🌍")
    st.page_link("pages/09_chapter_energy_electricity-09.py", label="Ch 09 · Energy and Electricity", icon="🔋")
    st.page_link("pages/10_chapter_space-10.py", label="Ch 10 · The Solar System", icon="🌌")
    st.page_link("pages/science_quiz.py",label="Science Game",icon="🎯")
    st.page_link("pages/video_library.py",label="Science Cinema",icon="🎬")
    
    st.markdown(
    """
    <hr style="border:2px solid lightblue;">
    """,
    unsafe_allow_html=True
)
   
with st.sidebar:st.caption("""© 2026 Science for Little Stars. All rights reserved.
Authored by <strong style="color:brown;">AMBREEN ABDUL RAHEEM</strong>
The Education Expert""", unsafe_allow_html=True)

# ─── Session State Defaults ──────────────────────────────────────────────────
for key in [
    "show_eye_fact", "show_ear_fact", "show_nose_fact",
    "show_tongue_fact", "show_skin_fact",
    "quiz_submitted",
]:
    if key not in st.session_state:
        st.session_state[key] = False

if "sense_picked"       not in st.session_state: st.session_state.sense_picked       = None
if "animal_sense_picked" not in st.session_state: st.session_state.animal_sense_picked = None
if "brain_step"         not in st.session_state: st.session_state.brain_step          = 0
if "quiz_answers"       not in st.session_state: st.session_state.quiz_answers        = {}

# ─── Helpers ─────────────────────────────────────────────────────────────────
def fun_card(emoji, title, body, bg="#e8f4fd", border="#4a90e2"):
    st.markdown(f"""
    <div style="background:{bg}; border-left:5px solid {border};
                border-radius:16px; padding:1.2rem 1.4rem; margin:0.6rem 0;
                box-shadow:0 3px 10px rgba(0,0,0,0.07);">
        <div style="font-size:2rem; margin-bottom:0.3rem;">{emoji}</div>
        <div style="font-weight:700; font-size:1.1rem; color:#2c3e50;
                    margin-bottom:0.4rem;">{title}</div>
        <div style="font-size:0.97rem; color:#444; line-height:1.7;">{body}</div>
    </div>""", unsafe_allow_html=True)

def section_header(emoji, title, subtitle=""):
    st.markdown(f"""
    <div style="text-align:center; margin: 2rem 0 1rem;">
        <div style="font-size:3.5rem; margin-bottom:0.3rem;">{emoji}</div>
        <h2 style="color:#2c3e50; font-size:1.9rem; margin:0;">{title}</h2>
        {"<p style='color:#6b7c93; font-size:1rem; margin-top:0.3rem;'>" + subtitle + "</p>" if subtitle else ""}
    </div>""", unsafe_allow_html=True)

def think_bubble(question):
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#e8f4fd,#f3e5f5);
                border-radius:20px; padding:1rem 1.4rem; margin:0.8rem 0;
                border:2px dashed #7b1fa2; text-align:center;">
        <span style="font-size:1.5rem;">🤔</span>
        <span style="font-weight:600; color:#2c3e50; margin-left:0.5rem;
                     font-size:0.97rem;">{question}</span>
    </div>""", unsafe_allow_html=True)

def fact_row(icon, label, fact, bg="#f5f5f5", color="#333"):
    st.markdown(f"""
    <div style="display:flex; align-items:flex-start; gap:0.7rem;
                padding:0.6rem; border-radius:10px; margin-bottom:0.4rem;
                background:{bg};">
        <span style="font-size:1.4rem; flex-shrink:0;">{icon}</span>
        <div><strong style="color:{color};">{label}:</strong>
        <span style="font-size:0.93rem; color:#444;"> {fact}</span></div>
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  CHAPTER BANNER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:linear-gradient(135deg,#1a0533,#4a148c,#880e4f,#1a0533);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; overflow:hidden;">
    <div style="font-size:1rem; color:#ce93d8; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 02 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.4);">
        ✨ The Five Senses ✨
    </h1>
    <p style="color:#e1bee7; font-size:1.05rem; margin:0.8rem 0 0;">
        Your body has 5 incredible superpowers — let's explore every single one!
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.5rem;">
        👀 👂 👃 👅 ✋
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ What the **5 senses** are and why we need them
        - ✅ How your **eyes** see the world
        - ✅ How your **ears** hear sounds
        - ✅ How your **nose** detects smells
        """)
    with col2:
        st.markdown("""
        - ✅ How your **tongue** tastes 5 flavours
        - ✅ How your **skin** feels touch, heat and pain
        - ✅ How your **brain** puts it all together
        - ✅ Animals with **super senses** + a quiz!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — WHAT ARE THE SENSES?
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Are the Five Senses?",
               "Your body's five amazing ways to understand the world!")


st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Right now, without even thinking about it, your body is doing something incredible.

    Your **eyes** are reading these words. Your **ears** might hear sounds around you.
    Your **skin** can feel the chair beneath you. Your **nose** might catch a smell nearby.
    And your **tongue** still remembers what you last ate! 😄

    These five abilities — **sight, hearing, smell, taste, and touch** — are called your
    **FIVE SENSES.** They are like five windows between you and the world.
    """)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#f3e5f5,#e8eaf6);
                border-radius:16px; padding:1.2rem 1.6rem; margin:0.8rem 0;
                border:2px solid #9c27b0;">
        <div style="font-weight:700; color:#4a148c; font-size:1.05rem; margin-bottom:0.8rem;">
            🧠 Your Senses and Their Organs:
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem;">
            <div style="background:rgba(255,255,255,0.7); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">👀</div>
                <div style="font-weight:700; color:#1565c0;">Sight</div>
                <div style="font-size:0.85rem; color:#666;">Eyes</div>
            </div>
            <div style="background:rgba(255,255,255,0.7); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">👂</div>
                <div style="font-weight:700; color:#2e7d32;">Hearing</div>
                <div style="font-size:0.85rem; color:#666;">Ears</div>
            </div>
            <div style="background:rgba(255,255,255,0.7); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">👃</div>
                <div style="font-weight:700; color:#e65100;">Smell</div>
                <div style="font-size:0.85rem; color:#666;">Nose</div>
            </div>
            <div style="background:rgba(255,255,255,0.7); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">👅</div>
                <div style="font-weight:700; color:#c62828;">Taste</div>
                <div style="font-size:0.85rem; color:#666;">Tongue</div>
            </div>
            <div style="background:rgba(255,255,255,0.7); border-radius:10px; padding:0.6rem; text-align:center; grid-column:1/3;">
                <div style="font-size:1.8rem;">✋</div>
                <div style="font-weight:700; color:#6a1b9a;">Touch</div>
                <div style="font-size:0.85rem; color:#666;">Skin (whole body!)</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    think_bubble("Close your eyes for 5 seconds. Which other senses do you notice more when you can't see? 👀")

with col2:
    fun_card("🧠", "Your Brain Is the Boss",
             "Your senses are messengers — they collect information and "
             "rush it to your BRAIN at lightning speed. Your brain then figures out "
             "what everything means and decides what to do! You couldn't use any "
             "sense without your brain. 🏆",
             bg="#f3e5f5", border="#8e24aa")
    fun_card("⚡", "Super Fast Signals",
             "Nerve signals travel from your senses to your brain at up to "
             "430 km per hour — faster than a racing car! That's why you pull "
             "your hand away from something hot almost instantly. ⚡🔥",
             bg="#fff8e1", border="#f9a825")
    fun_card("🤝", "Senses Work Together",
             "Imagine eating your favourite food — you see its colour, smell its aroma, "
             "taste its flavour, feel its texture, and maybe hear it crunch! "
             "Your senses always team up to give you the full experience. 🍕",
             bg="#e8f5e9", border="#43a047")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — THE FIVE SENSES IN DETAIL
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🔬", "Let's Explore Each Sense!",
               "Dive deep into how every sense works — they're more amazing than you think!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ─── SIGHT 👀 ─────────────────────────────────────────────────────────────────
st.markdown("### 👀 Sense 1 — Sight")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Sight** is often called our most powerful sense. Your eyes are like tiny cameras 
    that are on all day, sending a non-stop video straight to your brain! 📹

    **How do eyes work?**
    """)
    for step, icon, title, desc in [
        (1, "💡", "Light enters",        "Light bounces off everything around you and enters your eye through the PUPIL — the black circle in the middle of your eye."),
        (2, "🔍", "Lens focuses",        "The LENS (a clear disc behind your pupil) bends the light and focuses it into a sharp picture — just like a camera lens!"),
        (3, "🖼️", "Retina receives",     "The picture lands on the RETINA at the back of your eye. Millions of tiny cells called RODS and CONES detect the image."),
        (4, "⚡", "Signal sent to brain","The optic nerve carries the picture as an electrical signal to your brain in a tiny fraction of a second!"),
        (5, "🧠", "Brain sees",          "Your brain flips the image the right way up (the eye actually sees everything upside down!) and — you SEE! 🎉"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e3f2fd;">
            <span style="background:#1565c0; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#1565c0;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Why do your pupils get bigger in a dark room? What are they trying to do? 🌑")

with col2:
    st.markdown("##### 👀 Eye-Opening Facts")
    for icon, label, fact in [
        ("🌈", "Colours",       "Your eyes have special cells called CONES that detect colour — most humans see about 10 million different colours! Dogs see far fewer. 🐕"),
        ("🌙", "Night Vision",  "In dim light, ROD cells take over from cones. They don't see colour, but they're brilliant at detecting movement and shapes in the dark!"),
        ("😉", "Blinking",      "You blink about 15–20 times every MINUTE — that's over 10,000 blinks a day! Each blink cleans and moistens your eye in just 0.1 seconds."),
        ("🤩", "Pupils",        "Your pupils get BIGGER in darkness to let in more light, and SMALLER in bright light to protect your eye. Try looking at a mirror in different lights!"),
        ("👓", "Glasses",       "Some people's lenses focus light slightly in the wrong place. Glasses and contact lenses correct this by bending the light differently first. 🔧"),
        ("👁️", "Unique",        "Your iris (the coloured ring) has a pattern as unique as your fingerprint — no two people have the same iris pattern! 🌸"),
    ]:
        fact_row(icon, label, fact, "#e3f2fd", "#1565c0")

    if st.button("👀 Reveal an Eye Secret!", use_container_width=True, key="eye_btn"):
        st.session_state.show_eye_fact = not st.session_state.show_eye_fact
    if st.session_state.show_eye_fact:
        st.success("🎉 Your brain actually sees everything UPSIDE DOWN! "
                   "The eye projects an inverted image on the retina, "
                   "and your brain automatically flips it the right way up "
                   "so you see the world correctly — it has been doing this "
                   "since the moment you were born! 🙃➡️🙂")

# ─── HEARING 👂 ───────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)
st.markdown("### 👂 Sense 2 — Hearing")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Hearing** lets you enjoy music, understand speech, hear danger, and laugh at 
    funny sounds! Your ears are constantly working — even while you sleep! 😴

    **How do ears work?**
    """)
    for step, icon, title, desc in [
        (1, "🔊", "Sound waves travel",    "Everything that makes a sound — a voice, a drum, a thunderclap — creates invisible vibrations in the air called SOUND WAVES."),
        (2, "👂", "Outer ear collects",    "Your outer ear (the curly bit you can see) is shaped like a funnel to catch sound waves and guide them into the ear canal."),
        (3, "🥁", "Eardrum vibrates",      "Deep inside, the EARDRUM — a thin disc of skin — vibrates like a tiny drum when sound waves hit it. Loud sounds make it vibrate a lot!"),
        (4, "🦴", "Tiny bones amplify",    "Three of the smallest bones in your whole body — the hammer, anvil, and stirrup — carry and magnify the vibration further inside."),
        (5, "🌀", "Cochlea converts",      "The COCHLEA (a snail-shaped tube) turns the vibrations into electrical nerve signals, and whoosh — they shoot to your brain!"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#e8f5e9;">
            <span style="background:#2e7d32; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#2e7d32;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    fun_card("⚖️", "Ears Help You Balance Too!",
             "Deep inside each ear is a structure called the VESTIBULAR SYSTEM — "
             "three tiny fluid-filled loops that detect when you tilt or spin. "
             "That's why you feel dizzy after spinning in circles! 🌀 "
             "Your ears are your built-in balance system!",
             bg="#e8f5e9", border="#43a047")

with col2:
    st.markdown("##### 👂 Sound-Sational Facts")
    for icon, label, fact in [
        ("🔇", "Silence",       "Your ears are SO sensitive they can detect sound vibrations smaller than the width of a hydrogen atom — the smallest atom in existence! 🤯"),
        ("🎵", "Music",         "When you hear music you love, your brain releases a chemical called dopamine that makes you feel happy. Music literally changes your mood! 😊"),
        ("🦻", "Two Ears",      "Having TWO ears means you can tell which direction a sound comes from. Cover one ear and sounds become harder to locate. 🧭"),
        ("😴", "Always On",     "Your ears never switch off — not even when you sleep! Your brain is the one that decides to stop processing sounds during deep sleep."),
        ("🔴", "Loud Sounds",   "Very loud sounds (like concerts or headphones at full volume) can damage the tiny hair cells in your cochlea — and they NEVER grow back! 🎧⚠️"),
        ("🐘", "Elephant Ears", "Elephants use their huge ears like fans to cool down — blood flowing through the thin skin loses heat in the breeze! Smart cooling system! 🌬️"),
    ]:
        fact_row(icon, label, fact, "#e8f5e9", "#2e7d32")

    if st.button("👂 Tap for an Ear Surprise!", use_container_width=True, key="ear_btn"):
        st.session_state.show_ear_fact = not st.session_state.show_ear_fact
    if st.session_state.show_ear_fact:
        st.success("🎉 You have the three SMALLEST bones in your entire body inside your ear! "
                   "The stirrup bone is only 3mm long — smaller than a grain of rice! 🍚 "
                   "Yet these tiny bones are essential for hearing every sound you've ever heard. 🦴")

# ─── SMELL 👃 ─────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 👃 Sense 3 — Smell")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Smell** is our most ancient sense — animals have been using it for hundreds 
    of millions of years! It's also the sense most powerfully linked to memory. 🧠

    Have you ever smelled something — like freshly baked bread or rain on the ground — 
    and it instantly reminded you of a happy memory? That's your smell-memory connection at work! 💛

    **How does smell work?**
    """)
    for step, icon, title, desc in [
        (1, "💨", "Tiny particles float",  "Everything with a smell releases billions of microscopic chemical particles into the air — too tiny to see, but your nose can find them!"),
        (2, "👃", "Nose hairs filter",     "Tiny hairs inside your nostrils trap dust and germs, while the air carries the smell particles deeper inside."),
        (3, "🎯", "Receptors detect",      "High up inside your nose sits a patch of tissue with about 400 SMELL RECEPTORS — each one designed to detect a different type of smell particle."),
        (4, "⚡", "Signal to brain",       "When a smell particle clicks into a receptor (like a key in a lock!), it sends an electrical signal straight to the OLFACTORY BULB in your brain."),
        (5, "🧠", "Brain identifies",      "Your brain matches the signal to its library of remembered smells — and instantly tells you what it is! Cookies! Flowers! Rain! 🌸"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fff3e0;">
            <span style="background:#e65100; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#e65100;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("What is your FAVOURITE smell in the whole world? What memory does it remind you of? 🌸")

with col2:
    st.markdown("##### 👃 Nose-Worthy Facts")
    for icon, label, fact in [
        ("🔢", "Trillions!",     "Scientists once thought humans could smell 10,000 scents. New research suggests we can actually detect over ONE TRILLION different smells! 🤯"),
        ("😋", "Taste + Smell",  "About 80% of what you think you're TASTING is actually SMELL! Hold your nose while eating — food suddenly becomes much more bland. Try it! 🍎"),
        ("🤧", "Blocked Nose",   "When your nose is blocked from a cold, food loses most of its flavour — that's because the smell particles can't reach your receptors. 😫"),
        ("⚠️", "Warning System", "Bad smells are often a warning! Rotten food, smoke, and gas all smell bad to alert you to danger — your nose is your alarm system! 🚨"),
        ("🌧️", "Petrichor",      "The lovely smell of rain on dry ground has a name: PETRICHOR! It is caused by bacteria in the soil releasing a chemical when raindrops hit. 🌱"),
        ("💤", "Sleep Smell",    "Smell is the ONLY sense with a direct pathway to the memory and emotion centres of the brain — that's why smells trigger such strong memories!"),
    ]:
        fact_row(icon, label, fact, "#fff3e0", "#e65100")

    if st.button("👃 Reveal a Smell Secret!", use_container_width=True, key="nose_btn"):
        st.session_state.show_nose_fact = not st.session_state.show_nose_fact
    if st.session_state.show_nose_fact:
        st.success("🎉 Newborn babies recognise their own mother purely by SMELL "
                   "within the first few days of life — before they can see or hear well! "
                   "And mothers can identify their own baby by smell from the first day. "
                   "Smell is the original bonding superpower! 👶💛")

# ─── TASTE 👅 ─────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 👅 Sense 4 — Taste")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Taste** might be your most delicious sense! 😄 Your tongue is an extraordinary 
    muscle covered in tiny bumps — and each bump is packed with TASTE BUDS!

    **How does taste work?**
    """)
    for step, icon, title, desc in [
        (1, "🍎", "Food goes in mouth",   "When food or drink enters your mouth, your tongue and saliva get to work immediately."),
        (2, "💧", "Saliva dissolves",     "Your saliva dissolves the food into tiny chemical particles — taste only works with dissolved chemicals, not dry solid objects!"),
        (3, "🌸", "Taste buds detect",    "About 10,000 TASTE BUDS (mostly on your tongue, but some on your cheeks and throat!) detect the chemicals."),
        (4, "⚡", "Signals sent",         "Each taste bud sends a nerve signal to your brain describing what kind of taste it detected."),
        (5, "🧠", "Brain combines",       "Your brain combines the taste signal with the smell signal from your nose and the texture from your tongue — and creates the full flavour experience! 🎨"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fce4ec;">
            <span style="background:#c62828; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#c62828;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    # The 5 Tastes
    st.markdown("##### 🌈 The 5 Basic Tastes — Can You Name Them?")
    tastes = [
        ("🍬", "Sweet",  "Sugar, honey, ripe fruit", "#fff8e1", "#f9a825",
         "Sweetness signals that food has energy (sugar) — your body needs energy to run and play!"),
        ("🍋", "Sour",   "Lemons, vinegar, yoghurt", "#f9fbe7", "#8bc34a",
         "Sourness can mean unripe fruit or fermented food — it makes you pull that face! 😖"),
        ("🧂", "Salty",  "Salt, crisps, soy sauce",  "#e3f2fd", "#1e88e5",
         "Saltiness helps your body find the minerals it needs. Your body uses salt for nerves and muscles!"),
        ("☕", "Bitter", "Coffee, dark chocolate, spinach", "#efebe9", "#795548",
         "Bitterness often warns of poison — that's why children dislike bitter tastes and adults learn to enjoy some!"),
        ("🍖", "Umami",  "Meat, cheese, mushrooms",  "#f3e5f5", "#8e24aa",
         "Umami is a savoury, meaty taste discovered by scientists in 1908. It signals protein — which builds your muscles! 💪"),
    ]
    for emoji, name, eg, bg, border, why in tastes:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:12px; padding:0.7rem 1rem;
                    border-left:4px solid {border}; margin-bottom:0.4rem;">
            <div style="display:flex; align-items:center; gap:0.5rem;">
                <span style="font-size:1.4rem;">{emoji}</span>
                <strong style="color:{border}; font-size:1rem;">{name}</strong>
                <span style="font-size:0.85rem; color:#777;">· e.g. {eg}</span>
            </div>
            <div style="font-size:0.88rem; color:#555; margin-top:0.3rem; padding-left:1.9rem;">
                {why}
            </div>
        </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("##### 👅 Tasty Facts")
    for icon, label, fact in [
        ("🔄", "Renew",         "Your taste buds only live for about 10 days before they are replaced by brand new ones! You get entirely new taste buds nearly every two weeks. 🆕"),
        ("📉", "Getting Older", "Adults have about 10,000 taste buds, but as we age, many stop working. That's one reason why grown-ups enjoy strong flavours children find overwhelming!"),
        ("🌶️", "Spicy!",        "Spiciness is NOT a taste — it's actually a PAIN signal! Chilli contains a chemical (capsaicin) that triggers the same pain receptors as real heat. 🔥"),
        ("👶", "Born Sweet",    "Babies are born loving sweet tastes and hating bitter ones — this is hardwired to help them drink sweet breast milk and avoid potentially poisonous plants!"),
        ("🐱", "Cats",          "Cats CANNOT taste sweetness at all! They have no sweet taste receptors — which is why cats have no interest in chocolate cake. 🎂😹"),
        ("🦋", "Butterfly Feet","Butterflies taste with their FEET — they stand on food to decide if it's worth eating! Their taste sensors are 200 times stronger than a human tongue. 🦶"),
    ]:
        fact_row(icon, label, fact, "#fce4ec", "#c62828")

    if st.button("👅 Tap for a Tongue Secret!", use_container_width=True, key="tongue_btn"):
        st.session_state.show_tongue_fact = not st.session_state.show_tongue_fact
    if st.session_state.show_tongue_fact:
        st.success("🎉 The idea that different parts of your tongue taste different things "
                   "(sweet at the front, bitter at the back etc.) is a MYTH! 🙅 "
                   "ALL taste buds all over your tongue can detect ALL five tastes. "
                   "This map was a mistake in an old textbook that everyone believed! 😄")

    think_bubble("Hold your nose and eat a crisp or a piece of fruit. Does it still taste the same? 🤔")

# ─── TOUCH ✋ ──────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### ✋ Sense 5 — Touch")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    **Touch** is our largest sense — because our **entire skin** is the sense organ! 
    Your skin covers about 2 square metres and contains millions of tiny sensors.

    Touch is also our most essential sense for safety — it tells us when something 
    is dangerously hot, painfully sharp, or when we need to move! 🛡️

    **Touch detects FIVE different things:**
    """)
    touch_types = [
        ("🤏", "Pressure",    "#e3f2fd", "#1e88e5",
         "When you pick up a pencil or hug someone — sensors in your skin feel the push."),
        ("🔥", "Temperature", "#fff3e0", "#e65100",
         "Special sensors tell you if something is warm, hot, cool, or freezing cold. ❄️"),
        ("⚡", "Pain",        "#fce4ec", "#c62828",
         "Pain is an alarm! It tells your brain that something is damaging your body so you move away fast."),
        ("🪶", "Light touch",  "#f3e5f5", "#8e24aa",
         "Feeling a feather, a breeze, or someone gently tapping your shoulder."),
        ("🎸", "Vibration",   "#e8f5e9", "#43a047",
         "Feeling a phone buzz, music through a speaker, or a truck rumbling past."),
    ]
    for icon, name, bg, color, desc in touch_types:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.8rem;
                    padding:0.6rem 0.9rem; border-radius:12px; margin-bottom:0.4rem;
                    background:{bg}; border-left:4px solid {color};">
            <span style="font-size:1.5rem; flex-shrink:0;">{icon}</span>
            <div>
                <strong style="color:{color};">{name}:</strong>
                <span style="font-size:0.93rem; color:#444;"> {desc}</span>
            </div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Which part of your body do you think is the MOST sensitive to touch? Why? 🤔")

with col2:
    st.markdown("##### ✋ Touching Facts")
    for icon, label, fact in [
        ("👆", "Fingertips",    "Your fingertips have the highest density of touch sensors in your body — up to 2,500 sensors per square centimetre! That's why they are SO sensitive. 🎵"),
        ("🔴", "Reflex Action", "When you touch something very hot, your hand pulls back BEFORE your brain even processes the pain! Your spinal cord sends the reflex signal directly. ⚡"),
        ("💆", "Healing Touch", "Gentle touch releases a hormone called OXYTOCIN (the 'cuddle hormone') that reduces stress, lowers blood pressure, and makes you feel calm and safe. 🤗"),
        ("🧤", "Gloves",        "Wearing thick gloves reduces your sense of touch dramatically. Surgeons, pianists, and sculptors rely on extreme fingertip sensitivity for their work. 🎹"),
        ("👄", "Lips & Tongue", "Your lips and tongue are among the most sensitive touch organs in your body — that's why babies put everything in their mouths to explore it! 👶"),
        ("🥶", "Goosebumps",    "Goosebumps happen when you're cold or scared — tiny muscles pull your hair upright to trap warm air. It worked much better when we had thick body hair! 🦍"),
    ]:
        fact_row(icon, label, fact, "#f3e5f5", "#6a1b9a")

    if st.button("✋ Reveal a Touch Secret!", use_container_width=True, key="skin_btn"):
        st.session_state.show_skin_fact = not st.session_state.show_skin_fact
    if st.session_state.show_skin_fact:
        st.success("🎉 Some people can read with their fingertips! "
                   "BRAILLE is a system of raised dots that people who cannot see "
                   "read by feeling the patterns with their extremely sensitive fingertips. "
                   "Their brains process touch the same way sighted people process words. 🤩✋📖")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — HOW THE BRAIN PUTS IT TOGETHER
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧠", "Your Brain — The Master Controller!",
               "All five senses send their messages here — step through how your brain works! 🧩")

brain_steps = [
    ("📡", "Step 1: Senses Collect Information",
     "Right now, every second, your 5 senses are collecting an enormous amount of information. "
     "Your eyes are processing millions of pixels of visual data. Your ears are detecting sound waves. "
     "Your skin is monitoring temperature and pressure all over your body. "
     "All of this is happening automatically — you don't have to think about it! 🤖",
     "#e8f4fd", "#1565c0"),
    ("⚡", "Step 2: Nerves Carry the Signals",
     "Your body has a network of over 7 trillion nerve cells called NEURONS — "
     "like millions of tiny electrical wires running throughout your entire body! 🔌\n\n"
     "These neurons pass electrical signals from your sense organs toward your brain "
     "at speeds of up to 430 km per hour. If you stretched all your nerve fibres end to end, "
     "they would wrap around the Earth 2.5 times! 🌍",
     "#fff3e0", "#e65100"),
    ("🏠", "Step 3: Different Brain Areas",
     "Different areas of your brain specialise in different senses:\n\n"
     "- 👀 **Occipital lobe** (back of brain): Processes sight\n"
     "- 👂 **Temporal lobe** (sides of brain): Processes sound and some smell\n"
     "- ✋ **Parietal lobe** (top of brain): Processes touch and body position\n"
     "- 👃 **Olfactory bulb** (front, deep): Processes smell (directly, no relay!)\n"
     "- 🌐 **All areas together**: Work in parallel to create your experience!",
     "#f3e5f5", "#7b1fa2"),
    ("🎨", "Step 4: Brain Builds a Picture",
     "Your brain takes all the separate sense signals and combines them into "
     "one seamless experience of reality — what scientists call PERCEPTION. 🌅\n\n"
     "When you bite into an apple — the crunch (hearing), the sweetness (taste), "
     "the fruity aroma (smell), the firm texture (touch), and the shiny red colour (sight) "
     "all arrive at your brain at the same time and merge into: 'I am eating a delicious apple.' 🍎",
     "#e8f5e9", "#2e7d32"),
    ("🛡️", "Step 5: Brain Decides What to Do",
     "Once your brain understands what's happening, it decides how to respond!\n\n"
     "- 😊 See a friend → Brain sends 'smile and wave' signal\n"
     "- 🔥 Touch something hot → Brain sends 'PULL AWAY NOW!' signal\n"
     "- 🍕 Smell pizza → Brain sends 'feel hungry' signal\n"
     "- 🎵 Hear a favourite song → Brain sends 'feel happy' signal\n\n"
     "Your brain processes about **11 million bits** of information per second from your senses "
     "— but you're only consciously aware of about **40 bits!** Your brain does most of the work without telling you! 🤯",
     "#fce4ec", "#c62828"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Back", use_container_width=True, key="brain_prev"):
        st.session_state.brain_step = max(0, st.session_state.brain_step - 1)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="brain_next"):
        st.session_state.brain_step = min(len(brain_steps)-1, st.session_state.brain_step + 1)

idx   = st.session_state.brain_step
bstep = brain_steps[idx]
with col2:
    st.markdown(f"""
    <div style="background:{bstep[3]}; border-radius:20px; padding:2rem;
                text-align:center; border:3px solid {bstep[4]};
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="font-size:5rem; margin-bottom:0.5rem;">{bstep[0]}</div>
        <div style="font-size:1.25rem; font-weight:700; color:#2c3e50; margin-bottom:0.7rem;">
            {bstep[1]}
        </div>
        <div style="font-size:0.97rem; color:#444; line-height:1.75; text-align:left;">
            {bstep[2]}
        </div>
        <div style="margin-top:1.2rem; display:flex; justify-content:center; gap:0.4rem;">
            {"".join([
                f'<span style="font-size:1.2rem; opacity:{1 if i==idx else 0.25}; color:{bstep[4]}">●</span>'
                for i in range(len(brain_steps))
            ])}
        </div>
        <div style="font-size:0.82rem; color:#888; margin-top:0.5rem;">
            Step {idx+1} of {len(brain_steps)}
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — ANIMALS WITH SUPER SENSES
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🦸", "Animals With Super Senses!",
               "Some animals have senses far beyond anything humans can do — tap to explore! 🌍")

animal_senses = {
    "🐕 Dog": {
        "emoji": "🐕", "color": "#795548", "bg": "#efebe9",
        "tagline": "🏆 Super Smell Champion",
        "body": (
            "Dogs have an absolutely extraordinary sense of SMELL. 👃\n\n"
            "- 🔢 **Smell power**: A dog's sense of smell is **10,000 to 100,000 times** stronger than a human's\n"
            "- 🧬 **Nose design**: Dogs have up to 300 million smell receptors vs our 6 million\n"
            "- 🏥 **Medical dogs**: Specially trained dogs can smell cancer, diabetes crises, and seizures before they happen!\n"
            "- 💣 **Detection dogs**: Police dogs can sniff out drugs, explosives, and missing people from tiny scent traces days old\n"
            "- 🌡️ **Covid sniffing**: Dogs were trained to detect Covid-19 in humans with 94% accuracy just by smell! 🤯"
        )
    },
    "🦇 Bat": {
        "emoji": "🦇", "color": "#4527a0", "bg": "#ede7f6",
        "tagline": "🏆 Super Hearing — Echolocation!",
        "body": (
            "Bats navigate and hunt in complete darkness using an amazing hearing superpower called ECHOLOCATION. 👂\n\n"
            "- 🔊 **How it works**: Bats emit ultrasonic calls (too high-pitched for us to hear) up to 200 times per second\n"
            "- 📡 **Echo mapping**: The sound bounces off objects and returns as an echo — the bat's brain creates a detailed 3D map from the echoes!\n"
            "- 🎯 **Precision**: Bats can detect an obstacle as thin as a human hair in total darkness while flying at speed\n"
            "- 🐟 **Fishing bats**: Some bats can even detect a fish fin 1mm above a water surface using echolocation!\n"
            "- 🔬 **Inspired technology**: Echolocation inspired the invention of sonar used in submarines and ultrasound medical scans! 🏥"
        )
    },
    "🦅 Eagle": {
        "emoji": "🦅", "color": "#f57f17", "bg": "#fff8e1",
        "tagline": "🏆 Super Sight Champion",
        "body": (
            "Eagles have the sharpest eyes of any creature on Earth — their vision is extraordinary. 👀\n\n"
            "- 🔭 **Vision power**: Eagles can see **4–8 times further** than humans with perfect detail\n"
            "- 🐇 **Hunting precision**: A golden eagle can spot a rabbit from **3.2 kilometres away** — that's like seeing an ant from across a football pitch!\n"
            "- 🌈 **Colour vision**: Eagles see ultraviolet light that is invisible to humans — prey animals' urine glows in UV, making tracking easy! 💡\n"
            "- 👁️ **Two foveas**: Human eyes have one high-resolution focal point; eagles have TWO, allowing sharp vision both straight ahead and sideways\n"
            "- 🛡️ **Eye protection**: Eagles have a transparent third eyelid that protects their eye while diving at speed — built-in goggles! 🥽"
        )
    },
    "🐟 Shark": {
        "emoji": "🦈", "color": "#1565c0", "bg": "#e3f2fd",
        "tagline": "🏆 Sense of Electricity!",
        "body": (
            "Sharks possess a sense humans don't have at all — the ability to DETECT ELECTRICITY! ⚡\n\n"
            "- 🔌 **Electroreception**: Sharks have organs called AMPULLAE OF LORENZINI — jelly-filled pores around their snout that detect electrical fields\n"
            "- 💓 **Heartbeat detector**: Every living creature produces a tiny electrical field from muscle contractions. Sharks can detect the heartbeat of a fish buried under sand! 🏖️\n"
            "- 📏 **Range**: Can detect electrical fields as weak as one-billionth of a volt — equivalent to a AA battery connected between two points 1,600 km apart!\n"
            "- 🌍 **Navigation**: Sharks may also use Earth's magnetic field to navigate across entire oceans with pinpoint accuracy\n"
            "- 👃 **Smell too**: Sharks can also smell one drop of blood diluted in an Olympic swimming pool of water! 🩸"
        )
    },
    "🦉 Owl": {
        "emoji": "🦉", "color": "#33691e", "bg": "#f9fbe7",
        "tagline": "🏆 Super Night Vision + Hearing",
        "body": (
            "Owls are the ultimate night-time hunters — with two extraordinary senses perfectly tuned for darkness. 🌙\n\n"
            "- 👁️ **Night vision**: Owls' eyes are enormous relative to their skull — packed with rod cells for maximum light sensitivity. A barn owl can see a mouse by the light of a single candle from 500m away!\n"
            "- 🎯 **Asymmetric ears**: Owls have one ear higher than the other — allowing them to pinpoint a sound in THREE dimensions (up/down AND left/right)\n"
            "- 🍂 **Sound through snow**: A barn owl can hear and catch a mouse hidden under 30cm of snow, guided entirely by hearing\n"
            "- 🔇 **Silent wings**: Owls have special feathers with soft fringes that silence their wingbeats — prey never hears them coming! 🪶\n"
            "- 🌀 **Head rotation**: Can rotate head 270° because their eyes can't move — they need to turn their whole head to look sideways!"
        )
    },
    "🐙 Octopus": {
        "emoji": "🐙", "color": "#ad1457", "bg": "#fce4ec",
        "tagline": "🏆 Colour-Sensing Skin (While Colour-Blind!)",
        "body": (
            "The octopus has one of the most baffling sense mysteries in all of science! 🤯\n\n"
            "- 🎨 **Colour-blind but...**: Octopuses have only ONE type of colour receptor — they should be completely colour-blind, seeing only in black and white\n"
            "- 🌈 **Yet they match colours**: Despite this, they can change their skin to perfectly match coloured backgrounds — something scientists still can't fully explain!\n"
            "- 💡 **Current theory**: Their oddly-shaped pupils may allow them to distinguish colour using light intensity at different angles — 'seeing' colour with the shape of blur!\n"
            "- ✋ **Arm senses**: Each of an octopus's 8 arms has its own mini-nervous system and can taste, smell, and feel independently — like having 8 semi-independent brains!\n"
            "- 🛡️ **Camouflage speed**: Can change colour, pattern, and skin texture in under 200 milliseconds — faster than you can blink! 🫣"
        )
    },
}

sense_cols = st.columns(len(animal_senses))
for i, (aname, adata) in enumerate(animal_senses.items()):
    with sense_cols[i]:
        short = aname.split(" ")[1]
        if st.button(adata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"asense_{i}"):
            st.session_state.animal_sense_picked = aname

if st.session_state.animal_sense_picked and st.session_state.animal_sense_picked in animal_senses:
    aname = st.session_state.animal_sense_picked
    adata = animal_senses[aname]
    st.markdown(f"""
    <div style="background:{adata['bg']}; border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid {adata['color']}; margin-top:1rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.8rem;">
            <span style="font-size:3rem;">{adata['emoji']}</span>
            <div>
                <div style="font-size:1.35rem; font-weight:700; color:#2c3e50;">
                    {aname.split(' ', 1)[1]}
                </div>
                <div style="font-size:0.9rem; color:{adata['color']}; font-weight:700;">
                    {adata['tagline']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(adata["body"])
else:
    st.info("👆 Tap any animal above to discover its incredible superpower sense!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — LOOKING AFTER YOUR SENSES
# ═══════════════════════════════════════════════════════════════════════════════
section_header("💚", "Looking After Your Senses!",
               "Your senses are precious — here's how to keep them healthy! 🌟")

col1, col2 = st.columns(2, gap="large")
care_items = [
    ("👀", "Protect Your Eyes",
     "Never look directly at the Sun — even briefly, it can permanently damage your retina. "
     "Wear sunglasses in bright sunshine. Take screen breaks every 20 minutes — look at "
     "something 6 metres away for 20 seconds (the 20-20-20 rule). 🖥️",
     "#e3f2fd", "#1565c0"),
    ("👂", "Protect Your Ears",
     "Keep headphone volume below 60% — loud music can permanently destroy the tiny "
     "hair cells in your cochlea and they NEVER grow back! At concerts, wear ear protection. "
     "Never push anything (even cotton buds) inside your ear. 🎧⚠️",
     "#e8f5e9", "#2e7d32"),
    ("👃", "Keep Your Nose Healthy",
     "Breathe through your nose — it filters, warms, and moistens air before it reaches your lungs. "
     "Blow your nose gently (one nostril at a time). Strong chemical smells (like bleach) "
     "can damage smell receptors — ventilate rooms well. 🌬️",
     "#fff3e0", "#e65100"),
    ("👅", "Keep Your Tongue & Teeth Healthy",
     "Brush twice a day to keep your taste buds healthy — bacteria on your tongue dulls taste. "
     "Avoid very hot food that can burn taste buds. Very sweet food damages teeth and "
     "indirectly reduces your ability to taste a full range of flavours. 🦷",
     "#fce4ec", "#c62828"),
    ("✋", "Protect Your Skin",
     "Wear sunscreen to protect skin from UV rays which cause damage. Wear gloves when handling "
     "very hot or very cold things. Keep skin moisturised — dry, cracked skin loses sensitivity. "
     "Wash hands often to protect skin from harmful chemicals. 🧴",
     "#f3e5f5", "#8e24aa"),
    ("🥦", "Eat Well for All Senses",
     "Vitamin A (carrots, sweet potato) supports eye health. Zinc (nuts, seeds) supports smell. "
     "Omega-3 (fish, walnuts) protects nerve health for all senses. "
     "A colourful diet feeds your whole sensory system! 🌈🥕",
     "#e8f5e9", "#43a047"),
]
for i, (emoji, title, body, bg, border) in enumerate(care_items):
    col = col1 if i % 2 == 0 else col2
    with col:
        fun_card(emoji, title, body, bg, border)

think_bubble("Which of your five senses do you think you would find hardest to live without? Why? 💭")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Let's Test What You Know!",
               "6 sensational questions — answer them all then check your score! 🌟")

questions = [
    {
        "q":    "Q1 👀 — What part of the eye focuses light like a camera lens?",
        "opts": ["Pupil", "Retina", "Lens", "Cornea"],
        "ans":  "Lens",
        "explain": "The LENS bends and focuses light onto the retina at the back of your eye — just like a camera! 📸👀"
    },
    {
        "q":    "Q2 👂 — What do we call the thin skin inside your ear that vibrates with sound?",
        "opts": ["Cochlea", "Eardrum", "Anvil", "Stirrup"],
        "ans":  "Eardrum",
        "explain": "The EARDRUM vibrates when sound waves hit it — like a real drum! Those vibrations then travel deeper into your ear. 🥁"
    },
    {
        "q":    "Q3 👅 — About how many taste buds does a human have on their tongue?",
        "opts": ["100", "1,000", "10,000", "1,000,000"],
        "ans":  "10,000",
        "explain": "Adults have about 10,000 taste buds — and they are replaced with brand new ones every 10 days! 👅🔄"
    },
    {
        "q":    "Q4 👃 — What is the name of the amazing smell that rain makes on dry ground?",
        "opts": ["Geosmin", "Petrichor", "Chlorophyll", "Ozone"],
        "ans":  "Petrichor",
        "explain": "PETRICHOR is the beautiful earthy smell of rain on dry soil — caused by bacteria releasing chemicals when raindrops hit! 🌧️🌱"
    },
    {
        "q":    "Q5 🧠 — Which sense has the most DIRECT connection to your memory and emotions?",
        "opts": ["Sight", "Hearing", "Touch", "Smell"],
        "ans":  "Smell",
        "explain": "Smell is the only sense with a direct pathway to the brain's memory and emotion centres — that's why smells trigger such powerful memories! 👃💛"
    },
    {
        "q":    "Q6 🦇 — What is the name of the superpower bats use to 'see' in the dark?",
        "opts": ["Infrared Vision", "Echolocation", "Magnetoreception", "Electroreception"],
        "ans":  "Echolocation",
        "explain": "ECHOLOCATION! Bats send out sound waves and listen for the echoes to build a 3D map of everything around them — even in complete darkness! 🦇🔊"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"sense_q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="sense_quiz_submit"):
        st.session_state.quiz_submitted = True

if st.session_state.quiz_submitted:
    score = 0
    for i, q in enumerate(questions):
        ans = st.session_state.quiz_answers.get(i)
        if ans == q["ans"]:
            score += 1
            st.success(f"✅ **{q['q'].split('—')[1].strip()}** → Correct! 🎉 {q['explain']}")
        elif ans is None:
            st.warning(f"⚠️ **{q['q'].split('—')[1].strip()}** → You didn't answer this one!")
        else:
            st.error(f"❌ **{q['q'].split('—')[1].strip()}** → Not quite! "
                     f"The answer is **{q['ans']}**. {q['explain']}")

    badge_data = [
        (6, "🏆", "SENSORY SUPERSTAR!",       "#ffd700", "#fffde7"),
        (5, "🥇", "Brilliant Brain Scientist!", "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Sense Explorer!",      "#cd7f32", "#fff3e0"),
        (3, "🌟", "Good job, Sense Detective!", "#7b1fa2", "#f3e5f5"),
        (0, "✨", "Keep Exploring! Try Again!", "#1565c0", "#e3f2fd"),
    ]
    for threshold, icon, label, border, bg in badge_data:
        if score >= threshold:
            st.markdown(f"""
            <div style="background:{bg}; border:3px solid {border};
                        border-radius:20px; padding:1.5rem; text-align:center; margin-top:1rem;">
                <div style="font-size:4rem;">{icon}</div>
                <div style="font-size:1.5rem; font-weight:700; color:#2c3e50;">
                    You scored {score}/6!
                </div>
                <div style="font-size:1.1rem; color:{border}; font-weight:600;">{label}</div>
            </div>""", unsafe_allow_html=True)
            break

    if st.button("🔄 Try Again!", use_container_width=False, key="sense_quiz_reset"):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers   = {}
        st.rerun()

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Did We Learn Today?", "Your five senses — quick recap! 🎉")

summary_items = [
    ("👀", "Sight",   "Eyes see light · lens focuses · brain flips the image"),
    ("👂", "Hearing", "Ears catch sound waves · eardrum vibrates · cochlea converts"),
    ("👃", "Smell",   "400 receptors · links to memory · 1 trillion scents!"),
    ("👅", "Taste",   "10,000 taste buds · 5 tastes · 80% is actually smell!"),
    ("✋", "Touch",   "Whole skin · pressure, heat, pain, vibration, light touch"),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;
                    border-top:4px solid #9c27b0;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:1.5rem;
            background:linear-gradient(135deg,#1a0533,#4a148c,#880e4f,#1a0533);
            border-radius:20px; color:#fff;">
    <div style="font-size:2rem; margin-bottom:0.5rem;">
        ✨ Keep noticing the world around you, little scientist! ✨
    </div>
    <div style="color:#e1bee7; font-size:0.95rem;">
        Every sight, sound, smell, taste and touch is your amazing body telling you about the world!
    </div>
    <div style="margin-top:1rem; font-size:1.5rem; letter-spacing:0.6rem;">
        👀 👂 👃 👅 ✋ 🧠
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)


# Footer
st.caption("""© 2026 Science for Little Stars. All rights reserved.
Authored by <strong style="color:brown;">AMBREEN ABDUL RAHEEM</strong>
The Education Expert""", unsafe_allow_html=True)

