import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('ブログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('文字を入力します')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
# text = st.text_input('あなたの趣味を教えて下さい。')
# 'あなたの好きな数字は', text, 'です。'
#
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション', condition