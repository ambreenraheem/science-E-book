import streamlit as st

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(page_title="Chapter 01 · Our Amazing Body", layout="wide", initial_sidebar_state="expanded")

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
    "show_skeleton_fact", "show_muscle_fact",
    "show_heart_fact",    "show_brain_fact",
    "show_lungs_fact",    "show_digestion_fact",
    "quiz_submitted",
]:
    if key not in st.session_state:
        st.session_state[key] = False

if "system_picked" not in st.session_state: st.session_state.system_picked = None
if "animal_picked" not in st.session_state: st.session_state.animal_picked = None
if "body_step"     not in st.session_state: st.session_state.body_step     = 0
if "quiz_answers"  not in st.session_state: st.session_state.quiz_answers  = {}

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
<div style="background:linear-gradient(135deg,#1a0a2e,#6a1b9a,#880e4f,#1a0a2e);
            border-radius:24px; padding:2.5rem 2rem; text-align:center;
            margin-bottom:1.5rem; overflow:hidden;">
    <div style="font-size:1rem; color:#ce93d8; letter-spacing:0.15em;
                text-transform:uppercase; margin-bottom:0.5rem;">
        Chapter 01 · Science for Little Stars
    </div>
    <h1 style="color:#ffffff; font-size:clamp(1.8rem,5vw,3rem);
               margin:0; text-shadow:0 2px 8px rgba(0,0,0,0.4);">
        🦴 Our Amazing Body! ❤️
    </h1>
    <p style="color:#e1bee7; font-size:1.05rem; margin:0.8rem 0 0;">
        You are carrying the most incredible machine ever built — right inside you!
        Let's explore every amazing system in your body!
    </p>
    <div style="font-size:2rem; margin-top:1rem; letter-spacing:0.5rem;">
        🦴 💪 ❤️ 🧠 🫁 🫀 🦷 👁️
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("📚 What will I learn today?", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ How your **skeleton** gives you shape and protects you
        - ✅ How your **muscles** make every movement happen
        - ✅ How your **heart** pumps blood around your whole body
        - ✅ How your **lungs** bring oxygen into your body
        """)
    with col2:
        st.markdown("""
        - ✅ How your **brain** controls absolutely everything
        - ✅ How your **digestive system** turns food into energy
        - ✅ How all your body **systems work together**
        - ✅ Amazing animal body comparisons + a quiz!
        """)

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — THE AMAZING HUMAN BODY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "Your Body — The Most Amazing Machine!",
               "More complex than any computer, stronger than any engine — and it is YOU! 🤩")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1], gap="large")
with col1:
    st.markdown("""
    Right now, without you thinking about it, your body is doing something
    **extraordinary**. Your heart is beating. Your lungs are breathing.
    Your brain is reading these words. Your stomach is digesting your last meal.
    Your bones are growing. Your skin is repairing tiny scratches. All at once! 🤯

    Your body is made of about **37 TRILLION cells** — tiny living building blocks
    too small to see! Each one has a job to do. Together they form **tissues**,
    tissues form **organs**, and organs work in teams called **body systems**.

    There are **11 major body systems** — and today we are going to explore
    the most important ones, one magnificent step at a time! 🚀
    """)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#f3e5f5,#fce4ec);
                border-radius:16px; padding:1.2rem 1.6rem; margin:0.8rem 0;
                border:2px solid #880e4f;">
        <div style="font-weight:700; color:#880e4f; font-size:1.05rem; margin-bottom:0.8rem;">
            🧬 Your Body By The Numbers — Right Now!
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.5rem;">
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🦴</div>
                <div style="font-weight:700; color:#6a1b9a;">206</div>
                <div style="font-size:0.8rem; color:#666;">Bones in an adult body</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">💪</div>
                <div style="font-weight:700; color:#c62828;">600+</div>
                <div style="font-size:0.8rem; color:#666;">Muscles in your body</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">❤️</div>
                <div style="font-weight:700; color:#ad1457;">100,000</div>
                <div style="font-size:0.8rem; color:#666;">Heartbeats every day</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🧠</div>
                <div style="font-weight:700; color:#1565c0;">86 billion</div>
                <div style="font-size:0.8rem; color:#666;">Brain nerve cells</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🩸</div>
                <div style="font-weight:700; color:#b71c1c;">96,000 km</div>
                <div style="font-size:0.8rem; color:#666;">Blood vessels in your body</div>
            </div>
            <div style="background:rgba(255,255,255,0.85); border-radius:10px; padding:0.6rem; text-align:center;">
                <div style="font-size:1.8rem;">🫁</div>
                <div style="font-weight:700; color:#2e7d32;">23,000</div>
                <div style="font-size:0.8rem; color:#666;">Breaths you take each day</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    think_bubble("Put your hand on your chest — can you feel your heart beating? Count how many beats in 10 seconds, then multiply by 6! ❤️")

with col2:
    fun_card("🧬", "Cells — Your Tiniest Building Blocks!",
             "Everything in your body is made of <strong>cells</strong> — "
             "the smallest living units! You have about 37 trillion of them. "
             "Laid end to end they would stretch 400 times around the Earth! "
             "Different cells do different jobs — muscle cells contract, "
             "nerve cells send signals, blood cells carry oxygen. 🔬",
             bg="#f3e5f5", border="#6a1b9a")
    fun_card("🏗️", "Cells → Tissues → Organs → Systems",
             "Cells of the same type group together to form <strong>tissues</strong> "
             "(like muscle tissue). Tissues combine to form <strong>organs</strong> "
             "(like your heart). Organs work together in <strong>systems</strong> "
             "(like the circulatory system). It is the most perfect organisation in nature! 🌟",
             bg="#fce4ec", border="#ad1457")
    fun_card("🔄", "Always Working — Even While You Sleep!",
             "Your body never takes a break — not even for a second! "
             "While you sleep, your heart pumps, your lungs breathe, "
             "your brain consolidates memories, your body repairs damage, "
             "and your bones grow! Sleep is not rest for your body — "
             "it is maintenance time! 😴🔧",
             bg="#e8f5e9", border="#2e7d32")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — SKELETON AND MUSCLES
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🦴", "The Skeleton and Muscles!",
               "Your body's frame and its engine — working together every second! 💪")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 🦴 Your Skeleton — The Living Framework")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Your **skeleton** is the amazing framework of **206 bones** that gives your body
    its shape, holds you upright, and protects your most important organs! 🏗️

    And here is the most surprising thing — **your bones are ALIVE**!
    They have blood vessels and nerves running through them,
    they grow, they repair themselves when broken, and they are
    constantly being rebuilt from the inside! 🌱

    **What your skeleton does — step by step:**
    """)
    for step, icon, title, desc in [
        (1, "🏗️", "Gives you shape",         "Without your skeleton, you would be a soft blob on the floor! Your bones give your body its shape — your spine keeps you upright, your skull makes your face! 😄"),
        (2, "🛡️", "Protects vital organs",    "Your SKULL is a hard helmet protecting your brain. Your RIB CAGE is a bony cage protecting your heart and lungs. Your SPINE protects the spinal cord!"),
        (3, "💪", "Enables movement",         "Bones work with muscles like levers! When a muscle pulls on a bone, the bone moves — every step, kick, and wave of your hand is bones and muscles working together."),
        (4, "🩸", "Makes blood cells",         "Inside your larger bones is soft BONE MARROW — a factory that makes millions of new red and white blood cells every single second! 🏭"),
        (5, "🧪", "Stores minerals",           "Your bones store important minerals — especially CALCIUM and PHOSPHORUS — that your body uses for muscle contractions, nerve signals, and building more bone. 🥛"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#ede7f6;">
            <span style="background:#6a1b9a; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#6a1b9a;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("##### 🦴 Key Bones and What They Do")
    bones = [
        ("💀", "Skull",     "#ede7f6", "#6a1b9a", "22 bones fused together — a perfect helmet protecting your 1.4 kg brain! 🧠"),
        ("🦷", "Jaw",       "#f3e5f5", "#7b1fa2", "The ONLY moveable bone in your skull — opens and closes 2,000 times a day while you eat and talk! 😮"),
        ("🔗", "Spine",     "#e8eaf6", "#3949ab", "33 stacked vertebrae — flexible enough to bend and twist, strong enough to support your whole weight! 🤸"),
        ("🫀", "Ribs",      "#fce4ec", "#c62828", "12 pairs of ribs form a bony cage — protecting your heart and lungs while still allowing your chest to expand when you breathe! 🫁"),
        ("🦵", "Femur",     "#fff8e1", "#f57f17", "The thigh bone — the LONGEST and STRONGEST bone in your body! It can bear up to 30 times your body weight! 💪"),
        ("👂", "Stirrup",   "#e0f2f1", "#00695c", "The SMALLEST bone — tiny stirrup bone in your ear (just 3mm!) — yet essential for hearing every sound you have ever heard! 🔊"),
    ]
    for icon, name, bg, color, desc in bones:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:10px; padding:0.5rem 0.8rem;
                    margin-bottom:0.3rem; border-left:3px solid {color};
                    display:flex; align-items:flex-start; gap:0.5rem;">
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:{color};">{name}:</strong>
            <span style="font-size:0.85rem; color:#555;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    think_bubble("Babies are born with about 270 bones — but adults only have 206! What do you think happens to the extra bones? 🤔")

with col2:
    st.markdown("##### 🦴 Skeleton Facts")
    for icon, label, fact in [
        ("👶", "Baby bones",      "Babies are born with about 270 soft bones — many are still cartilage! As you grow, bones harden and some fuse together, leaving adults with just 206. 🧒"),
        ("🥛", "Calcium power",   "Drinking milk and eating leafy greens gives your bones calcium — the mineral that makes them hard and strong! Without calcium, bones become soft and brittle. 🥬"),
        ("🔧", "Self-repairing",  "When you break a bone, your body immediately starts repairing it! Special cells called OSTEOBLASTS lay down new bone tissue — most fractures heal completely in 6–8 weeks! 💪"),
        ("🌙", "Taller at night", "You are actually TALLER in the morning than at night! The cartilage between your spine vertebrae compresses during the day under gravity — and re-expands overnight! 😲"),
        ("🦴", "Strongest bone",  "The FEMUR (thigh bone) is so strong it can withstand pressure of 1,700 kg per square centimetre — stronger than reinforced concrete! 🏗️"),
        ("🔬", "Bone is living",  "Bone is constantly being broken down and rebuilt — your entire skeleton is completely replaced every 10 years! You literally have a new skeleton every decade! 🌟"),
    ]:
        fact_row(icon, label, fact, "#ede7f6", "#6a1b9a")

    if st.button("🦴 Reveal a Skeleton Secret!", use_container_width=True, key="skel_btn"):
        st.session_state.show_skeleton_fact = not st.session_state.show_skeleton_fact
    if st.session_state.show_skeleton_fact:
        st.success("🎉 The smallest bone in your entire body is the STIRRUP inside your ear — "
                   "just 3mm long — smaller than a grain of rice! 🍚 "
                   "Yet without it, you could not hear a single sound. "
                   "The largest bone is the FEMUR (thigh bone) — up to 50cm long in tall adults! "
                   "That is a size difference of over 150 times! 😱🦴")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

st.markdown("### 💪 Your Muscles — The Body's Engine")
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    You have over **600 muscles** in your body — and they are responsible for
    every single movement you make, from blinking to running a marathon! 🏃

    Muscles work by **contracting** (getting shorter and fatter) and
    **relaxing** (going back to normal length). They can ONLY pull — never push!
    That is why muscles always work in pairs. 🔄

    **How muscles work — step by step:**
    """)
    for step, icon, title, desc in [
        (1, "🧠", "Brain sends signal",      "Your brain sends an electrical signal down a nerve to the muscle — like sending a text message! The signal arrives in milliseconds. ⚡"),
        (2, "⚗️", "Chemical reaction",       "The nerve signal triggers a chemical reaction inside the muscle fibres — calcium floods in and tiny protein filaments (actin and myosin) grab each other!"),
        (3, "💪", "Muscle contracts",        "The protein filaments slide together, pulling the ends of the muscle toward the middle — the whole muscle gets shorter and fatter (contracts)! 💥"),
        (4, "🦴", "Bone is pulled",          "The muscle is attached to two bones by tough TENDONS. When the muscle contracts, it pulls the bone and the joint moves — you move! 🦵"),
        (5, "🔄", "Muscle pair relaxes",     "When the muscle relaxes, the opposing muscle on the other side of the joint contracts to move the bone back — muscles ALWAYS work in opposing pairs! 🤝"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#ffebee;">
            <span style="background:#c62828; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#c62828;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    st.markdown("##### 💪 The Three Types of Muscle")
    mtypes = [
        ("🏃", "Skeletal Muscle",  "#ffebee", "#c62828",
         "Muscles attached to bones — you control these VOLUNTARILY. Running, writing, smiling! 😄 They look striped under a microscope and tire quickly."),
        ("❤️", "Cardiac Muscle",   "#fce4ec", "#ad1457",
         "Only in your HEART — works INVOLUNTARILY (you cannot control it). Never tires — beats 100,000 times a day for your entire life without stopping! 💓"),
        ("🍎", "Smooth Muscle",    "#f3e5f5", "#7b1fa2",
         "Lines your organs — stomach, intestines, blood vessels. Works INVOLUNTARILY, slowly and rhythmically. Pushes food through your digestive system! 🔄"),
    ]
    for icon, name, bg, color, desc in mtypes:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:12px; padding:0.6rem 1rem;
                    border-left:4px solid {color}; margin-bottom:0.4rem;">
            <span style="font-size:1.3rem;">{icon}</span>
            <strong style="color:{color};"> {name}:</strong>
            <span style="font-size:0.87rem; color:#555;"> {desc}</span>
        </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("##### 💪 Muscle Facts")
    for icon, label, fact in [
        ("😊", "Smiling muscles",   "It takes about 12 muscles to smile and up to 11 to frown — so smiling is actually MORE efficient! Keep smiling! 😄"),
        ("👅", "Tongue muscles",    "Your tongue is made of 8 muscles woven together — it is the only muscle in your body attached at only one end! 🗣️"),
        ("👁️", "Eye muscles",       "The muscles moving your eyeballs are the busiest in your body — they make over 100,000 movements every day just tracking what you see! 👀"),
        ("🌡️", "Heat makers",       "Muscles generate about 85% of your body heat! That is why you shiver when cold — muscles rapidly contracting generate warmth! 🔥"),
        ("📈", "Gets stronger",     "The more you use a muscle, the bigger and stronger it grows — exercise causes tiny tears in muscle fibres which repair thicker and stronger! 🏋️"),
        ("😴", "Sleep and repair",  "Muscles repair and grow during SLEEP — not during exercise! Growth hormone is released during deep sleep, building stronger muscles overnight. 💤"),
    ]:
        fact_row(icon, label, fact, "#ffebee", "#c62828")

    if st.button("💪 Reveal a Muscle Secret!", use_container_width=True, key="muscle_btn"):
        st.session_state.show_muscle_fact = not st.session_state.show_muscle_fact
    if st.session_state.show_muscle_fact:
        st.success("🎉 The strongest muscle in your body (relative to its size) is the MASSETER — "
                   "your jaw muscle! It can close your teeth with a force of up to 91 kg — "
                   "enough to crack a walnut! 🦷💪 "
                   "The largest muscle is the GLUTEUS MAXIMUS (your bottom!) "
                   "and the longest is the SARTORIUS, which runs diagonally across your thigh. 🦵")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — HEART AND BLOOD (Step-through explorer)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("❤️", "Your Heart — The Incredible Pump!",
               "A fist-sized muscle that beats 100,000 times a day — for your entire life! 💓")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Your **heart** is the most hardworking organ in your whole body —
    it never stops, not even for a second, from before you are born
    until the very last moment of your life! 💓

    **How your heart pumps blood — step by step:**
    """)
    for step, icon, title, desc in [
        (1, "🫁", "Blood arrives from the lungs",  "Oxygen-rich red blood returns from your lungs into the LEFT side of your heart, ready to be pumped around the body! 🔴"),
        (2, "💥", "Left ventricle contracts",       "The powerful LEFT VENTRICLE (lower left chamber) squeezes hard — pumping the oxygen-rich blood out through the AORTA, the body's largest artery! 🚀"),
        (3, "🌍", "Blood travels the whole body",  "The blood races through 96,000 km of blood vessels — delivering oxygen and nutrients to every single cell in your body. A complete circuit in just 60 seconds! ⏱️"),
        (4, "🔵", "Used blood returns",            "After delivering its oxygen, the dark blue-red blood returns to the RIGHT side of the heart through large veins called the VENA CAVA. 🔵"),
        (5, "🫁", "Right side sends to lungs",     "The RIGHT VENTRICLE pumps the used blood to the LUNGS — where it picks up fresh oxygen and releases carbon dioxide. Then the whole cycle starts again! 🔄"),
    ]:
        st.markdown(f"""
        <div style="display:flex; align-items:flex-start; gap:0.7rem;
                    padding:0.55rem 0.8rem; border-radius:10px; margin-bottom:0.4rem;
                    background:#fce4ec;">
            <span style="background:#ad1457; color:#fff; border-radius:50%;
                         width:24px; height:24px; display:flex; align-items:center;
                         justify-content:center; font-weight:700; font-size:0.8rem;
                         flex-shrink:0; margin-top:2px;">{step}</span>
            <span style="font-size:1.2rem; flex-shrink:0;">{icon}</span>
            <div><strong style="color:#ad1457;">{title}:</strong>
            <span style="font-size:0.93rem; color:#444;"> {desc}</span></div>
        </div>""", unsafe_allow_html=True)

    fun_card("🩸", "The Blood — What is in It?",
             "Blood is not just one thing — it has four parts! "
             "<strong>Red blood cells</strong> carry oxygen (and make blood red!). "
             "<strong>White blood cells</strong> fight germs and infections like tiny soldiers! 🛡️ "
             "<strong>Platelets</strong> clot to seal cuts and stop bleeding. "
             "<strong>Plasma</strong> is the yellow liquid carrying everything else — nutrients, hormones, waste. 🌊",
             bg="#fce4ec", border="#ad1457")

    think_bubble("After exercise, why does your heart beat faster? What is your body trying to do? 🏃❤️")

with col2:
    st.markdown("##### ❤️ Heart and Blood Facts")
    for icon, label, fact in [
        ("👊", "Size of your fist",  "Your heart is roughly the same size as your closed fist — and it weighs only about 300 grams! Yet it pumps 5 litres of blood every minute! 💪"),
        ("🔢", "Lifetime beats",     "Your heart beats about 100,000 times per day — that is 2.5 billion beats in a 70-year lifetime! An extraordinary non-stop engine! 🏭"),
        ("🌍", "Blood vessels",      "Your body contains about 96,000 km of blood vessels — enough to wrap around the entire Earth more than twice! 🌎"),
        ("🩺", "Heart rate changes", "A resting child's heart beats 70–100 times per minute. During hard exercise it can reach 200 beats per minute — pumping 3x more blood! 🏃"),
        ("💉", "Blood types",        "Everyone has a blood type — A, B, AB, or O — plus a Rhesus factor (+ or -). Blood types must match for safe transfusions during surgery. 🏥"),
        ("🐋", "Whale heart",        "A blue whale's heart is the size of a small car and beats only 4–8 times per minute! You could hear it thumping from 3 km away underwater! 🐳"),
    ]:
        fact_row(icon, label, fact, "#fce4ec", "#ad1457")

    if st.button("❤️ Reveal a Heart Secret!", use_container_width=True, key="heart_btn"):
        st.session_state.show_heart_fact = not st.session_state.show_heart_fact
    if st.session_state.show_heart_fact:
        st.success("🎉 Your heart actually has its OWN electrical system! "
                   "A tiny cluster of cells called the SINOATRIAL NODE generates "
                   "the electrical signal that makes your heart beat — all by itself, "
                   "with no instructions from your brain! "
                   "Even if a heart is removed from the body and given nutrients, "
                   "it will keep beating on its own! 💓⚡")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — LUNGS AND BREATHING
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🫁", "Your Lungs — Breathing Life Into You!",
               "Two spongy miracles that bring oxygen into your body 23,000 times a day! 💨")

