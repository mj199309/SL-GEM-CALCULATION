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

# BASE VALUES (පැරණි ඇප් එකේ මිල ගණන් වලට 100% ක් ගැලපෙන සේ සකසා ඇත)
base_prices = {
    "නිල් මැණික් (Blue Sapphire - Light Blue)": 65625,
    "නිල් මැණික් (Blue Sapphire - Royal Blue)": 180000,
    "නිල් මැණික් (Blue Sapphire - Cornflower Blue)": 150000,
    "නිල් මැණික් (Blue Sapphire - Vivid Blue)": 140000,
    "නිල් මැණික් (Blue Sapphire - Velvet Blue)": 130000,
    "නිල් මැණික් (Blue Sapphire - Peacock Blue)": 120000,
    "නිල් මැණික් (Blue Sapphire - Deep Blue)": 100000,
    "නිල් මැණික් (Blue Sapphire - Medium Blue)": 85000,
    "රතු කැට (Ruby - Pigeon Blood)": 200000,
    "රතු කැට (Ruby - Vivid Red)": 180000,
    "පුෂ්පරාග (Yellow Sapphire)": 90000,
    "පද්මරාග (Padparadscha)": 190000,
    "පැණි වෛරෝඩි (Cat's Eye)": 150000,
    "මරකත (Emerald)": 130000
}

# 1. Main Gemstone Type & Color Category
st.markdown("### 1 මැණික් වර්ගය සහ වර්ණය (GEMSTONE TYPE & COLOR):")
selected_gem = st.selectbox("තෝරන්න (Select Gem):", list(base_prices.keys()), label_visibility="collapsed")

# 2. Gemstone Cut
st.markdown("### 2 කැපුම / හැඩය (GEMSTONE CUT):")
cut_options = {
    "Oval Brilliant Cut (Precision Cut) - 100%": 1.00,
    "Round Cut (රවුන්ඩ් / බ්‍රිලියන්ට්) - 100%": 1.00,
    "Princess Cut (හතරැස් හැඩය) - 0.88": 0.88,
    "Cushion Cut (කුෂන් / කොට්ට හැඩය) - 0.75": 0.75,
    "Native / Local Cut (සම්ප්‍රදායික දේශීය අත් කැපුම) - 0.40": 0.40
}
selected_cut = st.selectbox("තෝරන්න (Select Cut):", list(cut_options.keys()), label_visibility="collapsed")

# 3. Stone Body Tone
st.markdown("### 3 වර්ණ තීව්‍රතාවය (STONE BODY TONE):")
tone_options = {
    "Vibrant Tone (දීප්තිමත් වර්ණය) - 1.00": 1.00,
    "Normal Tone (සාමාන්‍ය පැහැය) - 0.85": 0.85,
    "Very Light / Pale Tone (ඉතා ලා පැහැති) - 0.40": 0.40
}
selected_tone = st.selectbox("තෝරන්න (Select Tone):", list(tone_options.keys()), label_visibility="collapsed")

# 4. Gemstone Clarity
st.markdown("### 4 පැහැදිලි බව (GEMSTONE CLARITY):")
clarity_options = {
    "100% Clean (Eye Clean / සම්පූර්ණ පිරිසිදු) - 1.00": 1.00,
    "90% Clean (Minor inclusions / සුළු රොඩු) - 0.80": 0.80,
    "75% Clean (Slightly Included) - 0.60": 0.60,
    "50% Clean (Heavily Included) - 0.35": 0.35
}
selected_clarity = st.selectbox("තෝරන්න (Select Clarity):", list(clarity_options.keys()), label_visibility="collapsed")

# 5. Treatment / Heat
st.markdown("### 5 පදම් කිරීම (TREATMENT / HEAT):")
treatment_options = {
    "UNHEATED (ස්වභාවික නිල් / රත් නොකළ) - 1.00": 1.00,
    "HEATED (සාමාන්‍ය පරිදි රත් කළ / තැම්බූ) - 0.60": 0.60,
    "TREATED / DIFFUSED (රසායනික ප්‍රතිකර්ම කළ) - 0.25": 0.25
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
    
    # Per Carat Calculation
    per_carat_rate = base_rate * cut_val * tone_val * clarity_val * treatment_val
    
    # Total Valuation with 40% Discount
    final_discounted_value = per_carat_rate * weight * 0.60
    
    # Per Carat Rate for display
    per_carat_display = final_discounted_value / weight if weight > 0 else 0
    min_range = final_discounted_value * 0.85
    max_range = final_discounted_value * 1.15

    st.write("---")
    st.success("📊 ගණනය කරන ලද අවසාන තක්සේරුව සාර්ථකයි!")
    
    # Bypassed st.markdown completely and used 100% isolated iframe components.html to prevent tags showing up
    card_html_content = f"""
    <div style="background: linear-gradient(145deg, #0b1c36 0%, #040d1a 100%); border: 2px solid #00d2ff; box-shadow: 0 0 15px rgba(0, 210, 255, 0.2); padding: 25px; border-radius: 16px; text-align: center; font-family: 'Helvetica Neue', Arial, sans-serif;">
        <div style="font-size: 45px; margin-bottom: 5px; filter: drop-shadow(0 0 8px rgba(0,210,255,0.6)); text-align: center;">💎</div>
        <p style="color: #ceddf0; font-size: 14px; margin: 0 0 5px 0; text-transform: uppercase; letter-spacing: 1px; text-align: center;">තක්සේරුකළ වටිනාකම (Valuation)</p>
        <h2 style="color: #2ecc71; margin: 0 0 15px 0; font-size: 32px; font-weight: bold; text-align: center;">LKR {final_discounted_value:,.2f}</h2>
        
        <div style="border-top: 1px solid rgba(0, 210, 255, 0.2); padding-top: 15px; text-align: left; padding-left: 10px; padding-right: 10px;">
            <p style="color: #e2f1ff; font-size: 15px; margin: 8px 0;">
                <b style="color: #ceddf0;">💰 වෙළඳපොළ සාධාරණ පරාසය:</b> <span style="color: #00d2ff; font-weight: bold;">LKR {min_range:,.2f} - LKR {max_range:,.2f}</span>
            </p>
            <p style="color: #e2f1ff; font-size: 14px; margin: 8px 0;">
                <b style="color: #a4c5e6;">📊 කැරට් එකක අගය (Per Carat):</b> <span style="color: #e2f1ff;">LKR {per_carat_display:,.2f}</span>
            </p>
            <p style="color: #e2f1ff; font-size: 14px; margin: 8px 0;">
                <b style="color: #a4c5e6;">⚖️ මුළු බර ප්‍රමාණය:</b> <span style="color: #2ecc71; font-weight: bold;">{weight} Carats (Cts)</span>
            </p>
        </div>
    </div>
    """
    components.html(card_html_content, height=280)
