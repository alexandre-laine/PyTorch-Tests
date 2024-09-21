"""
@utor : Alexandre Lainé 
Δate : 2024-09-19
"""

import plotly.graph_objects as go
import numpy as np

def loss_accuracy_graph(
        loss_train,
        loss_test,
        accuracy
):
    
    labels = ["loss_train","loss_test"]
    fig = go.Figure()

    for i,loss in enumerate([loss_train,loss_test]):
        
        fig.add_trace(
            go.Scatter(
                x=np.linspace(0, loss.shape[0], loss.shape[0]),
                y=loss,
                name=labels[i],
                line=dict(
                    width=1
                )
            )
        )

        fig.update_layout(
            title='Average High and Low Temperatures in New York',
            xaxis_title='num epochs',
            yaxis_title='loss'
        )
    
    fig.show()