col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown("""
    Your **lungs** are two spongy, pinkish-grey organs sitting inside your rib cage,
    one on each side of your heart. Together they are responsible for the most
    important exchange in your body — swapping oxygen for carbon dioxide! 🔄

    **How your lungs work — step by step:**
    """)
    for step, icon, title, desc in [
        (1, "🌬️", "Diaphragm pulls down",     "A dome-shaped muscle below your lungs (the DIAPHRAGM) flattens and pulls down — this creates more space and lower pressure, so air rushes IN. This is breathing in! 📥"),
        (2, "🌳", "Air travels down trachea",  "Air flows down your TRACHEA (windpipe), which splits into two BRONCHI — one for each lung — then into thousands of smaller tubes called BRONCHIOLES!"),
        (3, "🫧", "Reaches the alveoli",       "Each bronchiole ends in tiny air sacs called ALVEOLI — you have about 480 million of them! Each one is surrounded by a network of tiny blood vessels."),
        (4, "🔄", "The oxygen swap",           "Oxygen from the air passes through the thin alveoli walls into the blood. Carbon dioxide (waste gas) passes from the blood back into the alveoli. 🌬️"),
        (5, "💨", "Diaphragm relaxes",         "The diaphragm relaxes and springs back up — the lungs compress, pressure rises, and the CO₂-rich air rushes OUT. This is breathing out! 📤"),
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

    think_bubble("Take a deep breath right now — can you feel your ribs move outward and your tummy push forward? That is your diaphragm working! 🫁")

with col2:
    st.markdown("##### 🫁 Lung and Breathing Facts")
    for icon, label, fact in [
        ("📐", "Surface area",     "If you unfolded all your alveoli flat, their total surface area would be about 70 square metres — the size of a tennis court! All packed into your chest! 🎾"),
        ("🌬️", "Breath amount",    "You breathe in about 500 ml of air per breath — and take around 23,000 breaths per day. That is over 8 million breaths per year! 😤"),
        ("💨", "Sneeze speed",     "A sneeze expels air at up to 160 km/h — faster than most cars on a motorway! Your body fires out germs at tremendous speed to clear your airway! 🤧"),
        ("🏊", "Lung capacity",    "Your lungs can hold up to 6 litres of air at maximum capacity — but a normal resting breath only uses about 0.5 litres! Most of your lung capacity is in reserve. 💪"),
        ("🚭", "Smoking damage",   "Cigarette smoke destroys the delicate alveoli walls — permanently reducing the lung's ability to absorb oxygen. The damage cannot be reversed. ⚠️"),
        ("🐋", "Whale breath",     "Blue whales breathe through a blowhole on top of their head — and can exchange 90% of their lung air in a single breath (humans only manage 15%)! 🌊"),
    ]:
        fact_row(icon, label, fact, "#e8f5e9", "#2e7d32")

    if st.button("🫁 Reveal a Lung Secret!", use_container_width=True, key="lungs_btn"):
        st.session_state.show_lungs_fact = not st.session_state.show_lungs_fact
    if st.session_state.show_lungs_fact:
        st.success("🎉 Your LEFT lung is slightly SMALLER than your right lung — "
                   "because your heart sits slightly to the left and takes up space! "
                   "The left lung has 2 lobes and the right lung has 3 lobes. "
                   "Together they weigh about 1.3 kg — "
                   "and they are the only organs in your body that can float on water! 🌊🫁")

    fun_card("🤧", "Hiccups, Sneezes, and Yawns!",
             "These are all special breathing events! "
             "A <strong>hiccup</strong> is a sudden diaphragm spasm that snaps your vocal cords shut — HIC! 😄 "
             "A <strong>sneeze</strong> clears irritants from your airway at 160 km/h. "
             "A <strong>yawn</strong> draws in extra oxygen when your brain detects low oxygen levels — "
             "though scientists still debate exactly why we yawn! 🧠",
             bg="#e8f5e9", border="#2e7d32")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — THE BRAIN (Step-through explorer)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧠", "Your Brain — The Most Complex Object in the Universe!",
               "Step through the incredible regions of your brain! 🌟")

