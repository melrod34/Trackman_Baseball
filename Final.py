import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

def outfield_wall(x):
    a = 340 
    b = 380  
    c = 340  
    t = (x + 45) / 90  
    return (1 - t)**2 * a + 2 * (1 - t) * t * b + t**2 * c

def outfield_line(x):
    a = 100
    b = 160 
    c = 100 
    t = (x + 14) / 28 
    return (1 - t)**2 * a + 2 * (1 - t) * t * b + t**2 * c




trackman_data = pd.read_csv('UNCWBaseballc.csv')
st.write(trackman_data)
# Select Box
hitter_options = trackman_data[trackman_data['BatterTeam'] == 'UNC_SEA']['Batter'].unique()
selected_hitter = st.sidebar.selectbox('Select Hitter:', hitter_options)

play_result_options = ['Out', 'FieldersChoice', 'Error', 'Sacrifice', 'Single', 'Double', 'Triple', 'HomeRun']
selected_play_result = st.sidebar.selectbox('Select Play Result:', play_result_options)

# pitch_options = ['ChangeUp', 'Curveball', 'Cutter', 'Fastball', 'Sinker', 'Slider', 'Splitter']
# select_pitch = st.sidebar.selectbox('Select Pitch:', pitch_options)

# Filters
filtered_data = trackman_data[(trackman_data['Batter'] == selected_hitter) &
                              (trackman_data['PitchCall'] == 'InPlay') &
                              (trackman_data['BatterTeam'] == 'UNC_SEA') &
                              (trackman_data['PlayResult'] == selected_play_result) #&
                              # (trackman_data['AutoPitchType'] == select_pitch)
                              ] 


# Points
plt.figure(figsize=(10, 6))
alt.Chart(source).mark_circle(size=60).encode(
    x='Bearing',
    y='LastTrackedDistance',
)
plt.title(f'{selected_hitter} - Batter Spray Chart')

# Foul Lines
plt.plot([-45, 0, 45], [340, 0, 340], color='green', linestyle='--', linewidth=2)  
 

# Wall
x_curve = np.linspace(-45, 45, 100)
y_curve = outfield_wall(x_curve)
plt.plot(x_curve, y_curve, color='red', linewidth=2)

# Outfield Line
x_starting_line = np.linspace(-13.5, 13.5, 100)
y_starting_line = outfield_line(x_starting_line)
plt.plot(x_starting_line, y_starting_line, color='orange', linestyle='-', linewidth=2)

# Bases
plt.scatter([0], [127], color='yellow', marker='s', s=75, zorder=10)
plt.scatter([-12], [90], color='yellow', marker='s', s=75, zorder=10)
plt.scatter([12], [90], color='yellow', marker='s', s=75, zorder=10)
plt.scatter([0], [0], color='yellow', marker='s', s=75, zorder=10)

plt.xlim(-70, 70)



st.pyplot()
