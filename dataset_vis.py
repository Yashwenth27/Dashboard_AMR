import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

# Navbar HTML
navbar_html = '''
<style>
    .st-emotion-cache-12fmjuu{
        z-index: 100;
    }
    .st-emotion-cache-h4xjwg{
        z-index: 100;
    }
    h2{
    color: white;
    }
    .css-hi6a2p {padding-top: 0rem;}
    .navbar {
        background-color: #355E3B;
        padding: 0.3rem;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .navbar .logo {
        display: flex;
        align-items: center;
    }
    .navbar .logo img {
        height: 40px;
        margin-right: 10px;
    }
    .navbar .menu {
        display: flex;
        gap: 1.5rem;
    }
    .navbar .menu a {
        color: white;
        font-size: 1.2rem;
        text-decoration: none;
    }
    .content {
        padding-top: 5rem;  /* Adjust this based on navbar height */
    }
</style>

<nav class="navbar">
    <div class="logo">
        <h2 id="hh">Antimicrobial Resistant Dashboard</h2>
    </div>
    <div class="menu">
        <a href="">Dashboard</a>
        <a href="mvp">Multi Variable Plots</a>
        <a href="mlp">ML Predictions</a>
        <a href="ml-predictions">About Us</a>
    </div>
</nav>

<div class="content">
'''

# Injecting the navigation bar and content padding into the Streamlit app
st.markdown(navbar_html, unsafe_allow_html=True)
custom_css = """
<style>
    button {
        background-color: white;
        color: green;
        border: 2px solid green;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 0.9rem;
        cursor: pointer;
        text-align: center;
        display: inline-block;
        text-decoration: none;
    }
    button:hover {
        background-color: lightgreen;
        color: black;
    }
</style>
"""

# Inject custom CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

z,x = st.columns([0.9,0.1])
with z:
    st.title("Dataset Overview")


