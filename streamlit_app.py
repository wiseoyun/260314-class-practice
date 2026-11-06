import html

import streamlit as st

st.set_page_config(page_title="나를 소개합니다", page_icon="🌷", layout="wide")

PROFILE = {
    "name": "위서윤",
    "affiliation": "청주교육대학교 · 사회과교육과",
  "age": 21,
    "intro": "새로운 것을 배우고, 좋아하는 것을 오래 들여다보는 사람입니다. 작은 취향들을 모아 저를 소개해요.",
    "email": "hello@example.com",
    "image_url": "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=1200&q=85",
}

INTERESTS = ["귀여운 것들", "산책", "사진 찍기", "새로운 카페 찾기", "식물 키우기", "일기 쓰기"]

FAVORITE_MUSIC = [
  ("josee!", "데이먼스 이어 · 좋아하는 노래"),
    ("두 번째 좋아하는 노래", "아티스트 이름 · 기억에 남는 순간"),
    ("요즘 자주 듣는 노래", "아티스트 이름 · 추천하고 싶은 한마디"),
]

READ_BOOKS = [
    ("책 제목을 적어주세요", "작가 이름 · 마음에 남은 문장이나 감상"),
    ("기억에 남는 책", "작가 이름 · 읽은 시기 또는 짧은 감상"),
]

WATCHED_MOVIES = [
    ("영화 제목을 적어주세요", "감독 또는 주연 · 좋아하는 장면"),
    ("다시 보고 싶은 영화", "감독 또는 주연 · 추천하고 싶은 이유"),
]

PASTEL_TAGS = ["rose", "peach", "butter", "mint", "sky", "lilac", "aqua"]


def escape(value):
    return html.escape(str(value), quote=True)


def make_tags(items):
    return "".join(
        f'<span class="tag tag-{PASTEL_TAGS[index % len(PASTEL_TAGS)]}">{escape(item)}</span>'
        for index, item in enumerate(items)
    )


def make_list(items, icon):
    return "".join(
        f'<article class="list-item"><span class="list-icon">{icon}</span>'
        f'<div><h3>{escape(title)}</h3><p>{escape(detail)}</p></div></article>'
        for title, detail in items
    )


