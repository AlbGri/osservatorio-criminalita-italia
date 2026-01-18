"""Funzioni comuni per tutti i grafici."""
import plotly.graph_objects as go
from config import COVID_PERIOD, TEMPLATE


def add_covid_highlight(fig: go.Figure, position: str = 'top') -> None:
    """Aggiunge evidenziazione periodo COVID al grafico."""
    fig.add_vrect(
        x0=COVID_PERIOD['start'],
        x1=COVID_PERIOD['end'],
        fillcolor=COVID_PERIOD['color'],
        layer='below',
        line_width=0,
        annotation_text=COVID_PERIOD['label'],
        annotation_position=position,
        annotation=dict(font_size=9, font_color='gray')
    )


def apply_base_layout(fig: go.Figure, title: str, height: int = 550) -> None:
    """Applica layout base comune a tutti i grafici."""
    fig.update_layout(
        title=title,
        hovermode='x unified',
        template=TEMPLATE,
        height=height
    )
