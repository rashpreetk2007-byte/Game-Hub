import streamlit as st
import random

# ============================================================
# GAME HUB
# Created by: Rashpreet Kaur Arora
# ============================================================

st.set_page_config(
    page_title="FunZone Game Hub",
    page_icon="🎮",
    layout="wide"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #fff1f2 0%,
        #fef3c7 35%,
        #ecfeff 70%,
        #ede9fe 100%
    );
}

.title {
    text-align: center;
    font-size: 52px;
    font-weight: 900;
    margin-top: 15px;
}

.subtitle {
    text-align: center;
    font-size: 21px;
    font-weight: 600;
    margin-bottom: 20px;
}

.creator {
    text-align: center;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 25px;
}

.card {
    background: rgba(255,255,255,0.92);
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.10);
    margin-bottom: 20px;
}

.game-card {
    background: white;
    padding: 22px;
    border-radius: 22px;
    text-align: center;
    min-height: 180px;
    box-shadow: 0 7px 20px rgba(0,0,0,0.10);
    margin-bottom: 20px;
}

.big-emoji {
    font-size: 55px;
}

.center {
    text-align: center;
}

.footer {
    text-align: center;
    padding: 35px;
    color: #475569;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================

if "started" not in st.session_state:
    st.session_state.started = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "age" not in st.session_state:
    st.session_state.age = 0

if "selected_game" not in st.session_state:
    st.session_state.selected_game = "🎮 Game Selection"

# ============================================================
# GAME LIST
# ============================================================

games = [
    "❌⭕ XO Game",
    "🎨 Painting",
    "🧠 Memory Challenge",
    "🧩 Number Puzzle",
    "🎯 Target Challenge",
    "🐍 Snake Challenge",
    "🚀 Space Dodge",
    "🏃 Runner Challenge",
    "🧱 Brick Breaker",
    "🎈 Balloon Pop"
]

# ============================================================
# LOGIN / START
# ============================================================

if not st.session_state.started:

    st.markdown(
        '<div class="title">🎮 FunZone</div>',
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

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown("""
        <div class="card">
            <h1 style="text-align:center;">🌈 Welcome to FunZone!</h1>
            <p style="text-align:center;">
            A colorful collection of simple games for everyone.
            </p>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input(
            "👤 Username",
            placeholder="Enter your username"
        )

        age = st.number_input(
            "🎂 Age",
            min_value=3,
            max_value=100,
            value=18
        )

        if st.button(
            "🚀 NEXT",
            use_container_width=True
        ):

            if not username.strip():
                st.error("Please enter your username.")

            else:

                st.session_state.username = username.strip()
                st.session_state.age = age
                st.session_state.started = True
                st.session_state.selected_game = "🎮 Game Selection"

                st.rerun()

    st.markdown("""
    <div class="footer">
        🎮 FunZone Game Hub<br>
        Created by <b>Rashpreet Kaur Arora</b>
    </div>
    """, unsafe_allow_html=True)

    st.stop()

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">🎮 FunZone</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Play • Create • Challenge • Have Fun</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="creator">👋 Welcome, {st.session_state.username} • Age {st.session_state.age}</div>',
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🎮 FunZone")

st.sidebar.write(
    f"👤 **{st.session_state.username}**"
)

st.sidebar.write(
    f"🎂 Age: **{st.session_state.age}**"
)

st.sidebar.divider()

if st.sidebar.button(
    "🏠 Game Selection",
    use_container_width=True
):
    st.session_state.selected_game = "🎮 Game Selection"
    st.rerun()

if st.sidebar.button(
    "🚪 Exit",
    use_container_width=True
):
    st.session_state.started = False
    st.session_state.selected_game = "🎮 Game Selection"
    st.rerun()

# ============================================================
# GAME SELECTION
# ============================================================

if st.session_state.selected_game == "🎮 Game Selection":

    st.header("🎮 Choose Your Game")

    st.write(
        "Select **one game**. Only that game will open."
    )

    cols = st.columns(2)

    descriptions = {
        "❌⭕ XO Game": "Classic two-player Tic-Tac-Toe.",
        "🎨 Painting": "Create your own colorful digital artwork.",
        "🧠 Memory Challenge": "Test your memory.",
        "🧩 Number Puzzle": "Guess the hidden number.",
        "🎯 Target Challenge": "Try to hit the target.",
        "🐍 Snake Challenge": "Classic snake-style challenge.",
        "🚀 Space Dodge": "Avoid incoming space objects.",
        "🏃 Runner Challenge": "Test your reaction speed.",
        "🧱 Brick Breaker": "Break the virtual bricks.",
        "🎈 Balloon Pop": "Pop as many balloons as possible."
    }

    for i, game in enumerate(games):

        with cols[i % 2]:

            st.markdown(
                f"""
                <div class="game-card">
                    <div class="big-emoji">
                    {game.split(" ")[0]}
                    </div>
                    <h2>{game}</h2>
                    <p>{descriptions[game]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"▶ Play {game}",
                key=f"play_{i}",
                use_container_width=True
            ):
                st.session_state.selected_game = game
                st.rerun()

# ============================================================
# XO GAME
# ============================================================

elif st.session_state.selected_game == "❌⭕ XO Game":

    st.header("❌⭕ XO Game")

    if "xo_board" not in st.session_state:
        st.session_state.xo_board = [""] * 9

    if "xo_turn" not in st.session_state:
        st.session_state.xo_turn = "X"

    if "xo_winner" not in st.session_state:
        st.session_state.xo_winner = ""

    st.write(
        f"Current Turn: **{st.session_state.xo_turn}**"
    )

    board = st.session_state.xo_board

    cols = st.columns(3)

    for i in range(9):

        with cols[i % 3]:

            if st.button(
                board[i] if board[i] else " ",
                key=f"xo_{i}",
                use_container_width=True
            ):

                if board[i] == "" and not st.session_state.xo_winner:

                    board[i] = st.session_state.xo_turn

                    wins = [
                        [0,1,2],
                        [3,4,5],
                        [6,7,8],
                        [0,3,6],
                        [1,4,7],
                        [2,5,8],
                        [0,4,8],
                        [2,4,6]
                    ]

                    for a, b, c in wins:

                        if (
                            board[a]
                            and board[a] == board[b]
                            and board[b] == board[c]
                        ):
                            st.session_state.xo_winner = board[a]

                    if not st.session_state.xo_winner:

                        if all(board):
                            st.session_state.xo_winner = "DRAW"

                        else:
                            st.session_state.xo_turn = (
                                "O"
                                if st.session_state.xo_turn == "X"
                                else "X"
                            )

                    st.rerun()

    if st.session_state.xo_winner:

        if st.session_state.xo_winner == "DRAW":
            st.warning("🤝 It's a Draw!")

        else:
            st.success(
                f"🎉 Player {st.session_state.xo_winner} Wins!"
            )

    if st.button("🔄 Restart XO", use_container_width=True):

        st.session_state.xo_board = [""] * 9
        st.session_state.xo_turn = "X"
        st.session_state.xo_winner = ""
        st.rerun()

    st.divider()

    if st.button("⬅️ Back to Games", use_container_width=True):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# PAINTING
# ============================================================

elif st.session_state.selected_game == "🎨 Painting":

    st.header("🎨 Mini Painting Studio")

    st.write(
        "Create your own simple digital painting."
    )

    color = st.color_picker(
        "🎨 Choose Brush Color",
        "#ff4b4b"
    )

    brush = st.slider(
        "🖌️ Brush Size",
        1,
        30,
        10
    )

    st.info(
        f"Selected brush size: {brush}px"
    )

    canvas = st.text_area(
        "🎨 Your Drawing Area",
        placeholder="Use emojis and symbols to create your art!\n\n"
                    "🌸 🌈 ⭐ 🏠 🌳 🦋 🌻\n"
                    "❤️ 💛 💚 💙 💜",
        height=300
    )

    if st.button(
        "✨ Show My Artwork",
        use_container_width=True
    ):

        st.markdown(
            f"""
            <div class="card">
                <h2>🖼️ Your Artwork</h2>
                <div style="font-size:28px; white-space:pre-wrap;">
                {canvas if canvas else "🎨 Start creating!"}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button(
        "⬅️ Back to Games",
        use_container_width=True
    ):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# MEMORY GAME
# ============================================================

elif st.session_state.selected_game == "🧠 Memory Challenge":

    st.header("🧠 Memory Challenge")

    symbols = ["🍎", "🍌", "🍇", "🍓", "🍉", "🥝"]

    if "memory_sequence" not in st.session_state:
        st.session_state.memory_sequence = random.sample(
            symbols,
            4
        )

    if "memory_started" not in st.session_state:
        st.session_state.memory_started = False

    st.info(
        "Remember these symbols!"
    )

    if not st.session_state.memory_started:

        st.markdown(
            f"""
            <div class="card">
            <h1 style="text-align:center;">
            {" ".join(st.session_state.memory_sequence)}
            </h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "👀 I Remember — Start",
            use_container_width=True
        ):
            st.session_state.memory_started = True
            st.rerun()

    else:

        answer = st.text_input(
            "⌨️ Type the symbols in order",
            placeholder="Example: 🍎 🍌 🍇 🍓"
        )

        if st.button(
            "✅ Check Memory",
            use_container_width=True
        ):

            correct = " ".join(
                st.session_state.memory_sequence
            )

            if answer.strip() == correct:
                st.success("🎉 Excellent Memory!")

            else:
                st.error(
                    f"❌ Correct sequence: {correct}"
                )

    if st.button(
        "🔄 New Memory Challenge",
        use_container_width=True
    ):

        st.session_state.memory_sequence = random.sample(
            symbols,
            4
        )

        st.session_state.memory_started = False

        st.rerun()

    if st.button(
        "⬅️ Back to Games",
        use_container_width=True
    ):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# NUMBER PUZZLE
# ============================================================

elif st.session_state.selected_game == "🧩 Number Puzzle":

    st.header("🧩 Number Guessing Puzzle")

    if "target_number" not in st.session_state:
        st.session_state.target_number = random.randint(
            1,
            20
        )

    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    st.info("Guess a number between 1 and 20.")

    guess = st.number_input(
        "🔢 Your Guess",
        min_value=1,
        max_value=20,
        value=10
    )

    if st.button(
        "🎯 Check Guess",
        use_container_width=True
    ):

        st.session_state.attempts += 1

        if guess == st.session_state.target_number:

            st.success(
                f"🎉 Correct! You found it in "
                f"{st.session_state.attempts} attempts."
            )

        elif guess < st.session_state.target_number:

            st.warning("⬆️ Try a higher number.")

        else:

            st.warning("⬇️ Try a lower number.")

    if st.button(
        "🔄 New Puzzle",
        use_container_width=True
    ):

        st.session_state.target_number = random.randint(
            1,
            20
        )

        st.session_state.attempts = 0

        st.rerun()

    if st.button(
        "⬅️ Back to Games",
        use_container_width=True
    ):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# TARGET CHALLENGE
# ============================================================

elif st.session_state.selected_game == "🎯 Target Challenge":

    st.header("🎯 Target Challenge")

    if "target_score" not in st.session_state:
        st.session_state.target_score = 0

    st.markdown(
        f"""
        <div class="card">
        <h1 style="text-align:center;">
        🎯 SCORE: {st.session_state.target_score}
        </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    targets = [
        "🎯",
        "⭐",
        "🔥",
        "💎",
        "🏆"
    ]

    target = random.choice(targets)

    st.markdown(
        f"""
        <div style="text-align:center;font-size:100px;">
        {target}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "💥 HIT TARGET!",
        use_container_width=True
    ):

        st.session_state.target_score += random.randint(
            5,
            20
        )

        st.success("🎯 Target Hit!")

        st.rerun()

    if st.button(
        "🔄 Reset Score",
        use_container_width=True
    ):

        st.session_state.target_score = 0
        st.rerun()

    if st.button(
        "⬅️ Back to Games",
        use_container_width=True
    ):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# SNAKE CHALLENGE
# ============================================================

elif st.session_state.selected_game == "🐍 Snake Challenge":

    st.header("🐍 Snake Challenge")

    st.info(
        "Mini demo version: choose a direction and collect points."
    )

    if "snake_score" not in st.session_state:
        st.session_state.snake_score = 0

    direction = st.radio(
        "🎮 Choose Direction",
        ["⬆️ Up", "⬇️ Down", "⬅️ Left", "➡️ Right"]
    )

    if st.button(
        "🐍 Move",
        use_container_width=True
    ):

        if random.random() > 0.3:

            st.session_state.snake_score += 1

            st.success(
                f"🍎 Food collected! Score: "
                f"{st.session_state.snake_score}"
            )

        else:

            st.warning(
                "💥 You hit an obstacle!"
            )

    st.metric(
        "🐍 Score",
        st.session_state.snake_score
    )

    if st.button(
        "🔄 Restart Snake",
        use_container_width=True
    ):

        st.session_state.snake_score = 0
        st.rerun()

    if st.button(
        "⬅️ Back to Games",
        use_container_width=True
    ):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# SPACE DODGE
# ============================================================

elif st.session_state.selected_game == "🚀 Space Dodge":

    st.header("🚀 Space Dodge")

    st.info(
        "Choose your movement and try to avoid the asteroid."
    )

    movement = st.select_slider(
        "🚀 Move Spaceship",
        options=[
            "⬅️ Left",
            "⬅️ Slight Left",
            "⏺️ Center",
            "➡️ Slight Right",
            "➡️ Right"
        ]
    )

    asteroid = random.choice([
        "⬅️",
        "⏺️",
        "➡️"
    ])

    st.markdown(
        f"""
        <div class="card">
        <h2 style="text-align:center;">
        ☄️ Asteroid: {asteroid}
        </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "🚀 Dodge!",
        use_container_width=True
    ):

        if (
            ("Left" in movement and asteroid != "⬅️")
            or
            ("Right" in movement and asteroid != "➡️")
            or
            ("Center" in movement and asteroid != "⏺️")
        ):

            st.success("🎉 Great Dodge!")

        else:

            st.error("💥 Collision!")

    if st.button(
        "⬅️ Back to Games",
        use_container_width=True
    ):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# RUNNER
# ============================================================

elif st.session_state.selected_game == "🏃 Runner Challenge":

    st.header("🏃 Runner Challenge")

    st.write(
        "Press the button as quickly as possible!"
    )

    if "runner_score" not in st.session_state:
        st.session_state.runner_score = 0

    if st.button(
        "🏃 RUN!",
        use_container_width=True
    ):

        points = random.randint(1, 10)

        st.session_state.runner_score += points

        st.success(
            f"⚡ You gained {points} points!"
        )

    st.metric(
        "🏃 Score",
        st.session_state.runner_score
    )

    if st.button(
        "🔄 Restart",
        use_container_width=True
    ):

        st.session_state.runner_score = 0
        st.rerun()

    if st.button(
        "⬅️ Back to Games",
        use_container_width=True
    ):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# BRICK BREAKER
# ============================================================

elif st.session_state.selected_game == "🧱 Brick Breaker":

    st.header("🧱 Brick Breaker")

    if "brick_score" not in st.session_state:
        st.session_state.brick_score = 0

    bricks = [
        "🟥",
        "🟧",
        "🟨",
        "🟩",
        "🟦"
    ]

    st.markdown(
        f"""
        <div style="text-align:center;font-size:40px;">
        {" ".join(bricks)}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div style="text-align:center;font-size:50px;">
        🏓
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "💥 Hit Bricks",
        use_container_width=True
    ):

        broken = random.randint(1, 2)

        st.session_state.brick_score += broken

        st.success(
            f"💥 {broken} brick(s) broken!"
        )

    st.metric(
        "🧱 Score",
        st.session_state.brick_score
    )

    if st.button(
        "🔄 Restart",
        use_container_width=True
    ):

        st.session_state.brick_score = 0
        st.rerun()

    if st.button(
        "⬅️ Back to Games",
        use_container_width=True
    ):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# BALLOON POP
# ============================================================

elif st.session_state.selected_game == "🎈 Balloon Pop":

    st.header("🎈 Balloon Pop")

    if "balloon_score" not in st.session_state:
        st.session_state.balloon_score = 0

    balloon = random.choice([
        "🎈",
        "🎈",
        "🎈",
        "🎈"
    ])

    st.markdown(
        f"""
        <div style="text-align:center;font-size:100px;">
        {balloon}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "💥 POP!",
        use_container_width=True
    ):

        points = random.randint(1, 10)

        st.session_state.balloon_score += points

        st.success(
            f"🎉 Balloon popped! +{points} points"
        )

        st.rerun()

    st.metric(
        "🎈 Score",
        st.session_state.balloon_score
    )

    if st.button(
        "🔄 Restart",
        use_container_width=True
    ):

        st.session_state.balloon_score = 0
        st.rerun()

    if st.button(
        "⬅️ Back to Games",
        use_container_width=True
    ):

        st.session_state.selected_game = "🎮 Game Selection"
        st.rerun()

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
<hr>
<h2>🎮 FunZone Game Hub</h2>
<p>Play • Create • Challenge • Have Fun</p>
<p>Created by <b>Rashpreet Kaur Arora</b></p>
<p>Python • Streamlit</p>
<p>🎓 Student Project</p>
</div>
""", unsafe_allow_html=True)

    
