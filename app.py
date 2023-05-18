import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('streamlit test')
st.write('data frame')

'Start!!!'
latest_ite = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_ite.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!'

left_colum, right_colum = st.columns(2)
button = left_colum.button('右カラム表示')
if button:
    right_colum.write('右カラム')

exp = st.expander('問い合わせ')
exp.write('問い合わせの回答')

cond = st.sidebar.slider('調子は', 0, 100, 50)
'調子は', cond, 'です。'

option = st.sidebar.text_input('趣味は')
'趣味は', option, 'です。'

option = st.selectbox(
    '数字',
    list(range(1,11))
)
'数字は', option, 'です。'

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img, caption='Sample', use_column_width=True)

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import pandas as pd
import numpy as np
```
"""

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

