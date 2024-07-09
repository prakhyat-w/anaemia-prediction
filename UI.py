import streamlit as st
import requests

def fetch_message():
    url = 'http://127.0.0.1:5000/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('message')
    else:
        return None

def main():
    
    st.set_page_config(page_title='Anaemia Prediction')
    page_bg_img = '''
    <style>
    .appview-container.st-emotion-cache-1yiq2ps.ea3mdgi9 {
    background-image: url("https://www.healthcareradius.in/cloud/2022/01/04/eCdRaUvB-anaemia-1200x900.jpeg");
    background-size: cover;
    }
    .st-emotion-cache-1n76uvr.e1f1d6gn2{
    background-color: white;
    width: 110%;
    border-radius: 15px;
    padding: 50px 50px 50px 50px;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title("Anaemia Prediction")
    st.markdown("---")
    text = fetch_message()
    if text is not None:
        st.write("{}".format(text))
    else:
        None

    with st.form(key='values'):
        red = st.slider("Enter Red pixel percentage",39,54,40)
        green = st.slider("Enter Green pixel percentage",25,32,28)
        blue = st.slider("Enter Blue pixel percentage",20,30,25)
        hb = st.slider("Enter HB",2.8,16.3,7.5)
        gender = st.radio('Select gender',options=['Male','Female'])
        if gender == 'Male':
            M = 1
        else:
            M = 0
        submit = st.form_submit_button('Predict')
        if submit:
            user_data = {'red':red,'green': green,'blue': blue,'hb':hb,'M':M}
            url = 'http://127.0.0.1:5000/predict/'
            response = requests.post(url,json= user_data)
            print(response.status_code)

            if response.status_code == 200:
                result = response.json().get('result')
                print(result)
                if int(result) == 1:
                    st.success("You are Anaemic!")
                elif int(result) == 0:
                    st.success("You are Not Anaemic")  
            else:
                st.error('Error submitting data')

if __name__ == '__main__':
    main()    
