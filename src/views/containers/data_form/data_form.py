from matplotlib.pyplot import title
import pandas as pd
import re
import streamlit as st
from .utils import clean_data
from ...components.form import form_controller


def display_data_form():
    ptt_df = pd.read_csv('./src/views/containers/ptt_gossiping_clean.csv')
    category = st.selectbox('下拉選擇文句來源', options=['Select', '自行輸入','新聞', '問卦', '爆卦'])
    if category == '新聞':
        ptt_df = ptt_df[ptt_df['category'] == '新聞']
    elif category == '問卦':
        ptt_df = ptt_df[ptt_df['category'] == '問卦']
    elif category == '爆卦':
        ptt_df = ptt_df[ptt_df['category'] == '爆卦']
    
    # dependant selectbox: https://discuss.streamlit.io/t/depdendant-selectbox/17260/4
    if category != 'Select' and category != '自行輸入':
        content = st.selectbox('下拉選擇文章標題', options=ptt_df['title'])
        article = ptt_df['content'].loc[ptt_df['title']==content].item()
        # ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().: https://www.statology.org/python-truth-value-of-series-is-ambiguous/
        data = re.sub('\n\n', '', article)
        sub_data = re.sub('\\s', '', data)
        if article:
            input_data: str = st.text_area("你所選擇的文篇：", data, height=200)
            st.write('輸入字數：{}'.format(len(sub_data)))
            # st.text_area: https://docs.streamlit.io/library/api-reference/widgets/st.text_area
        
    elif category == '自行輸入':
        input = st.text_area("請輸入文句：", height=200)
        input_data: str = input
        sub_input_data = re.sub('\\s', '', input)
        if input:    
            st.write('輸入字數：{}'.format(len(sub_input_data)))
        
    
    submitted = st.button("確定")

    if submitted:
        cleaned_data = clean_data(input_data.strip())

        if not cleaned_data:
            st.error("請輸入句子！")
            return False

        st.session_state["input_data"] = cleaned_data
        return cleaned_data
