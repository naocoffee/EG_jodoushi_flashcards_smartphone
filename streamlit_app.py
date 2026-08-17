<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>助動詞フラッシュカード</title>
<style>
  @font-face {
    font-family: "YuGoFallback";
    src: local("Yu Gothic Medium"), local("游ゴシック Medium"), local("Hiragino Sans");
  }

  :root {
    --ink: #4a3f2a;
    --ink-dark: #2e2a20;
    --accent: #b5762c;
    --red: #d32f2f;
    --cream: #fffdf6;
    --badge: #ffe3b3;
    --good-bg: #eef7e6;
    --good-fg: #3d6b1f;
    --good-border: #6b8f3f;
    --rev-bg: #fdeee0;
    --rev-fg: #a5471f;
    --rev-border: #c0602c;
  }

  * { box-sizing: border-box; }

  html, body {
    margin: 0;
    padding: 0;
    background: #e9e4d8;
    font-family: "Yu Gothic", "游ゴシック", "Yu Gothic Medium", "YuGoFallback",
                 "Hiragino Sans", sans-serif;
    font-weight: 700;
    color: var(--ink-dark);
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    width: 100%;
  }

  /* ===== 9:15 のスマホフレーム ===== */
  #phone {
    position: relative;
    width: min(92vw, 54vh);
    aspect-ratio: 9 / 15;
    background: #ffffff;
    border-radius: 34px;
    box-shadow: 0 18px 40px rgba(74,63,42,0.35);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    border: 3px solid #2e2a20;
  }

  #notch {
    width: 34%;
    height: 18px;
    background: #2e2a20;
    border-radius: 0 0 14px 14px;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    z-index: 20;
  }

  #screen {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 30px 16px 14px;
    overflow-y: auto;
    background: #ffffff;
  }

  h1.app-title {
    color: var(--ink);
    font-size: 17px;
    text-align: center;
    margin: 4px 0 0;
    transform: rotate(-1deg);
    letter-spacing: 0.5px;
  }

  .subtitle-text {
    text-align: center;
    color: var(--ink);
    opacity: 0.75;
    font-size: 10px;
    margin: 2px 0 14px;
  }

  .base-text { font-size: 12px; text-align: center; margin: 6px 0; }

  /* ===== 共通ボタン ===== */
  button {
    font-family: inherit;
    font-weight: 700;
    font-size: 13px;
    border-radius: 10px 14px 12px 16px / 14px 10px 16px 12px;
    border: 2.5px solid var(--ink);
    background: var(--cream);
    color: var(--ink-dark);
    box-shadow: 3px 4px 0 rgba(74,63,42,0.25);
    padding: 9.5px 10px;
    cursor: pointer;
    transition: transform 0.1s ease-in-out;
    width: 100%;
  }
  button:active { transform: translate(1px,1px); box-shadow: 1px 2px 0 rgba(74,63,42,0.25); }
  button.primary { background: var(--badge); color: #7a4a12; }

  .btn-row { display: flex; gap: 8px; margin-top: 8px; }
  .btn-row button { flex: 1; font-size: 11.5px; padding: 9.5px 4px; }
  #backToFrontBtn { background: var(--badge); border-color: var(--accent); color: #7a4a12; }

  /* ===== チェックボックス ===== */
  .check-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    font-size: 12px;
    color: var(--ink);
    margin: 14px 0 20px;
  }
  .check-row input { width: 16px; height: 16px; accent-color: var(--accent); }

  /* ===== 進捗 ===== */
  .progress-wrap {
    width: 100%;
    height: 8px;
    background: #eee5cf;
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 4px;
  }
  .progress-bar { height: 100%; background: var(--accent); transition: width 0.25s ease; }
  .progress-caption { font-size: 10.5px; color: var(--ink); opacity: 0.8; text-align: center; margin-bottom: 10px; }

  /* ===== フラッシュカード ===== */
  .card-area { flex: 1; display: flex; align-items: center; justify-content: center; perspective: 1200px; }

  .flash-card {
    position: relative;
    width: 100%;
    min-height: 240px;
    border-radius: 10px 14px 12px 16px / 14px 10px 16px 12px;
    padding: 22px 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    box-shadow: 5px 7px 0px rgba(74,63,42,0.15);
    background: #ffffff;
  }
  .front-card { border: 3px solid var(--ink); transform: rotate(0.6deg); }
  .back-card  { border: 3px solid var(--accent); transform: rotate(-0.6deg); }

  .card-label {
    font-size: 10px;
    letter-spacing: 3px;
    opacity: 0.6;
    margin-bottom: 8px;
    text-transform: uppercase;
    border-bottom: 2px dashed var(--ink);
    padding-bottom: 5px;
  }
  .card-word { font-size: 26px; margin-bottom: 12px; line-height: 1.3; color: var(--red); word-break: break-word; }
  .card-usage {
    font-size: 11px;
    background: var(--badge);
    color: #000;
    display: inline-block;
    padding: 3px 14px;
    border-radius: 999px;
    margin-bottom: 12px;
    border: 2px solid var(--accent);
    transform: rotate(-2deg);
  }
  .card-example { font-size: 14.5px; line-height: 1.65; }
  .card-meaning { font-size: 21px; margin-bottom: 10px; color: var(--red); }
  .aux-highlight { color: var(--red); }

  .tap-hint {
    text-align: center;
    font-size: 10px;
    color: var(--ink);
    opacity: 0.55;
    margin-top: 8px;
  }

  /* ===== 統計 ===== */
  .stat-row { display: flex; gap: 10px; margin: 14px 0 4px; }
  .stat-box {
    flex: 1;
    text-align: center;
    border-radius: 12px 16px 14px 18px / 16px 12px 18px 14px;
    padding: 12px 6px;
    border: 3px solid var(--ink);
    transform: rotate(-1deg);
  }
  .stat-box .num { font-size: 22px; }
  .stat-box .lbl { font-size: 10px; margin-top: 2px; }

  .divider { border: none; border-top: 2px dashed #d8cfb8; margin: 14px 0; }

  .mini-stat-row { display: flex; gap: 10px; margin-bottom: 10px; }
  .mini-stat { flex: 1; text-align: center; background: #f7f3e6; border-radius: 10px; padding: 8px 4px; }
  .mini-stat .num { font-size: 17px; color: var(--ink); }
  .mini-stat .lbl { font-size: 9.5px; color: var(--ink); opacity: 0.8; }

  .review-list { font-size: 12px; line-height: 1.9; max-height: 140px; overflow-y: auto; padding-right: 2px; }
  .review-list strong { color: var(--ink-dark); }

  .center-msg { text-align: center; font-size: 13px; margin: 10px 0; }

  .screen-flex-center { flex: 1; display: flex; flex-direction: column; justify-content: center; }

  ::-webkit-scrollbar { width: 5px; }
  ::-webkit-scrollbar-thumb { background: #d8cfb8; border-radius: 4px; }

  [hidden] { display: none !important; }
</style>
</head>
<body>

<div id="phone">
  <div id="notch"></div>
  <div id="screen">

    <h1 class="app-title">助動詞Flash</h1>
    <p class="subtitle-text">助動詞・助動詞+have+PP をマスターしよう</p>

    <!-- ===== スタート画面 ===== -->
    <div id="view-start" class="screen-flex-center">
      <p class="base-text">全 <strong id="totalCount"></strong> 枚のカードが登録されています。</p>
      <div class="check-row">
        <input type="checkbox" id="shuffleCheck" checked>
        <label for="shuffleCheck">カードの順番をシャッフルする</label>
      </div>
      <button class="primary" id="startBtn">学習をスタート</button>
    </div>

    <!-- ===== 学習画面 ===== -->
    <div id="view-study" hidden style="flex:1; display:flex; flex-direction:column;">
      <div class="progress-wrap"><div class="progress-bar" id="progressBar"></div></div>
      <div class="progress-caption" id="progressCaption"></div>

      <div class="card-area">
        <div class="flash-card front-card" id="cardFront">
          <div class="card-label">Question</div>
          <div class="card-word" id="qWord"></div>
          <div class="card-example" id="qExample"></div>
        </div>
        <div class="flash-card back-card" id="cardBack" hidden>
          <div class="card-label">Answer</div>
          <div class="card-usage" id="aUsage"></div>
          <div class="card-meaning" id="aMeaning"></div>
          <div class="card-example" id="aExample"></div>
        </div>
      </div>

      <div id="frontControls">
        <p class="tap-hint">タップしてカードをめくる</p>
      </div>

      <div id="backControls" hidden>
        <p class="center-msg">できた？</p>
        <div class="btn-row">
          <button id="backToFrontBtn">表面へ</button>
          <button id="goodBtn">できた</button>
          <button id="reviewBtn">まだ不安</button>
        </div>
      </div>

      <hr class="divider">
      <div class="mini-stat-row">
        <div class="mini-stat"><div class="num" id="miniGood">0</div><div class="lbl">覚えた</div></div>
        <div class="mini-stat"><div class="num" id="miniReview">0</div><div class="lbl">まだ不安</div></div>
      </div>
      <button id="quitBtn">終了する</button>
    </div>

    <!-- ===== 結果画面 ===== -->
    <div id="view-finish" hidden class="screen-flex-center">
      <p class="center-msg" style="font-size:14px;">🎉 全カードを学習しました！お疲れさまでした。</p>
      <div class="stat-row">
        <div class="stat-box" style="background:var(--good-bg); color:var(--good-fg); border-color:var(--good-border);">
          <div class="num" id="finalGood">0</div><div class="lbl">覚えた (Good)</div>
        </div>
        <div class="stat-box" style="background:var(--rev-bg); color:var(--rev-fg); border-color:var(--rev-border);">
          <div class="num" id="finalReview">0</div><div class="lbl">まだ不安 (Review)</div>
        </div>
      </div>
      <p class="base-text" style="margin-top:16px;">復習が必要なカード一覧</p>
      <div class="review-list" id="reviewList"></div>
      <button class="primary" id="restartBtn" style="margin-top:16px;">最初からやり直す</button>
    </div>

  </div>
</div>

<script>
const flashcards = [
  {word:"must have done",usage:"過去のことへの確信",meaning:"～したに違いない",english_example:"She must have failed the exam.",japanese_example:"彼女は試験に合格しなかったに違いない。",aux_en:"must have",aux_ja:"に違いない",pp_en:"failed",pp_ja:"合格しなかった"},
  {word:"should have done",usage:"過去のことへの推量",meaning:"～したはずだ",english_example:"He should have received my email yesterday.",japanese_example:"彼は昨日、私のメールを受け取ったはずだ。",aux_en:"should have",aux_ja:"はずだ",pp_en:"received",pp_ja:"受け取った"},
  {word:"should have done",usage:"過去への後悔・非難",meaning:"～すべきだったのに",english_example:"I should have studied harder.",japanese_example:"もっと勉強しておくべきだった。",aux_en:"should have",aux_ja:"べきだった",pp_en:"studied",pp_ja:"勉強しておく"},
  {word:"ought to have done",usage:"過去のことへの推量",meaning:"～したはずだ",english_example:"He ought to have arrived by now.",japanese_example:"彼は今ごろもう到着したはずだ。",aux_en:"ought to have",aux_ja:"はずだ",pp_en:"arrived",pp_ja:"到着した"},
  {word:"cannot have done",usage:"過去のことへの確信（否定）",meaning:"～したはずがない",english_example:"He cannot have said such a thing.",japanese_example:"彼がそんなことを言ったはずがない。",aux_en:"cannot have",aux_ja:"はずがない",pp_en:"said",pp_ja:"言った"},
  {word:"couldn't have done",usage:"過去のことへの確信（否定）",meaning:"～したはずがない",english_example:"He couldn't have said such a thing.",japanese_example:"彼がそんなことを言ったはずがない。",aux_en:"couldn't have",aux_ja:"はずがない",pp_en:"said",pp_ja:"言った"},
  {word:"may have done",usage:"過去のことへの推量",meaning:"～したかもしれない",english_example:"He may have lost his way.",japanese_example:"彼は道に迷ったかもしれない。",aux_en:"may have",aux_ja:"かもしれない",pp_en:"lost",pp_ja:"迷った"},
  {word:"might have done",usage:"過去のことへの推量",meaning:"～したかもしれない",english_example:"He might have lost his way.",japanese_example:"彼は道に迷ったかもしれない。",aux_en:"might have",aux_ja:"かもしれない",pp_en:"lost",pp_ja:"迷った"},
  {word:"could have done",usage:"過去のことへの推量",meaning:"～したかもしれない",english_example:"He could have lost his way.",japanese_example:"彼は道に迷ったかもしれない。",aux_en:"could have",aux_ja:"かもしれない",pp_en:"lost",pp_ja:"迷った"},
  {word:"can",usage:"能力・可能",meaning:"～することができる",english_example:"She can play the piano.",japanese_example:"彼女はピアノが弾ける。",aux_en:"can",aux_ja:"弾ける"},
  {word:"can",usage:"許可",meaning:"～してもよい",english_example:"You can use my cell phone.",japanese_example:"私の携帯電話を使ってもいいですよ。",aux_en:"can",aux_ja:"てもいいです"},
  {word:"can",usage:"依頼",meaning:"～してくれますか",english_example:"Can you open the door?",japanese_example:"ドアを開けてくれますか。",aux_en:"Can",aux_ja:"てくれますか"},
  {word:"can",usage:"推量（可能性）",meaning:"～はあり得る",english_example:"An accident can happen at any time.",japanese_example:"事故はいつでも起こり得る。",aux_en:"can",aux_ja:"得る"},
  {word:"can't",usage:"否定の推量",meaning:"～のはずがない",english_example:"The rumor can't be true.",japanese_example:"そのうわさが本当であるはずがない。",aux_en:"can't",aux_ja:"はずがない"},
  {word:"may",usage:"許可",meaning:"～してもよい",english_example:"May I ask you a question?",japanese_example:"質問をしてもよろしいですか。",aux_en:"May",aux_ja:"てもよろしいです"},
  {word:"may",usage:"推量",meaning:"～かもしれない",english_example:"He may be at home.",japanese_example:"彼は家にいるかもしれない。",aux_en:"may",aux_ja:"かもしれない"},
  {word:"must",usage:"義務・必要",meaning:"～しなければならない",english_example:"You must get some sleep.",japanese_example:"あなたは少し寝ないといけません。",aux_en:"must",aux_ja:"ないといけません"},
  {word:"must",usage:"推量（確信）",meaning:"～に違いない",english_example:"He must be tired.",japanese_example:"彼は疲れているに違いない。",aux_en:"must",aux_ja:"に違いない"},
  {word:"must not",usage:"禁止",meaning:"～してはいけない",english_example:"You must not take pictures here.",japanese_example:"ここで写真を撮ってはいけません。",aux_en:"must not",aux_ja:"てはいけません"},
  {word:"should (ought to)",usage:"義務・助言",meaning:"～すべきだ",english_example:"You should be more careful.",japanese_example:"君はもっと気を付けるべきだ。",aux_en:"should",aux_ja:"べきだ"},
  {word:"should (ought to)",usage:"推量",meaning:"～のはずだ",english_example:"They should arrive here soon.",japanese_example:"彼らはもうすぐここに着くはずだ。",aux_en:"should",aux_ja:"はずだ"},
  {word:"will",usage:"未来の予測",meaning:"～だろう",english_example:"It will rain this afternoon.",japanese_example:"今日の午後は雨が降るだろう。",aux_en:"will",aux_ja:"だろう"},
  {word:"will",usage:"意志",meaning:"～するつもりだ",english_example:"I'll do my homework after dinner.",japanese_example:"私は夕食後に宿題をするつもりです。",aux_en:"'ll",aux_ja:"つもりです"},
  {word:"will / would",usage:"過去の習慣",meaning:"よく～したものだ",english_example:"We would often go to the movies.",japanese_example:"私たちはよく映画を見に行ったものだ。",aux_en:"would",aux_ja:"ものだ"},
  {word:"shall I ～?",usage:"申し出",meaning:"(私が)～しましょうか",english_example:"Shall I open the window?",japanese_example:"窓を開けましょうか。",aux_en:"Shall I",aux_ja:"ましょうか"},
  {word:"shall we ～?",usage:"提案",meaning:"(一緒に)～しませんか",english_example:"Shall we go to a movie tomorrow?",japanese_example:"明日、映画に行きませんか。",aux_en:"Shall we",aux_ja:"ませんか"},
  {word:"used to",usage:"過去の習慣",meaning:"(以前は)～したものだ",english_example:"I used to walk to school with my friends.",japanese_example:"私は(以前は)友達と歩いて登校したものだ。",aux_en:"used to",aux_ja:"ものだ"},
  {word:"had better",usage:"命令・忠告",meaning:"～しなさい，～するのがよい",english_example:"You had better see a doctor.",japanese_example:"医者に診てもらいなさい。",aux_en:"had better",aux_ja:"なさい"}
];

const TOTAL = flashcards.length;

let state = {
  order: [],
  index: 0,
  flipped: false,
  good: 0,
  review: 0,
  reviewWords: []
};

document.getElementById('totalCount').textContent = TOTAL;

const viewStart = document.getElementById('view-start');
const viewStudy = document.getElementById('view-study');
const viewFinish = document.getElementById('view-finish');

function escapeHtml(s){
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function highlight(text, target){
  if(!target) return escapeHtml(text);
  const idx = text.indexOf(target);
  if(idx === -1) return escapeHtml(text);
  const before = escapeHtml(text.slice(0, idx));
  const mid = escapeHtml(text.slice(idx, idx + target.length));
  const after = escapeHtml(text.slice(idx + target.length));
  return `${before}<span class="aux-highlight">${mid}</span>${after}`;
}

function renderCard(){
  const card = flashcards[state.order[state.index]];

  let enHTML = highlight(card.english_example, card.aux_en);
  let jaHTML = highlight(card.japanese_example, card.aux_ja);
  if(card.pp_en){
    // second pass highlight for PP portion (works on plain text separately)
    const enPlain = card.english_example;
    const idxPP = enPlain.indexOf(card.pp_en);
    if(idxPP !== -1 && card.pp_en !== card.aux_en){
      enHTML = buildDoubleHighlight(enPlain, card.aux_en, card.pp_en);
    }
  }
  if(card.pp_ja){
    const jaPlain = card.japanese_example;
    const idxPP = jaPlain.indexOf(card.pp_ja);
    if(idxPP !== -1 && card.pp_ja !== card.aux_ja){
      jaHTML = buildDoubleHighlight(jaPlain, card.aux_ja, card.pp_ja);
    }
  }

  document.getElementById('qWord').textContent = card.word;
  document.getElementById('qExample').innerHTML = enHTML;
  document.getElementById('aUsage').textContent = card.usage;
  document.getElementById('aMeaning').textContent = card.meaning;
  document.getElementById('aExample').innerHTML = jaHTML;

  const progressNum = state.index + 1;
  document.getElementById('progressBar').style.width = (progressNum / TOTAL * 100) + '%';
  document.getElementById('progressCaption').textContent = `${progressNum} / ${TOTAL} 問目`;

  document.getElementById('miniGood').textContent = state.good;
  document.getElementById('miniReview').textContent = state.review;
}

function buildDoubleHighlight(text, a, b){
  // Highlight two distinct substrings within text, in order of appearance
  const marks = [];
  let ia = text.indexOf(a);
  if(ia !== -1) marks.push({start: ia, end: ia + a.length});
  let ib = text.indexOf(b);
  if(ib !== -1) marks.push({start: ib, end: ib + b.length});
  marks.sort((x,y) => x.start - y.start);

  let result = '';
  let cursor = 0;
  for(const m of marks){
    if(m.start < cursor) continue;
    result += escapeHtml(text.slice(cursor, m.start));
    result += `<span class="aux-highlight">${escapeHtml(text.slice(m.start, m.end))}</span>`;
    cursor = m.end;
  }
  result += escapeHtml(text.slice(cursor));
  return result;
}

function showFront(){
  state.flipped = false;
  document.getElementById('cardFront').hidden = false;
  document.getElementById('cardBack').hidden = true;
  document.getElementById('frontControls').hidden = false;
  document.getElementById('backControls').hidden = true;
}

function showBack(){
  state.flipped = true;
  document.getElementById('cardFront').hidden = true;
  document.getElementById('cardBack').hidden = false;
  document.getElementById('frontControls').hidden = true;
  document.getElementById('backControls').hidden = false;
}

function goNext(isGood){
  const card = flashcards[state.order[state.index]];
  if(isGood){
    state.good++;
  } else {
    state.review++;
    state.reviewWords.push(card);
  }
  state.index++;

  if(state.index >= TOTAL){
    finish();
  } else {
    showFront();
    renderCard();
  }
}

function finish(){
  viewStudy.hidden = true;
  viewFinish.hidden = false;
  document.getElementById('finalGood').textContent = state.good;
  document.getElementById('finalReview').textContent = state.review;

  const listEl = document.getElementById('reviewList');
  if(state.reviewWords.length === 0){
    listEl.innerHTML = '<p class="center-msg" style="opacity:0.7;">復習が必要なカードはありません。素晴らしい！</p>';
  } else {
    listEl.innerHTML = state.reviewWords.map(w =>
      `<div>・<strong>${escapeHtml(w.word)}</strong> ： ${escapeHtml(w.meaning)}</div>`
    ).join('');
  }
}

function resetAll(){
  state = { order: [], index: 0, flipped: false, good: 0, review: 0, reviewWords: [] };
  viewStart.hidden = false;
  viewStudy.hidden = true;
  viewFinish.hidden = true;
}

function shuffleArray(arr){
  for(let i = arr.length - 1; i > 0; i--){
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// ===== イベント =====
document.getElementById('startBtn').addEventListener('click', () => {
  let order = Array.from({length: TOTAL}, (_, i) => i);
  if(document.getElementById('shuffleCheck').checked){
    order = shuffleArray(order);
  }
  state.order = order;
  state.index = 0;
  state.good = 0;
  state.review = 0;
  state.reviewWords = [];

  viewStart.hidden = true;
  viewStudy.hidden = false;
  showFront();
  renderCard();
});

document.getElementById('cardFront').addEventListener('click', showBack);

document.getElementById('backToFrontBtn').addEventListener('click', showFront);
document.getElementById('goodBtn').addEventListener('click', () => goNext(true));
document.getElementById('reviewBtn').addEventListener('click', () => goNext(false));

document.getElementById('quitBtn').addEventListener('click', resetAll);
document.getElementById('restartBtn').addEventListener('click', resetAll);
</script>

</body>
</html>