import streamlit as st

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(page_title="Video Library", layout="wide", initial_sidebar_state="expanded")

# ─── Global CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    #MainMenu, footer { display: none; }
    div[data-testid="stSidebarNav"] { display: none; }

    html, body, [class*="css"] { font-family: 'Segoe UI', sans-serif; }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d2b5e 0%, #1565c0 50%, #0d47a1 100%);
    }
    section[data-testid="stSidebar"] * { color: #e3f2fd !important; }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 { color: #ffffff !important; }

    div.stButton > button {
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }

    /* ── Video page specific ── */
    .vlib-header {
        background: linear-gradient(135deg, #0d2b5e 0%, #1565c0 60%, #0288d1 100%);
        border-radius: 20px;
        padding: 40px 36px;
        margin-bottom: 32px;
        position: relative;
        overflow: hidden;
        text-align: center;
    }
    .vlib-header h1 { color: white; font-size: 2.2rem; font-weight: 800; margin: 0 0 6px; }
    .vlib-header p  { color: rgba(255,255,255,0.72); font-size: 1rem; margin: 0; }

    .topic-filter-bar {
        display: flex; gap: 10px; flex-wrap: wrap;
        justify-content: center; margin-bottom: 28px;
    }
    .filter-pill {
        padding: 7px 18px; border-radius: 25px; font-size: 13px; font-weight: 700;
        border: 2px solid; cursor: pointer; transition: all 0.15s ease;
        font-family: 'Segoe UI', sans-serif;
    }

    .video-card {
        background: white;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 3px 14px rgba(0,0,0,0.09);
        border: 2px solid #F0F0F0;
        transition: transform 0.18s ease, box-shadow 0.18s ease;
        margin-bottom: 24px;
        height: 100%;
    }
    .video-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 28px rgba(0,0,0,0.14);
    }
    .video-card-header {
        padding: 14px 16px 0;
        display: flex; align-items: center; gap: 10px;
    }
    .topic-badge {
        font-size: 11px; font-weight: 700;
        padding: 3px 10px; border-radius: 20px;
        border: 1px solid;
    }
    .video-card-title {
        font-weight: 800; font-size: 15px; color: #0D1D2F;
        padding: 10px 16px 4px; line-height: 1.35;
    }
    .video-card-desc {
        font-size: 12.5px; color: #777;
        padding: 0 16px 14px; line-height: 1.5;
    }
    .video-embed {
        padding: 0 16px 16px;
    }
    .section-title {
        font-size: 1.3rem; font-weight: 800; color: #0d2b5e;
        margin: 8px 0 18px; display: flex; align-items: center; gap: 10px;
    }
    .section-divider {
        border: none; border-top: 2px solid #E8EEF8; margin: 32px 0;
    }
    .add-video-box {
        background: linear-gradient(135deg, #EFF6FF, #DBEAFE);
        border: 2px dashed #93C5FD;
        border-radius: 16px;
        padding: 32px;
        text-align: center;
        margin-top: 20px;
    }
    .add-video-box h3 { color: #1D4ED8; font-size: 1.1rem; margin-bottom: 8px; }
    .add-video-box p  { color: #6B7280; font-size: 13px; margin: 0; }
    .stats-bar {
        display: flex; gap: 16px; flex-wrap: wrap;
        justify-content: center; margin-bottom: 28px;
    }
    .stat-pill {
        background: rgba(255,255,255,0.18); border: 1px solid rgba(255,255,255,0.3);
        border-radius: 25px; padding: 6px 16px;
        color: white; font-size: 13px; font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar (same as your other pages) ──────────────────────────────────────
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

# ─── VIDEO DATA ───────────────────────────────────────────────────────────────
# 👇 TO ADD YOUR OWN VIDEOS: paste a YouTube URL and fill in title/desc/topic
# YouTube embed format: https://www.youtube.com/embed/VIDEO_ID
# Get VIDEO_ID from any YouTube link: youtube.com/watch?v=VIDEO_ID_IS_HERE

VIDEOS = [
    # ── Our Body ──────────────────────────────────────────────────────────────
    {
        "topic":   "Our Amazing Body",
        "icon":    "🦴",
        "color":   "#C0392B",
        "bg":      "#FDF0EE",
        "border":  "#F1948A",
        "title":   "How Does the Human Body Work?",
        "desc":    "A fun animated tour of our organs and how they work together.",
        "url":     "https://www.youtube.com/embed/E1RaVPoA5ns",   # ← replace with your video ID
    },
    {
        "topic":   "Our Amazing Body",
        "icon":    "🦴",
        "color":   "#C0392B",
        "bg":      "#FDF0EE",
        "border":  "#F1948A",
        "title":   "The Heart and Blood — For Kids",
        "desc":    "Learn how your heart pumps blood all around your body every second!",
        "url":     "https://www.youtube.com/embed/9eu1bbOy5xw",   # ← replace with your video ID
    },

    # ── Five Senses ───────────────────────────────────────────────────────────
    {
        "topic":   "Five Senses",
        "icon":    "👁️",
        "color":   "#6C3483",
        "bg":      "#F5EEF8",
        "border":  "#C39BD3",
        "title":   "The Five Senses Song",
        "desc":    "Sing along and learn about sight, hearing, smell, taste and touch!",
        "url":     "https://www.youtube.com/embed/XUMiPK6LZBI",   # ← replace
    },

    # ── Plants ────────────────────────────────────────────────────────────────
    {
        "topic":   "Plants",
        "icon":    "🌱",
        "color":   "#27AE60",
        "bg":      "#EDFAF1",
        "border":  "#82E0AA",
        "title":   "How Do Plants Grow?",
        "desc":    "Watch a seed sprout and grow into a plant — photosynthesis explained simply.",
        "url":     "https://www.youtube.com/embed/kM7x1K_uCoc",   # ← replace
    },

    # ── Animals ───────────────────────────────────────────────────────────────
    {
        "topic":   "Animals",
        "icon":    "🐾",
        "color":   "#1E8449",
        "bg":      "#EAFAF1",
        "border":  "#76D7A8",
        "title":   "Amazing Animals of the World",
        "desc":    "Explore Animal classification for Kids: mammals, birds, reptiles, amphibians, and fish.",
        "url":     "https://www.youtube.com/embed/EDIcqxwxb90",   # ← replace
    },

    # ── Magnets ───────────────────────────────────────────────────────────────
    {
        "topic":   "Magnets",
        "icon":    "🧲",
        "color":   "#1A5276",
        "bg":      "#EBF5FB",
        "border":  "#7FB3D3",
        "title":   "What is a Magnet? — For Kids",
        "desc":    "See how magnets attract and repel, and discover where we use them every day. How do magnets get attracted to each other",
        "url":     "https://www.youtube.com/embed/yXCeuSiTOug ",   # ← replace
    },
    
    # ── Water & Weather ───────────────────────────────────────────────────────
    {
        "topic":   "Water & Weather",
        "icon":    "☁️",
        "color":   "#0E6655",
        "bg":      "#E8F8F5",
        "border":  "#76D7C4",
        "title":   "The Water Cycle Explained",
        "desc":    "Evaporation, condensation and precipitation — the water cycle in a fun video.",
        "url":     "https://www.youtube.com/embed/TD3XSIE4ymo",   # ← replace
    },

    # ── Simple Machines ───────────────────────────────────────────────────────
    {
        "topic":   "Simple Machines",
        "icon":    "🛠️",
        "color":   "#784212",
        "bg":      "#FEF5E7",
        "border":  "#F0B27A",
        "title":   "Six Simple Machines for Kids",
        "desc":    "Levers, pulleys, wheels, ramps — discover how they make our lives easier!",
        "url":     "https://www.youtube.com/embed/tk9iUjMEnaY",   # ← replace
    },
        {
        "topic":   "Simple Machines",
        "icon":    "🛠️",
        "color":   "#784212",
        "bg":      "#FEF5E7",
        "border":  "#F0B27A",
        "title":   "Simple and Complex Machines",
        "desc":    "Here you will learn about simple machines and use of machines.",
        "url":     "https://www.youtube.com/embed/dM6AtIy60gQ",   # ← replace
    },

    # ── Space ─────────────────────────────────────────────────────────────────
    {
        "topic":   "Space",
        "icon":    "🌌",
        "color":   "#154360",
        "bg":      "#EAF2FF",
        "border":  "#7FB3D3",
        "title":   "Our Solar System — Tour the Planets",
        "desc":    "Fly past all 8 planets and learn amazing facts about each one.",
        "url":     "https://www.youtube.com/embed/libKVRa01L8",   # ← replace
    },
    {
        "topic":   "Space",
        "icon":    "🌌",
        "color":   "#154360",
        "bg":      "#EAF2FF",
        "border":  "#7FB3D3",
        "title":   "Neil Armstrong and the Moon Landing",
        "desc":    "The incredible true story of the first humans to walk on the Moon in 1969.",
        "url":     "https://www.youtube.com/embed/S9HdPi9Ikhk",   # ← replace
    },
]

# ─── Get unique topics for filter ────────────────────────────────────────────
all_topics = ["All Topics"] + sorted(list(set(v["topic"] for v in VIDEOS)))

# ─── Page Header ─────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="vlib-header">
    <div style="font-size:3rem; margin-bottom:10px;">🎬</div>
    <h1>Science Video Library</h1>
    <p>Watch, learn and explore — fun science videos for curious young minds</p>
    <div class="stats-bar" style="margin-top:18px;margin-bottom:0">
        <span class="stat-pill">📹 {len(VIDEOS)} Videos</span>
        <span class="stat-pill">📚 {len(all_topics)-1} Topics</span>
        <span class="stat-pill">🎓 Ages 5–8</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── Topic Filter ─────────────────────────────────────────────────────────────
selected_topic = st.selectbox(
    "Filter by topic:",
    options=all_topics,
    index=0,
    label_visibility="collapsed",
)

# ─── Filter Videos ───────────────────────────────────────────────────────────
filtered = VIDEOS if selected_topic == "All Topics" else [v for v in VIDEOS if v["topic"] == selected_topic]

# ─── Group by topic and render ────────────────────────────────────────────────
from itertools import groupby

# Group filtered videos by topic
topic_groups = {}
for v in filtered:
    if v["topic"] not in topic_groups:
        topic_groups[v["topic"]] = []
    topic_groups[v["topic"]].append(v)

for topic_name, vids in topic_groups.items():
    # Topic section header
    sample = vids[0]
    st.markdown(f"""
    <div class="section-title">
        <span style="font-size:1.6rem">{sample['icon']}</span>
        <span>{topic_name}</span>
        <span style="font-size:13px;font-weight:600;color:#999;margin-left:4px">{len(vids)} video{'s' if len(vids)>1 else ''}</span>
    </div>
    """, unsafe_allow_html=True)

    # Video cards in columns of 2
    for row_start in range(0, len(vids), 2):
        row_vids = vids[row_start:row_start+2]
        cols = st.columns(len(row_vids))
        for col, v in zip(cols, row_vids):
            with col:
                st.markdown(f"""
                <div class="video-card">
                    <div class="video-card-header">
                        <span class="topic-badge" style="background:{v['bg']};color:{v['color']};border-color:{v['border']}">
                            {v['icon']} {v['topic']}
                        </span>
                    </div>
                    <div class="video-card-title">{v['title']}</div>
                    <div class="video-card-desc">{v['desc']}</div>
                    <div class="video-embed">
                        <iframe
                            width="100%" height="210"
                            src="{v['url']}"
                            frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen
                            style="border-radius:12px;">
                        </iframe>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown(
    """
    <hr style="border:2px solid lightblue;">
    """,
    unsafe_allow_html=True
)

# ─── Add More Videos — instruction box ───────────────────────────────────────
# st.markdown("""
# <div class="add-video-box">
#     <h3>➕ Add Your Own Videos</h3>
#     <p>
#         Open <strong>video_library.py</strong> and find the <strong>VIDEOS list</strong> at the top.<br>
#         Copy any YouTube link, grab the Video ID from the URL, and add a new entry like this:
#     </p>
#     <pre style="background:#DBEAFE;border-radius:10px;padding:14px;margin-top:14px;text-align:left;font-size:12px;color:#1D4ED8">
# {
#     "topic":  "Space",
#     "icon":   "🌌",
#     "color":  "#154360",
#     "bg":     "#EAF2FF",
#     "border": "#7FB3D3",
#     "title":  "Your Video Title Here",
#     "desc":   "A short description of what children will learn.",
#     "url":    "https://www.youtube.com/embed/YOUR_VIDEO_ID",
# }</pre>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# Footer
st.caption("""© 2026 Science for Little Stars. All rights reserved.
Authored by <strong style="color:brown;">AMBREEN ABDUL RAHEEM</strong>
The Education Expert""", unsafe_allow_html=True)