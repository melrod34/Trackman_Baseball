import altair as alt
import streamlit as st
import matplotlib as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sportypy.surfaces.baseball import NCAAField 

st.set_option('deprecation.showPyplotGlobalUse', False)
trackman_data = pd.read_csv('UNCWBaseballc.csv')
st.write(trackman_data)
fig = NCAAField()


# hitter_options = trackman_data[trackman_data['BatterTeam'] == 'UNC_SEA']['Batter'].unique()
# selected_hitter = st.sidebar.selectbox('Select Hitter:', hitter_options)

# play_result_options = ['Out', 'FieldersChoice', 'Error', 'Sacrifice', 'Single', 'Double', 'Triple', 'HomeRun']
# selected_play_result = st.sidebar.selectbox('Select Play Result:', play_result_options)

# # pitch_options = ['ChangeUp', 'Curveball', 'Cutter', 'Fastball', 'Sinker', 'Slider', 'Splitter']
# # select_pitch = st.sidebar.selectbox('Select Pitch:', pitch_options)

# filtered_data = trackman_data[(trackman_data['Batter'] == selected_hitter) &
#                               (trackman_data['PitchCall'] == 'InPlay') &
#                               (trackman_data['BatterTeam'] == 'UNC_SEA') &
#                               (trackman_data['PlayResult'] == selected_play_result) #&
#                               # (trackman_data['AutoPitchType'] == select_pitch)
#                               ] 

# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='HorizontalDistance', y='Distance', data=filtered_data, hue='PlayResult', marker='o', s=100)
# plt.title(f'{selected_hitter} - Baseball Field with Spray Chart')
# plt.xlabel('Horizontal Distance (feet)')
# plt.ylabel('Vertical Distance (feet)')

st.pyplot()