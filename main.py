import streamlit as st
from scrape import scrape_site, extract_html_content, clean_html_content, split_dom_content
from parse import parse_with_ollama




st.title("AI Webscraper")
url = st.text_input("Enter a Website: ")
item = st.text_input("Enter an item: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")

    result = scrape_site(url, item)
    body_content = extract_html_content(result)
    cleaned_content = clean_html_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height= 300)



if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chucks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chucks, parse_description)
            st.write(result)





























































