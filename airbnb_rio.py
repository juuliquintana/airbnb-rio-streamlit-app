import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components
import plotly.graph_objects as go
import chardet


# Configuración de la página de Streamlit
st.set_page_config(page_title="Rio de Janeiro - Airbnb", layout="wide", page_icon=":house:")

# Cargar los archivos HTML generados
def load_html(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()
    
# Function to load data
@st.cache_resource # This ensures that any modifications made to the df within the function are persisted in the cache.
def load_data():
    df = pd.read_csv('df_copy1.csv')
    return df


# Custom HTML and CSS for the title
st.markdown(
    """
    <style>
    .banner {
        background-image: url('https://images.adsttc.com/media/images/6449/6c61/2def/3401/7a85/1139/slideshow/a-historia-do-calcadao-de-copacabana_3.jpg?1682533486');
        background-size: cover;
        background-position: center;
        padding: 50px 0;
        text-align: center;
    }
    .title {
        font-family: 'Calibri', sans-serif;
        font-weight: bold;
        color: #FF5A5F;
        text-align: center;
        font-size: 6em;
        margin-bottom: 0.5em;
        text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
    }
    .header {
        font-family: 'Calibri', sans-serif;
        color: #008B8B;
        font-weight: bold;
        text-align: center;
        font-size: 3em;
        margin-bottom: 0.5em;
    }
    .subheader {
        font-family: 'Calibri', sans-serif;
        color: #F08080;
        text-align: center;
        font-size: 2em;
        margin-bottom: 0.5em;
    }
    .subsubheader {
        font-family: 'Calibri', sans-serif;
        color: #E9967A;
        text-align: center;
        font-size: 1.5em;
        margin-bottom: 0.5em;
    }
    .subsubheader_sidebar {
        font-family: 'Calibri', sans-serif;
        font-weight: bold;
        color: #778899;
        font-size: 1.5em;
        margin-bottom: 0.5em;
    }
    .centered-text {
        font-family: 'Calibri', sans-serif;
        text-align: center;
        font-size: 1em;
        margin: 20px;
    }
    .scroll-up-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #8FBC8F;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        z-index: 100;
    }
    .stTabs [role="tablist"] {
        justify-content: center;
    }
    .about-us {
        text-align: center;
        font-family: 'Calibri', sans-serif;
        margin: 20px;
    }
    .about-us img {
        width: 100%;
        max-width: 600px;
        height: auto;
        margin: 20px 0;
    }
    </style>

    <button onclick="scrollToTop()" class="scroll-up-button">Scroll to Top</button>

    <script>
    function scrollToTop() {
        window.scrollTo({top: 0, behavior: 'smooth'});
    }
    </script>
    """,
    unsafe_allow_html=True
)

def main():
    # Título de la página con banner de fondo
    st.markdown(
        """
        <div class="banner">
            <div class="title">Rio de Janeiro - Airbnb</div>
        </div>
        """, unsafe_allow_html=True
    )

    # Crear las pestañas
    tabs = st.tabs(["About Us", "Price", "Neighbourhood", "Room Type", "Distance to Turistic Places", "Find your Best Place"])

    # Load data
    df_copy1 = load_data()

    # Pestaña de presentacion
    with tabs[0]:
        st.markdown('<div class="header">About Us</div>', unsafe_allow_html=True)
        st.markdown(
        """
        <div class="subheader">Welcome to <b>Rio de Janeiro</b></div>
        <div class="about-us">
            <p>Discover the <i>vibrant</i> city of <b>Rio de Janeiro</b> <i>with us</i>. Our project aims to provide you with all the information you need to make your stay <u>unforgettable</u>. Whether you're looking for the <b>best</b> neighbourhoods, the perfect room type, or proximity to the most famous tourist attractions, <b>we've got you covered</b>.</p>
            <p>Our goal is to make <u>your trip planning</u> as smooth and enjoyable as possible by offering insights and <i><u>data-driven recommendations</u></i>. Enjoy the beautiful landscapes, immerse yourself in the local culture, and <u>make the most of your stay</u> in this marvelous city.</p>
            <p>Browse through our <i><u>interactive maps and charts</u></i> to find the <b>best</b> accommodations that suit your needs and preferences. Let us <b>help you</b> create <u>memories</u> that will last a lifetime!</p>
            <img src="https://img.freepik.com/foto-gratis/teleferico-montana-pan-azucar-puesta-sol_181624-36743.jpg?t=st=1719492605~exp=1719496205~hmac=76dc7c4f5ae0180e250b01341cde19e4787c9b0b8118543830b8f6e89c199c89&w=740" alt="Rio de Janeiro">
            <img src="https://img.freepik.com/foto-gratis/grupo-amigos-colombianos-pasando-tiempo-juntos-divirtiendose_23-2151356426.jpg?t=st=1719492515~exp=1719496115~hmac=846b61ffd6da91c2fddcd4a10c368ec7b7ded625e9d2af39bd29fa9bfb60194c&w=740" alt="Carnaval">
        </div>
        """, unsafe_allow_html=True
        )


    # Pestaña de precios
    with tabs[1]:
        st.markdown('<div class="header">Price Analysis</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">In this section, we analyze the distribution of Airbnb prices in Rio de Janeiro.</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">The histogram below shows the frequency distribution of prices. We see that the distribution of prices is centered on 100€ per night (this being the median), however, there is a wide distribution of prices ranging from less than 50€ to 400€.</div>', unsafe_allow_html=True)
        st.markdown('<div class="subheader">Distribution of Prices</div>', unsafe_allow_html=True)
        fig = px.histogram(df_copy1, x='price', nbins=60, marginal='box', color_discrete_sequence=['#66CDAA'])
        fig.update_layout(
            xaxis_title='Price',
            yaxis_title='Count'
        )
        st.plotly_chart(fig)
        st.markdown('<div class="subheader">Price vs Reviews Score Rating</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">Here, we explore the relationship between price and review scores. The scatter plot shows how the price varies with the review scores for different room types, being lower in the case of shared rooms.</div> <br>', unsafe_allow_html=True)
        fig = px.scatter(df_copy1, x='price', y='review_scores_rating', color='room_type', color_discrete_sequence=['#FA8072', '#20B2AA', '#9370DB', '#FFC0CB'])
        fig.update_layout(
            xaxis_title='Price',
            yaxis_title='Review Scores Rating'
        )
        st.plotly_chart(fig)

        # Crear y mostrar el mapa de Folium
        st.markdown('<div class="subheader">Price distribution Map</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">The map below displays the distribution of Airbnb prices across different neighborhoods. We can observe how most of the accommodations are located in coastal areas, and how the highest prices correspond to the beaches of Copacabana and Ipanema.</div> <br>', unsafe_allow_html=True)
        colT1,colT2 = st.columns([18,82])
        with colT2:
            map_html = load_html('map1.html')
            st.components.v1.html(map_html, width=1100, height=850)
            
        # Configuración de la aplicación Streamlit
        st.markdown('<div class="subheader">Average Prices Along the Year</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">This section shows the average prices of Airbnbs throughout the year, helping you identify the best times to book your stay. We can clearly see two peaks that correspond to two of the most touristic and characteristic periods of Rio: New Years Eve and Carnival. The rest of the small peaks correspond to the weekends.</div> <br>', unsafe_allow_html=True)
        colT1,colT2 = st.columns([13,87])
        with colT2:
            map4_html = load_html('map4.html')
            st.components.v1.html(map4_html, width=1300, height=1050)
        

    # Pestaña de barrios
    with tabs[2]:
        st.markdown('<div class="header">Neighbourhood Analysis</div>', unsafe_allow_html=True)
        st.markdown('<div class="subheader">Neighbourhood by Average Price</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">In this section, we explore the average prices of Airbnbs in different neighbourhoods. We can observe the large number of neighborhoods in Rio de Janerio (156) and the great difference in average prices among them. The neighborhoods with the highest prices are Jacarezinho, Malhães Bastos, Caju and Ipanema.</div> <br>', unsafe_allow_html=True)
        df_avg_price = df_copy1.groupby('neighbourhood_cleansed')['price'].mean().reset_index()
        df_avg_price = df_avg_price.sort_values(by='price', ascending=False)
        
        fig = go.Figure(data=[
            go.Bar(name=neighbourhood, x=[neighbourhood],
                y=[df_avg_price[df_avg_price['neighbourhood_cleansed'] == neighbourhood]['price'].values[0]])
            for neighbourhood in df_avg_price['neighbourhood_cleansed']
        ])

        fig.update_layout(
            barmode='group',  # Configurar el barmode como 'group'
            xaxis_title='Neighbourhood',
            yaxis_title='Average Price',
            bargap=0.2,  # Reducir el espacio entre las barras
            bargroupgap=0.1,  # Reducir el espacio entre los grupos de barras
        )
        st.plotly_chart(fig)

        # Mostrar el mapa en Streamlit
        st.markdown('<div class="subheader">Average Airbnb Prices by neighborhoods</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">The map below shows the average Airbnb prices by neighborhoods,  providing a visual representation of the price distribution across the city.</div> <br>', unsafe_allow_html=True)
        colT1,colT2 = st.columns([18,82])
        with colT2:
            map2_html = load_html('map2.html')
            st.components.v1.html(map2_html, width=1100, height=850)

 
    # Pestaña de tipos de habitación
    with tabs[3]:
        st.markdown('<div class="header">Room Type Analysis</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">This section analyzes the distribution of different room types available on Airbnb</div> <br>', unsafe_allow_html=True)
        st.markdown('<div class="subheader">Room Type Distribution</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">In this graph it can be seen that most of them correspond to house or complete apartments, followed by private rooms, and in very small proportion shared rooms and hotels. This may be due to the fact that although there are a large number of hotels in Rio, these are not usually promoted on Airbnb.</div> <br>', unsafe_allow_html=True)
        fig = px.histogram(df_copy1, x='room_type', color='room_type', color_discrete_sequence=['#FA8072', '#20B2AA', '#9370DB', '#FFC0CB'])
        fig.update_layout(
            xaxis_title='Room Type',
            yaxis_title='Count'
        )
        st.plotly_chart(fig)
        st.markdown('<div class="subheader">Price by Room Type</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">And as previously mentioned, here we can see that the prices of shared rooms are the cheapest, followed by private rooms. While hotel rooms and complete houses or apartments have higher prices.</div> <br>', unsafe_allow_html=True)
        fig = px.violin(df_copy1, x='room_type', y='price', color='room_type', box=True, points='all', color_discrete_sequence=['#FA8072', '#20B2AA', '#6A5ACD', '#FFC0CB'])
        fig.update_layout(
            xaxis_title='Room Type',
            yaxis_title='Price'
        )
        st.plotly_chart(fig)

    # Pestaña de distancia a lugares turísticos
    with tabs[4]:
        st.markdown('<div class="header">Distance to Turistic Places</div>', unsafe_allow_html=True)
        st.markdown('<div class="subheader">Turistic places Map</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">This map shows the locations of Airbnbs in Rio de Janeiro relative to popular tourist attractions: Christ the Redeemer, the Sugar Loaf, the Botanical Garden and the beaches of Copacabana and Ipanema.. Use this map to find accommodations close to the sites you want to visit.</div> <br>', unsafe_allow_html=True)
        colT1,colT2 = st.columns([18,82])
        with colT2:
            map3_html = load_html('map3.html')
            st.components.v1.html(map3_html, width=1100, height=850)

    # Pestaña de filtros Power BI
    with tabs[5]:
        st.markdown('<div class="header">Find your best place</div>', unsafe_allow_html=True)
        st.markdown('<div class="subheader">Interactive Power BI Dashboard</div>', unsafe_allow_html=True)
        st.markdown(r'<div class="centered-text">Use this interactive Power BI dashboard to filter and find the best Airbnb accommodations in Rio de Janeiro based on your preferences.</div> <br>', unsafe_allow_html=True)
        # URL de inserción del panel de Power BI
        power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiN2YzOWE0OTAtNjA0Mi00YzAxLWJkMzgtNGViNTRlOWExNjc2IiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
        
        # Insertar el panel de Power BI usando un iframe
        colT1, colT2 = st.columns([18,82])
        with colT2:
            st.components.v1.iframe(src=power_bi_url, width=1200, height=950)


if __name__ == "__main__":
    main()