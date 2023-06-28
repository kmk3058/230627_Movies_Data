import streamlit as st

# Outer Tabs
tab_menus = ["Tab 1", "Tab 2", "Tab 3"]
tab = st.sidebar.radio("Outer Tabs", tab_menus)

if tab == "Tab 1":
    # Inner Tabs for Tab 1
    inner_tab_menus = ["Inner Tab 1-1", "Inner Tab 1-2"]
    inner_tab = st.radio("Inner Tabs for Tab 1", inner_tab_menus)

    if inner_tab == "Inner Tab 1-1":
        st.write("Content for Inner Tab 1-1")

    elif inner_tab == "Inner Tab 1-2":
        st.write("Content for Inner Tab 1-2")

elif tab == "Tab 2":
    # Inner Tabs for Tab 2
    inner_tab_menus = ["Inner Tab 2-1", "Inner Tab 2-2"]
    inner_tab = st.radio("Inner Tabs for Tab 2", inner_tab_menus)

    if inner_tab == "Inner Tab 2-1":
        st.write("Content for Inner Tab 2-1")

    elif inner_tab == "Inner Tab 2-2":
        st.write("Content for Inner Tab 2-2")

elif tab == "Tab 3":
    # Inner Tabs for Tab 3
    inner_tab_menus = ["Inner Tab 3-1", "Inner Tab 3-2"]
    inner_tab = st.radio("Inner Tabs for Tab 3", inner_tab_menus)

    if inner_tab == "Inner Tab 3-1":
        st.write("Content for Inner Tab 3-1")

    elif inner_tab == "Inner Tab 3-2":
        st.write("Content for Inner Tab 3-2")
