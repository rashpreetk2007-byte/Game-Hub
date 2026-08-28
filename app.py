import streamlit as st
import random
import time

# ============================================================
# PLAYVERSE
# All-in-One Mini Gaming Universe
# Created by Rashpreet Kaur Arora
# ============================================================

st.set_page_config(
    page_title="PLAYVERSE",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 10% 10%, #ffd6e7 0%, transparent 25%),
        radial-gradient(circle at 90% 10%, #c9f4ff 0%, transparent 25%),
        radial-gradient(circle at 50% 90%, #e8d7ff 0%, transparent 30%),
        linear-gradient(135deg, #fff7ed, #f5f3ff, #ecfeff);
}

.main-title {
    text-align: center;
    font-size: 64px;
    font-weight: 1000;
    color: #6d28d9;
    text-shadow: 3px 3px 0px #fbcfe8;
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    font-size: 21px;
    font-weight: 700;
    color: #475569;
}

.creator {
    text-align: center;
    color: #db2777;
    font-weight: 800;
    font-size: 16px;
    margin-bottom: 25px;
}

.hero {
    padding: 35px;
    border-radius: 30px;
    text-align: center;
    background: linear-gradient(135deg, #fce7f3, #ede9fe, #cffafe);
    box-shadow: 0 15px 40px rgba(0,0,0,0.12);
    margin: 20px 0;
}

.hero h1 {
    color: #581c87;
    font-size: 38px;
}

.card {
    background: rgba(255,255,255,0.88);
    padding: 24px;
    border-radius: 25px;
    margin: 12px 0;
    box-shadow: 0 8px 25px rgba(15,23,42,0.10);
    border: 2px solid rgba(255,255,255,0.8);
}

.game-card {
    background: white;
    padding: 24px;
    border-radius: 25px;
    min-height: 190px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.10);
    text-align: center;
    margin-bottom: 18px;
}

.game-card h2 {
    color: #4c1d95;
}

.stat-card {
    background: linear-gradient(135deg, #ffffff, #f5f3ff);
    padding: 20px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 7px 20px rgba(0,0,0,0.10);
}

.big-number {
    font-size: 35px;
    font-weight: 900;
    color: #7c3aed;
}

.footer {
    text-align: center;
    padding: 35px;
    color: #64748b;
}

.stButton > button {
    border-radius: 15px;
    font-weight: 800;
    min-height: 45px;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 18px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "logged_in": False,
    "username": "",
    "age": "",
    "page": "🏠 Home",
    "coins": 100,
    "xp": 0,
    "games_played": 0,
    "wins": 0,
    "best_score": 0,
    "streak": 1,
    "selected_game": "",
    "xo_board": [""] * 9,
    "xo_turn": "X",
    "xo_message": "",
    "memory_cards": [],
    "memory_flipped": [],
    "memory_matched": [],
    "memory_score": 0,
    "runner_score": 0,
    "runner_started": False,
    "quiz_score": 0,
    "quiz_question": 0,
    "quiz_answered": False,
    "quiz_current": None,
    "theme": "🌸 Pink Dream"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def add_reward(points=5, coins=5):
    st.session_state.xp += points
    st.session_state.coins += coins
    st.session_state.games_played += 1

    if points > st.session_state.best_score:
        st.session_state.best_score = points


def reset_xo():
    st.session_state.xo_board = [""] * 9
    st.session_state.xo_turn = "X"
    st.session_state.xo_message = ""


def check_winner(board):
    combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]

    if all(board):
        return "DRAW"

    return None


def computer_xo_move():
    empty = [
        i for i, value in enumerate(st.session_state.xo_board)
        if value == ""
    ]

    if empty:
        move = random.choice(empty)
        st.session_state.xo_board[move] = "O"


def start_memory():
    cards = ["🍎", "🍌", "🍇", "🍉", "🍓", "🥝"]
    cards = cards + cards
    random.shuffle(cards)

    st.session_state.memory_cards = cards
    st.session_state.memory_flipped = []
    st.session_state.memory_matched = []
    st.session_state.memory_score = 0
# ============================================================
# LOGIN
# ============================================================

if not st.session_state.logged_in:

    st.markdown(
        '<div class="main-title">🎮 PLAYVERSE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Play • Create • Challenge • Have Fun</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="creator">Created by Rashpreet Kaur Arora</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero">
        <h1>🌈 Welcome to Your Gaming Universe!</h1>
        <p>Mini Games • Creative Fun • Challenges • Achievements</p>
        <p>🏃 🎨 🧩 🧠 ❌⭕ 🐍 🧱 🫧</p>
    </div>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown(
            '<div class="card"><h2 style="text-align:center;">👤 Player Setup</h2></div>',
            unsafe_allow_html=True
        )

        username = st.text_input(
            "🎮 Enter Username",
            placeholder="Enter your gaming name"
        )

        age = st.text_input(
            "🎂 Enter Age",
            placeholder="Example: 20"
        )

        if st.button(
            "🚀 NEXT",
            use_container_width=True
        ):

            if not username.strip():
                st.error("Please enter your username.")

            elif not age.strip():
                st.error("Please enter your age.")

            else:

                st.session_state.username = username.strip()
                st.session_state.age = age.strip()
                st.session_state.logged_in = True
                st.session_state.page = "🏠 Home"

                st.rerun()

    st.markdown("""
    <div class="footer">
        <h3>🎮 PLAYVERSE</h3>
        <p>Created by <b>Rashpreet Kaur Arora</b></p>
        <p>All-in-One Mini Gaming Universe</p>
    </div>
    """, unsafe_allow_html=True)

    st.stop()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## 🎮 PLAYVERSE")

st.sidebar.write(
    f"👋 **{st.session_state.username}**"
)

st.sidebar.write(
    f"🎂 Age: {st.session_state.age}"
)

st.sidebar.divider()

pages = [
    "🏠 Home",
    "🎮 Game Hub",
    "🏃 Endless Runner",
    "❌⭕ XO Battle",
    "🎨 Color Splash",
    "🧩 Memory Match",
    "🐍 Snake Rush",
    "🧱 Brick Breaker",
    "🫧 Bubble Pop",
    "🧠 Quick Quiz",
    "🔢 Number Challenge",
    "🏆 Achievements",
    "📊 Player Dashboard",
    "🎨 Themes"
]

selected_page = st.sidebar.radio(
    "Navigation",
    pages,
    index=pages.index(st.session_state.page)
)

st.session_state.page = selected_page

st.sidebar.divider()

if st.sidebar.button("🚪 Logout", use_container_width=True):
    st.session_state.logged_in = False
    st.rerun()

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎮 PLAYVERSE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your Mini Gaming Universe</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="creator">Created by Rashpreet Kaur Arora • Player: {st.session_state.username}</div>',
    unsafe_allow_html=True
)

# ============================================================
# HOME
# ============================================================

if st.session_state.page == "🏠 Home":

    st.markdown(f"""
    <div class="hero">
        <h1>👋 Welcome, {st.session_state.username}!</h1>
        <p>Ready to play something fun?</p>
        <h2>🏆 Level {1 + st.session_state.xp // 100}</h2>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🪙 Coins", st.session_state.coins)

    with c2:
        st.metric("⭐ XP", st.session_state.xp)

    with c3:
        st.metric("🎮 Games", st.session_state.games_played)

    with c4:
        st.metric("🏆 Wins", st.session_state.wins)

    st.write("")

    st.subheader("🔥 Featured Games")

    cols = st.columns(3)

    featured = [
        ("🏃", "Endless Runner", "Run and collect points."),
        ("❌⭕", "XO Battle", "Challenge the computer."),
        ("🎨", "Color Splash", "Create your own artwork.")
    ]

    for i, item in enumerate(featured):

        icon, title, description = item

        with cols[i]:

            st.markdown(
                f"""
                <div class="game-card">
                    <h1>{icon}</h1>
                    <h2>{title}</h2>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"▶ Play {title}",
                key=f"home_{i}",
                use_container_width=True
            ):
                st.session_state.page = title if title != "Color Splash" else "🎨 Color Splash"
                st.rerun()

    st.subheader("🌟 Why PLAYVERSE?")

    a, b, c = st.columns(3)

    with a:
        st.info("🎮 Multiple mini-games")

    with b:
        st.success("🏆 XP and achievements")

    with c:
        st.warning("🎨 Creative activities")

# ============================================================
# GAME HUB
# ============================================================

elif st.session_state.page == "🎮 Game Hub":

    st.header("🎮 Game Hub")

    games = [
        ("🏃", "Endless Runner", "Avoid obstacles and chase a high score."),
        ("❌⭕", "XO Battle", "Play Tic-Tac-Toe against the computer."),
        ("🎨", "Color Splash", "Create a colorful digital drawing."),
        ("🧩", "Memory Match", "Find matching pairs."),
        ("🐍", "Snake Rush", "Guide the snake and collect food."),
        ("🧱", "Brick Breaker", "Break blocks and increase your score."),
        ("🫧", "Bubble Pop", "Pop bubbles before time runs out."),
        ("🧠", "Quick Quiz", "Answer fun general knowledge questions."),
        ("🔢", "Number Challenge", "Solve quick number challenges.")
    ]

    cols = st.columns(3)

    for i, game in enumerate(games):

        icon, name, description = game

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="game-card">
                    <h1>{icon}</h1>
                    <h2>{name}</h2>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"🎮 PLAY",
                key=f"hub_{i}",
                use_container_width=True
            ):
                st.session_state.page = (
                    name if name in ["🏃 Endless Runner", "❌⭕ XO Battle"]
                    else f"{icon} {name}"
                )

                if name == "Endless Runner":
                    st.session_state.page = "🏃 Endless Runner"

                elif name == "XO Battle":
                    st.session_state.page = "❌⭕ XO Battle"

                elif name == "Color Splash":
                    st.session_state.page = "🎨 Color Splash"

                elif name == "Memory Match":
                    st.session_state.page = "🧩 Memory Match"

                elif name == "Snake Rush":
                    st.session_state.page = "🐍 Snake Rush"

                elif name == "Brick Breaker":
                    st.session_state.page = "🧱 Brick Breaker"

                elif name == "Bubble Pop":
                    st.session_state.page = "🫧 Bubble Pop"

                elif name == "Quick Quiz":
                    st.session_state.page = "🧠 Quick Quiz"

                elif name == "Number Challenge":
                    st.session_state.page = "🔢 Number Challenge"

                st.rerun()

# ============================================================
# ENDLESS RUNNER
# ============================================================

elif st.session_state.page == "🏃 Endless Runner":

    st.header("🏃 Endless Runner")

    st.markdown("""
    <div class="hero">
        <h1>🏃 RUN!</h1>
        <p>Choose your action and build your score.</p>
    </div>
    """, unsafe_allow_html=True)

    if "runner_position" not in st.session_state:
        st.session_state.runner_position = 1

    if "runner_score_game" not in st.session_state:
        st.session_state.runner_score_game = 0

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🏆 Score",
            st.session_state.runner_score_game
        )

    with c2:
        st.metric(
            "🪙 Coins",
            st.session_state.coins
        )

    with c3:
        st.metric(
            "📍 Position",
            st.session_state.runner_position
        )

    st.progress(
        min(
            st.session_state.runner_score_game / 100,
            1.0
        )
    )

    st.write("")

    a, b, c = st.columns(3)

    with a:
        if st.button("⬅️ LEFT", use_container_width=True):
            st.session_state.runner_position = max(
                0,
                st.session_state.runner_position - 1
            )

    with b:
        if st.button("⬆️ JUMP", use_container_width=True):

            points = random.randint(5, 20)

            st.session_state.runner_score_game += points
            st.session_state.coins += 2

            st.success(
                f"🪙 Great jump! +{points} points"
            )

    with c:
        if st.button("➡️ RIGHT", use_container_width=True):
            st.session_state.runner_position = min(
                2,
                st.session_state.runner_position + 1
            )

    st.write("")

    if st.button("🏁 Finish Run", use_container_width=True):

        score = st.session_state.runner_score_game

        st.session_state.xp += score
        st.session_state.coins += score // 5
        st.session_state.games_played += 1

        if score > st.session_state.best_score:
            st.session_state.best_score = score

        st.success(
            f"🏆 Run completed! Score: {score}"
        )

        st.session_state.runner_score_game = 0

# ============================================================
# XO
# ============================================================

elif st.session_state.page == "❌⭕ XO Battle":

    st.header("❌⭕ XO Battle")

    st.info("You are ❌. Computer is ⭕.")

    if not st.session_state.xo_board:
        reset_xo()

    winner = check_winner(st.session_state.xo_board)

    if winner:

        if winner == "X":
            st.success("🎉 You won!")
        elif winner == "O":
            st.error("🤖 Computer won!")
        else:
            st.warning("🤝 It's a draw!")

        if winner == "X":
            st.session_state.wins += 1
            st.session_state.coins += 20
            st.session_state.xp += 30

    cols = st.columns(3)

    for i in range(9):

        with cols[i % 3]:

            symbol = st.session_state.xo_board[i]

            if st.button(
                symbol if symbol else "⬜",
                key=f"xo_{i}",
                use_container_width=True
            ):

                if (
                    not symbol
                    and not winner
                    and st.session_state.xo_turn == "X"
                ):

                    st.session_state.xo_board[i] = "X"

                    if not check_winner(
                        st.session_state.xo_board
                    ):
                        computer_xo_move()

                    st.rerun()

    st.write("")

    if st.button(
        "🔄 New Game",
        use_container_width=True
    ):
        reset_xo()
        st.rerun()
      # ============================================================
# COLOR SPLASH
# ============================================================

elif st.session_state.page == "🎨 Color Splash":

    st.header("🎨 Color Splash")

    st.markdown("""
    <div class="hero">
        <h1>🌈 CREATE SOMETHING BEAUTIFUL</h1>
        <p>Choose a color and make your own digital artwork.</p>
    </div>
    """, unsafe_allow_html=True)

    color = st.color_picker(
        "🎨 Choose Brush Color",
        "#7C3AED"
    )

    size = st.slider(
        "🖌️ Brush Size",
        1,
        30,
        10
    )

    drawing = st.text_area(
        "✏️ Drawing Canvas",
        placeholder="Describe your artwork here, or use this space as your creative canvas.",
        height=250
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "💾 Save Artwork",
            use_container_width=True
        ):

            if drawing.strip():
                st.success("🎨 Artwork saved in this demo session!")
                st.session_state.xp += 10
                st.session_state.coins += 5
            else:
                st.warning("Create something first.")

    with c2:

        if st.button(
            "🧹 Clear Canvas",
            use_container_width=True
        ):
            st.rerun()

    st.markdown(
        f"""
        <div class="card">
            <h2>🖌️ Current Brush</h2>
            <p>Color: {color}</p>
            <p>Size: {size}px</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# MEMORY MATCH
# ============================================================

elif st.session_state.page == "🧩 Memory Match":

    st.header("🧩 Memory Match")

    if not st.session_state.memory_cards:

        start_memory()

    st.write(
        f"🏆 Matches: {len(st.session_state.memory_matched) // 2}/6"
    )

    cols = st.columns(4)

    for i, card in enumerate(
        st.session_state.memory_cards
    ):

        with cols[i % 4]:

            visible = (
                i in st.session_state.memory_flipped
                or i in st.session_state.memory_matched
            )

            label = card if visible else "❓"

            if st.button(
                label,
                key=f"memory_{i}",
                use_container_width=True
            ):

                if (
                    i not in st.session_state.memory_flipped
                    and i not in st.session_state.memory_matched
                ):

                    st.session_state.memory_flipped.append(i)

                    if len(
                        st.session_state.memory_flipped
                    ) == 2:

                        a, b = st.session_state.memory_flipped

                        if (
                            st.session_state.memory_cards[a]
                            ==
                            st.session_state.memory_cards[b]
                        ):

                            st.session_state.memory_matched.extend(
                                [a, b]
                            )

                            st.session_state.memory_score += 10
                            st.session_state.xp += 10
                            st.session_state.coins += 5

                            st.success("🎉 Match!")

                        else:

                            st.warning("Not a match.")

                        st.session_state.memory_flipped = []

                        st.rerun()

    if len(st.session_state.memory_matched) == 12:

        st.success("🏆 You completed the Memory Match!")

    if st.button(
        "🔄 New Memory Game",
        use_container_width=True
    ):

        start_memory()
        st.rerun()

# ============================================================
# SNAKE
# ============================================================

elif st.session_state.page == "🐍 Snake Rush":

    st.header("🐍 Snake Rush")

    st.markdown("""
    <div class="hero">
        <h1>🐍 SNAKE RUSH</h1>
        <p>Collect food and grow your score!</p>
    </div>
    """, unsafe_allow_html=True)

    if "snake_score" not in st.session_state:
        st.session_state.snake_score = 0

    st.metric(
        "🏆 Snake Score",
        st.session_state.snake_score
    )

    directions = [
        "⬆️ UP",
        "⬇️ DOWN",
        "⬅️ LEFT",
        "➡️ RIGHT"
    ]

    direction = st.radio(
        "Choose movement",
        directions,
        horizontal=True
    )

    if st.button(
        "🍎 MOVE & COLLECT",
        use_container_width=True
    ):

        points = random.randint(5, 15)

        st.session_state.snake_score += points
        st.session_state.xp += points
        st.session_state.coins += 2

        st.success(
            f"{direction} → 🍎 +{points} points!"
        )

    if st.button(
        "🔄 Restart Snake",
        use_container_width=True
    ):

        st.session_state.snake_score = 0
        st.rerun()

# ============================================================
# BRICK BREAKER
# ============================================================

elif st.session_state.page == "🧱 Brick Breaker":

    st.header("🧱 Brick Breaker")

    if "brick_score" not in st.session_state:
        st.session_state.brick_score = 0

    st.metric(
        "🏆 Score",
        st.session_state.brick_score
    )

    st.progress(
        min(
            st.session_state.brick_score / 100,
            1.0
        )
    )

    if st.button(
        "🏓 HIT THE BALL",
        use_container_width=True
    ):

        points = random.randint(5, 25)

        st.session_state.brick_score += points
        st.session_state.coins += 3
        st.session_state.xp += points

        st.success(
            f"💥 Brick destroyed! +{points}"
        )

    if st.session_state.brick_score >= 100:

        st.balloons()

        st.success(
            "🏆 LEVEL COMPLETE!"
        )

    if st.button(
        "🔄 Restart Level",
        use_container_width=True
    ):

        st.session_state.brick_score = 0
        st.rerun()

# ============================================================
# BUBBLE POP
# ============================================================

elif st.session_state.page == "🫧 Bubble Pop":

    st.header("🫧 Bubble Pop")

    if "bubble_score" not in st.session_state:
        st.session_state.bubble_score = 0

    st.metric(
        "🫧 Bubble Score",
        st.session_state.bubble_score
    )

    bubbles = [
        "🔴",
        "🟢",
        "🔵",
        "🟡",
        "🟣",
        "🟠"
    ]

    cols = st.columns(3)

    for i in range(12):

        with cols[i % 3]:

            bubble = random.choice(bubbles)

            if st.button(
                bubble,
                key=f"bubble_{i}",
                use_container_width=True
            ):

                points = random.randint(1, 10)

                st.session_state.bubble_score += points
                st.session_state.coins += 1
                st.session_state.xp += points

                st.rerun()

    if st.button(
        "🔄 Reset Bubble Score",
        use_container_width=True
    ):

        st.session_state.bubble_score = 0
        st.rerun()

# ============================================================
# QUIZ
# ============================================================

elif st.session_state.page == "🧠 Quick Quiz":

    st.header("🧠 Quick Quiz")

    quiz = [
        (
            "Which planet is known as the Red Planet?",
            ["Earth", "Mars", "Venus", "Jupiter"],
            "Mars"
        ),
        (
            "How many days are in a week?",
            ["5", "6", "7", "8"],
            "7"
        ),
        (
            "Which animal is known as the King of the Jungle?",
            ["Tiger", "Lion", "Elephant", "Bear"],
            "Lion"
        ),
        (
            "What is H2O commonly called?",
            ["Salt", "Water", "Oxygen", "Hydrogen"],
            "Water"
        ),
        (
            "Which shape has three sides?",
            ["Square", "Circle", "Triangle", "Rectangle"],
            "Triangle"
        )
    ]

    q_index = st.session_state.quiz_question % len(quiz)

    question, options, correct = quiz[q_index]

    st.markdown(
        f"""
        <div class="card">
            <h2>Question {q_index + 1}</h2>
            <h2>{question}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    answer = st.radio(
        "Choose your answer",
        options,
        key=f"quiz_radio_{q_index}_{st.session_state.quiz_question}"
    )

    if st.button(
        "✅ Submit Answer",
        use_container_width=True
    ):

        if answer == correct:

            st.success("🎉 Correct!")

            st.session_state.quiz_score += 1
            st.session_state.xp += 10
            st.session_state.coins += 5

        else:

            st.error(
                f"❌ Correct answer: {correct}"
            )

        st.session_state.quiz_question += 1

    st.metric(
        "🏆 Quiz Score",
        st.session_state.quiz_score
    )

    if st.button(
        "🔄 Restart Quiz",
        use_container_width=True
    ):

        st.session_state.quiz_score = 0
        st.session_state.quiz_question = 0
        st.rerun()

# ============================================================
# NUMBER CHALLENGE
# ============================================================

elif st.session_state.page == "🔢 Number Challenge":

    st.header("🔢 Number Challenge")

    if "number_a" not in st.session_state:
        st.session_state.number_a = random.randint(1, 20)

    if "number_b" not in st.session_state:
        st.session_state.number_b = random.randint(1, 20)

    a = st.session_state.number_a
    b = st.session_state.number_b

    st.markdown(
        f"""
        <div class="hero">
            <h1>{a} + {b} = ?</h1>
            <p>How fast can you solve it?</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    answer = st.number_input(
        "✍️ Your Answer",
        min_value=0,
        step=1
    )

    if st.button(
        "⚡ CHECK",
        use_container_width=True
    ):

        if answer == a + b:

            st.success("🎉 Correct!")

            st.session_state.xp += 15
            st.session_state.coins += 10

        else:

            st.error(
                f"❌ Correct answer is {a + b}"
            )

    if st.button(
        "🔄 New Question",
        use_container_width=True
    ):

        st.session_state.number_a = random.randint(1, 20)
        st.session_state.number_b = random.randint(1, 20)

        st.rerun()

# ============================================================
# ACHIEVEMENTS
# ============================================================

elif st.session_state.page == "🏆 Achievements":

    st.header("🏆 Achievements")

    achievements = [
        (
            "🥇",
            "First Step",
            st.session_state.games_played >= 1
        ),
        (
            "🎮",
            "Game Explorer",
            st.session_state.games_played >= 5
        ),
        (
            "⭐",
            "XP Hunter",
            st.session_state.xp >= 100
        ),
        (
            "🪙",
            "Coin Collector",
            st.session_state.coins >= 200
        ),
        (
            "🏆",
            "Winner",
            st.session_state.wins >= 1
        ),
        (
            "🔥",
            "High Scorer",
            st.session_state.best_score >= 50
        )
    ]

    cols = st.columns(2)

    for i, achievement in enumerate(achievements):

        icon, title, unlocked = achievement

        with cols[i % 2]:

            status = "UNLOCKED ✅" if unlocked else "LOCKED 🔒"

            st.markdown(
                f"""
                <div class="card">
                    <h1>{icon}</h1>
                    <h2>{title}</h2>
                    <p>{status}</p>
                </div>
                """,
                unsafe_allow_html=True
  )
          # ============================================================
# PLAYER DASHBOARD
# ============================================================

elif st.session_state.page == "📊 Player Dashboard":

    st.header("📊 Player Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🪙 Coins",
            st.session_state.coins
        )

    with c2:
        st.metric(
            "⭐ XP",
            st.session_state.xp
        )

    with c3:
        st.metric(
            "🎮 Games",
            st.session_state.games_played
        )

    with c4:
        st.metric(
            "🏆 Wins",
            st.session_state.wins
        )

    st.write("")

    level = 1 + st.session_state.xp // 100
    level_progress = (st.session_state.xp % 100) / 100

    st.subheader(f"⭐ Level {level}")

    st.progress(level_progress)

    st.write(
        f"{st.session_state.xp % 100}/100 XP to next level"
    )

    st.subheader("📊 Game Activity")

    activity = {
        "Games Played": st.session_state.games_played,
        "Wins": st.session_state.wins,
        "XP": st.session_state.xp,
        "Coins": st.session_state.coins
    }

    for label, value in activity.items():

        st.write(f"**{label}**")

        max_value = max(
            value,
            1
        )

        st.progress(
            min(
                value / max(max_value, 100),
                1.0
            )
        )

    st.subheader("🏆 Best Score")

    st.metric(
        "Highest Score",
        st.session_state.best_score
    )

# ============================================================
# THEMES
# ============================================================

elif st.session_state.page == "🎨 Themes":

    st.header("🎨 Choose Your Theme")

    themes = [
        "🌸 Pink Dream",
        "🌊 Ocean",
        "🌌 Galaxy",
        "🌅 Sunset",
        "🌲 Forest",
        "🍭 Candy",
        "⚡ Neon"
    ]

    theme = st.selectbox(
        "Choose a theme",
        themes
    )

    st.session_state.theme = theme

    st.markdown(
        f"""
        <div class="hero">
            <h1>{theme}</h1>
            <p>Your selected PLAYVERSE theme</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "✨ Apply Theme",
        use_container_width=True
    ):

        st.session_state.coins = max(
            0,
            st.session_state.coins - 10
        )

        st.success(
            f"{theme} selected!"
        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    <hr>
    <h2>🎮 PLAYVERSE</h2>
    <p>Play • Create • Challenge • Have Fun</p>
    <p>Created by <b>Rashpreet Kaur Arora</b></p>
    <p>🐍 Python • Streamlit</p>
    <p>🎓 Educational Student Project</p>
    <p>
        ⚠️ This application is a student gaming prototype.
        It does not involve real-money gambling or rewards.
    </p>
</div>
""", unsafe_allow_html=True)
