import streamlit as st
import pandas as pd
import os

location = os.path.dirname(__file__)
fname = "Heros_Journal_Sidequests.xlsx"
my_cards = pd.read_excel(os.path.join(location, fname))

def random_card(category=None):
    # Choose a relevant card based on the category
    if category:
        valid_cards = my_cards[my_cards["Category"] == category]
    else:
        valid_cards = my_cards
    quest = valid_cards.sample(n=1).iloc[0].to_dict()

    # Get Quest Details
    action = quest["Side Quest"]
    quote = quest["Quote"]
    author = quest["Author"]
    category = quest["Category"]

    # Display the card
    st.markdown(f"## {category} Quest: {action}")
    st.markdown(f"*{quote}*")
    st.markdown(f"*--{author}*")

def main():
    st.title("Hero's Sidequests: Istoria Magic Academy")
    categories = [
        "Learn", "Create", "Rest", "Go"
    ]
    choice = None
    with st.sidebar:
        if st.button("Any Quest"):
            choice = "Random"
        for category in categories:
            if st.button(f"{category} Quest"):
                choice = category
        if st.button("View All Quests"):
            choice = "All"
    with st.sidebar.container():
        st.markdown(
            """
            <div>
                <p><a href="https://theherosjournal.co/products/istoria-magic-academy-sidequest-deck">
                    Get the original
                </a></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    if choice is None:
        st.write("Choose a card!")
    elif choice == "All":
        st.write(my_cards)
    elif choice == "Random":
        random_card()
    else:
        random_card(choice)

if __name__ == "__main__":
    main()
