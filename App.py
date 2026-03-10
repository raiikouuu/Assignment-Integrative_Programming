import streamlit as st

st.set_page_config(page_title="Pokémon App", page_icon="⚡")

st.title("⚡ Pokémon Trainer App")
st.write("Click a Pokémon name to see its photo!")

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
    }
}

pokemon = st.radio("Choose your Pokémon:", list(pokemon_data.keys()))

st.subheader(pokemon)

st.image(pokemon_data[pokemon]["Image"], width=200)

st.write("**Type:**", pokemon_data[pokemon]["Type"])
st.write("**Description:**", pokemon_data[pokemon]["Description"])

trainer = st.text_input("Enter your Trainer Name:")

if st.button("Start Journey"):
    if trainer:
        st.success(f"Good luck on your adventure, Trainer {trainer}!")
        st.balloons()
    else:
        st.warning("Please enter your trainer name.")
