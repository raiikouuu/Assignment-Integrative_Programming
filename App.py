import streamlit as st

st.set_page_config(page_title="Pokémon App", page_icon="⚡", layout="centered")

st.title("⚡ Pokémon Trainer App")
st.subheader("Welcome, Trainer!")

st.write("Choose your Pokémon and learn about it.")

pokemon_data = {
    "Pikachu": {"Type": "Electric", "Description": "Pikachu stores electricity in its cheeks and releases it in battle."},
    "Charmander": {"Type": "Fire", "Description": "Charmander has a flame on its tail that shows its strength."},
    "Squirtle": {"Type": "Water", "Description": "Squirtle uses its shell for protection and shoots water."},
    "Bulbasaur": {"Type": "Grass / Poison", "Description": "Bulbasaur carries a plant seed on its back that grows."}
}

pokemon = st.selectbox("Choose your Pokémon:", list(pokemon_data.keys()))

if st.button("Show Pokémon Info"):
    st.success(f"You chose {pokemon}!")
    st.write("**Type:**", pokemon_data[pokemon]["Type"])
    st.write("**Description:**", pokemon_data[pokemon]["Description"])

trainer = st.text_input("Enter your Trainer Name:")

if st.button("Start Journey"):
    if trainer:
        st.balloons()
        st.success(f"Good luck on your adventure, Trainer {trainer}!")
    else:
        st.warning("Please enter your trainer name.")

st.subheader("Mini Pokédex")
st.table({
    "Pokémon": ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"],
    "Type": ["Electric", "Fire", "Water", "Grass/Poison"]
})
