import streamlit as st

class Card:
    def __init__(self, book):
        self.bookDetails = book
        st.image(self.bookDetails["cover"], width=150)
        st.markdown(f"**{self.bookDetails['title']}**")
        st.markdown(f"*by {self.bookDetails['author']}*")
        st.write("---")  # Separator

st.header("**Fictions** *Heaven*")

Fictions_genere = st.selectbox("Ganre",["Historical fiction", "Thriller", "Fantasy", "Romance", "Rom-com", "Sci-fi","Desi","Royal","Horror"])

books = {
    "Historical fiction": [
        {"title": "Vikramsamhita", "author": "Ira Alessia", "cover": "https://img.wattpad.com/cover/355714196-512-k431250.jpg"},
        {"title": "Duchess of Sebria", "author": "Ashley", "cover": "https://img.wattpad.com/cover/322457239-512-k77583.jpg"},
    ],
    "Thriller": [
        {"title": "Project Oxygen", "author": "Violadevis", "cover": "https://img.wattpad.com/cover/126462571-256-k701360.jpg"},
        {"title": "Four Walls", "author": "M C Roman", "cover": "https://img.wattpad.com/cover/124780656-256-k100974.jpg"},
    ],
    "Fantasy": [
        {"title": "Given", "author": "Naandi Taylor", "cover": "https://img.wattpad.com/cover/212138504-256-k900623.jpg"},
        {"title": "The Rejected Crown", "author": "J.R.Roman", "cover": "https://img.wattpad.com/cover/378658834-256-k664168.jpg"},
    ],
    "Romance": [
        {"title": "Breaking the Ice", "author": "Ellie", "cover": "https://img.wattpad.com/cover/254608450-512-k973227.jpg"},
        {"title": "All The Wild Ones", "author": "Amelie", "cover": "https://img.wattpad.com/cover/262949035-512-k390656.jpg"},
    ],
    "Rom-com": [
        {"title": "Dancing with the Devil", "author": "Automn touched", "cover": "https://img.wattpad.com/cover/329394344-256-k350313.jpg"},
        {"title": "Her Healer", "author": "Icy Vines", "cover": "https://img.wattpad.com/cover/329394344-256-k350313.jpg"},
    ],
    "Sci-fi": [
        {"title": "FAMOUXX", "author": "Kassandra Tate", "cover": "https://img.wattpad.com/cover/250703835-256-k129237.jpg"},
        {"title": "BaYou", "author": "Wendizzy", "cover": "https://img.wattpad.com/cover/193397749-256-k745958.jpg"},
    ],
    "Desi": [
        {"title": "Rooh: His Replced Bride", "author": "Tara", "cover": "https://img.wattpad.com/cover/343108799-352-k92236.jpg"},
        {"title": "Veiled Bride", "author": "Vanya", "cover": "https://img.wattpad.com/cover/352224503-256-k404175.jpg"},
    ],
    "Royal": [
        {"title": "The Empire Of Rajwansh", "author": "Anmi", "cover": "https://img.wattpad.com/cover/357903924-144-k792453.jpg"},
        {"title": "FORCED Queen", "author": "jiaha", "cover": "https://img.wattpad.com/cover/356173774-144-k980914.jpg"},
    ],
    "Horror": [
        {"title": "FINDING HUMANITY", "author": "Nina Marks", "cover": "https://img.wattpad.com/cover/89990411-256-k812681.jpg"},
        {"title": "The Dead Walk Among Us", "author": "Jenna Merissa", "cover": "https://img.wattpad.com/cover/89990411-256-k812681.jpg"},
    ],
}
st.subheader(f"Trending {Fictions_genere} Books")

if Fictions_genere in books:
    for book in books[Fictions_genere]:
        Card(book=book)
        
        
if Fictions_genere in books:
    for book in books[Fictions_genere]:
        Card(book=book)
        
else:
    st.write("No books found for this genre.")