import streamlit as st
import pandas as pd
st.title('فرم نظرسنجی برای جمع‌آوری بازخورد کاربران')

# ایجاد فرم نظرسنجی
with st.form(key='survey_form'):
    name = st.text_input('نام')
    email = st.text_input('ایمیل')
    rating = st.slider('امتیاز شما به محصول یا خدمات (از ۱ تا ۵)', 1, 5)
    feedback = st.text_area('نظرات و پیشنهادات شما')
    submit_button = st.form_submit_button(label='ارسال')

if submit_button:
  
    data = {
        'نام': [name],
        'ایمیل': [email],
        'امتیاز': [rating],
        'نظرات': [feedback]
    }
    df = pd.DataFrame(data)
    df.to_csv('survey_results.csv', mode='a', header=False, index=False)
    
    st.success('نظر شما با موفقیت ثبت شد!')

st.header('داده‌های جمع‌آوری شده')
try:
    survey_data = pd.read_csv('survey_results.csv', names=['نام', 'ایمیل', 'امتیاز', 'نظرات'])
    st.dataframe(survey_data)

    st.header('تحلیل داده‌ها')
    avg_rating = survey_data['امتیاز'].mean()
    st.write(f'میانگین امتیاز: {avg_rating:.2f}')
    
    st.write('تعداد نظرات بر اساس امتیاز:')
    st.bar_chart(survey_data['امتیاز'].value_counts())
    
except FileNotFoundError:
    st.write('هنوز هیچ داده‌ای ثبت نشده است.')

# اجرای برنامه استریم لیت
# در ترمینال اجرا کنید: streamlit run survey_app.py
