import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



st.set_option('deprecation.showPyplotGlobalUse', False)

def outfield_wall(x):
    a = 340 
    b = 380  
    c = 340  
    t = (x + 90) / 180  
    return (1 - t)**2 * a + 2 * (1 - t) * t * b + t**2 * c

def outfield_line(x):
    a = 100
    b = 160 
    c = 100 
    t = (x + 21) / 42 
    return (1 - t)**2 * a + 2 * (1 - t) * t * b + t**2 * c



def read_data():
    trackman_data = pd.read_csv('UNCWBaseballc.csv')
    return trackman_data
# Select Box
trackman_data = read_data()
hitter_options = trackman_data[trackman_data['BatterTeam'] == 'UNC_SEA']['Batter'].unique()
selected_hitter = st.sidebar.selectbox('Select Hitter:', hitter_options)



play_result_options = ['Out', 'FieldersChoice', 'Error', 'Sacrifice', 'Single', 'Double', 'Triple', 'HomeRun']
selected_play_result = st.sidebar.selectbox('Select Play Result:', play_result_options)
# if selected_play_result == 'All':
#     trackman_data = read_data()
# else:
#     trackman_data = trackman_data[trackman_data['PlayResult'].isin(selected_play_result)]

# hit_type_options = ['GroundBall', 'LineDrive', 'FlyBall', 'Bunt', 'Popup']
# selected_hit_type = st.sidebar.selectbox('Select Hit Type:', hit_type_options)

# pitch_type_options = ['All'] + list(trackman_data['TaggedPitchType'].unique())
# selected_pitch_type = st.sidebar.selectbox('Select Pitch Type:', pitch_type_options)


# if selected_pitch_type != 'All':
#     filtered_data = trackman_data[trackman_data['TaggedPitchType'] == selected_pitch_type]


# Filters
filtered_data = trackman_data[(trackman_data['Batter'] == selected_hitter) &
                              (trackman_data['PitchCall'] == 'InPlay') &
                              (trackman_data['BatterTeam'] == 'UNC_SEA') &
                              (trackman_data['PlayResult'] == selected_play_result) 
                            #   (trackman_data['TaggedPitchType'] == pitch_type_options)
                              ] 



import math

def get_x_y_pos(row):
    row['x_pos'] = math.cos(90 - math.radians(row['Bearing'])) * row['Distance']
    row['y_pos'] = math.sin(90 - math.radians(row['Bearing'])) * row['Distance']
    return row

new_df = filtered_data.apply(get_x_y_pos, axis=1)




# Points
plt.figure(figsize=(20, 15))

scatter = plt.scatter(
    new_df['x_pos'],
    new_df['LastTrackedDistance'],
    c=new_df['ExitSpeed'],  
    cmap='Reds',  
    marker='o',
    s=100
)
cbar = plt.colorbar(scatter, label='ExitSpeed')
cbar.set_label('ExitSpeed', rotation=270, labelpad=15, fontsize = 20)
cbar.set_ticks(np.linspace(new_df['ExitSpeed'].min(), new_df['ExitSpeed'].max(), 5))
cbar.ax.tick_params(labelsize=16)


plt.title(f'{selected_hitter} - Batter Spray Chart', fontsize = 40)

# Foul Lines
plt.plot([-90, 0, 90], [340, 0, 340], color='green', linestyle='--', linewidth=4)  
 

# Wall
x_curve = np.linspace(-90, 90, 100)
y_curve = outfield_wall(x_curve)
plt.plot(x_curve, y_curve, color='red', linewidth=4)

# Outfield Line
x_starting_line = np.linspace(-24, 24, 110)
y_starting_line = outfield_line(x_starting_line)
plt.plot(x_starting_line, y_starting_line, color='orange', linestyle='-', linewidth=4)

# Bases
plt.scatter([0], [127], color='red', marker='s', s=75, zorder=10)
plt.scatter([-24], [90], color='red', marker='s', s=75, zorder=10)
plt.scatter([24], [90], color='red', marker='s', s=75, zorder=10)
plt.scatter([0], [0], color='red', marker='s', s=75, zorder=10)

plt.xlim(-110, 110)
plt.ylim(-10, 425)

st.text('Spray Chart for all UNCW Batters during the 22-23 season.')
st.text('You can use the SelectBoxs on the left side to filter by hit') 
st.text('type as well as each batter. This data was gathered using Tackman.')
st.pyplot()


st.write(new_df)