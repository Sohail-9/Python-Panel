import streamlit as st 

st.set_page_config(page_title="OmniqAi", page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Hi :wave:, my name is sohail and currently im learning python panel using streamlit")
    st.title("Software engineer")
    st.write("Tech enthusiast by day and laid-back hacker by night always up for chill time")

# with st.container():
#     st.write("----")
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.header("What I do")
#         st.write("###")
#         st.write(
#             """ 
#             Panel: A powerful and versatile library for building interactive web applications.
#             Bokeh: A well-established library for data visualization and interactive plots.
#             Dash: A high-level framework for building analytical apps.
#             Streamlit: A simple and efficient library for creating data apps.
#             """
#         )

x = st.text_input("skills you have ?")
st.write(f"you have unique skills like: {x}")


st.write("## learning")