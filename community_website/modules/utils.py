import base64
from datetime import date, datetime

import pandas as pd
import streamlit as st


@st.cache_data
def add_bg_from_local(background_img_path, sidebar_background_img_path):
    with open(background_img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    with open(sidebar_background_img_path, "rb") as image_file:
        sidebar_encoded_string = base64.b64encode(image_file.read())

    return f"""<style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string.decode()});
            background-size: 1500px 700px;
        }}

        section[data-testid="stSidebar"] {{
            background-image: url(data:image/png;base64,{sidebar_encoded_string.decode()});
            background-size: 400px 800px;
        }}
    </style>"""


def set_page_config():
    st.set_page_config(
        page_title="Bilgisayar Topluluğu",
        page_icon="💻",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://github.com/TOBB-ETU-CS-Community",
            "Report a bug": "https://tobbetu-bilgisayar-toplulugu.streamlit.app/Geri_Bildirim_Formu",
            "About": "Topluluğumuza ait web sayfasında bize dair pek çok bilgiye ulaşabilirsiniz. \
                Her türlü geri bildiriminize her zaman açığız.",
        },
    )


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    style = """<style>
        .row-widget.stButton {text-align: center;}
        div[data-testid="column"]:nth-of-type(1)
            {
                text-align: center;
            }
            div[data-testid="column"]:nth-of-type(2)
            {
                text-align: center;
            }
            div[data-testid="column"]:nth-of-type(3)
            {
                text-align: center;
            }
    </style>"""
    st.markdown(style, unsafe_allow_html=True)


@st.cache_data
def load_excel(
    file_path: str,
    date_columns: list = None,
    original_format: str = "%d.%m.%Y",
    new_format: str = "%Y-%m-%d",
):
    """Read workbook data and return typed, chronologically sorted date columns.

    Excel cells may contain native dates or strings in ``original_format``.
    ``new_format`` remains accepted for compatibility; display formatting belongs
    to the caller because these columns contain datetime values, not strings.
    """
    excel = pd.read_excel(
        io=file_path,
        sheet_name="Sheet1",
    )
    if date_columns:
        for date_column in date_columns:

            def parse_date(value):
                if pd.isna(value):
                    return pd.NaT
                if isinstance(value, str):
                    return datetime.strptime(value.strip(), original_format)
                if isinstance(value, (datetime, date, pd.Timestamp)):
                    return pd.Timestamp(value).normalize()
                raise ValueError(
                    f"Unsupported date value in {date_column}: {value!r}"
                )

            excel[date_column] = pd.to_datetime(
                excel[date_column].map(parse_date)
            )
        excel = excel.sort_values(
            by=date_columns, kind="stable", na_position="last"
        )
        excel = excel.reset_index(drop=True)
    return excel
