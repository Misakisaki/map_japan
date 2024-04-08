import streamlit as st
import folium
from streamlit_folium import folium_static

def main():
    st.title('日本の詳細な地図表示アプリ')

    # 日本の中心座標
    japan_coords = (35.682839, 139.759455)

    # foliumの地図オブジェクトを作成
    m = folium.Map(location=japan_coords, zoom_start=5)

    # 地図をStreamlitアプリに表示
    folium_static(m)

if __name__ == '__main__':
    main()

    