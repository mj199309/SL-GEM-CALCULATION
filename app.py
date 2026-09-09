import streamlit as st
import time

# 1. Page Configuration (Desktop & Mobile Scaling)
st.set_page_config(page_title="MJ GEMS Admin Portal", page_icon="💎", layout="centered")

# --- 2. LUXURY GEMSTONES ROTATING LOADER ANIMATION (5 SECONDS) ---
if "loaded" not in st.session_state:
    st.session_state.loaded = False

if not st.session_state.loaded:
    st.markdown(
        """
        <div id="loading-screen">
          <div class="gem-ring">
            <div class="gem-particle" style="top: 0px; left: 42px; background: #00d2ff;"></div>
            <div class="gem-particle" style="top: 12px; left: 72px; background: #ff5252;"></div>
            <div class="gem-particle" style="top: 42px; left: 84px; background: #ffeb3b;"></div>
            <div class="gem-particle" style="top: 72px; left: 72px; background: #e040fb;"></div>
            <div class="gem-particle" style="top: 84px; left: 42px; background: #00e676;"></div>
            <div class="gem-particle" style="top: 72px; left: 12px; background: #ff9100;"></div>
            <div class="gem-particle" style="top: 42px; left: 0px; background: #00b0ff;"></div>
            <div class="gem-particle" style="top: 12px; left: 12px; background: #ff4081;"></div>
          </div>
          <div class="loading-text">Loading Portal...</div>
        </div>
        <style>
          #loading-screen {
            position: fixed; top: 0px; left: 0px; width: 100vw; height: 100vh;
            background: linear-gradient(135deg, #060c17, #03070e);
            display: flex; flex-direction: column; justify-content: center; align-items: center;
            z-index: 99999;
          }
          .gem-ring { position: relative; width: 100px; height: 100px; animation: spinRing 2.5s linear infinite; transform-style: preserve-3d; perspective: 500px; }
          .gem-particle { position: absolute; width: 16px; height: 16px; border-radius: 50%; box-shadow: 0 0 15px rgba(0,210,255,0.6); }
          @keyframes spinRing { 0% { transform: rotate(0deg) rotateX(20deg); } 100% { transform: rotate(360deg) rotateX(20deg); } }
          .loading-text { margin-top: 25px; font-family: sans-serif; font-size: 20px; font-weight: 500; color: #e2f1ff; letter-spacing: 3px; text-transform: uppercase; }
        </style>
        """,
        unsafe_allow_html=True
    )
    time.sleep(5.0)
    st.session_state.loaded = True
    st.rerun()

