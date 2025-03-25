import streamlit as st


st.markdown("""
    <style>
        .stButton > button {
            height: 70px;
            width: 100px;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Calculator 🖩")


# Initialize session state
if "calc_input" not in st.session_state:
    st.session_state.calc_input = ""


input_field = st.text_input("", st.session_state.calc_input, key="display")


# Function to update input field
def add_value(num):
    if num != "=" and num != "AC":
        st.session_state.calc_input += num
    elif num == "=":
        try:
            st.session_state.calc_input = str(eval(st.session_state.calc_input)) 
        except:
            st.session_state.calc_input = "Error"  
    elif num == "AC":
        st.session_state.calc_input = ""
    else:
         st.session_state.calc_input = "Error"  
        


# Button layout
col1, col2, col3, col4, = st.columns(4)

with col1:
    st.button("AC", on_click=add_value, args=("AC",), key="btn1")
    st.button("7", on_click=add_value, args=("7",))
    st.button("4", on_click=add_value, args=("4",))
    st.button("1", on_click=add_value, args=("1",))
    st.button("0", on_click=add_value, args=("0",))

with col2:
    st.button("(", on_click=add_value, args=("(",), key="btn2")
    st.button("8", on_click=add_value, args=("8",))
    st.button("5", on_click=add_value, args=("5",))
    st.button("2", on_click=add_value, args=("2",))
    st.button(".", on_click=add_value, args=(".",), key="btn4")

with col3:
    st.button(")", on_click=add_value, args=(")",), key="btn3")
    st.button("9", on_click=add_value, args=("9",))
    st.button("6", on_click=add_value, args=("6",))
    st.button("3", on_click=add_value, args=("3",))
    st.button("=", on_click=add_value, args=("=",))


with col4:
    st.button("%", on_click=add_value, args=("%",))
    st.button("✖️", on_click=add_value, args=("*",))
    st.button("➖", on_click=add_value, args=("-",))
    st.button("➕", on_click=add_value, args=("+",))
    st.button("➗", on_click=add_value, args=("/",))



