import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

## -------------------------------------------------------------------------------------------------------
df_a = pd.read_json(r'C:\Users\KDT54\Desktop\KDT_14\[3]STREAMLIT\data\heart_failure_a.json')
df_b = pd.read_json(r'C:\Users\KDT54\Desktop\KDT_14\[3]STREAMLIT\data\heart_failure_b.json')
df = pd.merge(df_a, df_b, on='person_id', how='inner')


# # 그대로 streamlit으로 구현

st.write('그래프를 그려보아용~~~')
g = sns.jointplot(df, x='ejection_fraction', y='age', hue='DEATH_EVENT')
st.pyplot(g.figure)
## -------------------------------------------------------------------------------------------------------

# - 스모킹 여부를 한꺼번에 표시하지 말고 라디오로 선택하여 다른 그래프를 볼 수 있도록 구현
st.write('흡연 여부에 따른 그래프를 그려보아용~~~')
smoking_status = st.radio("흡연여부", ["흡연", "비흡연"])

fig, ax = plt.subplots()

if smoking_status == "흡연":
    st.write("흡연자 그래프")
    g = sns.violinplot(df, x='DEATH_EVENT', y='platelets', hue='smoking', split=True)
else:
    non_smoke_df = df[df['smoking'] == 0]
    sns.violinplot(data=non_smoke_df, x='DEATH_EVENT', y='platelets', color='skyblue', ax=ax)
    
st.pyplot(fig)
## -------------------------------------------------------------------------------------------------------
# 심박출(ejection_fraction)로 범위를 한정하여 그래프 구현
# 심박출의 범위는 slider로 선택하여 그래프를 그려보아용~~~

st.write('ejection_fraction 범위를 선택하여 그래프를 그려보아용~~~')
ran = st.slider("ejection_fraction 범위", 0., 80., (0., 80.))

df_filtered = df[(df['ejection_fraction'] >= ran[0]) & (df['ejection_fraction'] <= ran[1])]


fig, ax = plt.subplots()
sns.histplot(data=df_filtered, x='time', bins=20, hue='DEATH_EVENT', ax=ax)
st.pyplot(fig)