brain_steps = [
    ("🧠", "What is Your Brain?",
     "Your **brain** is the command centre for everything you are — every thought, every feeling, "
     "every movement, every memory! 🌟\n\n"
     "It weighs about **1.4 kg** — roughly the weight of a large grapefruit. "
     "It contains **86 billion neurons** (nerve cells) connected by **100 trillion synapses** (connections). "
     "The number of possible connections in your brain is greater than the number of stars in the observable universe! 🌌\n\n"
     "It uses about **20% of all your body's energy** — even though it is only 2% of your body weight. "
     "Your brain needs a constant supply of oxygen and glucose to function — "
     "cut off blood flow for just 4 minutes and permanent damage begins. 💉",
     "#f3e5f5", "#6a1b9a"),
    ("🎨", "The Cerebrum — Thinking, Learning, Feeling",
     "The **CEREBRUM** is the largest part — the big wrinkly outer layer you picture when you think of a brain! 🌊\n\n"
     "It is divided into two HEMISPHERES (halves) and four LOBES, each with specialised jobs:\n\n"
     "- 🎨 **Frontal lobe** (front): Thinking, planning, personality, decision-making, speaking! This is what makes you YOU.\n"
     "- 👁️ **Occipital lobe** (back): Processes everything you see — colour, shape, motion, faces.\n"
     "- ✋ **Parietal lobe** (top): Processes touch, pain, temperature, and body position.\n"
     "- 👂 **Temporal lobe** (sides): Processes sound, language, and stores long-term memories.\n\n"
     "The surface of the cerebrum is deeply wrinkled — those wrinkles dramatically increase its surface area, "
     "packing more brain cells into a small space! 🧩",
     "#e8eaf6", "#3949ab"),
    ("⚖️", "The Cerebellum — Balance and Coordination",
     "The **CEREBELLUM** sits at the back and bottom of your brain — it looks like a small crinkled ball! 🎱\n\n"
     "Its job is **coordination, balance, and fine motor control** — making sure all your movements are smooth and precise:\n\n"
     "- 🚲 **Riding a bike**: The cerebellum coordinates the hundreds of tiny muscle adjustments that keep you balanced!\n"
     "- ✏️ **Neat handwriting**: Every letter you write requires the cerebellum to precisely control your hand muscles.\n"
     "- 🎵 **Playing an instrument**: Musicians have a notably larger cerebellum — years of practice physically grow it!\n"
     "- 🏃 **Running without falling**: Every step adjusts automatically through cerebellar feedback loops — you do not think about it! 🔄\n\n"
     "The cerebellum contains MORE neurons than the rest of the brain combined — about 69 billion! 🤯",
     "#e0f2f1", "#00695c"),
    ("💓", "The Brain Stem — Life's Control Panel",
     "The **BRAIN STEM** connects your brain to your spinal cord — and controls the things "
     "that keep you alive without you even thinking about them! 🌟\n\n"
     "- 💓 **Heart rate**: Your brain stem controls your heartbeat — speeding it up when you exercise, slowing it during sleep.\n"
     "- 🫁 **Breathing**: Controls the automatic rhythm of breathing — you do not have to remember to breathe! 😤\n"
     "- 😴 **Sleep and wake cycles**: Regulates when you feel sleepy and when you wake up — your internal body clock! ⏰\n"
     "- 🤢 **Vomiting reflex**: The brain stem triggers vomiting to expel harmful substances — an ancient protection system!\n"
     "- 👀 **Eye movements**: Controls automatic eye movements — like keeping your eyes focused as you move your head.\n\n"
     "The brain stem is the most ancient part — similar brain stems exist in fish, reptiles, and birds. "
     "It controls life's most basic functions that evolution has preserved for 500 million years! 🦎",
     "#fff8e1", "#f57f17"),
    ("💾", "Memory — How Your Brain Remembers",
     "Memory is one of the most amazing things your brain does — storing your entire life experience! 📖\n\n"
     "**Two main types of memory:**\n\n"
     "- ⚡ **Short-term (working) memory**: Holds about 7 items for about 20 seconds — like remembering a phone number just long enough to dial it! It is like a mental notepad. 📝\n"
     "- 💾 **Long-term memory**: Stores information for years — or a lifetime! Divided into memories for facts (semantic), events (episodic), and skills like riding a bike (procedural).\n\n"
     "**How memories form:** When you learn something new, neurons form new connections (synapses). "
     "Repeat it enough — SLEEP on it — and those connections strengthen permanently. "
     "This is why sleep after studying is so important! 😴\n\n"
     "The HIPPOCAMPUS (deep inside the brain) is the memory's gateway — it converts short-term to long-term memories! 🔄",
     "#fce4ec", "#ad1457"),
]

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("◀️ Back", use_container_width=True, key="brain_prev"):
        st.session_state.body_step = max(0, st.session_state.body_step - 1)
