import streamlit as st
import os
import random
# import openai

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Science for Little Stars ⭐",
    layout="wide",
    initial_sidebar_state="expanded",
)

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

# sidebar/ setting of all pages:


with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:0.5rem 0;">
        <div style="font-size:2.5rem;">🔬</div>
        <div style="font-weight:700; font-size:1.1rem; color:#fff;">Science for Little Stars</div>
        <div style="font-size:0.8rem; color:#90caf9;">Grades 1-3 · Ages 5-8</div>
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

    # st.markdown("### 🔑 API Configuration")
    # api_key = st.text_input("Enter OpenAI API Key", type="password", help="Get your key from https://platform.openai.com/")
    # if api_key:
    #     os.environ["OPENAI_API_KEY"] = api_key
    #     st.success("API Key saved for this session!")
    # else:
    #     st.warning("Please enter an API key to talk to Spark.")


# # ─── Session State ────────────────────────────────────────────────────────────
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []


# ═══════════════════════════════════════════════════════════════════════════════
#  HERO BANNER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="background:linear-gradient(135deg,#0a0a2e,#0d2b5e,#1b5e20,#880e4f,#0a0a2e);
            border-radius:28px; padding:3rem 2.5rem; text-align:center;
            margin-bottom:2rem; box-shadow:0 8px 40px rgba(0,0,0,0.3);">
    <div style="font-size:1rem; color:#90caf9; letter-spacing:0.2em;
                text-transform:uppercase; margin-bottom:0.6rem;">
        An Interactive Science Journey · Ages 5-8 · Grade 1-3
    </div>
    <h1 style="color:#ffffff; font-size:clamp(2rem,6vw,3.6rem);
               margin:0; text-shadow:0 3px 12px rgba(0,0,0,0.5); line-height:1.2;">
        ⭐ Science for Little Stars ⭐
    </h1>
    <p style="color:#e1bee7; font-size:1.15rem; margin:1rem 0 0.5rem; line-height:1.7;
              max-width:700px; margin-left:auto; margin-right:auto;">
        Embark on an incredible journey through <strong style="color:#fff9c4;">10 thrilling chapters</strong>
        that bring the wonders of science to life, with stories, discoveries,
        interactive explorers, and a quiz in every chapter! 🚀
    </p>
    <div style="font-size:2rem; margin-top:1.2rem; letter-spacing:0.45rem;">
        🦴  👁️ 🌱 🐾🐶 🧲 ☁️ 🛠️ 🌍 🔋 🌌
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  WELCOME MESSAGE + START BUTTON
# ═══════════════════════════════════════════════════════════════════════════════
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("""
    <div style="background:linear-gradient(135deg,#e8f4fd,#f3e5f5);
                border-radius:20px; padding:1.8rem 2rem;
                border-left:6px solid #0d47a1;
                box-shadow:0 4px 20px rgba(0,0,0,0.07);
                margin-bottom:1rem;">
        <div style="font-size:2.5rem; margin-bottom:0.5rem;">👩‍🔬 Hello, Little Scientist! 👨‍🔬</div>
        <div style="font-size:1.05rem; color:#2c3e50; line-height:1.85;">
            Welcome to your very own interactive science e-book — where every page
            is packed with <strong>amazing facts</strong>, <strong>fun experiments</strong>,
            <strong>cool discoveries</strong>, and <strong>brilliant quizzes!</strong><br><br>
            This is not an ordinary book, you can click explore and discover things at your own pace. Every chapter is full of surprises, secret facts, and interactive explorers designed just for curious minds like yours! 🤩<br><br>
            Science is not just something you read, it is something you <strong>live</strong>. It is in every breath you take, every star you see at night, every puddle that disappears on a sunny day. <strong>You are already a scientist</strong> — this book will show you why! 🌟
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("""
        <div style="background:#e8f5e9; border-radius:14px; padding:1rem;
                    text-align:center; border-top:4px solid #2e7d32;">
            <div style="font-size:2.2rem;">📖</div>
            <div style="font-weight:700; color:#2e7d32; font-size:0.95rem;">10 Chapters</div>
            <div style="font-size:0.82rem; color:#555;"><strong>Full curriculum from Space to Planet Earth!</strong></div>
        </div>""", unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div style="background:#e3f2fd; border-radius:14px; padding:1rem;
                    text-align:center; border-top:4px solid #1565c0;">
            <div style="font-size:2.2rem;">🧩</div>
            <div style="font-weight:700; color:#1565c0; font-size:0.95rem;">10 Quizzes</div>
            <div style="font-size:0.82rem; color:#555;"><strong>6 questions + badges in every chapter!</strong></div>
        </div>""", unsafe_allow_html=True)
    with col_c:
        st.markdown("""
        <div style="background:#f3e5f5; border-radius:14px; padding:1rem;
                    text-align:center; border-top:4px solid #6a1b9a;">
            <div style="font-size:2.2rem;">🤖</div>
            <div style="font-weight:700; color:#6a1b9a; font-size:0.95rem;">AI Assistant</div>
            <div style="font-size:0.82rem; color:#555;"><strong>Ask Spark anything — 24/7 science help!</strong></div>
        </div>""", unsafe_allow_html=True)

