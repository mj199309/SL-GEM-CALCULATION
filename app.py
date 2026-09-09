import streamlit as st
import time

# Page configuration for desktop and mobile scaling
st.set_page_config(page_title="MJ GEMS Admin Portal", page_icon="💎", layout="centered")

# --- 1. LUXURY GEMSTONES ROTATING LOADER ANIMATION (5 SECONDS) ---
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
          .loading-text { margin-top: 25px; font-family: sans-serif; font-size: 20px; font-weight: 500; color: #e2f1ff; letter-spacing: 3px; text-transform: uppercase; animation: pulseText 1.5s ease-in-out infinite; }
          @keyframes pulseText { 0%, 100% { opacity: 0.5; } 50% { opacity: 1; } }
        </style>
        """,
        unsafe_allow_html=True
    )
    time.sleep(5.0)
    st.session_state.loaded = True
    st.rerun()

# --- 2. CUSTOM CSS FOR LUXURY DARK THEME BACKGROUND ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #060c17, #0b1528, #03070e);
    }
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #e2f1ff !important;
    }
    div[data-baseweb="select"], div[data-baseweb="input"], div[data-baseweb="radio"] {
        background-color: rgba(15, 27, 49, 0.8) !important;
        border: 1px solid rgba(0, 210, 255, 0.3) !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] span {
        white-space: normal !important;
        word-break: break-word !important;
    }
    .metric-box {
        background-color: rgba(0, 210, 255, 0.05);
        border: 1px solid rgba(0, 210, 255, 0.3);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 10px;
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

# Data Registry Category Groups (Aruna Gems Standard)
categories = [
    "CORUNDUM (කුරුන්දු / සෆයාර්)",
    "CHRYSOBERYL (කනක / වෛරෝඩි)",
    "SPINEL (කිරිංචි / ස්පිනෙල්)",
    "GARNET (රබහ / ගෝමේද)",
    "TOURMALINE (තෝරමල්ලි)",
    "BERYL & TOPAZ (බෙරිල් සහ තෝපස්)",
    "QUARTZ & FELDSPAR (පළිඟු / පුෂ්පකාන්ත)",
    "OTHER GEMS (දුර්ලභ සහ අනෙකුත් මැණික් වර්ග)"
]
st.markdown("### 1 මැණික් කාණ්ඩය (GEMSTONE CATEGORY):")
selected_cat = st.selectbox("කාණ්ඩය තෝරන්න:", categories, label_visibility="collapsed")

gem_registry = {
    "CORUNDUM (කුරුන්දු / සෆයාර්)": {
        "නිල් මැණික් (Blue Sapphire)": (475000, 1150000),
        "පුෂ්පරාග (Yellow Sapphire)": (250000, 600000),
        "රෝස සෆයාර් (Pink Sapphire)": (180000, 420000),
        "සුදු සෆයාර් (White Sapphire)": (65000, 150000),
        "කොළ සෆයාර් (Green Sapphire)": (75000, 180000),
        "පද්මරාග (Padparadscha)": (525000, 1500000),
        "රතු කැට (Ruby)": (900000, 1850000),
        "ආරුල් නිල් මැණික් (Star Sapphire)": (220000, 650000),
        "ආරුල් රතු කැට (Star Ruby)": (350000, 850000),
        "ගෙවුඩ (Geuda)": (50000, 120000),
        "ඔට්ටු මැණික් (Ottu Sapphire)": (120000, 300000)
    },
    "CHRYSOBERYL (කනක / වෛරෝඩි)": {
        "කහ කනක (Yellow Chrysoberyl)": (150000, 350000),
        "කොළ කනක (Green Chrysoberyl)": (160000, 380000),
        "පැණි වෛරෝඩි (Cat's Eye - Chrysoberyl)": (550000, 1300000),
        "ඇලෙක්සැන්ඩ්‍රයිට් (Alexandrite)": (850000, 1950000),
        "ඇලෙක්සැන්ඩ්‍රයිට් වෛරෝඩි (Alexandrite Cat's Eye)": (950000, 2200000)
    },
    "SPINEL (කිරිංචි / ස්පිනෙල්)": {
        "රතු කිරිංචි (Red Spinel)": (360000, 360000),
        "රෝස කිරිංචි (Pink Spinel)": (150000, 150000),
        "නිල් කිරිංචි (Blue Spinel)": (180000, 180000),
        "දම් කිරිංචි (Purple Spinel)": (120000, 120000),
        "කළු කිරිංචි (Black Spinel)": (25000, 25000)
    },
    "GARNET (රබහ / ගෝමේද)": {
        "රතු රබහ (Almandine Garnet)": (35000, 75000),
        "ගෝමේද (Hessonite Garnet)": (45000, 90000),
        "රතු ගානට් (Pyrope Garnet)": (40000, 80000),
        "තැඹිලි ගානට් (Spessartine Garnet)": (60000, 130000),
        "වර්ණ මාරු ගානට් (Colour-change Garnet)": (95000, 210000),
        "ආරුල් ගානට් (Star Garnet)": (50000, 110000)
    },
    "TOURMALINE (තෝරමල්ලි)": {
        "පච්ච තෝරමල්ලි (Green Tourmaline)": (75000, 160000),
        "දුඹුරු තෝරමල්ලි (Brown Tourmaline)": (45000, 95000),
        "කළු තෝරමල්ලි (Black Tourmaline)": (15000, 35000),
        "රෝස තෝරමල්ලි (Pink Tourmaline)": (85000, 180000),
        "රූබිලයිට් (Rubellite)": (125000, 270000),
        "බහු වර්ණ තෝරමල්ලි (Multicoloured Tourmaline)": (90000, 195000)
    },
    "BERYL & TOPAZ (බෙරිල් සහ තෝපස්)": {
        "පච්ච පඩියන් (Aquamarine)": (110000, 250000),
        "මරකත (Emerald)": (400000, 950000),
        "රන් පඩියන් (Golden Beryl)": (85000, 190000),
        "රෝස බෙරිල් (Morganite)": (95000, 210000),
        "සුදු බෙරිල් (Goshenite)": (35000, 75000),
        "සුදු තෝපස් (Colourless Topaz)": (20000, 45000),
        "කහ තෝපස් (Yellow Topaz)": (45000, 95000),
        "ඉම්පීරියල් තෝපස් (Imperial Topaz)": (180000, 400000),
        "නිල් තෝපස් (Blue Topaz)": (35000, 75000),
        "රෝස තෝපස් (Pink Topaz)": (75000, 160000)
    },
    "QUARTZ & FELDSPAR (පළිඟු / පුෂ්පකාන්ත)": {
        "සුදු පළිඟු (Rock Crystal)": (10000, 25000),
        "දම් පළිඟු (Amethyst)": (30000, 65000),
        "කහ පළිඟු (Citrine)": (25000, 55000),
        "රෝස පළිඟු (Rose Quartz)": (15000, 35000),
        "දුම් පළිඟු (Smoky Quartz)": (15000, 35000),
        "කිරි පළිඟු (Milky Quartz)": (8000, 18000),
        "වෛරෝඩි පළිඟු (Cat's eye Quartz)": (45000, 95000),
        "පුෂ්පකාන්ත (Moonstone)": (25000, 55000),
        "මහෝත්පල (Orthoclase)": (35000, 75000),
        "ලැබ්‍රඩොරයිට් (Labradorite)": (30000, 65000)
    },
    "OTHER GEMS (දුර්ලභ සහ අනෙකුත් මැණික් වර්ග)": {
        "සුදු ජාගුන් (Colourless Zircon)": (45000, 95000),
        "සංක ජාගුන් (Golden Zircon)": (55000, 115000),
        "පච්ච තෝර (Green Zircon)": (65000, 135000),
        "දුඹුරු ජාගුන් (Brown Zircon)": (30000, 70000),
        "රතු ජාගුන් (Reddish Zircon)": (45000, 90000),
        "නිල් ජාගුන් (Blue Zircon)": (70000, 150000),
        "පෙරිඩොට් (Peridot)": (65000, 140000),
        "අයොලයිට් (Iolite)": (40000, 85000),
        "ස්කැපොලයිට් (Scapolite)": (35000, 75000),
        "ඩයොප්සයිඩ් (Dioside)": (30000, 65000),
        "සිංහලයිට් (Sinhalite)": (150000, 350000),
        "තාෆීට් (Taaffeite)": (850000, 2500000),
        "එකනයිට් (Ekanite)": (50000, 110000),
        "සෙරන්ඩිබයිට් (Serendibite)": (950000, 3000000),
        "දියමන්ති / වජ්‍ර (Diamond)": (1500000, 3500000),
        "මුතු (Pearl)": (100000, 450000),
        "පබළු (Coral)": (25000, 60000)
    }
}

st.markdown("### 2 මැණික් වර්ගය සහ වර්ණය (GEMSTONE TYPE & COLOR):")
available_gems = gem_registry.get(selected_cat, {})
selected_gem = st.selectbox("වර්ගය තෝරන්න:", list(available_gems.keys()), label_visibility="collapsed")

cut_options = {
    "Round Cut (රවුන්ඩ් / බ්‍රිලියන්ට්) - 100%": 1.00,
    "Princess Cut (ප්‍රින්සස් / හතරැස් හැඩය) - 88%": 0.88,
    "Marquise Cut (මාර්කිස් / ඔරු හැඩය) - 82%": 0.82,
    "Oval Cut (ඕවල් / ප්‍රමිතිගත බිත්තර හැඩය) - 75%": 0.75,
    "Cushion Cut (කුෂන් / කොට්ට හැඩය) - 70%": 0.70,
    "Pear Cut (පෙයාර් / කඳුළු බිංදු හැඩය) - 68%": 0.68,
    "Emerald Cut (එමරල්ඩ් / පියගැටපෙළ හැඩය) - 62%": 0.62,
    "Native / Local Cut (සම්ප්‍රදායික දේශීය අත් කැපුම) - 40%": 0.40
}
st.markdown("### 3 කැපුම / හැඩය (GEMSTONE CUT):")
selected_cut = st.selectbox("කැපුම තෝරන්න:", list(cut_options.keys()), label_visibility="collapsed")

tone_options = {
    "Vibrant Tone (දීප්තිමත් වර්ණය)": 1.10,
    "Normal Tone (සාමාන්ය පැහැය)": 1.00,
    "Dark / Brownish Tone (අඳුරු පැහැය)": 0.65
}
st.markdown("### 4 වර්ණ තීව්රතාවය (STONE BODY TONE):")
selected_tone = st.selectbox("පැහැය තෝරන්න:", list(tone_options.keys()), label_visibility="collapsed")

clarity_options = {
    "100% Good (Pure / Clean)": 1.00, "90% Clean": 0.90, "80% Clean": 0.80, "70% Clean": 0.70,
    "60% Slight Inclusions": 0.60, "50% Inclusions": 0.50, "40% Medium Inclusions": 0.40,