with col3:
    if st.button("Next ▶️", use_container_width=True, key="brain_next"):
        st.session_state.body_step = min(len(brain_steps)-1, st.session_state.body_step + 1)

idx   = st.session_state.body_step
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
            Brain Region {idx+1} of {len(brain_steps)}
        </div>
    </div>""", unsafe_allow_html=True)

if st.button("🧠 Reveal a Brain Secret!", use_container_width=False, key="brain_btn"):
    st.session_state.show_brain_fact = not st.session_state.show_brain_fact
if st.session_state.show_brain_fact:
    st.success("🎉 Your brain cannot feel pain! "
               "It has no pain receptors — so brain surgery can be performed "
               "while the patient is AWAKE and talking to the surgeon! "
               "This helps surgeons avoid damaging areas controlling speech or movement. "
               "The skull and surrounding membranes DO feel pain — "
               "but the brain tissue itself feels absolutely nothing! 🤯🧠")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — BODY SYSTEMS EXPLORER (Topic selector)
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🔬", "Explore All Your Body Systems!",
               "Tap each system to discover everything about how it keeps you alive! 🌟")

body_systems = {
    "🦷 Digestive": {
        "emoji": "🍎", "color": "#e65100", "bg": "#fff3e0",
        "tagline": "🍎 Turning food into fuel — a 9-metre journey!",
        "body": (
            "Your digestive system breaks food down into tiny nutrients your body can use — a remarkable 9-metre-long processing line! 🏭\n\n"
            "- 👄 **Mouth (0–10 seconds)**: Teeth chew food into smaller pieces (mechanical digestion) while SALIVA starts breaking down starch chemically. 32 adult teeth, each shaped for a different job! 🦷\n"
            "- 🍝 **Oesophagus (10 seconds)**: Muscles squeeze food down a 25cm tube to your stomach — so strong you could swallow food upside down! The process is called PERISTALSIS. 🌊\n"
            "- 🫙 **Stomach (2–4 hours)**: A muscular bag that churns food and drenches it in HYDROCHLORIC ACID (pH 2!) — strong enough to dissolve metal! Kills germs and breaks protein. 🧪\n"
            "- 🌀 **Small intestine (4–6 hours)**: 6 metres of tightly coiled tube where nutrients are absorbed into the blood. The inner wall has millions of tiny finger-like VILLI to maximise absorption! 🌿\n"
            "- 💧 **Large intestine (10–59 hours)**: Absorbs water and compacts waste. Hosts trillions of helpful bacteria — your GUT MICROBIOME — which help immunity and mood! 🦠\n"
            "- ⏱️ **Total journey**: From mouth to exit — about 24–72 hours for a complete digestive cycle! 🕐"
        )
    },
    "🛡️ Immune": {
        "emoji": "🛡️", "color": "#1565c0", "bg": "#e3f2fd",
        "tagline": "🛡️ Your personal army of billions!",
        "body": (
            "Your immune system is a vast biological army constantly patrolling your body for invaders! 🔬\n\n"
            "- 🛡️ **First line — skin**: Your skin is your first and most important defence — an unbroken barrier that keeps most germs out entirely. Even the acid in your stomach and the hairs in your nose are first-line defences! 💪\n"
            "- 🤧 **Second line — inflammation**: When germs get through, the body triggers inflammation — flooding the area with blood and immune cells. This is why injuries get red, warm, and swollen! 🔴\n"
            "- 🏹 **White blood cells**: These are your soldiers! NEUTROPHILS engulf and destroy bacteria. LYMPHOCYTES produce ANTIBODIES — custom-built protein weapons designed for each specific germ! 🎯\n"
            "- 🧠 **Immune memory**: Once your immune system defeats a germ, it keeps a memory of it — so if the same germ attacks again, it is destroyed before you even feel ill! This is how VACCINES work! 💉\n"
            "- 🌡️ **Fever**: A high temperature is your immune system's weapon — most germs cannot survive above 38°C, so your body deliberately raises its temperature to kill them! 🔥\n"
            "- 🦠 **Gut microbiome**: Trillions of helpful bacteria in your intestines train and support your immune system — another reason a healthy diet matters! 🥗"
        )
    },
    "🦷 Teeth": {
        "emoji": "🦷", "color": "#546e7a", "bg": "#eceff1",
        "tagline": "🦷 Your toughest body parts!",
        "body": (
            "Your teeth are the hardest structures in your entire body — and they are perfectly engineered tools! ⚙️\n\n"
            "- 🔢 **Two sets**: You get BABY TEETH (20 of them) starting at 6 months, then adult teeth (32 including wisdom teeth) replacing them from age 6 onwards. You only get two sets — look after the second! 😬\n"
            "- 🔪 **Incisors (8)**: The flat-edged front teeth — perfect for biting and cutting food. Like tiny chisels! ✂️\n"
            "- 🐶 **Canines (4)**: Pointed teeth for tearing food — much longer in carnivores like dogs and cats! 🐺\n"
            "- 🪨 **Molars (20)**: The large, flat back teeth for grinding food into paste — generating enormous force! 💪\n"
            "- 💎 **Enamel**: The outer coating of your tooth is TOOTH ENAMEL — the hardest substance your body produces! Even harder than bone. But it cannot repair itself if damaged — brush twice a day! 🪥\n"
            "- 🦠 **Tooth decay**: Bacteria in your mouth feed on sugar and produce acid — this acid dissolves enamel, creating cavities. Fluoride toothpaste strengthens enamel against this attack! 🛡️"
        )
    },
    "🌡️ Skin": {
        "emoji": "🌡️", "color": "#795548", "bg": "#efebe9",
        "tagline": "🌡️ Your largest organ — all 2 square metres of it!",
        "body": (
            "Your skin is your largest organ — it covers about 2 square metres and performs extraordinary jobs! 🌟\n\n"
            "- 🛡️ **Protection**: Skin is a waterproof, flexible armour that keeps germs, chemicals, and UV radiation out — and keeps your internal fluids in. 💧\n"
            "- 🌡️ **Temperature control**: When hot, blood vessels near the skin surface widen and you sweat — water evaporation cools you. When cold, vessels narrow and you shiver (muscle heat)! ❄️\n"
            "- 🔬 **Three layers**: EPIDERMIS (outer — renews every 2–4 weeks), DERMIS (middle — hair follicles, sweat glands, nerves), HYPODERMIS (deep — fat insulation and cushioning). 🍰\n"
            "- ☀️ **Vitamin D factory**: Sunlight on skin triggers production of VITAMIN D — essential for strong bones and a healthy immune system. 15 minutes of sunshine a day is enough! 🌞\n"
            "- 🔵 **Melanin and colour**: Skin colour comes from MELANIN — a protective pigment. More sun exposure = more melanin = darker skin = better UV protection. All skin colours are equally beautiful! 🌈\n"
            "- 🔄 **Constant renewal**: You shed about 30,000 skin cells every hour — and completely replace your outer skin layer every 2–4 weeks! Much of the dust in your home is shed skin. 😱"
        )
    },
    "👁️ Eyes": {
        "emoji": "👁️", "color": "#1e88e5", "bg": "#e3f2fd",
        "tagline": "👁️ 130 million light sensors in each eye!",
        "body": (
            "Your eyes are among the most sophisticated optical instruments ever made — and you have two of them! 🔬\n\n"
            "- 🌈 **Iris and pupil**: The coloured IRIS controls the size of your PUPIL — widening in dim light to let more light in, narrowing in bright light to protect your retina. 🔆\n"
            "- 🔍 **Lens and focus**: A flexible LENS bends light to focus it precisely on the RETINA at the back of your eye. Muscles change its shape to focus on near and far objects — like a camera autofocus! 📸\n"
            "- 🌟 **130 million receptors**: Your RETINA contains about 120 million ROD cells (detect light and dark in dim conditions) and 6–7 million CONE cells (detect colour in bright light)! 🎨\n"
            "- 🙃 **Upside-down image**: Your eye actually projects an INVERTED (upside-down) image onto the retina — your brain automatically flips it the right way up! 🔄\n"
            "- 😉 **Blinking**: You blink about 15–20 times per minute — each blink cleans, lubricates, and protects your cornea in 0.1 seconds. That is over 10,000 blinks a day! 👁️\n"
            "- 🌈 **Colour blindness**: About 8% of males and 0.5% of females have colour blindness — usually difficulty distinguishing red and green. The world still looks beautiful — just differently! 💚"
        )
    },
    "🦴 Growth": {
        "emoji": "📏", "color": "#2e7d32", "bg": "#e8f5e9",
        "tagline": "📏 From tiny baby to tall adult — how you grow!",
        "body": (
            "Growth is one of the most remarkable things your body does — and it happens mainly while you sleep! 💤\n\n"
            "- 🌱 **Growth plates**: Bones grow from special areas near their ends called GROWTH PLATES — zones of soft cartilage that gradually turn to bone as you grow. Growth plates close around age 18. 🦴\n"
            "- 💤 **Growth hormone**: GROWTH HORMONE is released mainly during deep sleep — this is why children NEED 9–11 hours of sleep per night! Staying up late literally slows your growth! 😴\n"
            "- 🍎 **Food for growth**: Protein (meat, eggs, beans) builds muscle and tissue. Calcium (milk, cheese, broccoli) builds bones. Vitamins and minerals (fruit, vegetables) keep all systems running! 🥦\n"
            "- 📈 **Growth spurts**: Children do not grow at a steady rate — they have GROWTH SPURTS, usually around ages 2, 4–5, and puberty (10–14). You can grow 10cm in a single year during a spurt! 🚀\n"
            "- 🌙 **Taller in the morning**: You really are taller when you wake up! The cartilage between your spine vertebrae compresses during the day under gravity — and re-expands overnight. 📏\n"
            "- 👶 **From birth**: You were born at about 50cm long. By adulthood, you will be about 3.5 times that height — most dramatic growth happens in the first two years of life! 🤱"
        )
    },
}

s_cols = st.columns(len(body_systems))
for i, (sname, sdata) in enumerate(body_systems.items()):
    with s_cols[i]:
        short = sname.split(" ", 1)[1]
        if st.button(sdata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"sys_{i}"):
            st.session_state.system_picked = sname

if st.session_state.system_picked and st.session_state.system_picked in body_systems:
    sname = st.session_state.system_picked
    sdata = body_systems[sname]
    st.markdown(f"""
    <div style="background:{sdata['bg']}; border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid {sdata['color']}; margin-top:1rem;
                box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <div style="display:flex; align-items:center; gap:1rem; margin-bottom:0.8rem;">
            <span style="font-size:3rem;">{sdata['emoji']}</span>
            <div>
                <div style="font-size:1.35rem; font-weight:700; color:#2c3e50;">
                    {sname.split(' ', 1)[1]}
                </div>
                <div style="font-size:0.9rem; color:{sdata['color']}; font-weight:700;">
                    {sdata['tagline']}
                </div>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    st.markdown(sdata["body"])
