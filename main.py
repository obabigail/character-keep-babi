import streamlit as st

APP_TITLE = "Character-Keep Babi"

SIDEBAR_LOGO = "./assets/raven-silhouette-vector-art.png"

def _set_page_config() -> None:
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=":material/raven:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def _render_global_ui() -> None:
    if not GLOBAL_UI_COMPONENTS.exists():
        return

    spec = importlib.util.spec_from_file_location("ui_global_components", GLOBAL_UI_COMPONENTS)
    if spec is None or spec.loader is None:
        return

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    render_global_css = getattr(module, "render_global_css", None)
    if callable(render_global_css):
        render_global_css()

def _render_sidebar_global() -> None:
    with st.sidebar:
        if SIDEBAR_LOGO:
            st.image(str(SIDEBAR_LOGO), width="stretch")

# Define a estrutura de navegação do app, com páginas organizadas em seções, e controla o acesso às páginas com base no progresso do usuário (login e configuração do projeto).
def _build_pages() -> Dict[str, List[st.Page]]:
    pages: Dict[str, List[st.Page]] = {
        "DND Keep": [
            st.Page(
                "./pages/dnd-page/dnd-creator.py",
                title="DND Keep",
                icon=":material/door_open:",
                default=True,
            ),
        ],
    }

    return pages

def main() -> None:
    _set_page_config()
    _render_global_ui
    _render_sidebar_global()

    pages = _build_pages()
    pg = st.navigation(pages, position="sidebar", expanded=True)
    st.title("Welcome to Character Keep Babi!")
    pg.run()

if __name__ == "__main__":
    main()