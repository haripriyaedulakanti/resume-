import streamlit as st

st.set_page_config(page_title="Notes App", page_icon="📝", layout="wide")

st.title("📝 Simple Notes App")

# Initialize session state for notes
if "notes" not in st.session_state:
    st.session_state.notes = []

# Input for new note
new_note = st.text_area("Write your note here:")

if st.button("Add Note"):
    if new_note.strip():
        st.session_state.notes.append(new_note.strip())
        st.success("Note added successfully!")
    else:
        st.warning("Note is empty!")

# Display saved notes
st.subheader("Your Notes:")

if st.session_state.notes:
    for i, note in enumerate(st.session_state.notes, 1):
        st.write(f"**{i}.** {note}")
else:
    st.info("No notes yet. Add your first one above ⬆️")
