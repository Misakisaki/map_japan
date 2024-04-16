import streamlit as st
import pya3rt
import folium
from streamlit_folium import folium_static

apikey = "ZZ9CS9Casc3EzRmRVWGgdTEbhzRLFjZs"

client = pya3rt.TalkClient(apikey)

st.title("Chatbot with streamlit")
st.subheader("メッセージを入力してから送信をタップしてください")
message = st.text_input("メッセージ")

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