import streamlit as st

import functions

todos = functions.read_file()


def add_todo():
    new_todo = st.session_state['new todo'] + '\n'
    if new_todo.strip() != '':
        todos.append(new_todo)
        functions.write_file(todos)
        st.session_state['new todo'] = ''


def delete_todo():
    for to_do in todos:
        if st.session_state[to_do]:
            todos.remove(todo)
            functions.write_file(todos)
            del st.session_state[to_do]


st.title('My To Do App')
st.subheader('This is my to do app.')
st.write('This app is designed to increase your productivity.')

for todo in todos:
    st.checkbox(todo, key=todo, on_change=delete_todo)

st.text_input(label='Enter new todo', placeholder='Add new todo...', label_visibility='hidden', key='new todo',
              on_change=add_todo)
