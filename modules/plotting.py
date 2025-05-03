import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

def plot_sip(df):
    
    latest = df.iloc[-1]
    invested_final = latest['Total Invested']
    future_value_final = latest['Future Value']
    returns = future_value_final - invested_final

    
    fig = make_subplots(rows=1, cols=2, 
                        specs=[[{"type": "xy"}, {"type": "domain"}]],
                        column_widths=[0.6, 0.4],
                        subplot_titles=("SIP Growth Over Time", "Investment Breakdown"))

    
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Total Invested'], name='Total Invested', line=dict(color='blue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Future Value'], name='Future Value', line=dict(color='green')), row=1, col=1)
    fig.update_xaxes(tickformat="%d-%m-%y", row=1, col=1)
    fig.update_yaxes(title_text='Amount (₹)', row=1, col=1)

    
    fig.add_trace(go.Pie(labels=["Total Invested", "Final Returns"], 
                         values=[invested_final, returns], 
                         hole=0.4,
                         textinfo='label+percent',
                         marker=dict(colors=["#1f77b4", "#2ca02c"])), row=1, col=2)

    
    fig.update_layout(title_text="SIP Analysis",
                      showlegend=False)
    
  
    st.plotly_chart(fig, use_container_width=True)