st.markdown("""
    <hr style="border: 3px solid green;" />
    """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# Load country data
country_data = pd.read_excel('countrycount.xlsx')

# Define latitude and longitude for centering the map on specific countries
lat_lon_data = {
    'Argentina': [-38.4161, -63.6167],
    'Australia': [-25.2744, 133.7751],
    'Austria': [47.5162, 14.5501],
    'Belgium': [50.8503, 4.3517],
    'Brazil': [-14.2350, -51.9253],
    'Bulgaria': [42.7339, 25.4858],
    'Cameroon': [3.8480, 11.5021],
    'Canada': [56.1304, -106.3468],
    'Chile': [-35.6751, -71.5430],
    'China': [35.8617, 104.1954],
    'Colombia': [4.5709, -74.2973],
    'Costa Rica': [9.7489, -83.7534],
    'Croatia': [45.1, 15.2],
    'Czech Republic': [49.8175, 15.4730],
    'Denmark': [56.2639, 9.5018],
    'Dominican Republic': [18.7357, -70.1627],
    'Ecuador': [-1.8312, -78.1834],
    'Egypt': [26.8206, 30.8025],
    'El Salvador': [13.7942, -88.8965],
    'Finland': [61.9241, 25.7482],
    'France': [46.6034, 1.8883],
    'Germany': [51.1657, 10.4515],
    'Ghana': [7.9465, -1.0232],
    'Greece': [39.0742, 21.8243],
    'Guatemala': [15.7835, -90.2308],
    'Honduras': [15.2000, -86.2419],
    'Hong Kong': [22.3193, 114.1694],
    'Hungary': [47.1625, 19.5033],
    'India': [20.5937, 78.9629],
    'Indonesia': [-0.7893, 113.9213],
    'Ireland': [53.1424, -7.6921],
    'Israel': [31.0461, 34.8516],
    'Italy': [41.8719, 12.5674],
    'Ivory Coast': [7.5400, -5.5471],
    'Jamaica': [18.1096, -77.2975],
    'Japan': [36.2048, 138.2529],
    'Jordan': [30.5852, 36.2384],
    'Kenya': [-1.2921, 36.8219],
    'Korea, South': [35.9078, 127.7669],
    'Kuwait': [29.3117, 47.4818],
    'Latvia': [56.8796, 24.6032],
    'Lebanon': [33.8547, 35.8623],
    'Lithuania': [55.1694, 23.8813],
    'Malawi': [-13.2543, 34.3015],
    'Malaysia': [4.2105, 101.9758],
    'Mauritius': [-20.3484, 57.5522],
    'Mexico': [23.6345, -102.5528],
    'Morocco': [31.7917, -7.0926],
    'Namibia': [-22.9576, 18.4904],
    'Netherlands': [52.1326, 5.2913],
    'New Zealand': [-40.9006, 174.8860],
    'Nicaragua': [12.8654, -85.2072],
    'Nigeria': [9.0820, 8.6753],
    'Norway': [60.4720, 8.4689],
    'Oman': [21.5126, 55.9233],
    'Pakistan': [30.3753, 69.3451],
    'Panama': [8.5380, -80.7821],
    'Philippines': [12.8797, 121.7740],
    'Poland': [51.9194, 19.1451],
    'Portugal': [39.3999, -8.2245],
    'Puerto Rico': [18.2208, -66.5901],
    'Qatar': [25.3548, 51.1839],
    'Romania': [45.9432, 24.9668],
    'Russia': [61.5240, 105.3188],
    'Saudi Arabia': [23.8859, 45.0792],
    'Serbia': [44.0165, 21.0059],
    'Singapore': [1.3521, 103.8198],
    'Slovak Republic': [48.6690, 19.6990],
    'Slovenia': [46.1512, 14.9955],
    'South Africa': [-30.5595, 22.9375],
    'Spain': [40.4637, -3.7492],
    'Sweden': [60.1282, 18.6435],
    'Switzerland': [46.8182, 8.2275],
    'Taiwan': [23.6978, 120.9605],
    'Thailand': [15.8700, 100.9925],
    'Tunisia': [33.8869, 9.5375],
    'Turkey': [38.9637, 35.2433],
    'Uganda': [1.3733, 32.2903],
    'Ukraine': [48.3794, 31.1656],
    'United Kingdom': [55.3781, -3.4360],
    'United States': [37.0902, -95.7129],
    'Venezuela': [6.4238, -66.5897],
    'Vietnam': [14.0583, 108.2772]
}

# Main content container
a,b,c = st.columns(3)
with a:
    with st.container():
        # Title
        st.subheader("Geographical Distribution of Isolates")
        selected_country="All"
        # Plot
        discrete_colors = ['#FF5733', '#33FF57', '#3357FF', '#F9C433', '#FF33A1']


        if selected_country == 'All':
            fig = px.choropleth(country_data, 
                                locations="Country", 
                                locationmode='country names', 
                                color="Sum", 
                                hover_name="Country", 
                                hover_data={"Country": True, "Sum": True},
                                color_continuous_scale=discrete_colors,
                                labels={'Sum': 'Counts'}
                            )
            fig.update_layout(autosize=True,
                            geo=dict(
                                showcoastlines=True,
                                coastlinecolor="Black",
                                showland=True,
                                landcolor="white",
                                showocean=True,
                                oceancolor="lightblue"
                            ))
        else:
            if selected_country in lat_lon_data:
                center_lat, center_lon = lat_lon_data[selected_country]
            else:
                center_lat, center_lon = 0, 0  
            

            fig = px.choropleth(country_data, 
                                locations="Country", 
                                locationmode='country names', 
                                color="Sum", 
                                hover_name="Country", 
                                hover_data={"Country": True, "Sum": True},
                                color_discrete_sequence=discrete_colors,
                                labels={'Sum': 'Counts'}
                            )
                            
            fig.update_layout(autosize=True,
                            geo=dict(
                                center={'lat': center_lat, 'lon': center_lon}, 
                                showcoastlines=True,
                                coastlinecolor="Black",
                                showland=True,
                                landcolor="white",
                                showocean=True,
                                oceancolor="lightblue",
                                projection_scale=3  
                            ),
                             width=1200,  # Set width of the plot
    height=800)
        st.plotly_chart(fig)
with b:
    with st.container():
        # Speciality Plot
        speciality_data = pd.read_excel('specialitycount.xlsx')
        speciality_data.rename(columns={'Speciality': 'Speciality', 'Sum': 'No of Isolates'}, inplace=True)
        fig = px.bar(speciality_data, x='Speciality', y='No of Isolates', text='No of Isolates', 
                    hover_data={'Speciality': True, 'No of Isolates': True})
        st.subheader('Speciality Distribution')
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

with c:
    with st.container():
        import streamlit as st
        import pandas as pd
        import plotly.express as px
        
        # Load the data
        data = pd.read_excel('organism.xlsx')
        
        # Create the donut chart
        fig = px.pie(data, names='Organism ', values='Percentage'
                     hole=0.4,  # Creating the donut chart
                     color_discrete_sequence=px.colors.qualitative.Set1)  # Set1 has good contrast
        
        # Update the hover template to show the percentage clearly
        fig.update_traces(hovertemplate='%{label}<br>% of Isolates: %{value:.2f}%')
        
        # Set the layout for legend and visual appeal
        fig.update_layout(legend_title_text='Isolates',
                          showlegend=True,
                          margin=dict(t=40, b=0, l=0, r=0))

# Show the figure in Streamlit
        st.subheader("Organism Distribution")
        st.plotly_chart(fig)

# Compact Layout with 3 Columns
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    # Age Plot
    with st.container():
        age_data = pd.read_excel('agecount.xlsx')
        age_data.rename(columns={'Sum': 'No of Isolates'}, inplace=True)
        age_data = age_data[age_data['Age Group'] != 'Unknown']
        fig = px.bar(age_data, y='Age Group', x='No of Isolates', text='No of Isolates', 
                    orientation='h', hover_data={'Age Group': True, 'No of Isolates': True})
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        st.subheader('Age Group Distribution')
        st.plotly_chart(fig, use_container_width=True)

with col2:
    # Gender Plot
    with st.container():
        gender_data = pd.read_excel('gendercount.xlsx')
        sns.set_style("whitegrid")
        plt.figure(figsize=(4,4))  # Adjust size for compactness
        plt.pie(gender_data['Sum'], labels=gender_data['Gender'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=90, wedgeprops={'edgecolor': 'black'})
        st.subheader('Gender Distribution')
        plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
        st.pyplot(plt)

with col3:
    # Source Plot
    with st.container():
        source_data = pd.read_excel('sourcecount.xlsx', header=None)
        source_data.columns = ['Source Type', 'Sum', 'Total', 'Percentage']
        source_data = source_data[['Source Type', 'Sum']]
        source_data = source_data[(source_data['Source Type'] != 'Others') & (source_data['Source Type'] != 'Not Given')]

        # Convert 'Sum' to numeric and drop rows with non-numeric values
        source_data['Sum'] = pd.to_numeric(source_data['Sum'], errors='coerce')
        source_data = source_data.dropna(subset=['Sum'])

        # Sort the DataFrame by 'Sum' in descending order
        source_data = source_data.sort_values(by='Sum', ascending=False)
        
        fig = px.bar(source_data, y='Source Type', x='Sum', text='Sum', 
                    orientation='h', hover_data={'Source Type': True, 'Sum': True})
        st.subheader("Source Type Distribution")
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)




