import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(page_title="MJ GEMS Admin Portal", page_icon="💎", layout="centered")

# --- CUSTOM CSS FOR PREMIUM STYLING ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #060c17 0%, #0b1528 50%, #03070e 100%);
    }
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #e2f1ff !important;
    }
    div[data-baseweb="select"], div[data-baseweb="input"], div[data-baseweb="radio"], div[data-baseweb="input-container"] {
        background-color: rgba(15, 27, 49, 0.6) !important;
        border: 1px solid rgba(0, 210, 255, 0.2) !important;
        border-radius: 8px !important;
    }
    input, select, textarea {
        color: #e2f1ff !important;
    }
    .metric-box {
        background-color: rgba(0, 210, 255, 0.05);
        border: 1px solid rgba(0, 210, 255, 0.3);
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-top: 10px;
    }
    .detail-container {
        background-color: rgba(11, 21, 40, 0.8);
        border: 1px solid rgba(0, 210, 255, 0.15);
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 3D ROTATING TITLE EFFECT ---
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

st.subheader("💎 ලංකාවේ සැබෑ මැණික් මිල ගණනය යෙදුම")
st.caption("Advanced Gem Valuation & Treatment Matrix (40% Discount Enabled)")
st.write("---")

# BASE VALUES (Based on Per-Carat baseline calculation from your original system)
base_prices = {
    "නිල් මැණික් (Blue Sapphire - Royal Blue)": 850000,
    "නිල් මැණික් (Blue Sapphire - Cornflower Blue)": 750000,
    "නිල් මැණික් (Blue Sapphire - Vivid Blue)": 700000,
    "නිල් මැණික් (Blue Sapphire - Velvet Blue)": 650000,
    "නිල් මැණික් (Blue Sapphire - Peacock Blue)": 600000,
    "නිල් මැණික් (Blue Sapphire - Deep Blue)": 550000,
    "නිල් මැණික් (Blue Sapphire - Medium Blue)": 450000,
    "නිල් මැණික් (Blue Sapphire - Light Blue)": 300000,
    "රතු කැට (Ruby - Pigeon Blood)": 950000,
    "රතු කැට (Ruby - Vivid Red)": 850000,
    "පුෂ්පරාග (Yellow Sapphire)": 400000,
    "පද්මරාග (Padparadscha)": 900000,
    "පැණි වෛරෝඩි (Cat's Eye)": 750000,
    "මරකත (Emerald)": 600000
}

# 1. Main Gemstone Type & Color Category
st.markdown("### 1 මැණික් වර්ගය සහ වර්ණය (GEMSTONE TYPE & COLOR):")
selected_gem = st.selectbox("තෝරන්න (Select Gem):", list(base_prices.keys()), label_visibility="collapsed")

# 2. Gemstone Cut
st.markdown("### 2 කැපුම / හැඩය (GEMSTONE CUT):")
cut_options = {
    "Oval Brilliant Cut (Precision Cut) - 100%": 1.00,
    "Round Cut (රවුන්ඩ් / බ්‍රිලියන්ට්) - 100%": 1.00,
    "Princess Cut (හතරැස් හැඩය) - 88%": 0.88,
    "Cushion Cut (කුෂන් / කොට්ට හැඩය) - 75%": 0.75,
    "Native / Local Cut (සම්ප්‍රදායික දේශීය අත් කැපුම) - 40%": 0.40
}
selected_cut = st.selectbox("තෝරන්න (Select Cut):", list(cut_options.keys()), label_visibility="collapsed")

# 3. Stone Body Tone
st.markdown("### 3 වර්ණ තීව්‍රතාවය (STONE BODY TONE):")
tone_options = {
    "Vivid Tone (දීප්තිමත් වර්ණය) - 100%": 1.00,
    "Normal Tone (සාමාන්‍ය පැහැය) - 85%": 0.85,
    "Very Light / Pale Tone (ඉතා ලා පැහැති) - 40%": 0.40
}
selected_tone = st.selectbox("තෝරන්න (Select Tone):", list(tone_options.keys()), label_visibility="collapsed")

# 4. Gemstone Clarity
st.markdown("### 4 පැහැදිලි බව (GEMSTONE CLARITY):")
clarity_options = {
    "100% Clean (Eye Clean / සම්පූර්ණ පිරිසිදු) - 100%": 1.00,
    "90% Clean (Minor inclusions / සුළු රොඩු) - 80%": 0.80,
    "75% Clean (Slightly Included) - 60%": 0.60,
    "50% Clean (Heavily Included) - 35%": 0.35
}
selected_clarity = st.selectbox("තෝරන්න (Select Clarity):", list(clarity_options.keys()), label_visibility="collapsed")

# 5. Treatment / Heat (බොහෝ සෙයින් ඉල්ලා සිටි කොටස)
st.markdown("### 5 පදම් කිරීම (TREATMENT / HEAT):")
treatment_options = {
    "UNHEATED (ස්වභාවික නිල් / රත් නොකළ) - 100%": 1.00,
    "HEATED (සාමාන්‍ය පරිදි රත් කළ / තැම්බූ) - 60%": 0.60,
    "TREATED / DIFFUSED (රසායනික ප්‍රතිකර්ම කළ) - 25%": 0.25
}
selected_treatment = st.radio("තෝරන්න (Select Treatment):", list(treatment_options.keys()), label_visibility="collapsed")

# 6. Weight in Carats
st.markdown("### 6 බර කැරට් ප්‍රමාණය (WEIGHT IN CARATS):")
weight = st.number_input("කැරට් ප්‍රමාණය ඇතුලත් කරන්න (Enter Carats):", min_value=0.05, max_value=50.0, value=0.25, step=0.05)

# --- CALCULATE LOGIC ---
if st.button("💰 මිල ගණනය කරන්න (Calculate Value)"):
    base_rate = base_prices[selected_gem]
    cut_val = cut_options[selected_cut]
    tone_val = tone_options[selected_tone]
    clarity_val = clarity_options[selected_clarity]
    treatment_val = treatment_options[selected_treatment]
    
    # Per Carat Calculation incorporating all factors
    per_carat_rate = base_rate * cut_val * tone_val * clarity_val * treatment_val
    
    # Total Valuation
    total_market_value = per_carat_rate * weight
    
    # 40% Discount Applied Value
    final_discounted_value = total_market_value * 0.60
    
    # Generate Range Boundaries (±15% for fair market spread)
    min_range = final_discounted_value * 0.85
    max_range = final_discounted_value * 1.15

    st.write("---")
    
    # Output UI matching your premium format
    st.markdown(
        f"""
        <div class="metric-box" style="background-color: rgba(46, 204, 113, 0.1); border: 1px solid #2ecc71;">
            <h3 style='color: #2ecc71; margin: 0; font-size: 22px;'>තක්සේරුකළ වටිනාකම: LKR {final_discounted_value:,.2f}</h3>
            <p style='color: #a4c5e6; font-size: 15px; margin: 10px 0 5px 0;'>
                <b>වෙළඳපොළ සාධාරණ පරාසය:</b> LKR {min_range:,.2f} - LKR {max_range:,.2f}
            </p>
            <p style='color: #ceddf0; font-size: 13px; margin: 0;'>
                <b>කැරට් එකක අගය (Per Carat Rate):</b> LKR {per_carat_rate:,.2f}
            </p>
            
            <!-- DETAIL BOX -->
            <div class="detail-container">
                <h4 style="color: #00d2ff; margin: 0 0 8px 0; font-size: 14px; border-bottom: 1px solid rgba(0, 210, 255, 0.2);">📝 සාරාංශය (Detail Box):</h4>
                <p style="margin: 2px 0; font-size: 12px;">💎 වර්ගය: {selected_gem}</p>
                <p style="margin: 2px 0; font-size: 12px;">✂️ කැපුම: {selected_cut.split(' - ')[0]}</p>
                <p style="margin: 2px 0; font-size: 12px;">🔍 පැහැදිලි බව: {selected_clarity.split(' - ')[0]}</p>
                <p style="margin: 2px 0; font-size: 12px;">🔥 පදම් කිරීම: {selected_treatment.split(' - ')[0]}</p>
                <p style="margin: 2px 0; font-size: 12px;">⚖️ බර: {weight} Cts</p>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