with col2:
    # Stats card
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0d2b5e,#1565c0);
                border-radius:20px; padding:1.5rem; color:#fff;
                box-shadow:0 6px 24px rgba(0,0,0,0.2); margin-bottom:0.8rem;">
        <div style="font-size:1.1rem; font-weight:700; margin-bottom:1rem;
                    text-align:center; color:#90caf9; letter-spacing:0.05em;">
            📊 Inside This E-Book
        </div>
        <div style="display:flex; flex-direction:column; gap:0.55rem;">
            <div style="background:rgba(255,255,255,0.1); border-radius:10px;
                        padding:0.5rem 0.8rem; display:flex; align-items:center; gap:0.6rem;">
                <span style="font-size:1.4rem;">📚</span>
                <div>
                    <div style="font-weight:700; font-size:1rem;">10 Chapters</div>
                    <div style="font-size:0.78rem; color:#90caf9;">Space to Planet Earth</div>
                </div>
            </div>
            <div style="background:rgba(255,255,255,0.1); border-radius:10px;
                        padding:0.5rem 0.8rem; display:flex; align-items:center; gap:0.6rem;">
                <span style="font-size:1.4rem;">🔬</span>
                <div>
                    <div style="font-weight:700; font-size:1rem;">100+ Science Topics</div>
                    <div style="font-size:0.78rem; color:#90caf9;">Fully age-appropriate</div>
                </div>
            </div>
            <div style="background:rgba(255,255,255,0.1); border-radius:10px;
                        padding:0.5rem 0.8rem; display:flex; align-items:center; gap:0.6rem;">
                <span style="font-size:1.4rem;">🎯</span>
                <div>
                    <div style="font-weight:700; font-size:1rem;">60 Quiz Questions</div>
                    <div style="font-size:0.78rem; color:#90caf9;">With instant feedback</div>
                </div>
            </div>
            <div style="background:rgba(255,255,255,0.1); border-radius:10px;
                        padding:0.5rem 0.8rem; display:flex; align-items:center; gap:0.6rem;">
                <span style="font-size:1.4rem;">🏆</span>
                <div>
                    <div style="font-weight:700; font-size:1rem;">50 Achievement Badges</div>
                    <div style="font-size:0.78rem; color:#90caf9;">Earn one in every quiz!</div>
                </div>
            </div>
            <div style="background:rgba(255,255,255,0.1); border-radius:10px;
                        padding:0.5rem 0.8rem; display:flex; align-items:center; gap:0.6rem;">
                <span style="font-size:1.4rem;">🤖</span>
                <div>
                    <div style="font-weight:700; font-size:1rem;">AI Science Assistant</div>
                    <div style="font-size:0.78rem; color:#90caf9;">Spark — always here to help!</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_x, col_y = st.columns(2)
    with col_x:
        if st.button("🚀 Start Chapter 01", use_container_width=True):
            st.success("Head to **Chapter 01 · Our Amazing Body** in the sidebar! 🦴")
    with col_y:
        chapters=[
            ("pages/01_chapter_our_body-01.py")
            ("pages/02_chapter_senses-02.py")
            ("pages/03_chapter_plants-03.py")
            ("pages/04_chapter_animals-04.py")
            ("pages/05_chapter_magnets-05.py")
            ("pages/06_chapter_weather-06.py")
            ("pages/07_chapter_simple_machines-07.py")
            ("pages/08_chapter_saving_our_planet-08.py")
            ("pages/09_chapter_energy_electricity-09.py")
            ("pages/10_chapter_space-10.py")
        ]
        if st.button("🎲 Surprise Me!", use_container_width=True):
            import random
            pick = random.choice(chapters)
            st.info(f"Try **Chapter {pick[0]} · {pick[1]} {pick[2]}** today! ✨")