else:
    st.info("👆 Tap any body system above to discover everything about it!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — AMAZING ANIMAL BODIES
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🦸", "Amazing Animal Bodies vs Yours!",
               "Compare your incredible body to some of nature's most extraordinary creatures! 🌍")

animal_bodies = {
    "🦒 Giraffe": {
        "emoji": "🦒", "color": "#e65100", "bg": "#fff3e0",
        "tagline": "🫀 The most extreme heart in the animal kingdom!",
        "body": (
            "A giraffe's body faces engineering challenges that would stump the best human designers! 🏗️\n\n"
            "- 🫀 **Giant heart**: A giraffe's heart weighs 11 kg and generates blood pressure TWICE that of humans — it must pump blood 2 metres upward to reach the brain! 💪\n"
            "- 🦴 **Long neck vertebrae**: Despite having a 2-metre neck, giraffes have the SAME number of neck vertebrae as humans — just 7! Each one is simply enormously elongated. 😲\n"
            "- 🧠 **Dizziness prevention**: Special valves in giraffe neck veins prevent a deadly rush of blood to the brain when they lower their head to drink — an extraordinary physiological adaptation! 🩺\n"
            "- 👅 **50cm tongue**: A giraffe's black tongue is 50cm long — perfectly sized to reach around thorny acacia branches. The dark colour protects it from sunburn! ☀️\n"
            "- 😴 **Almost no sleep**: Giraffes only sleep about 30 minutes a day in very short bursts — lying down is dangerous for such a large animal! 😬"
        )
    },
    "🐙 Octopus": {
        "emoji": "🐙", "color": "#6a1b9a", "bg": "#f3e5f5",
        "tagline": "🧠 Nine brains and three hearts!",
        "body": (
            "The octopus has one of the most extraordinary body plans of any animal — biology at its most creative! 🎨\n\n"
            "- 🧠 **Nine brains**: An octopus has a central brain AND a mini-brain in each of its 8 arms — 9 brains total! Each arm can act independently, solve problems, and react without the central brain! 🤯\n"
            "- 💓 **Three hearts**: Two branchial hearts pump blood through the gills; one systemic heart pumps it to the body. When an octopus swims, the systemic heart stops — which is why they prefer crawling! 💔\n"
            "- 🩵 **Blue blood**: Octopus blood is BLUE because it uses copper-based haemocyanin to carry oxygen (humans use iron-based haemoglobin which is red)! 🔵\n"
            "- 🔄 **9 arms or 8?**: Technically, octopuses have 6 arms and 2 legs — they use two tentacles for walking and six for manipulating objects! 🐙\n"
            "- 🦷 **No bones at all**: The only hard part of an octopus is its beak — meaning it can squeeze through any opening larger than its beak! 😱"
        )
    },
    "🦅 Eagle": {
        "emoji": "🦅", "color": "#f57f17", "bg": "#fff8e1",
        "tagline": "👁️ Eyes eight times sharper than yours!",
        "body": (
            "A bald eagle's body is perfectly engineered for aerial hunting at incredible speed! ⚡\n\n"
            "- 👁️ **Super vision**: Eagle eyes have 4–8 times more visual acuity than human eyes — they can spot a rabbit from 3.2 km away! They also see ultraviolet light, invisible to humans. 🌈\n"
            "- 🦴 **Hollow bones**: Eagle bones are hollow and air-filled — making them extremely light without sacrificing strength. The entire skeleton weighs less than the feathers! 🪶\n"
            "- 🫁 **One-way breathing**: Birds breathe in a completely different way — air flows in ONE direction through their lungs continuously (not in and out). This extracts far more oxygen per breath! 🌬️\n"
            "- 🌡️ **Feather insulation**: Thousands of feathers trap warm air against the body — so effective that eagles can fly in Arctic temperatures without discomfort! ❄️\n"
            "- 💓 **Fast heart**: An eagle's heart beats about 300 times per minute in flight — three times human resting rate — powering enormously strong flight muscles! 🚀"
        )
    },
    "🐘 Elephant": {
        "emoji": "🐘", "color": "#546e7a", "bg": "#eceff1",
        "tagline": "🧠 The biggest brain on land!",
        "body": (
            "Elephants have the most complex and emotionally rich brains of any land animal — and extraordinary bodies to match! 🌍\n\n"
            "- 🧠 **5kg brain**: An elephant's brain weighs 5 kg — the largest of any land animal! It has the same number of neurons as a human brain, but distributed differently. 🤯\n"
            "- 🪝 **The trunk**: 150,000 muscle units in the trunk (humans have about 600 muscles total!). It can lift 350 kg or pick up a single blade of grass. It smells, breathes, drinks, and communicates! 💧\n"
            "- 🦷 **Replacing teeth**: Elephants go through 6 sets of molars in their lifetime — when the last set wears out (around age 60–70), they can no longer chew and die of starvation. 😢\n"
            "- 👂 **Ear cooling**: Elephant ears are full of blood vessels — flapping them in the breeze cools the blood circulating through, acting as a giant radiator! ❄️\n"
            "- 😢 **Emotions**: Elephants cry, mourn their dead, feel joy, and show empathy — their emotional range rivals humans, reflecting their extraordinarily complex brain. 💕"
        )
    },
    "🐝 Honeybee": {
        "emoji": "🐝", "color": "#f9a825", "bg": "#fffde7",
        "tagline": "🫀 Five eyes and two stomachs!",
        "body": (
            "A honeybee's tiny body is packed with remarkable biological engineering! ⚙️\n\n"
            "- 👁️ **Five eyes**: Bees have 2 large compound eyes (made of thousands of lenses each) AND 3 simple eyes on top of the head for detecting light intensity! 5 eyes total! 🤩\n"
            "- 🧠 **Tiny but mighty brain**: A bee's brain has only 1 million neurons (vs your 86 billion) — yet it can navigate, communicate, recognise faces, count, and solve problems! 🌸\n"
            "- 🫙 **Two stomachs**: Bees have a regular stomach AND a special honey stomach (crop) just for storing nectar to bring back to the hive! 🍯\n"
            "- 💓 **Temperature control**: Worker bees vibrate their flight muscles to generate heat — keeping the hive at a precise 35°C in all weather. They are living thermostats! 🌡️\n"
            "- 🪽 **Wing engineering**: Bee wings beat 230 times per second — creating the characteristic buzz! Each wing is perfectly shaped to generate lift despite the bee's 'aerodynamically impossible' body. 🎵"
        )
    },
    "🦈 Shark": {
        "emoji": "🦈", "color": "#0277bd", "bg": "#e1f5fe",
        "tagline": "🦷 20,000 teeth in a lifetime!",
        "body": (
            "A shark's body is one of evolution's greatest masterpieces — unchanged for 450 million years for good reason! ⚡\n\n"
            "- 🦷 **Endless teeth**: Sharks have up to 50 teeth in multiple rows — when one falls out, a new one moves forward within days! Up to 20,000 teeth in a lifetime! 😮\n"
            "- 🦴 **No bones**: A shark's entire skeleton is made of CARTILAGE — the same material as your ear and nose! Much lighter and more flexible than bone. 🌊\n"
            "- 💧 **Must keep swimming**: Most sharks must swim continuously to breathe — water must flow over their gills. Stop swimming = stop breathing. They literally cannot stop! 🏊\n"
            "- 🔌 **Sixth sense**: AMPULLAE OF LORENZINI — hundreds of tiny pores around their snout detect the electrical fields generated by every living creature's heartbeat. 💓\n"
            "- 🩹 **Super healing**: Sharks heal from injuries astonishingly quickly — and rarely get infections even in bacteria-filled water. Scientists are studying shark immune systems for medical breakthroughs! 🔬"
        )
    },
}

