
import streamlit as st


def title():
    return 'Json {}'


def run():

    with st.echo():

        seb = '''
            {
              "login": "ssaunier",
              "id": 414418,
              "node_id": "MDQ6VXNlcjQxNDQxOA==",
              "avatar_url": "https://avatars3.githubusercontent.com/u/414418?v=4",
              "created_at": "2010-09-24T13:31:21Z",
              "updated_at": "2020-08-08T14:26:53Z"
            }
        '''
        st.json(seb)