st.markdown(
    """
    <hr style="border:2px solid lightblue;">
    """,
    unsafe_allow_html=True
)

# ═══════════════════════════════════════════════════════════════════════════════
#  CHAPTER CARDS GRID
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="text-align:center; margin:1rem 0 1.5rem;">
    <div style="font-size:3rem; margin-bottom:0.3rem;">🗺️</div>
    <h2 style="color:#2c3e50; font-size:1.9rem; margin:0;">Explore All 10 Chapters</h2>
    <p style="color:#6b7c93; font-size:1rem; margin-top:0.3rem;">
        Click any chapter in the sidebar to dive straight in! 📖
    </p>
</div>
""", unsafe_allow_html=True)

chapter_cards = [
    ("01", "🦴", "Our Amazing Body",
     "206 bones, 600 muscles, 86 billion brain cells, and a heart that beats 100,000 times a day — discover the machine inside YOU!",
     "#4a0072", "#f3e5f5"),
    ("02", "👁️", "The Five Senses",
     "How do your eyes see colour? Why can you smell rain? How does your tongue taste sweet and sour? Explore your extraordinary senses!",
     "#880e4f", "#fce4ec"),
    ("03", "🌱", "Plants and Growth",
     "From tiny seeds to giant sequoias! Discover photosynthesis, roots, flowers, pollination, and why plants are the foundation of all life.",
     "#1b5e20", "#e8f5e9"),
    ("04", "🐾🐶", "Animals and Habitats",
     "Explore the animal kingdom! Mammals, reptiles, insects, and ocean creatures — plus the habitats they call home worldwide.",
     "#4a148c", "#f3e5f5"),
    ("05", "🧲", "Marvelous Magnets",
     "Attract, repel, and discover! The invisible force field around magnets, magnetic materials, the Earth as a giant magnet, and more!",
     "#b71c1c", "#ffebee"),
    ("06", "☁️", "Water and Weather",
     "The water cycle, types of clouds, snowflakes, wind, rainbows, and why no two weather days are ever exactly the same!",
     "#01579b", "#e1f5fe"),
    ("07", "🛠️", "Simple Machines",
     "Levers, wheels, pulleys, ramps, wedges, and screws — six tools that built every pyramid, skyscraper, and spacecraft ever made!",
     "#3e2723", "#efebe9"),
    ("08", "🌍", "Saving Our Planet",
     "Climate change, recycling, precious water, disappearing forests, and endangered animals — discover how YOU can be a Green Hero!",
     "#1b5e20", "#e8f5e9"),
    ("09", "🔋", "Energy and Electricity",
     "The Sun, circuits, lightning, renewable energy, and the electric eel — energy is everything, and it never disappears!",
     "#e65100", "#fff3e0"),
    ("10", "🌌", "The Solar System",
     "Blast off into space! Explore all 8 planets, the Sun, Moon phases, asteroids, and the astonishing scale of our solar system.",
     "#0d2b5e", "#e8eaf6"),
]

for row_start in range(0, len(chapter_cards), 2):
    col1, col2 = st.columns(2, gap="large")
    for col, cidx in zip([col1, col2], [row_start, row_start + 1]):
        if cidx < len(chapter_cards):
            num, emoji, title, desc, dark, light = chapter_cards[cidx]
            with col:
                st.markdown(f"""
                <div style="background:{light}; border-radius:18px; padding:1.3rem 1.5rem;
                            border-left:6px solid {dark}; margin-bottom:0.8rem;
                            box-shadow:0 3px 14px rgba(0,0,0,0.07);
                            transition:transform 0.2s;">
                    <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.6rem;">
                        <div style="background:{dark}; color:#fff; border-radius:50%;
                                    width:42px; height:42px; display:flex; align-items:center;
                                    justify-content:center; font-weight:700; font-size:0.9rem;
                                    flex-shrink:0;">Ch{num}</div>
                        <div style="font-size:2rem;">{emoji}</div>
                        <div style="font-size:1.15rem; font-weight:700; color:#2c3e50;">{title}</div>
                    </div>
                    <div style="font-size:0.91rem; color:#555; line-height:1.65; padding-left:3.5rem;">
                        {desc}
                    </div>
                </div>""", unsafe_allow_html=True)

st.markdown(
    """
    <hr style="border:2px solid lightblue;">
    """,
    unsafe_allow_html=True
)

# ═══════════════════════════════════════════════════════════════════════════════
#  WHAT'S INSIDE EVERY CHAPTER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="text-align:center; margin:1rem 0 1.5rem;">
    <div style="font-size:3rem; margin-bottom:0.3rem;">✨</div>
    <h2 style="color:#2c3e50; font-size:1.9rem; margin:0;">What's Inside Every Chapter?</h2>
    <p style="color:#6b7c93; font-size:1rem; margin-top:0.3rem;">
        Every single chapter is packed with these brilliant features! 🌟
    </p>
</div>
""", unsafe_allow_html=True)