an_cols = st.columns(len(animal_bodies))
for i, (aname, adata) in enumerate(animal_bodies.items()):
    with an_cols[i]:
        short = aname.split(" ", 1)[1]
        if st.button(adata["emoji"] + "\n" + short,
                     use_container_width=True, key=f"anb_{i}"):
            st.session_state.animal_picked = aname

if st.session_state.animal_picked and st.session_state.animal_picked in animal_bodies:
    aname = st.session_state.animal_picked
    adata = animal_bodies[aname]
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
    st.info("👆 Tap any animal above to compare its amazing body to yours!")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — KEEPING YOUR BODY HEALTHY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("💚", "Keeping Your Amazing Body Healthy!",
               "Your body is extraordinary — here is how to take great care of it! 🌟")

col1, col2 = st.columns(2, gap="large")
care_items = [
    ("🥗", "Eat a Rainbow of Food!",
     "Your body needs over 40 different nutrients to work properly! "
     "Eat <strong>protein</strong> (meat, fish, eggs, beans) for muscles and growth. "
     "<strong>Carbohydrates</strong> (rice, bread, pasta) for energy. "
     "<strong>Fruits and vegetables</strong> (the more colourful the better!) for vitamins and minerals. "
     "<strong>Dairy</strong> (milk, cheese) for calcium and strong bones. 🥦🍊🫐",
     "#e8f5e9", "#2e7d32"),
    ("💧", "Drink Plenty of Water!",
     "Your body is about <strong>60% water</strong> — and you lose it constantly through breathing, sweating, and digestion! "
     "Children need about 5–7 glasses of water per day. "
     "Dehydration makes you tired, gives you headaches, and makes it hard to concentrate at school. "
     "Your urine should be pale yellow — dark yellow means you need more water! 🫧",
     "#e3f2fd", "#1565c0"),
    ("😴", "Sleep — The Body's Repair Time!",
     "Children aged 5–7 need <strong>9–11 hours of sleep</strong> every night — not just for energy, but for growth! "
     "Growth hormone is released during deep sleep. "
     "Your brain consolidates memories and learning during sleep. "
     "Your immune system strengthens overnight. "
     "A regular bedtime routine helps your brain prepare for deep, restorative sleep. 🌙",
     "#f3e5f5", "#6a1b9a"),
    ("🏃", "Move Your Body Every Day!",
     "Children need at least <strong>60 minutes of active movement</strong> every day — running, dancing, swimming, playing! "
     "Exercise strengthens bones and muscles, improves heart and lung fitness, "
     "releases happy chemicals (endorphins) in your brain, "
     "helps you concentrate better at school, and improves your sleep! "
     "Any movement counts — even dancing in the kitchen! 🎵💃",
     "#fff8e1", "#f57f17"),
    ("🪥", "Take Care of Your Teeth!",
     "Brush twice a day for <strong>2 full minutes</strong> — morning and before bed. "
     "Use fluoride toothpaste to protect enamel from acid attacks. "
     "Floss to remove food between teeth where your brush cannot reach. "
     "Limit sugary drinks and sweets — bacteria LOVE sugar and produce tooth-destroying acid. "
     "Visit the dentist every 6 months — even if nothing hurts! 🦷😁",
     "#eceff1", "#546e7a"),
    ("🧼", "Hygiene — Your First Defence!",
     "Wash hands with soap for <strong>20 seconds</strong> after the toilet, before eating, and after coughing. "
     "Most infections spread through unwashed hands — soap physically scrubs germs off your skin. "
     "Cover your mouth with your elbow (not hand!) when you sneeze or cough. "
     "Shower or bath regularly to remove bacteria from your skin. "
     "Change clothes regularly — bacteria grow in warm, moist fabric! 🧽",
     "#fce4ec", "#ad1457"),
]
for i, (emoji, title, body, bg, border) in enumerate(care_items):
    col = col1 if i % 2 == 0 else col2
    with col:
        fun_card(emoji, title, body, bg, border)