# --- 3. CUSTOM CSS FOR LUXURY DARK THEME BACKGROUND ---
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(135deg, #060c17, #0b1528, #03070e); }
    h1, h2, h3, p, span, label, .stMarkdown { color: #e2f1ff !important; }
    div[data-baseweb="select"], div[data-baseweb="input"], div[data-baseweb="radio"] {
        background-color: rgba(15, 27, 49, 0.8) !important;
        border: 1px solid rgba(0, 210, 255, 0.3) !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] span { white-space: normal !important; word-break: break-word !important; }
    .metric-box {
        background-color: rgba(0, 210, 255, 0.05); border: 1px solid rgba(0, 210, 255, 0.3);
        padding: 20px; border-radius: 12px; text-align: center; margin-top: 10px;
    }
    .rotating-title {
        font-size: 42px; font-weight: bold; color: #00d2ff; text-align: center;
        text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px;
        text-shadow: 0 0 10px #00d2ff, 0 0 20px #0088cc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="rotating-title">💎 MJ GEMS 💎</div>', unsafe_allow_html=True)
st.subheader("💎 ලංකාවේ සැබෑ මැණික් මිල ගණනය යෙදුම")
st.caption("Adjusted Market Rates & Gem Knowledge Framework")
st.write("---")

# 1. Main Category Select
categories = [
    "CORUNDUM (කුරුන්දු කුලය)", "CHRYSOBERYL (කනක / වෛරෝඩි)", "SPINEL (කිරිංචි / ස්පිනෙල්)",
    "GARNET (රබහ / ගෝමේද)", "TOURMALINE (තෝරමල්ලි)", "BERYL & TOPAZ (බෙරිල් සහ තෝපස්)",
    "QUARTZ & FELDSPAR (פළිඟු / පුෂ්පකාන්ත)", "OTHER GEMS (දුර්ලභ සහ අනෙකුත් මැණික් වර්ග)"
]
st.markdown("### 1 මැණික් කාණ්ඩය (GEMSTONE CATEGORY):")
selected_cat = st.selectbox("කාණ්ඩය තෝරන්න:", categories, label_visibility="collapsed")

# 2. Gemstone Sub-Type & Color Mapping Engine
gem_registry = {
    "CORUNDUM (කුරුන්දු කුලය)": {
        "නිල් මැණික් (Blue Sapphire - Royal Blue)": (475000, 1150000),
        "නිල් මැණික් (Blue Sapphire - Cornflower Blue)": (325000, 775000),
        "නිල් මැණික් (Blue Sapphire - Vivid Blue)": (375000, 925000),
        "නිල් මැණික් (Blue Sapphire - Pastel / Light Blue)": (105000, 225000),
        "නිල් මැණික් (Blue Sapphire - Velvet Blue)": (300000, 700000),
        "නිල් මැණික් (Blue Sapphire - Peacock Blue)": (250000, 575000),
        "නිල් මැණික් (Blue Sapphire - Deep Blue)": (175000, 400000),
        "නිල් මැණික් (Blue Sapphire - Sky Blue)": (85000, 185000),
        "නිල් මැණික් (Blue Sapphire - Navy Blue)": (105000, 225000),
        "පුෂ්පරාග (Yellow Sapphire - Golden Yellow)": (250000, 600000),
        "පුෂ්පරාග (Yellow Sapphire - Vivid Yellow)": (200000, 450000),
        "පුෂ්පරාග (Yellow Sapphire - Honey Yellow)": (175000, 375000),
        "පුෂ්පරාග (Yellow Sapphire - Lemon Yellow)": (105000, 225000),
        "පද්මරාග (Padparadscha - Lotus Pink)": (525000, 1500000),
        "පද්මරාග (Padparadscha - Sunset Orange)": (450000, 1150000),
        "පද්මරාග (Padparadscha - Peach / Salmon Pink)": (375000, 900000),
        "රතු කැට (Ruby - Pigeon Blood Red)": (900000, 1850000),
        "රතු කැට (Ruby - Deep Red)": (285000, 550000),
        "රතු කැට (Ruby - Medium Red)": (170000, 310000),
        "රෝස සෆයාර් (Pink Sapphire)": (180000, 420000),
        "සුදු සෆයාර් (White Sapphire)": (65000, 150000),
        "කොළ සෆයාර් (Green Sapphire)": (75000, 180000),
        "ආරුල් නිල් මැණික් (Star Sapphire)": (220000, 650000),
        "ආරුල් රතු කැට (Star Ruby)": (350000, 850000),
        "ගෙවුඩ (Geuda)": (50000, 120000),
        "ඔට්ටු මැණික් (Ottu Sapphire)": (120000, 300000)
    },
    "CHRYSOBERYL (කනක / වෛරෝඩි)": {
        "පැණි වෛරෝඩි (Cat's Eye - Chrysoberyl)": (550000, 1300000),
        "ඇලෙක්සැන්ඩ්‍රයිට් (Alexandrite - Color Change)": (850000, 1950000),
        "ඇලෙක්සැන්ඩ්‍රයිට් වෛරෝඩි (Alexandrite Cat's Eye)": (950000, 2200000),
        "කහ කනක (Yellow Chrysoberyl)": (150000, 350000),
        "කොළ කනක (Green Chrysoberyl)": (160000, 380000)
    },
    "SPINEL (කිරිංචි / ස්පිනෙල්)": {
        "රතු කිරිංචි (Red Spinel)": (360000, 360000),
        "රෝස කිරිංචි (Pink Spinel)": (150000, 150000),
        "නිල් කිරිංචි (Blue Spinel)": (180000, 180000),
        "දම් කිරිංචි (Purple Spinel)": (120000, 120000),
        "කළු කිරිංචි (Black Spinel)": (25000, 25000)
    },
    "GARNET (රබහ / ගෝමේද)": {
        "ගෝමේද (Hessonite Garnet)": (45000, 90000),
        "රතු රබහ (Almandine Garnet)": (35000, 75000),
        "රතු ගානට් (Pyrope Garnet)": (40000, 80000),
        "තැඹිලි ගානට් (Spessartine Garnet)": (60000, 130000),
        "වර්ණ මාරු ගානට් (Colour-change Garnet)": (95000, 210000),
        "ආරුල් ගානට් (Star Garnet)": (50000, 110000)
    },
    "TOURMALINE (තෝරමල්ලි)": {
        "පච්ච තෝරමල්ලි (Green Tourmaline)": (75000, 160000),
        "රෝස තෝරමල්ලි (Pink Tourmaline)": (85000, 180000),
        "රූබිලයිට් (Rubellite)": (125000, 270000),
        "දුඹුරු තෝරමල්ලි (Brown Tourmaline)": (45000, 95000),
        "බහු වර්ණ තෝරමල්ලි (Multicoloured Tourmaline)": (90000, 195000),
        "කළු තෝරමල්ලි (Black Tourmaline)": (15000, 35000)
    },
    "BERYL & TOPAZ (බෙරිල් සහ තෝපස්)": {
        "පච්ච පඩියන් (Aquamarine)": (110000, 250000),
        "මරකත (Emerald)": (400000, 950000),
        "රන් පඩියන් (Golden Beryl)": (85000, 190000),
        "රෝස බෙරිල් (Morganite)": (95000, 210000),
        "සුදු බෙරිල් (Goshenite)": (35000, 75000),
        "ඉම්පීරියල් තෝපස් (Imperial Topaz)": (180000, 400000),
        "කහ තෝපස් (Yellow Topaz)": (45000, 95000),
        "නිල් තෝපස් (Blue Topaz)": (35000, 75000),
        "රෝස තෝපස් (Pink Topaz)": (75000, 160000),
        "සුදු තෝපස් (Colourless Topaz)": (20000, 45000)
    },
    "QUARTZ & FELDSPAR (පළිඟු / පුෂ්පකාන්ත)": {
        "දම් පළිඟු (Amethyst)": (30000, 65000),
        "කහ පළිඟු (Citrine)": (25000, 55000),
        "පුෂ්පකාන්ත (Moonstone)": (25000, 55000),
        "සුදු පළිඟු (Rock Crystal)": (10000, 25000),
        "රෝස පළිඟු (Rose Quartz)": (15000, 35000),
        "දුම් පළිඟු (Smoky Quartz)": (15000, 35000),
        "වෛරෝඩි පළිඟු (Cat's eye Quartz)": (45000, 95000),
        "මහෝත්පල (Orthoclase)": (35000, 75000),
        "ලැබ්‍රඩොරයිට් (Labradorite)": (30000, 65000),
        "කිරි පළිඟු (Milky Quartz)": (8000, 18000)
    },
    "OTHER GEMS (දුර්ලභ සහ අනෙකුත් මැණික් වර්ග)": {
        "නිල් ජාගුන් (Blue Zircon)": (70000, 150000),
        "පච්ච තෝර (Green Zircon)": (65000, 135000),
        "සුදු ජාගුන් (Colourless Zircon)": (45000, 95000),
        "පෙරිඩොට් (Peridot)": (65000, 140000),
        "අයොලයිට් (Iolite)": (40000, 85000),
        "සිංහලයිට් (Sinhalite)": (150000, 350000),
        "තාෆීට් (Taaffeite)": (850000, 2500000),
        "සෙරන්ඩිබයිට් (Serendibite)": (950000, 3000000),
        "දියමන්ති / වජ්‍ර (Diamond)": (1500000, 3500000),
        "මුතු (Pearl)": (100000, 450000),
        "ස්කැපොලයිට් (Scapolite)": (35000, 75000),
        "ඩයොප්සයිඩ් (Dioside)": (30000, 65000),
        "එකනයිට් (Ekanite)": (50000, 110000),
        "පබළු (Coral)": (25000, 60000)
    }
}

st.markdown("### 2 මැණික් වර්ගය සහ වර්ණය (GEMSTONE TYPE & COLOR):")
available_gems = gem_registry.get(selected_cat, {})
selected_gem = st.selectbox("වර්ගය තෝරන්න:", list(available_gems.keys()), label_visibility="collapsed")

# 3. Gemstone Cut
cut_options = {
    "Round Cut (රවුන්ඩ් / බ්‍රිලියන්ට්) - 100%": 1.00,
    "Princess Cut (ප්‍රින්සස් / හතරැස් හැඩය) - 88%": 0.88,
    "Marquise Cut (මාර්කිස් / ඔරු හැඩය) - 82%": 0.82,
    "Oval Cut (ඕවල් / ප්‍රමිතිගත බිත්තර හැඩය) - 75%": 0.75,
    "Cushion Cut (කුෂන් / කොට්ට හැඩය) - 70%": 0.70,
    "Pear Cut (පෙයාර් / kඳුළු බිංදු හැඩය) - 68%": 0.68,
