import streamlit as st

st.set_page_config(page_title="Pokémon Trainer App", page_icon="⚪")

page = st.sidebar.selectbox("Navigation", ["Home", "Pokédex"])

pokemon_data = {
    "Pikachu": {
        "Type": "Electric",
        "Description": "Pikachu stores electricity in its cheeks.",
        "Image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    },
    "Charmander": {
        "Type": "Fire",
        "Description": "Charmander has a flame on its tail.",
        "Image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"
    },
    "Squirtle": {
        "Type": "Water",
        "Description": "Squirtle shoots water from its mouth.",
        "Image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"
    },
    "Bulbasaur": {
        "Type": "Grass / Poison",
        "Description": "Bulbasaur has a plant seed on its back.",
        "Image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
    },
    "Jigglypuff": {
        "Type": "Fairy",
        "Description": "Jigglypuff sings a lullaby that makes enemies sleep.",
        "Image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png"
    },
    "Meowth": {
        "Type": "Normal",
        "Description": "Meowth loves shiny coins and treasures.",
        "Image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/52.png"
    }
}

if page == "Home":
    st.title("⚪ Pokémon Trainer App")
    st.subheader("Welcome, Trainer!")

    trainer = st.text_input("Enter your Trainer Name:")

    if st.button("Start Journey"):
        if trainer:
            st.success(f"Welcome to your adventure, Trainer {trainer}!")
            st.balloons()
        else:
            st.warning("Please enter your trainer name.")

elif page == "Pokédex":

    st.title("📖 Pokédex")

    selected_pokemon = st.selectbox("Choose a Pokémon", list(pokemon_data.keys()))

    st.subheader(selected_pokemon)

    st.image(pokemon_data[selected_pokemon]["Image"], width=200)

    st.write("**Type:**", pokemon_data[selected_pokemon]["Type"])
    st.write("**Description:**", pokemon_data[selected_pokemon]["Description"])

    st.divider()

    st.subheader("All Pokémon")

    cols = st.columns(3)

    i = 0
    for name, info in pokemon_data.items():
        with cols[i % 3]:
            st.image(info["Image"], width=100)
            st.caption(name)
        i += 1