think_bubble("Which of these healthy habits do you already do well? Which one could you improve starting today? 💪🌟")

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 9 — QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🧩", "Body Quiz — Test What You Know!",
               "6 brilliant body questions — answer them all, then check your score! 🌟")

questions = [
    {
        "q":    "Q1 🦴 — How many bones does an adult human body have?",
        "opts": ["106", "206", "306", "406"],
        "ans":  "206",
        "explain": "An adult human body has exactly 206 bones! Babies are born with about 270, but many fuse together as we grow. The smallest is the stirrup in the ear, the largest is the femur (thigh bone)! 🦴"
    },
    {
        "q":    "Q2 ❤️ — Roughly how many times does your heart beat every day?",
        "opts": ["1,000", "10,000", "100,000", "1,000,000"],
        "ans":  "100,000",
        "explain": "Your amazing heart beats about 100,000 times every single day — that is 2.5 BILLION beats in a 70-year lifetime! All without ever stopping for a rest! ❤️💓"
    },
    {
        "q":    "Q3 🫁 — What is the name of the muscle that makes you breathe in?",
        "opts": ["The intercostal", "The diaphragm", "The pectoral", "The trapezius"],
        "ans":  "The diaphragm",
        "explain": "The DIAPHRAGM is a dome-shaped muscle below your lungs — when it flattens and pulls down, it creates more space so air rushes into your lungs. It is your breathing engine! 🫁💨"
    },
    {
        "q":    "Q4 🧠 — Which part of the brain controls balance and coordination?",
        "opts": ["The cerebrum", "The brain stem", "The cerebellum", "The hippocampus"],
        "ans":  "The cerebellum",
        "explain": "The CEREBELLUM (at the back of the brain) controls balance, coordination, and fine motor movements — making sure everything you do is smooth and precise! Cyclists and musicians have larger cerebellums! 🎵🚲"
    },
    {
        "q":    "Q5 💪 — Muscles can only PULL bones — they cannot push. How do they move bones in both directions?",
        "opts": ["They use springs between them", "They work in opposing pairs", "They push on tendons", "They use gravity to return"],
        "ans":  "They work in opposing pairs",
        "explain": "Muscles ALWAYS work in pairs — when one contracts and pulls the bone one way, the opposite muscle contracts to pull it back! Your bicep and tricep are a perfect example — they work opposite each other! 💪🔄"
    },
    {
        "q":    "Q6 🦒 — Why does a giraffe need a much stronger heart than a human?",
        "opts": ["Because it runs faster", "Because it is bigger overall", "Because it must pump blood 2 metres up to reach the brain", "Because its blood is thicker"],
        "ans":  "Because it must pump blood 2 metres up to reach the brain",
        "explain": "A giraffe's heart must generate twice the blood pressure of a human heart — to pump blood 2 metres straight up against gravity to reach the brain! It weighs 11 kg and is an engineering marvel! 🦒🫀"
    },
]

