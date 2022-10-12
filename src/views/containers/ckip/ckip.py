import streamlit as st
from typing import List
from ...services import request

divider_tag = "<hr style='margin-top: 1rem;margin-bottom: 1rem;border: 0;border-top: 1px solid rgba(0,0,0,.1);'/>"


def create_expander(nlp_model: str, visualizer: str, sentence_list: List[str]):
    fetch_method = list(visualizer.keys())[0]
    title = visualizer[fetch_method]
    html_tags = request(fetch_method, nlp_model, sentence_list)
    # html_string = divider_tag.join(html_tags)
    html_string = divider_tag.join(filter(lambda x: x if x is not None else '', html_tags))
    # Sequence item 0: expected str instance, NoneType found: https://bobbyhadz.com/blog/python-typeerror-sequence-item-0-expected-str-instance-nonetype-found

    with st.expander(title, expanded=True):
        st.markdown(html_string, unsafe_allow_html=True)


def display_ckip(nlp_model: str, visualizers: List[str], sentence_list: List[str]):
    for visualizer in visualizers:
        create_expander(nlp_model, visualizer, sentence_list)
