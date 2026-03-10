import streamlit as st
import requests
import random
import pandas as pd

POKEBALL_ICON = "https://upload.wikimedia.org/wikipedia/commons/5/53/Pok%C3%A9_Ball_icon.svg"
st.set_page_config(page_title="Pokédex App", page_icon=POKEBALL_ICON, layout="centered")

st.markdown("""
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
""", unsafe_allow_html=True)

type_icons = {
"Normal":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/normal.svg",
"Fire":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/fire.svg",
"Water":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/water.svg",
"Electric":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/electric.svg",
"Grass":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/grass.svg",
"Ice":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/ice.svg",
"Fighting":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/fighting.svg",
"Poison":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/poison.svg",
"Ground":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/ground.svg",
"Flying":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/flying.svg",
"Psychic":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/psychic.svg",
"Bug":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/bug.svg",
"Rock":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/rock.svg",
"Ghost":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/ghost.svg",
"Dragon":"https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/dragon.svg"
}

@st.cache_data
def get_gen1_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    data = requests.get(url).json()
    return [p["name"].capitalize() for p in data["results"]]

def get_pokemon_info(name):
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}").json()
    sprite = data["sprites"]["front_default"]
    types = [t["type"]["name"].capitalize() for t in data["types"]]
    stats = {s["stat"]["name"].capitalize(): s["base_stat"] for s in data["stats"]}
    return sprite, types, stats

def get_type_matchup(type_name):
    data = requests.get(f"https://pokeapi.co/api/v2/type/{type_name.lower()}").json()
    strengths = [t["name"].capitalize() for t in data["damage_relations"]["double_damage_to"]]
    weaknesses = [t["name"].capitalize() for t in data["damage_relations"]["double_damage_from"]]
    return strengths, weaknesses

pokemon_list = get_gen1_pokemon()

page = st.sidebar.selectbox("Navigation", ["Home", "Pokédex", "About"])

if page == "Home":
    st.title("⚪ Pokémon Trainer Home")

    trainer = st.text_input("Trainer Name")

    level = st.slider("Trainer Level", 1, 100, 10)

    starter = st.radio("Choose Starter Pokémon", ["Bulbasaur","Charmander","Squirtle"])

    if st.button("Start Adventure"):
        sprite, types, stats = get_pokemon_info(starter)
        st.success(f"Trainer {trainer} chose {starter}")
        st.image(sprite, width=200)
        st.write("Type:", ", ".join(types))
        st.balloons()

    st.divider()

    st.subheader("🎮 Pokémon Type Guide")

    cols = st.columns(5)
    for i, type_name in enumerate(type_icons):
        with cols[i % 5]:
            st.image(type_icons[type_name], width=50)
            if st.button(type_name):
                strengths, weaknesses = get_type_matchup(type_name)
                st.write("###", type_name)
                st.write("⚔️ Strong Against:", ", ".join(strengths) if strengths else "None")
                st.write("⚠️ Weak Against:", ", ".join(weaknesses) if weaknesses else "None")

    st.divider()

    st.subheader("🎲 Discover a Random Pokémon")

    if st.button("Generate Random Pokémon"):
        random_pokemon = random.choice(pokemon_list)
        sprite, types, stats = get_pokemon_info(random_pokemon)
        st.write(f"You discovered **{random_pokemon}!**")
        st.image(sprite, width=200)
        st.write("Type:", ", ".join(types))

elif page == "Pokédex":
    st.title("📖 Gen 1 Pokédex")
    selected = st.selectbox("Choose a Pokémon", pokemon_list)
    sprite, types, stats = get_pokemon_info(selected)
    st.image(sprite, width=200)
    st.subheader(selected)
    st.write("Type:", ", ".join(types))
    st.divider()
    stats_df = pd.DataFrame(list(stats.items()), columns=["Stat","Base Value"])
    st.table(stats_df)

elif page == "About":
    st.title("ℹ️ About This App")
    st.write("""
Welcome to the **Pokédex App**! This app lets you:
- Select a starter Pokémon and track your Trainer Level
- Explore all **151 Generation 1 Pokémon**
- See Pokémon types, strengths, and weaknesses
- Generate a random Pokémon for fun
- Check Pokémon base stats

This app is made using **Streamlit** and **PokéAPI**, perfect for Pokémon fans and school ICT projects!
    """)

    st.markdown("Created with ❤️ using Python and Streamlit")
    st.success("Try exploring the Pokémon types and stats!")
    st.info("Click on the type icons on Home to see strengths and weaknesses.")
