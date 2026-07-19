import plotly.express as px


def create_gdp_line_chart(df):
    """
    Create GDP historical line chart.
    """

    fig = px.line(
        df,
        x="Year",
        y="Value",
        title=f"{df['Country'].iloc[0]} GDP History",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="GDP (USD)",
        template="plotly_white"
    )

    return fig



def create_gdp_ranking_chart(df):
    """
    Create Top 10 GDP Countries bar chart.
    """

    fig = px.bar(
        df,
        x="Country",
        y="GDP",
        title="🏆 Top 10 GDP Countries",
        text="GDP"
    )

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="GDP (USD)",
        template="plotly_white"
    )

    return fig

def create_per_capita_chart(df):
    """
    Create GDP per capita comparison chart.
    """

    fig = px.bar(
        df,
        x="Country",
        y="GDP Per Capita",
        title="💰 GDP Per Capita Comparison",
        text="GDP Per Capita"
    )

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="GDP Per Capita (USD)",
        template="plotly_white"
    )

    return fig

def create_country_comparison_chart(df):

    fig = px.bar(
        df,
        x="Country",
        y="GDP",
        title="🌎 GDP Comparison",
        text="GDP"
    )


    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="GDP (USD)",
        template="plotly_white"
    )


    return fig



def create_per_capita_comparison_chart(df):

    fig = px.bar(
        df,
        x="Country",
        y="GDP Per Capita",
        title="💰 GDP Per Capita Comparison",
        text="GDP Per Capita"
    )


    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="GDP Per Capita (USD)",
        template="plotly_white"
    )


    return fig

import plotly.express as px


def create_world_gdp_map(df):
    """
    Create an interactive world GDP map.
    """

    fig = px.choropleth(
        df,
        locations="ISO",
        color="GDP",
        hover_name="Country",
        color_continuous_scale="Viridis",
        projection="natural earth",
        title="🌍 World GDP Map"
    )

    fig.update_layout(
        template="plotly_white",
        margin=dict(l=0, r=0, t=50, b=0)
    )

    return fig