for i, q in enumerate(questions):
    st.markdown(f"**{q['q']}**")
    st.session_state.quiz_answers[i] = st.radio(
        label=q["q"], options=q["opts"],
        index=None, key=f"body_q_{i}", label_visibility="collapsed"
    )

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✅ Check My Answers!", use_container_width=True, key="body_quiz_submit"):
        st.session_state.quiz_submitted = True

if st.session_state.quiz_submitted:
    score = 0
    for i, q in enumerate(questions):
        ans = st.session_state.quiz_answers.get(i)
        if ans == q["ans"]:
            score += 1
            st.success(f"✅ **{q['q'].split('—')[1].strip()}** → Correct! 🎉 {q['explain']}")
        elif ans is None:
            st.warning(f"⚠️ **{q['q'].split('—')[1].strip()}** → You did not answer this one!")
        else:
            st.error(f"❌ **{q['q'].split('—')[1].strip()}** → Not quite! "
                     f"The answer is **{q['ans']}**. {q['explain']}")

    badge_data = [
        (6, "🏆", "BODY SCIENCE CHAMPION! 🦴❤️🧠",      "#ffd700", "#fffde7"),
        (5, "🥇", "Brilliant Body Scientist! 💪",        "#c0c0c0", "#f5f5f5"),
        (4, "🥈", "Great Body Explorer! 🫁",             "#cd7f32", "#fff3e0"),
        (3, "🌟", "Good job, Body Detective! 🔍",        "#7b1fa2", "#f3e5f5"),
        (0, "✨", "Keep Exploring — You Can Do It! 💪",  "#1565c0", "#e3f2fd"),
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

    if st.button("🔄 Try Again!", use_container_width=False, key="body_quiz_reset"):
        st.session_state.quiz_submitted = False
        st.session_state.quiz_answers   = {}
        st.rerun()

st.markdown("""
<hr style="border:2px solid lightblue;">
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  SECTION 10 — SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════
section_header("🌟", "What Did We Learn Today?",
               "Our Amazing Body — your quick recap! 🎉")

summary_items = [
    ("🦴", "Skeleton",  "206 bones — your living framework, shield, and blood factory!"),
    ("💪", "Muscles",   "600+ muscles — contracting pairs that power every movement!"),
    ("❤️", "Heart",     "100,000 beats a day — pumping blood around 96,000 km of vessels!"),
    ("🫁", "Lungs",     "23,000 breaths a day — swapping oxygen for carbon dioxide!"),
    ("🧠", "Brain",     "86 billion neurons — controlling everything you think and do!"),
    ("🍎", "Digestion", "A 9-metre journey — turning food into energy and nutrients!"),
]

cols = st.columns(len(summary_items))
for col, (emoji, title, desc) in zip(cols, summary_items):
    with col:
        st.markdown(f"""
        <div style="background:#fff; border-radius:14px; padding:1rem;
                    box-shadow:0 3px 12px rgba(0,0,0,0.08); text-align:center; height:100%;
                    border-top:4px solid #880e4f;">
            <div style="font-size:2.2rem;">{emoji}</div>
            <div style="font-weight:700; color:#2c3e50; margin:0.3rem 0;">{title}</div>
            <div style="font-size:0.87rem; color:#6b7c93; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; padding:1.5rem;
            background:linear-gradient(135deg,#1a0a2e,#6a1b9a,#880e4f,#1a0a2e);
            border-radius:20px; color:#fff;">
    <div style="font-size:2rem; margin-bottom:0.5rem;">
        ✨ Amazing work, little scientist! You are a Body Science Champion! ✨
    </div>
    <div style="color:#e1bee7; font-size:0.95rem;">
        Your body is the most extraordinary machine ever built — treasure it, look after it, and never stop marvelling at it!
    </div>
    <div style="margin-top:1rem; font-size:1.5rem; letter-spacing:0.6rem;">
        🦴 💪 ❤️ 🧠 🫁 🫀 🦷 👁️
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
