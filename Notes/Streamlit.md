
# 🧠 STREAMLIT FULL CHEAT SHEET — 2025 Edition

> Build web apps with Python 🚀

---

## 🔧 1. **Installation**

```bash
pip install streamlit
```

To run:

```bash
streamlit run your_app.py
```

---

## 🛠️ 2. **Basic Setup**

```python
import streamlit as st
import pandas as pd
import numpy as np
```

App configuration (set title & layout):

```python
st.set_page_config(page_title="My App", layout="wide", initial_sidebar_state="expanded")
```

---

## 📝 3. **Text Elements**

```python
st.title("Main Title")
st.header("Header")
st.subheader("Subheader")
st.text("This is plain text.")
st.markdown("### Markdown Heading\n**Bold** *Italic*")
st.caption("This is a caption.")
st.code("print('Hello World')", language='python')
st.latex(r"\frac{a}{b} = c")
```

---

## 🧮 4. **Display Data**

```python
df = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])

st.write(df)              # Auto-detect display
st.dataframe(df)          # Interactive table
st.table(df)              # Static table
st.json({"name": "Selva", "score": 95})
```

---

## 🎮 5. **Widgets / Inputs**

```python
name = st.text_input("Enter your name")
age = st.number_input("Your Age", min_value=1)
bio = st.text_area("About you")

option = st.selectbox("Choose option", ["A", "B", "C"])
multi = st.multiselect("Choose multiple", ["X", "Y", "Z"])
date = st.date_input("Pick a date")
time = st.time_input("Pick a time")

agree = st.checkbox("I agree")
gender = st.radio("Gender", ["Male", "Female", "Other"])

slider = st.slider("Volume", 0, 100)
upload = st.file_uploader("Upload a file")
camera = st.camera_input("Take a picture")

btn = st.button("Click Me")
```

---

## 📊 6. **Charts & Graphs**

### Basic Charts

```python
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
```

### Matplotlib

```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(df["A"])
st.pyplot(fig)
```

### Seaborn

```python
import seaborn as sns
fig = sns.heatmap(df.corr())
st.pyplot(fig)
```

### Plotly

```python
import plotly.express as px
fig = px.line(df, x=df.index, y="A")
st.plotly_chart(fig)
```

---

## 🎞️ 7. **Media Elements**

```python
st.image("file.png", caption="Sample Image", use_column_width=True)
st.audio("audio.mp3")
st.video("video.mp4")
```

---

## 🗃️ 8. **Layouts and Containers**

```python
st.sidebar.title("Sidebar Title")
st.sidebar.selectbox("Pick", ["One", "Two"])

col1, col2 = st.columns(2)
with col1:
    st.write("Left side")
with col2:
    st.write("Right side")

with st.expander("Click to expand"):
    st.write("Hidden content")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
```

---

## 🔁 9. **Control Flow**

```python
if st.button("Run"):
    st.success("You clicked Run!")

st.stop()  # Stops app execution

with st.spinner("Loading..."):
    time.sleep(2)

st.success("Done!")
st.error("Something went wrong!")
st.warning("Be careful!")
st.info("Just a heads-up.")
```

---

## 🧪 10. **Forms**

```python
with st.form("form1"):
    name = st.text_input("Name")
    submit = st.form_submit_button("Submit")
    if submit:
        st.write("Hello", name)
```

---

## 🗂️ 11. **Session State (Save user inputs)**

```python
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase"):
    st.session_state.counter += 1

st.write("Count:", st.session_state.counter)
```

---

## 🚀 12. **Caching Functions**

```python
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")
```

Old (now deprecated):

```python
@st.cache
def my_func():
    ...
```

---

## 🗃️ 13. **Working with Files**

```python
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)
```

---

## 🌐 14. **API Requests**

```python
import requests
res = requests.get("https://api.github.com")
st.json(res.json())
```

---

## 🧰 15. **Utilities**

```python
import time
st.progress(0)
for i in range(100):
    st.progress(i + 1)
    time.sleep(0.01)
```

---

## 🧱 16. **HTML & CSS (limited)**

```python
st.markdown("""
<div style="background-color:#f1f1f1;padding:10px;border-radius:10px">
    <h3 style="color:green;">Custom HTML Box</h3>
</div>
""", unsafe_allow_html=True)
```

---

## 📁 17. **Multiple Pages (New Format)**

Use `pages/` folder.

```text
your_app/
├── Home.py
├── pages/
│   ├── 1_About.py
│   └── 2_Analysis.py
```

In each file:

```python
st.title("Page Name")
```

---

## 🌍 18. **Deploy Streamlit App**

### Option 1: Streamlit Cloud

* Push to GitHub
* Go to: [https://share.streamlit.io](https://share.streamlit.io)
* Connect repo & deploy

### Option 2: Local network

```bash
streamlit run app.py --server.address=0.0.0.0
```

---

## 📚 19. **Useful Resources**

| 🔗 Tool | URL                                                          |
| ------- | ------------------------------------------------------------ |
| Docs    | [https://docs.streamlit.io](https://docs.streamlit.io)       |
| Gallery | [https://streamlit.io/gallery](https://streamlit.io/gallery) |
| Deploy  | [https://streamlit.io/cloud](https://streamlit.io/cloud)     |

---

## ✅ 20. **Best Practices**

* Use **sidebar** for filters and navigation
* Use **@st.cache\_data** for expensive operations
* Handle file upload and type-checks carefully
* Design with columns/tabs for clean UI
* Use **session\_state** for user interaction tracking

---
