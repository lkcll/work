import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="彰化地區互動地圖", page_icon="🗺️", layout="wide")

st.title("彰化地區互動式地圖")

initial_coordinates = [24.0685, 120.5571]
zoom_level = 11

m = folium.Map(location=initial_coordinates, zoom_start=zoom_level, tiles="OpenStreetMap")

with st.sidebar:
    st.header("地圖設定")
    add_marker = st.checkbox("加入自訂標記點")
    if add_marker:
        lat = st.number_input("緯度 (Lat)", value=24.0685)
        lon = st.number_input("經度 (Lon)", value=120.5571)
        marker_info = st.text_input("標記點說明", "這是我的標記點")
        if st.button("新增標記"):
            folium.Marker([lat, lon], popup=marker_info).add_to(m)

folium.Marker(
    location=[24.0813, 120.5381],
    popup="彰化火車站",
    icon=folium.Icon(icon="train", color="blue"),
).add_to(m)

folium.LayerControl().add_to(m)

st_folium(m, width=700, height=500)
