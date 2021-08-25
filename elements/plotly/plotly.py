
import streamlit as st

import pandas as pd
import numpy as np

def run():

    with st.echo():

        @st.cache
        def get_plotly_data():

            z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
            z = z_data.values
            sh_0, sh_1 = z.shape
            x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
            return x, y, z

        import plotly.graph_objects as go

        x, y, z = get_plotly_data()

        fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
        fig.update_layout(title='IRR', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
        st.plotly_chart(fig)