features = [
    ("📖", "Deep Dive Content",    "#e8f5e9", "#2e7d32",
     "Dozens of rich, age-perfect explanations written specially for ages 5–7 — curious, detailed, and never boring!"),
    ("🔍", "Secret Fact Reveals",  "#e3f2fd", "#1565c0",
     "Click to reveal a hidden science secret in every section — collected one button press at a time! 🤫"),
    ("🎮", "Interactive Explorers","#f3e5f5", "#6a1b9a",
     "Step through complex topics with prev/next navigators — the water cycle, brain regions, lightning, and more!"),
    ("🏆", "Topic Selectors",      "#fff8e1", "#e65100",
     "Tap colourful buttons to expand detailed panels on animals, planets, machines, and body systems!"),
    ("🤔", "Think Bubbles",        "#fce4ec", "#c62828",
     "Thoughtful questions sprinkled throughout to spark curiosity and classroom discussion!"),
    ("🦁", "Animal Spotlights",    "#e0f2f1", "#00695c",
     "Every chapter features an animal connection — showing science working brilliantly in the natural world!"),
    ("🧩", "Chapter Quiz",         "#ede7f6", "#4527a0",
     "6 multiple-choice questions with instant per-question feedback and a 5-tier achievement badge! 🥇"),
    ("🤖", "Spark AI Assistant",   "#fff3e0", "#e65100",
     "Ask your AI science tutor Spark any question — safe, child-appropriate, powered by GPT-4o-mini!"),
]

cols = st.columns(4)
for i, (emoji, title, bg, color, desc) in enumerate(features):
    with cols[i % 4]:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:16px; padding:1.1rem;
                    border-top:4px solid {color}; text-align:center; margin-bottom:0.8rem;
                    box-shadow:0 3px 10px rgba(0,0,0,0.06); height:100%;">
            <div style="font-size:2.2rem; margin-bottom:0.4rem;">{emoji}</div>
            <div style="font-weight:700; color:{color}; font-size:0.97rem;
                        margin-bottom:0.4rem;">{title}</div>
            <div style="font-size:0.83rem; color:#555; line-height:1.55;">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown(
    """
    <hr style="border:2px solid lightblue;">
    """,
    unsafe_allow_html=True
)

# import os
# from dotenv import load_dotenv

# load_dotenv()

# # ── Init chat history ─────────────────────────────────────────────────────────
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # ═══════════════════════════════════════════════════════════════════════════════
# #  SPARK CHATBOT — SIDEBAR
# # ═══════════════════════════════════════════════════════════════════════════════
# with st.sidebar:

#     st.markdown("""
#     <div style="<div style="background:#f3e5f5; color:#000000;
#                 border-radius:16px; padding:1.2rem 1rem; text-align:center;
#                 color:#fff; margin-bottom:1rem;
#                 box-shadow:0 4px 16px rgba(0,0,0,0.3);">
#         <div style="font-size:2.5rem; margin-bottom:0.3rem;">🤖</div>
#         <div style="font-size:1.1rem; font-weight:700;">Hi, I'm Spark!</div>
#         <div style="font-size:0.78rem; color:#e1bee7; line-height:1.6; margin-top:0.4rem;">
#             Your AI science tutor ⚡<br>Ask me anything about science!
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # ── Chat history display ──────────────────────────────────────────────────
#     for msg in st.session_state.chat_history:
#         if msg["role"] == "user":
#             st.markdown(f"""
#             <div style="display:flex; justify-content:flex-end; margin-bottom:0.5rem;">
#                 <div style="background:#f3e5f5; color:#000000;
#                             border-radius:14px 14px 4px 14px;
#                             padding:0.6rem 0.9rem; max-width:90%;
#                             font-size:0.83rem;">
#                     👤 {msg["content"]}
#                 </div>
#             </div>""", unsafe_allow_html=True)
#         else:
#             st.markdown(f"""
#             <div style="display:flex; justify-content:flex-start; margin-bottom:0.5rem;">
#                 style="background:#f3e5f5; color:#000000;
#                             border-radius:14px 14px 14px 4px;
#                             padding:0.6rem 0.9rem; max-width:90%;
#                             font-size:0.83rem; border:1px solid #ce93d8;">
#                 🤖 <strong style="color:#6a1b9a;">Spark:</strong> {msg["content"]}
#                 </div>
#             </div>""", unsafe_allow_html=True)

