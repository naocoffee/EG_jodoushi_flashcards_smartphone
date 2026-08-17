import random
import streamlit as st

# =========================================================
# データ定義
# =========================================================
flashcards = [
    # --- 助動詞 + have + PP 一覧 ---
    {
        "word": "must have done",
        "usage": "過去のことへの確信",
        "meaning": "～したに違いない",
        "english_example": "She must have failed the exam.",
        "japanese_example": "彼女は試験に合格しなかったに違いない。",
        "aux_en": "must have",
        "aux_ja": "に違いない",
        "pp_en": "failed",
        "pp_ja": "合格しなかった"
    },
    {
        "word": "should have done",
        "usage": "過去のことへの推量",
        "meaning": "～したはずだ",
        "english_example": "He should have received my email yesterday.",
        "japanese_example": "彼は昨日、私のメールを受け取ったはずだ。",
        "aux_en": "should have",
        "aux_ja": "はずだ",
        "pp_en": "received",
        "pp_ja": "受け取った"
    },
    {
        "word": "should have done",
        "usage": "過去への後悔・非難",
        "meaning": "～すべきだったのに",
        "english_example": "I should have studied harder.",
        "japanese_example": "もっと勉強しておくべきだった。",
        "aux_en": "should have",
        "aux_ja": "べきだった",
        "pp_en": "studied",
        "pp_ja": "勉強しておく"
    },
    {
        "word": "ought to have done",
        "usage": "過去のことへの推量",
        "meaning": "～したはずだ",
        "english_example": "He ought to have arrived by now.",
        "japanese_example": "彼は今ごろもう到着したはずだ。",
        "aux_en": "ought to have",
        "aux_ja": "はずだ",
        "pp_en": "arrived",
        "pp_ja": "到着した"
    },
    {
        "word": "cannot have done",
        "usage": "過去のことへの確信（否定）",
        "meaning": "～したはずがない",
        "english_example": "He cannot have said such a thing.",
        "japanese_example": "彼がそんなことを言ったはずがない。",
        "aux_en": "cannot have",
        "aux_ja": "はずがない",
        "pp_en": "said",
        "pp_ja": "言った"
    },
    {
        "word": "couldn't have done",
        "usage": "過去のことへの確信（否定）",
        "meaning": "～したはずがない",
        "english_example": "He couldn't have said such a thing.",
        "japanese_example": "彼がそんなことを言ったはずがない。",
        "aux_en": "couldn't have",
        "aux_ja": "はずがない",
        "pp_en": "said",
        "pp_ja": "言った"
    },
    {
        "word": "may have done",
        "usage": "過去のことへの推量",
        "meaning": "～したかもしれない",
        "english_example": "He may have lost his way.",
        "japanese_example": "彼は道に迷ったかもしれない。",
        "aux_en": "may have",
        "aux_ja": "かもしれない",
        "pp_en": "lost",
        "pp_ja": "迷った"
    },
    {
        "word": "might have done",
        "usage": "過去のことへの推量",
        "meaning": "～したかもしれない",
        "english_example": "He might have lost his way.",
        "japanese_example": "彼は道に迷ったかもしれない。",
        "aux_en": "might have",
        "aux_ja": "かもしれない",
        "pp_en": "lost",
        "pp_ja": "迷った"
    },
    {
        "word": "could have done",
        "usage": "過去のことへの推量",
        "meaning": "～したかもしれない",
        "english_example": "He could have lost his way.",
        "japanese_example": "彼は道に迷ったかもしれない。",
        "aux_en": "could have",
        "aux_ja": "かもしれない",
        "pp_en": "lost",
        "pp_ja": "迷った"
    },
    # --- 基本助動詞マスターシート ---
    {
        "word": "can",
        "usage": "能力・可能",
        "meaning": "～することができる",
        "english_example": "She can play the piano.",
        "japanese_example": "彼女はピアノが弾ける。",
        "aux_en": "can",
        "aux_ja": "弾ける"
    },
    {
        "word": "can",
        "usage": "許可",
        "meaning": "～してもよい",
        "english_example": "You can use my cell phone.",
        "japanese_example": "私の携帯電話を使ってもいいですよ。",
        "aux_en": "can",
        "aux_ja": "てもいいです"
    },
    {
        "word": "can",
        "usage": "依頼",
        "meaning": "～してくれますか",
        "english_example": "Can you open the door?",
        "japanese_example": "ドアを開けてくれますか。",
        "aux_en": "Can",
        "aux_ja": "てくれますか"
    },
    {
        "word": "can",
        "usage": "推量（可能性）",
        "meaning": "～はあり得る",
        "english_example": "An accident can happen at any time.",
        "japanese_example": "事故はいつでも起こり得る。",
        "aux_en": "can",
        "aux_ja": "得る"
    },
    {
        "word": "can't",
        "usage": "否定の推量",
        "meaning": "～のはずがない",
        "english_example": "The rumor can't be true.",
        "japanese_example": "そのうわさが本当であるはずがない。",
        "aux_en": "can't",
        "aux_ja": "はずがない"
    },
    {
        "word": "may",
        "usage": "許可",
        "meaning": "～してもよい",
        "english_example": "May I ask you a question?",
        "japanese_example": "質問をしてもよろしいですか。",
        "aux_en": "May",
        "aux_ja": "てもよろしいです"
    },
    {
        "word": "may",
        "usage": "推量",
        "meaning": "～かもしれない",
        "english_example": "He may be at home.",
        "japanese_example": "彼は家にいるかもしれない。",
        "aux_en": "may",
        "aux_ja": "かもしれない"
    },
    {
        "word": "must",
        "usage": "義務・必要",
        "meaning": "～しなければならない",
        "english_example": "You must get some sleep.",
        "japanese_example": "あなたは少し寝ないといけません。",
        "aux_en": "must",
        "aux_ja": "ないといけません"
    },
    {
        "word": "must",
        "usage": "推量（確信）",
        "meaning": "～に違いない",
        "english_example": "He must be tired.",
        "japanese_example": "彼は疲れているに違いない。",
        "aux_en": "must",
        "aux_ja": "に違いない"
    },
    {
        "word": "must not",
        "usage": "禁止",
        "meaning": "～してはいけない",
        "english_example": "You must not take pictures here.",
        "japanese_example": "ここで写真を撮ってはいけません。",
        "aux_en": "must not",
        "aux_ja": "てはいけません"
    },
    {
        "word": "should (ought to)",
        "usage": "義務・助言",
        "meaning": "～すべきだ",
        "english_example": "You should be more careful.",
        "japanese_example": "君はもっと気を付けるべきだ。",
        "aux_en": "should",
        "aux_ja": "べきだ"
    },
    {
        "word": "should (ought to)",
        "usage": "推量",
        "meaning": "～のはずだ",
        "english_example": "They should arrive here soon.",
        "japanese_example": "彼らはもうすぐここに着くはずだ。",
        "aux_en": "should",
        "aux_ja": "はずだ"
    },
    {
        "word": "will",
        "usage": "未来の予測",
        "meaning": "～だろう",
        "english_example": "It will rain this afternoon.",
        "japanese_example": "今日の午後は雨が降るだろう。",
        "aux_en": "will",
        "aux_ja": "だろう"
    },
    {
        "word": "will",
        "usage": "意志",
        "meaning": "～するつもりだ",
        "english_example": "I'll do my homework after dinner.",
        "japanese_example": "私は夕食後に宿題をするつもりです。",
        "aux_en": "'ll",
        "aux_ja": "つもりです"
    },
    {
        "word": "will / would",
        "usage": "過去の習慣",
        "meaning": "よく～したものだ",
        "english_example": "We would often go to the movies.",
        "japanese_example": "私たちはよく映画を見に行ったものだ。",
        "aux_en": "would",
        "aux_ja": "ものだ"
    },
    {
        "word": "shall I ～?",
        "usage": "申し出",
        "meaning": "(私が)～しましょうか",
        "english_example": "Shall I open the window?",
        "japanese_example": "窓を開けましょうか。",
        "aux_en": "Shall I",
        "aux_ja": "ましょうか"
    },
    {
        "word": "shall we ～?",
        "usage": "提案",
        "meaning": "(一緒に)～しませんか",
        "english_example": "Shall we go to a movie tomorrow?",
        "japanese_example": "明日、映画に行きませんか。",
        "aux_en": "Shall we",
        "aux_ja": "ませんか"
    },
    {
        "word": "used to",
        "usage": "過去の習慣",
        "meaning": "(以前は)～したものだ",
        "english_example": "I used to walk to school with my friends.",
        "japanese_example": "私は(以前は)友達と歩いて登校したものだ。",
        "aux_en": "used to",
        "aux_ja": "ものだ"
    },
    {
        "word": "had better",
        "usage": "命令・忠告",
        "meaning": "～しなさい，～するのがよい",
        "english_example": "You had better see a doctor.",
        "japanese_example": "医者に診てもらいなさい。",
        "aux_en": "had better",
        "aux_ja": "なさい"
    }
]

