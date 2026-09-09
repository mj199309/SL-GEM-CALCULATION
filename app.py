import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="MJ GEMS Admin Portal", page_icon="💎", layout="centered")

# --- CUSTOM CSS FOR LUXURY BACKGROUND & PREMIUM STYLING ---
st.markdown(
    """
    <style>
    /* Premium Deep Sapphire Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #060c17 0%, #0b1528 50%, #03070e 100%);
    }
    
    /* Clean text styling over dark theme */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #e2f1ff !important;
    }
    
    /* Subtle neon border around input fields to lock premium look */
    div[data-baseweb="select"], div[data-baseweb="input"], div[data-baseweb="radio"], div[data-baseweb="input-container"] {
        background-color: rgba(15, 27, 49, 0.6) !important;
        border: 1px solid rgba(0, 210, 255, 0.2) !important;
        border-radius: 8px !important;
    }
    
    /* Input element text color adjustment */
    input, select, textarea {
        color: #e2f1ff !important;
    }
    
    /* Metrics panel decoration */
    .metric-box {
        background-color: rgba(0, 210, 255, 0.05);
        border: 1px solid rgba(0, 210, 255, 0.3);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 100% WORKING PURE HTML/CSS 3D ROTATING TITLE EFFECT ---
components.html(
    """
    <div style="display: flex; justify-content: center; align-items: center; background: transparent; height: 140px; overflow: hidden;">
        <div class="rotating-title">💎 MJ GEMS 💎</div>
        <style>
            .rotating-title {
                font-size: 42px;
                font-weight: bold;
                color: #00d2ff;
                font-family: 'Helvetica Neue', Arial, sans-serif;
                text-transform: uppercase;
                letter-spacing: 2px;
                animation: rotateTitle 4s linear infinite;
                transform-style: preserve-3d;
                perspective: 1000px;
            }
            @keyframes rotateTitle {
                0% { transform: rotateY(0deg); text-shadow: 0 0 10px #00d2ff, 0 0 20px #0088cc; }
                50% { transform: rotateY(180deg); text-shadow: 0 0 20px #00ffff, 0 0 30px #00d2ff; }
                100% { transform: rotateY(360deg); text-shadow: 0 0 10px #00d2ff, 0 0 20px #0088cc; }
            }
        </style>
    </div>
    """,
    height=140,
)

# Subheader and Header
st.subheader("💎 ලංකාවේ සැබෑ මැණික් මිල ගණනය යෙදුම")
st.caption("Adjusted Market Rates & Gem Cut Analytics")
st.write("---")

# 1. Gemstone Type (COMPLETE DATA CAPTURED FROM ARUNA GEMS CHART)
base_prices = {
    # === 1. CORUNDUM (කුරුන්දු / කොරන්ඩම්) ===
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
    "ඔට්ටු මැණික් (Ottu Sapphire)": (120000, 300000),

    # === 2. CHRYSOBERYL (කනක) ===
    "කහ කනක (Yellow Chrysoberyl)": (150000, 350000),
    "කොළ කනක (Green Chrysoberyl)": (160000, 380000),
    "පැණි වෛරෝඩි (Cat's Eye - Chrysoberyl)": (550000, 1300000),
    "ඇලෙක්සැන්ඩ්‍රයිට් (Alexandrite)": (850000, 1950000),
    "ඇලෙක්සැන්ඩ්‍රයිට් වෛරෝඩි (Alexandrite Cat's Eye)": (950000, 2200000),

    # === 3. ZIRCON (ප්‍රන්ජුන් / ජාගුන් තෝර) ===
    "සුදු ජාගුන් (Colourless Zircon)": (45000, 95000),
    "සංක ජාගුන් (Golden Zircon)": (55000, 115000),
    "පච්ච තෝර (Green Zircon)": (65000, 135000),
    "දුඹුරු ජාගුන් (Brown Zircon)": (30000, 70000),
    "රතු ජාගුන් (Reddish Zircon)": (45000, 90000),
    "නිල් ජාගුන් (Blue Zircon)": (70000, 150000),

    # === 4. SPINEL (කිරිංචි / කිරිංචිච්) ===
    "රතු කිරිංචි (Red Spinel)": (360000, 360000),
    "රෝස කිරිංචි (Pink Spinel)": (150000, 150000),
    "නිල් කිරිංචි (Blue Spinel)": (180000, 180000),
    "දම් කිරිංචි (Purple Spinel)": (120000, 120000),
    "කළු කිරිංචි (Black Spinel)": (25000, 25000),

    # === 5. GARNET (රබහ / ගෝමේද) ===
    "රතු රබහ (Almandine Garnet)": (35000, 75000),
    "ගෝමේද (Hessonite Garnet)": (45000, 90000),
    "රතු ගානට් (Pyrope Garnet)": (40000, 80000),
    "තැඹිලි ගානට් (Spessartine Garnet)": (60000, 130000),
    "වර්ණ මාරු ගානට් (Colour-change Garnet)": (95000, 210000),
    "ආරුල් ගානට් (Star Garnet)": (50000, 110000),

    # === 6. TOURMALINE (තෝරමල්ලි / තුරමල්ලි) ===
    "පච්ච තෝරමල්ලි (Green Tourmaline)": (75000, 160000),
    "දුඹුරු තෝරමල්ලි (Brown Tourmaline)": (45000, 95000),
    "කළු තෝරමල්ලි (Black Tourmaline)": (15000, 35000),
    "රෝස තෝරමල්ලි (Pink Tourmaline)": (85000, 180000),
    "රූබිලයිට් (Rubellite)": (125000, 270000),
    "බහු වර්ණ තෝරමල්ලි (Multicoloured Tourmaline)": (90000, 195000),

    # === 7. BERYL (බෙරිල් / පඩියන් කුලය) ===
    "පච්ච පඩියන් (Aquamarine)": (110000, 250000),
    "මරකත (Emerald)": (400000, 950000),
    "රන් පඩියන් (Golden Beryl)": (85000, 190000),
    "රෝස බෙරිල් (Morganite)": (95000, 210000),
    "සුදු බෙරිල් (Goshenite)": (35000, 75000),

    # === 8. TOPAZ (පඩියන් / තෝපස්) ===
    "සුදු පඩියන් (Colourless Topaz)": (20000, 45000),
    "කහ පඩියන් (Yellow Topaz)": (45000, 95000),
    "ඉම්පීරියල් තෝපස් (Imperial Topaz)": (180000, 400000),
    "නිල් තෝපස් (Blue Topaz)": (35000, 75000),
    "රෝස තෝපස් (Pink Topaz)": (75000, 160000),

    # === 9. QUARTZ (පළිඟු) ===
    "සුදු පළිඟු (Rock Crystal)": (10000, 25000),
    "දම් පළිඟු (Amethyst)": (30000, 65000),
    "කහ පළිඟු (Citrine)": (25000, 55000),
    "රෝස පළිඟු (Rose Quartz)": (15000, 35000),
    "දුම් පළිඟු (Smoky Quartz)": (15000, 35000),
    "කිරි පළිඟු (Milky Quartz)": (8000, 18000),
    "වෛරෝඩි පළිඟු (Cat's eye Quartz)": (45000, 95000),

    # === 10. FELDSPAR (ලෙල්ස්පාර්) ===
    "පුෂ්පකාන්ත (Moonstone)": (25000, 55000),
    "මහෝත්පල (Orthoclase)": (35000, 75000),
    "ලැබ්‍රඩොරයිට් (Labradorite)": (30000, 65000),

    # === 11. OTHER SRI LANKAN GEMS (තවත් මැණික් වර්ග) ===
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

st.markdown("### 1 මැණික් වර්ගය (GEMSTONE TYPE):")
selected_gem = st.selectbox("තෝරන්න (Select Gemstone):", list(base_prices.keys()), label_visibility="collapsed")

# 2. Gemstone Cut
st.markdown("### 2 කැපුම / හැඩය (GEMSTONE CUT):")
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
selected_cut = st.selectbox("තෝරන්න (Select Cut):", list(cut_options.keys()), label_visibility="collapsed")

# 3. Stone Body Tone
st.markdown("### 3 වර්ණ තීව්රතාවය (STONE BODY TONE):")
tone_options = {
    "Vibrant Tone (දීප්තිමත් වර්ණය)": 1.10,
    "Normal Tone (සාමාන්ය පැහැය)": 1.00,
    "Dark / Brownish Tone (අඳුරු / බොඳ වූ පැහැය)": 0.75
}
selected_tone = st.selectbox("තෝරන්න (Select Tone):", list(tone_options.keys()), label_visibility="collapsed")

# 4. Weight in Carats
st.markdown("### 4 බර කැරට් ප්‍රමාණය (WEIGHT IN CARATS):")
weight = st.number_input("කැරට් ප්‍රමාණය ඇතුලත් කරන්න (Enter Carats):", min_value=0.05, max_value=50.0, value=1.0, step=0.05)

# --- PRICE CALCULATION LOGIC ---
if st.button("💰 මිල ගණනය කරන්න (Calculate Value)"):
    min_base, max_base = base_prices[selected_gem]
    cut_multiplier = cut_options[selected_cut]
    tone_multiplier = tone_options[selected_tone]
    
    # Calculate final price boundaries based on parameters
    final_min_price = min_base * weight * cut_multiplier * tone_multiplier
    final_max_price = max_base * weight * cut_multiplier * tone_multiplier
    
    st.write("---")
    st.markdown("### 📊 ගණනය කරන ලද තක්සේරු මිල (Estimated Valuation):")
    
    # Custom stylized container for final results
    st.markdown(
        f"""
        <div class="metric-box">
            <h2 style='color: #00d2ff; margin: 0;'>LKR {final_min_price:,.2f} - LKR {final_max_price:,.2f}</h2>
            <p style='color: #a4c5e6; font-size: 14px; margin-top: 5px;'>
                තෝරාගත් වර්ගය: <b>{selected_gem}</b> | බර: <b>{weight} Cts</b><br>
                කැපුම් අගය: <b>{selected_cut}</b> | වර්ණ තීව්‍රතාවය: <b>{selected_tone}</b>
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
