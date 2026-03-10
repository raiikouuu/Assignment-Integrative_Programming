import streamlit as st
import requests
import random
import pandas as pd

st.set_page_config(page_title="Pokédex App", page_icon="⚪")

BACKGROUND = """
<style>
[data-testid="stAppViewContainer"]{
background-image:url("https://e0.pxfuel.com/wallpapers/147/62/desktop-wallpaper-pokemon-pokedex.jpg");
background-size:cover;
background-position:center;
}
[data-testid="stSidebar"]{
background:rgba(255,255,255,0.9);
}
h1,h2,h3{
color:#FFD700;
text-shadow:2px 2px 4px black;
}
</style>
"""
st.markdown(BACKGROUND, unsafe_allow_html=True)

@st.cache_data
def get_gen1_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    data = requests.get(url).json()
    return [p["name"].capitalize() for p in data["results"]]


def get_pokemon_info(name):

    data = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    ).json()

    sprite = data["sprites"]["front_default"]

    types = [t["type"]["name"].capitalize() for t in data["types"]]

    stats = {
        s["stat"]["name"].capitalize(): s["base_stat"]
        for s in data["stats"]
    }

    return sprite, types, stats


def get_weakness(types):

    weaknesses = set()

    for t in types:

        data = requests.get(
            f"https://pokeapi.co/api/v2/type/{t.lower()}"
        ).json()

        for w in data["damage_relations"]["double_damage_from"]:
            weaknesses.add(w["name"].capitalize())

    return list(weaknesses)

pokemon_list = get_gen1_pokemon()

page = st.sidebar.selectbox("Navigation", ["Home", "Pokédex"])

if page == "Home":

    st.title("⚪ Pokémon Trainer Home")

    trainer = st.text_input("Trainer Name")

    level = st.slider("Trainer Level", 1, 100, 10)

    starter = st.radio(
        "Choose your Starter Pokémon",
        ["Bulbasaur", "Charmander", "Squirtle"]
    )

    if st.button("Start Adventure"):

        sprite, types, stats = get_pokemon_info(starter)

        st.success(f"Trainer {trainer} chose {starter}!")

        st.image(sprite, width=200)

        st.write("Type:", ", ".join(types))

        st.balloons()

    st.divider()

    st.subheader("🎲 Discover a Random Pokémon")

    if st.button("Generate Random Pokémon"):

        random_pokemon = random.choice(pokemon_list)

        sprite, types, stats = get_pokemon_info(random_pokemon)

        st.write(f"You discovered **{random_pokemon}**!")

        st.image(sprite, width=200)

        st.write("Type:", ", ".join(types))

elif page == "Pokédex":

    st.title("📖 Gen 1 Pokédex")

    selected = st.selectbox(
        "Choose a Pokémon",
        pokemon_list
    )

    sprite, types, stats = get_pokemon_info(selected)

    weaknesses = get_weakness(types)

    st.image(sprite, width=200)

    st.subheader(selected)

    st.write("**Type:**", ", ".join(types))

    st.write("⚠️ **Weakness:**", ", ".join(weaknesses))

    st.divider()

    st.subheader("📊 Base Stats")

    stats_df = pd.DataFrame(
        list(stats.items()),
        columns=["Stat", "Base Value"]
    )

    st.table(stats_df)