TOTAL = len(flashcards)

# =========================================================
# ページ設定 & CSS
# =========================================================
st.set_page_config(page_title="助動詞Flash", layout="centered")

st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-weight: 700 !important;
    }

    html, body {
        background-color: #e9e4d8 !important;
        height: 100%;
        overflow: hidden;
    }

    .stApp {
        background-color: #e9e4d8;
        height: 100vh;
        overflow: hidden;
    }

    /* --- Streamlitの既定UI（ヘッダー・ハンバーガー・フッター）を隠してアプリ感を出す --- */
    #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
    }

    .main {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        overflow: hidden;
    }

    /* --- スマホアプリ画面フレーム（アスペクト比 9:15固定） --- */
    .main .block-container {
        position: relative;
        width: min(92vw, calc(62vh * 9 / 15));
        aspect-ratio: 9 / 15;
        max-height: 92vh;
        overflow-y: auto;
        overflow-x: hidden;
        margin: 0 auto !important;
        background: #ffffff;
        border: 3px solid #2e2a20;
        border-radius: 34px;
        box-shadow: 0 18px 40px rgba(74, 63, 42, 0.35);
        padding: 2.4rem 1.1rem 1rem !important;
    }

    /* --- ノッチ --- */
    .main .block-container::before {
        content: "";
        position: sticky;
        display: block;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 34%;
        height: 16px;
        background: #2e2a20;
        border-radius: 0 0 14px 14px;
        margin-top: -2.4rem;
        margin-bottom: 10px;
        z-index: 50;
    }

    h1, h2, h3, .stCaption, p, span, div, label {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-weight: 700 !important;
    }

    h1 {
        color: #4a3f2a !important;
        transform: rotate(-1deg);
        font-size: 26px !important;
        text-align: center;
    }

    /* --- フラッシュカード本体：手書きノート風 --- */
    .flash-card {
        position: relative;
        border-radius: 10px 14px 12px 16px / 14px 10px 16px 12px;
        padding: 30px 18px;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-bottom: 16px;
        transform: rotate(-0.6deg);
        box-shadow: 5px 7px 0px rgba(74, 63, 42, 0.15);
    }

    .front-card {
        background: #ffffff;
        color: #000000;
        border: 3px solid #4a3f2a;
        transform: rotate(0.6deg);
    }

    .back-card {
        background: #ffffff;
        color: #000000;
        border: 3px solid #b5762c;
        transform: rotate(-0.6deg);
    }

    .card-label {
        font-size: 11px;
        letter-spacing: 3px;
        opacity: 0.6;
        margin-bottom: 8px;
        text-transform: uppercase;
        font-weight: 700;
        border-bottom: 2px dashed #4a3f2a;
        padding-bottom: 5px;
    }

    .card-word {
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 14px;
        line-height: 1.3;
        color: #d32f2f;
    }

    .card-usage {
        font-size: 12px;
        font-weight: 700;
        background: #ffe3b3;
        color: #000000;
        display: inline-block;
        padding: 3px 14px;
        border-radius: 999px;
        margin-bottom: 12px;
        border: 2px solid #b5762c;
        transform: rotate(-2deg);
    }

    .card-example {
        font-size: 16px;
        font-weight: 700;
        line-height: 1.65;
        color: #000000;
        opacity: 1;
    }

    .aux-highlight {
        color: #d32f2f;
    }

    .card-meaning {
        font-size: 23px;
        font-weight: 700;
        margin-bottom: 12px;
        color: #d32f2f;
    }

    .stat-box {
        text-align: center;
        border-radius: 12px 16px 14px 18px / 16px 12px 18px 14px;
        padding: 14px 8px;
        font-weight: 700;
        border: 3px solid #4a3f2a;
        transform: rotate(-1deg);
    }

    /* --- ボタン：手描き風の枠線（縦方向を0.8倍に短く） --- */
    .stButton > button {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        border-radius: 10px 14px 12px 16px / 14px 10px 16px 12px !important;
        border: 3px solid #4a3f2a !important;
        background: #fffdf6 !important;
        color: #2e2a20 !important;
        box-shadow: 3px 4px 0px rgba(74, 63, 42, 0.25);
        transition: transform 0.1s ease-in-out;
        padding: 0.32rem 0.9rem !important;
    }
    .stButton > button:hover {
        transform: translate(-2px, -2px);
        box-shadow: 5px 6px 0px rgba(74, 63, 42, 0.25);
        color: #b5762c !important;
        border-color: #b5762c !important;
    }
    /* primary系ボタン（スタート/やり直す/タップしてめくる/表面へ）：用法バッジと同じ配色 */
    .stButton > button[kind="primary"] {
        background: #ffe3b3 !important;
        color: #000000 !important;
        border: 3px solid #b5762c !important;
    }

    /* --- 進捗バー --- */
    .stProgress > div > div {
        background-color: #b5762c !important;
    }

    /* --- チェックボックス文字 --- */
    .stCheckbox label {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        color: #4a3f2a !important;
    }

    /* --- キャプション文字 --- */
    .stCaption, [data-testid="stCaptionContainer"] {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-weight: 700 !important;
        color: #4a3f2a !important;
        font-size: 11px !important;
    }

    /* --- 「全◯枚のカードが登録されています」等の基準テキスト --- */
    .base-text {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        color: #000000;
        text-align: center;
    }

    /* --- st.metric の数値・ラベル --- */
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-weight: 700 !important;
        color: #4a3f2a !important;
    }
    /* --- サブタイトル文字（小さめ） --- */
    .subtitle-text {
        font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "游ゴシック体", sans-serif !important;
        font-weight: 700 !important;
        color: #4a3f2a !important;
        opacity: 0.8;
        text-align: center;
        font-size: 11px;
        margin-top: -8px;
        margin-bottom: 12px;
    }

    .tap-hint {
        text-align: center;
        font-size: 11px;
        color: #4a3f2a;
        opacity: 0.6;
        margin-top: -4px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# セッション状態の初期化
# =========================================================
def init_session():
    if "started" not in st.session_state:
        st.session_state.started = False
    if "order" not in st.session_state:
        st.session_state.order = list(range(TOTAL))
    if "index" not in st.session_state:
        st.session_state.index = 0
    if "flipped" not in st.session_state:
        st.session_state.flipped = False
    if "good_count" not in st.session_state:
        st.session_state.good_count = 0
    if "review_count" not in st.session_state:
        st.session_state.review_count = 0
    if "review_words" not in st.session_state:
        st.session_state.review_words = []
    if "finished" not in st.session_state:
        st.session_state.finished = False


def reset_all():
    st.session_state.started = False
    st.session_state.order = list(range(TOTAL))
    st.session_state.index = 0
    st.session_state.flipped = False
    st.session_state.good_count = 0
    st.session_state.review_count = 0
    st.session_state.review_words = []
    st.session_state.finished = False


init_session()

st.title("助動詞Flash")
st.markdown(
    '<p class="subtitle-text">助動詞・助動詞+have+PP をマスターしよう</p>',
    unsafe_allow_html=True,
)

# =========================================================
# スタート画面
# =========================================================
if not st.session_state.started:
    st.write("")
    st.markdown(
        f'<p class="base-text">全 <strong>{TOTAL}</strong> 枚のカードが登録されています。</p>',
        unsafe_allow_html=True,
    )
    shuffle_option = st.checkbox("カードの順番をシャッフルする", value=True)

    if st.button("学習をスタート", type="primary", use_container_width=True):
        order = list(range(TOTAL))
        if shuffle_option:
            random.shuffle(order)
        st.session_state.order = order
        st.session_state.index = 0
        st.session_state.flipped = False
        st.session_state.good_count = 0
        st.session_state.review_count = 0
        st.session_state.review_words = []
        st.session_state.finished = False
        st.session_state.started = True
        st.rerun()

# =========================================================
# 結果画面
# =========================================================
elif st.session_state.finished:
    st.success("全カードを学習しました！お疲れさまでした。")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""
            <div class="stat-box" style="background:#eef7e6; color:#3d6b1f; border-color:#6b8f3f;">
                <div style="font-size:26px; font-weight:700;">{st.session_state.good_count}</div>
                <div>覚えた (Good)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div class="stat-box" style="background:#fdeee0; color:#a5471f; border-color:#c0602c;">
                <div style="font-size:26px; font-weight:700;">{st.session_state.review_count}</div>
                <div>まだ不安 (Review)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    if st.session_state.review_words:
        st.subheader("復習が必要なカード一覧")
        for item in st.session_state.review_words:
            st.markdown(f"- **{item['word']}** ： {item['meaning']}")
    else:
        st.info("復習が必要なカードはありません。素晴らしい！")

    st.write("")
    if st.button("最初からやり直す", type="primary", use_container_width=True):
        reset_all()
        st.rerun()

# =========================================================
# 学習画面
# =========================================================
else:
    current_idx = st.session_state.order[st.session_state.index]
    card = flashcards[current_idx]

    # 例文中の助動詞部分を赤色でハイライト
    highlighted_en = card["english_example"].replace(
        card["aux_en"], f'<span class="aux-highlight">{card["aux_en"]}</span>'
    )
    highlighted_ja = card["japanese_example"].replace(
        card["aux_ja"], f'<span class="aux-highlight">{card["aux_ja"]}</span>'
    )
    # 「助動詞 + have + PP」のカードは、PP（過去分詞）部分も赤色でハイライト
    if "pp_en" in card:
        highlighted_en = highlighted_en.replace(
            card["pp_en"], f'<span class="aux-highlight">{card["pp_en"]}</span>'
        )
    if "pp_ja" in card:
        highlighted_ja = highlighted_ja.replace(
            card["pp_ja"], f'<span class="aux-highlight">{card["pp_ja"]}</span>'
        )

    # 進捗バー
    progress_num = st.session_state.index + 1
    st.progress(progress_num / TOTAL)
    st.caption(f"{progress_num} / {TOTAL} 問目")

    # カード表示
    if not st.session_state.flipped:
        st.markdown(
            f"""
            <div class="flash-card front-card">
                <div class="card-label">Question</div>
                <div class="card-word">{card['word']}</div>
                <div class="card-example">{highlighted_en}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="flash-card back-card">
                <div class="card-label">Answer</div>
                <div class="card-usage">{card['usage']}</div>
                <div class="card-meaning">{card['meaning']}</div>
                <div class="card-example">{highlighted_ja}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # コントロールボタン
    if not st.session_state.flipped:
        if st.button("タップしてカードをめくる", type="primary", use_container_width=True):
            st.session_state.flipped = True
            st.rerun()
    else:
        st.markdown('<p class="base-text">できた？</p>', unsafe_allow_html=True)

        def go_to_next(is_good):
            if is_good:
                st.session_state.good_count += 1
            else:
                st.session_state.review_count += 1
                st.session_state.review_words.append(card)

            st.session_state.index += 1
            st.session_state.flipped = False

            if st.session_state.index >= TOTAL:
                st.session_state.finished = True

        col_good, col_review = st.columns(2)
        with col_good:
            if st.button("できた", use_container_width=True):
                go_to_next(True)
                st.rerun()
        with col_review:
            if st.button("まだ不安", use_container_width=True):
                go_to_next(False)
                st.rerun()

        if st.button("表面へ", type="primary", use_container_width=True):
            st.session_state.flipped = False
            st.rerun()

    st.write("")
    st.divider()
    stat_col1, stat_col2 = st.columns(2)
    stat_col1.metric("覚えた", st.session_state.good_count)
    stat_col2.metric("まだ不安", st.session_state.review_count)

    st.write("")
    if st.button("終了する", use_container_width=True):
        reset_all()
        st.rerun()