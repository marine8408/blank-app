import streamlit as st
import xmltodict
import requests

def main():
    url = 'https://api.vworld.kr/ned/wfs/getLandUseWFS?typename=dt_d154&bbox=37.5296746178359,127.19724442364,37.5313916173634,127.200314866579,EPSG:4326&pnu=4145011800100320003&maxFeatures=10&resultType=results&srsName=EPSG:4326&output=text/xml; subtype=gml/2.1.2&key=86DD225C-DC5B-3B81-B9EB-FB135EEEB78C&domain='
    req = requests.get(url)
    req.text


    st.write("네")

main()

st.title("🎈 My new app")
st.write(
)
