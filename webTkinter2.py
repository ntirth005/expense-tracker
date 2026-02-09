import webview

def plotGraphs(plot):
    fig, title = plot
    webview.create_window(title, html=fig.to_html(full_html=False, include_plotlyjs='cdn'))
    webview.start()
