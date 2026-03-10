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

type_sprites = {
"Normal":"https://archives.bulbagarden.net/media/upload/8/83/Normal_icon_SwSh.png",
"Fire":"https://archives.bulbagarden.net/media/upload/a/ab/Fire_icon_SwSh.png",
"Water":"https://archives.bulbagarden.net/media/upload/8/80/Water_icon_SwSh.png",
"Electric":"https://archives.bulbagarden.net/media/upload/7/7b/Electric_icon_SwSh.png",
"Grass":"https://archives.bulbagarden.net/media/upload/a/a8/Grass_icon_SwSh.png",
"Ice":"https://archives.bulbagarden.net/media/upload/1/15/Ice_icon_SwSh.png",
"Fighting":"https://archives.bulbagarden.net/media/upload/7/7d/Fighting_icon_SwSh.png",
"Poison":"https://archives.bulbagarden.net/media/upload/8/8d/Poison_icon_SwSh.png",
"Ground":"https://archives.bulbagarden.net/media/upload/8/8f/Ground_icon_SwSh.png",
"Flying":"https://archives.bulbagarden.net/media/upload/b/b5/Flying_icon_SwSh.png",
"Psychic":"https://archives.bulbagarden.net/media/upload/7/73/Psychic_icon_SwSh.png",
"Bug":"https://archives.bulbagarden.net/media/upload/9/9c/Bug_icon_SwSh.png",
"Rock":"https://archives.bulbagarden.net/media/upload/b/bb/Rock_icon_SwSh.png",
"Ghost":"https://archives.bulbagarden.net/media/upload/0/01/Ghost_icon_SwSh.png",
"Dragon":"https://archives.bulbagarden.net/media/upload/0/03/Dragon_icon_SwSh.png"
}

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


def get_type_matchup(type_name):

    data = requests.get(
        f"https://pokeapi.co/api/v2/type/{type_name.lower()}"
    ).json()

    strengths = [
        t["name"].capitalize()
        for t in data["damage_relations"]["double_damage_to"]
    ]

    weaknesses = [
        t["name"].capitalize()
        for t in data["damage_relations"]["double_damage_from"]
    ]

    return strengths, weaknesses

pokemon_list = get_gen1_pokemon()

page = st.sidebar.selectbox("Navigation", ["Home", "Pokédex"])

if page == "Home":

    st.title("⚪ Pokémon Trainer Home")

    trainer = st.text_input("Trainer Name")

    level = st.slider("Trainer Level",1,100,10)

    starter = st.radio(
        "Choose Starter Pokémon",
        ["Bulbasaur","Charmander","Squirtle"]
    )

    if st.button("Start Adventure"):

        sprite, types, stats = get_pokemon_info(starter)

        st.success(f"Trainer {trainer} chose {starter}")

        st.image(sprite,width=200)

        st.write("Type:",", ".join(types))

        st.balloons()

    st.divider()

    st.subheader("🎮 Pokémon Type Guide")

    cols = st.columns(5)

    for i, type_name in enumerate(type_sprites):

        with cols[i % 5]:

            st.image(type_sprites[type_name],width=60)

            if st.button(type_name):

                strengths, weaknesses = get_type_matchup(type_name)

                st.subheader(type_name)

                st.write("⚔️ Strong Against:", ", ".join(strengths) if strengths else "None")

                st.write("⚠️ Weak Against:", ", ".join(weaknesses) if weaknesses else "None")

elif page == "Pokédex":

    st.title("📖 Gen 1 Pokédex")

    selected = st.selectbox("Choose a Pokémon", pokemon_list)

    sprite, types, stats = get_pokemon_info(selected)

    st.image(sprite,width=200)

    st.subheader(selected)

    st.write("Type:",", ".join(types))

    st.divider()

    st.subheader("📊 Base Stats")

    stats_df = pd.DataFrame(
        list(stats.items()),
        columns=["Stat","Base Value"]
    )

    st.table(stats_df)