#     # ── Input ─────────────────────────────────────────────────────────────────
#     user_input = st.chat_input("Ask Spark a question… 🔬")

#     if user_input:
#         st.session_state.chat_history.append({"role": "user", "content": user_input})

#         try:
#             from openai import OpenAI
#             client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#             response = client.chat.completions.create(
#                 model="gpt-4o-mini",
#                 messages=[
#                     {
#                         "role": "system",
#                         "content": (
#                             "You are Spark, a friendly science assistant for children aged 5-7 (Grade 1). "
#                             "Explain science clearly, simply, and engagingly. "
#                             "Use short sentences, fun comparisons, and lots of encouragement. "
#                             "Always be positive, safe, and age-appropriate. "
#                             "Add one emoji at the end of each answer. "
#                             "Keep answers to 3-4 sentences maximum."
#                         )
#                     },
#                     *[{"role": m["role"], "content": m["content"]}
#                       for m in st.session_state.chat_history]
#                 ],
#                 max_tokens=300
#             )
#             answer = response.choices[0].message.content

#         except Exception as e:
#             answer = f"Oops! Something went wrong. 😵 Error: {str(e)}"

#         st.session_state.chat_history.append({"role": "assistant", "content": answer})
#         st.rerun()

#     # ── Clear button ──────────────────────────────────────────────────────────
#     if st.session_state.chat_history:
#         if st.button("🗑️ Clear chat", key="clear_chat", use_container_width=True):
#             st.session_state.chat_history = []
#             st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
#  LEARNING PATH GUIDE
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="text-align:center; margin:1rem 0 1.5rem;">
    <div style="font-size:3rem; margin-bottom:0.3rem;">🗺️</div>
    <h2 style="color:#2c3e50; font-size:1.9rem; margin:0;">How to Use This E-Book</h2>
    <p style="color:#6b7c93; font-size:1rem; margin-top:0.3rem;">
        Get the most out of every chapter with these tips! 🌟
    </p>
</div>
""", unsafe_allow_html=True)

steps = [
    ("1️⃣", "Choose a Chapter",     "#e8f5e9", "#1b5e20",
     "Pick any chapter from the sidebar — start with Chapter 01 for the full journey, or jump to any topic that excites you! There is no wrong order! 🚀"),
    ("2️⃣", "Read and Explore",     "#e3f2fd", "#1565c0",
     "Read each section carefully, try the interactive step-through explorers, and click the topic selector buttons to dig deeper into what interests you most! 🔍"),
    ("3️⃣", "Reveal the Secrets!",  "#f3e5f5", "#6a1b9a",
     "Look for the secret fact reveal buttons in every section — they are full of the most amazing and surprising science facts! 🤫✨"),
    ("4️⃣", "Think and Discuss",    "#fff8e1", "#e65100",
     "The 🤔 think bubbles throughout the chapters are conversation starters — try discussing them with a classmate, parent, or teacher! 💬"),
    ("5️⃣", "Take the Quiz!",       "#fce4ec", "#c62828",
     "At the end of each chapter, test your knowledge with the 6-question quiz. Aim for the GOLD TROPHY badge — can you get 6/6 in every chapter? 🏆"),
    ("6️⃣", "Ask Spark!",           "#e0f2f1", "#00695c",
     "If you do not understand something, just ask Spark! No question is too small or too big — your curiosity is always welcome! 🤖💡"),
]

cols = st.columns(3)
for i, (num, title, bg, color, desc) in enumerate(steps):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="background:{bg}; border-radius:16px; padding:1.2rem;
                    border-left:5px solid {color}; margin-bottom:0.8rem;
                    box-shadow:0 3px 10px rgba(0,0,0,0.06);">
            <div style="font-size:1.8rem; margin-bottom:0.3rem;">{num}</div>
            <div style="font-weight:700; color:{color}; font-size:1rem;
                        margin-bottom:0.5rem;">{title}</div>
            <div style="font-size:0.87rem; color:#555; line-height:1.6;">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown(
    """
    <hr style="border:2px solid lightblue;">
    """,
    unsafe_allow_html=True
)

# ═══════════════════════════════════════════════════════════════════════════════
#  CURRICULUM OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="text-align:center; margin:1rem 0 1.5rem;">
    <div style="font-size:3rem; margin-bottom:0.3rem;">📋</div>
    <h2 style="color:#2c3e50; font-size:1.9rem; margin:0;">Curriculum Overview</h2>
    <p style="color:#6b7c93; font-size:1rem; margin-top:0.3rem;">
        Aligned with Grade 1 science standards — covering the whole amazing world! 🌍
    </p>
</div>
""", unsafe_allow_html=True)

