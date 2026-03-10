import streamlit as st
import requests
import random

st.set_page_config(
    page_title="Pokédex App",
    page_icon="⚪",
    layout="centered"
)

BACKGROUND = """
<style>
[data-testid="stAppViewContainer"]{
background-image:url("https://wallpaperaccess.com/full/170249.jpg");
background-size:cover;
background-position:center;
}

[data-testid="stSidebar"]{
background:rgba(255,255,255,0.85);
}

h1,h2,h3{
color:#FFD700;
text-shadow:2px 2px 5px black;
}
</style>
"""
st.markdown(BACKGROUND, unsafe_allow_html=True)

@st.cache_data
def get_gen1_pokemon():
    """Fetch the first 151 Pokémon"""
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    data = requests.get(url).json()
    return [p["name"].capitalize() for p in data["results"]]


def get_pokemon_info(name):
    """Fetch individual Pokémon data"""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    data = requests.get(url).json()

    sprite = data["sprites"]["front_default"]
    types = [t["type"]["name"].capitalize() for t in data["types"]]

    return sprite, types


pokemon_list = get_gen1_pokemon()

page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Pokédex"]
)

if page == "Home":

    st.title("⚪ Pokémon Trainer Home")

    trainer_name = st.text_input("Trainer Name")

    level = st.slider("Trainer Level", 1, 100, 5)

    starter = st.radio(
        "Choose your Starter Pokémon",
        ["Bulbasaur", "Charmander", "Squirtle"]
    )

    if st.button("Start Adventure"):

        sprite, types = get_pokemon_info(starter)

        st.success(
            f"Trainer {trainer_name} started with {starter}!"
        )

        st.image(sprite, width=200)

        st.write("Type:", ", ".join(types))

        st.balloons()

    st.divider()

    st.subheader("🎲 Discover a Random Pokémon")

    if st.button("Generate Random Pokémon"):

        random_pokemon = random.choice(pokemon_list)

        sprite, types = get_pokemon_info(random_pokemon)

        st.write(f"You discovered **{random_pokemon}!**")

        st.image(sprite, width=200)

        st.write("Type:", ", ".join(types))



elif page == "Pokédex":

    st.title("📖 Gen 1 Pokédex")

    selected = st.selectbox(
        "Choose a Pokémon",
        pokemon_list
    )

    sprite, types = get_pokemon_info(selected)

    st.image(sprite, width=200)

    st.subheader(selected)

    st.write("Type:", ", ".join(types))

    st.divider()

    st.subheader("All Generation 1 Pokémon")

    cols = st.columns(5)

    for i, name in enumerate(pokemon_list):

        sprite, _ = get_pokemon_info(name)

        with cols[i % 5]:
            st.image(sprite, width=80)
            st.caption(name)
