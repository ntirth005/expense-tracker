import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def create_transaction_balance_plot(data):
    
    title = 'Balance Over Time'

    fig = go.Figure()

    cumulative_balance = (data['Credit'].fillna(0) - data['Debit'].fillna(0)).cumsum()
    fig.add_trace(
        go.Scatter(x=data['Date'], y=cumulative_balance, mode='lines', name='Cumulative Balance', line=dict(color='blue', width=2))
    )

    fig.update_layout(
        title=title,
        xaxis_title='Date',
        yaxis_title='Cumulative Balance',
        hovermode='x unified'
    )
    
    return fig, title

def create_credits_debits_bar_chart(data):
    title = 'Credits and Debits Over Time'
    
    fig = go.Figure()
    
    data['Debit_Negative'] = -data['Debit']

    fig.add_trace(go.Bar(x=data['Date'], y=data['Debit_Negative'], name='Debit', marker_color='red'))
    fig.add_trace(go.Bar(x=data['Date'], y=data['Credit'], name='Credit', marker_color='green'))

    fig.update_layout(
        title=title,
        barmode='relative',
        yaxis_title='Amount',
        hovermode='x unified'
    )

    return fig, title

def create_transaction_types_pie_chart(data):

    title='Distribution of Transaction Types'
    
    try:
        transaction_types = data['Remarks'].apply(lambda x: x.split('/')[0] if '/' in x else x)
        type_counts = transaction_types.value_counts()

        type_counts_df = pd.DataFrame({'Type': type_counts.index, 'Count': type_counts.values})

        fig = px.pie(type_counts_df, values='Count', names='Type', title=title)
        return fig, title
    except Exception as e:
        print(f"Error creating pie chart: {str(e)}")

def create_cumulative_credits_debits_chart(data):
    cumulative_credit = data['Credit'].fillna(0).cumsum()
    cumulative_debit = data['Debit'].fillna(0).cumsum()

    title = 'Continuous Cumulative Credits and Debits Over Time'
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=cumulative_credit, fill='tozeroy', name='Cumulative Credit'))
    fig.add_trace(go.Scatter(x=data['Date'], y=cumulative_debit, fill='tozeroy', name='Cumulative Debit'))
    fig.update_layout(title=title)
    
    return fig, title