curriculum = [
    ("🌌 Space & Earth Science",  "#e8eaf6", "#3949ab",
     ["Solar System — 8 planets, Sun, Moon phases",
      "Water cycle, weather, clouds, rain & snow",
      "Climate change & protecting our planet"]),
    ("🌱 Life Science",           "#e8f5e9", "#2e7d32",
     ["Plants — photosynthesis, seeds, growth",
      "Animals — habitats, adaptations, food chains",
      "Human body — skeleton, muscles, heart, brain"]),
    ("⚙️ Physical Science",       "#fff3e0", "#e65100",
     ["Magnets — attract, repel, poles, uses",
      "Simple machines — 6 types, everyday examples",
      "Energy & electricity — types, circuits, renewable"]),
    ("🔬 Science Skills",         "#f3e5f5", "#6a1b9a",
     ["Observation using all 5 senses",
      "Asking questions and making predictions",
      "Recording findings and drawing conclusions"]),
]

curr_cols = st.columns(4)
for col, (title, bg, color, topics) in zip(curr_cols, curriculum):
    with col:
        bullet_items = "".join([
            f'<li style="margin-bottom:0.3rem;">{t}</li>' for t in topics
        ])
        st.markdown(f"""
        <div style="background:{bg}; border-radius:16px; padding:1.2rem;
                    border-top:4px solid {color}; height:100%;
                    box-shadow:0 3px 10px rgba(0,0,0,0.06);">
            <div style="font-weight:700; color:{color}; font-size:0.97rem;
                        margin-bottom:0.7rem;">{title}</div>
            <ul style="padding-left:1.2rem; margin:0; font-size:0.85rem;
                       color:#444; line-height:1.7;">
                {bullet_items}
            </ul>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  GRAND FOOTER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style="text-align:center; margin-top:3rem; padding:2.5rem 2rem;
            background:linear-gradient(135deg,#0a0a2e,#0d2b5e,#1b5e20,#880e4f,#0a0a2e);
            border-radius:28px; color:#fff;
            box-shadow:0 8px 40px rgba(0,0,0,0.3);">
    <div style="font-size:3rem; margin-bottom:0.5rem;">⭐🔬🌍</div>
    <div style="font-size:1.6rem; font-weight:700; margin-bottom:0.6rem;">
        Science for Little Stars
    </div>
    <div style="font-size:0.95rem; color:#c8e6c9; line-height:1.8; margin-bottom:1.2rem;
                max-width:600px; margin-left:auto; margin-right:auto;">
        An interactive science e-book for curious minds aged 5-8 ·
        10 chapters · 60 quiz questions · Spark AI Assistant<br>
        Every child is born a scientist — this book helps them remember that! 💚
    </div>
    <div style="font-size:1.5rem; letter-spacing:0.5rem; margin-bottom:1rem;">
        🦴 👁️ 🌱 🐾🐶 🧲 ☁️ 🛠️ 🌍 🔋 🌌
    </div>
    <div style="font-size:0.85rem; color:#a5d6a7;">
        ✍️ Authored by <strong style="color:#ffffff;">AMBREEN ABDUL RAHEEM</strong>
        · The Education Expert
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    """
    <hr style="border:2px solid lightblue;">
    """,
    unsafe_allow_html=True
)

# Footer
st.caption("""© 2026 Science for Little Stars. All rights reserved.
Authored by <strong style="color:brown;">AMBREEN ABDUL RAHEEM</strong>
The Education Expert""", unsafe_allow_html=True)