st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&family=Gowun+Dodum&display=swap');

    :root {{
        --ink: #413b45;
        --muted: #77717a;
        --paper: #fffaf4;
        --rose: #f7bfd0;
        --peach: #ffd5bc;
        --butter: #fff0a8;
        --mint: #c9ead8;
        --sky: #c8e2f5;
        --lilac: #ddd0f2;
        --aqua: #c1e9e5;
        --coral: #ffc9b9;
        --lemon: #f4efbd;
        --sage: #dce8c8;
        --pink: #f4d0e5;
        --blue: #d0d7f4;
    }}

    [data-testid="stAppViewContainer"] {{
        background-color: var(--paper);
        background-image: linear-gradient(rgba(141, 118, 130, .035) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(141, 118, 130, .035) 1px, transparent 1px);
        background-size: 28px 28px;
    }}
    [data-testid="stHeader"], [data-testid="stToolbar"], footer {{ visibility: hidden; }}
    .stMainBlockContainer {{ max-width: 1120px; padding: 1.5rem 1.5rem 4rem; }}
    .stMarkdown {{ color: var(--ink); }}
    .site {{ color: var(--ink); font-family: 'Gowun Dodum', sans-serif; }}
    .topbar {{ display: flex; justify-content: space-between; align-items: center; padding: .5rem 0 1.4rem; border-bottom: 1px dashed #d9cbd0; }}
    .brand {{ color: var(--ink); font: 700 1.5rem 'Gaegu', cursive; text-decoration: none; }}
    .top-note {{ color: var(--muted); font-size: .86rem; }}
    .hero {{ display: grid; grid-template-columns: 1.15fr .85fr; gap: 3.5rem; align-items: center; padding: 4.2rem 1rem 4.8rem; }}
    .eyebrow {{ color: #8d727d; font-size: .9rem; letter-spacing: 0; margin: 0 0 .7rem; }}
    .hero h1 {{ font: 700 3.6rem/1.18 'Gaegu', cursive; letter-spacing: 0; margin: 0; }}
    .hero h1 em {{ color: #d77791; font-style: normal; }}
    .affiliation {{ display: inline-block; margin: 1.1rem 0 .7rem; padding: .45rem .8rem; background: var(--butter); border-radius: 999px; font-size: .9rem; }}
    .age-note {{ display: inline-block; margin-left: .35rem; padding: .45rem .8rem; background: var(--pink); border-radius: 999px; font-size: .9rem; }}
    .intro {{ max-width: 540px; color: #655e68; font-size: 1.05rem; line-height: 1.9; margin: .7rem 0 1.3rem; }}
    .hello-note {{ display: inline-block; color: #665c66; background: white; border: 1px solid #f0dfe4; border-radius: 5px; padding: .65rem .9rem; font-size: .88rem; transform: rotate(-1deg); }}
    .hero-art {{ position: relative; width: min(100%, 370px); justify-self: center; padding: .75rem; background: white; border: 1px solid #eadfe2; border-radius: 20px 20px 7px 20px; box-shadow: 8px 10px 0 var(--rose); transform: rotate(2deg); }}
    .hero-art img {{ display: block; width: 100%; height: 330px; object-fit: cover; border-radius: 14px 14px 4px 14px; }}
    .photo-caption {{ padding: .7rem .4rem .1rem; text-align: center; font: 700 1.35rem 'Gaegu', cursive; }}
    .photo-sticker {{ position: absolute; top: -1.15rem; right: -1.25rem; display: grid; place-items: center; width: 62px; height: 62px; border-radius: 50%; background: var(--butter); font-size: 1.65rem; transform: rotate(9deg); }}
    .section {{ padding: 2.1rem 1rem 2.6rem; border-top: 1px dashed #d9cbd0; }}
    .section-heading {{ display: flex; gap: .75rem; align-items: center; margin: 0 0 1.25rem; }}
    .section-heading .emoji {{ display: grid; place-items: center; width: 42px; height: 42px; border-radius: 14px; font-size: 1.25rem; }}
    .section-heading h2 {{ margin: 0; font: 700 2rem 'Gaegu', cursive; letter-spacing: 0; }}
    .section-heading p {{ margin: .1rem 0 0; color: var(--muted); font-size: .85rem; }}
    .interests {{ background: linear-gradient(90deg, rgba(201,234,216,.25), rgba(255,250,244,0)); border-radius: 12px; }}
    .tag-row {{ display: flex; flex-wrap: wrap; gap: .7rem; }}
    .tag {{ display: inline-block; padding: .58rem .95rem; border: 1px solid rgba(80, 65, 75, .08); border-radius: 999px; font-size: .92rem; color: #514a54; }}
    .tag-rose {{ background: var(--rose); }} .tag-peach {{ background: var(--peach); }}
    .tag-butter {{ background: var(--butter); }} .tag-mint {{ background: var(--mint); }}
    .tag-sky {{ background: var(--sky); }} .tag-lilac {{ background: var(--lilac); }}
    .tag-aqua {{ background: var(--aqua); }}
    .collections {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }}
    .collection {{ padding: 1.15rem 1.2rem .8rem; border-radius: 8px; border: 1px solid rgba(80, 65, 75, .07); }}
    .collection.music {{ background: #fff2f1; }} .collection.books {{ background: #f0f8f1; }} .collection.movies {{ background: #f1f5fc; }}
    .collection-title {{ margin: 0 0 .8rem; font: 700 1.45rem 'Gaegu', cursive; }}
    .list-item {{ display: flex; gap: .65rem; padding: .75rem 0; border-top: 1px dashed rgba(80,65,75,.16); }}
    .list-icon {{ flex: 0 0 auto; display: grid; place-items: center; width: 31px; height: 31px; border-radius: 10px; background: white; }}
    .list-item h3 {{ margin: 0 0 .15rem; font: 700 1rem 'Gowun Dodum', sans-serif; }}
    .list-item p {{ margin: 0; color: var(--muted); font-size: .82rem; line-height: 1.55; }}
    .footer {{ display: flex; justify-content: space-between; align-items: center; gap: 1rem; padding: 1.5rem 1rem .5rem; border-top: 1px dashed #d9cbd0; color: var(--muted); font-size: .86rem; }}
    .footer a {{ color: #b65f7c; text-decoration: none; }}

    @media (max-width: 760px) {{
        .stMainBlockContainer {{ padding: 1rem 1rem 2.5rem; }}
        .hero {{ grid-template-columns: 1fr; gap: 2.4rem; padding: 2.8rem .25rem 3rem; }}
        .hero h1 {{ font-size: 2.7rem; }}
        .hero-art {{ width: min(88%, 370px); }}
        .hero-art img {{ height: 280px; }}
        .section {{ padding: 1.7rem .25rem 2rem; }}
        .collections {{ grid-template-columns: 1fr; gap: .8rem; }}
        .footer {{ align-items: flex-start; flex-direction: column; }}
    }}
    </style>

    <div class="site">
      <header class="topbar">
        <a class="brand" href="#home">my little page ✿</a>
        <span class="top-note">작은 취향을 모아 만든 자기소개</span>
      </header>

      <main>
        <section class="hero" id="home">
          <div>
            <p class="eyebrow">A LITTLE INTRODUCTION ABOUT ME</p>
            <h1>안녕하세요,<br /><em>{escape(PROFILE['name'])}</em>입니다!</h1>
            <p class="affiliation">{escape(PROFILE['affiliation'])}</p>
            <span class="age-note">{escape(PROFILE['age'])}살</span>
            <p class="intro">{escape(PROFILE['intro'])}</p>
            <span class="hello-note">반가워요, 천천히 둘러봐 주세요 ♡</span>
          </div>
          <div class="hero-art">
            <img src="{escape(PROFILE['image_url'])}" alt="내가 좋아하는 분위기의 꽃 사진" />
            <div class="photo-caption">오늘의 나를 한 장에 담기</div>
            <span class="photo-sticker" aria-hidden="true">🌼</span>
          </div>
        </section>

        <section class="section interests" id="interests">
          <div class="section-heading">
            <span class="emoji" style="background:var(--mint)">♡</span>
            <div><h2>요즘 좋아하는 것</h2><p>저를 기분 좋게 만드는 작은 취향들</p></div>
          </div>
          <div class="tag-row">{make_tags(INTERESTS)}</div>
        </section>

        <section class="section" id="favorites">
          <div class="section-heading">
            <span class="emoji" style="background:var(--lilac)">✦</span>
            <div><h2>마음에 오래 남은 것들</h2><p>좋아하는 음악, 책, 그리고 영화</p></div>
          </div>
          <div class="collections">
            <div class="collection music"><h3 class="collection-title">♫ 좋아하는 음악</h3>{make_list(FAVORITE_MUSIC, '♫')}</div>
            <div class="collection books"><h3 class="collection-title">▤ 읽은 책</h3>{make_list(READ_BOOKS, '▤')}</div>
            <div class="collection movies"><h3 class="collection-title">▷ 본 영화</h3>{make_list(WATCHED_MOVIES, '▷')}</div>
          </div>
        </section>
      </main>

      <footer class="footer">
        <span>읽어줘서 고마워요. 오늘도 다정한 하루 보내세요 ☁</span>
        <a href="mailto:{escape(PROFILE['email'])}">편하게 인사하기 · {escape(PROFILE['email'])}</a>
      </footer>
    </div>
    """,
    unsafe_allow_html=True,
)
