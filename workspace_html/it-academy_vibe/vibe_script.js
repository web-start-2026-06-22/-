/* =====================================
    DOM
===================================== */

const header = document.querySelector("header");

const modal = document.getElementById("gameModal");

const openGameBtn =
    document.getElementById("openGame");

const closeBtn =
    document.querySelector(".close-btn");

const gameArea =
    document.getElementById("gameArea");

const counters =
    document.querySelectorAll(".counter");

const darkBtn =
    document.getElementById("darkModeBtn");



/* =====================================
    HEADER SCROLL
===================================== */

window.addEventListener("scroll", () => {

    if (window.scrollY > 50) {

        header.classList.add("scroll");

    } else {

        header.classList.remove("scroll");

    }

});



/* =====================================
    COUNTER
===================================== */

const counterObserver =
    new IntersectionObserver(entries => {


        entries.forEach(entry => {


            if (!entry.isIntersecting)
                return;


            const counter =
                entry.target;


            const target =
                Number(counter.dataset.target);


            let current = 0;


            const increase = () => {


                current += target / 80;


                if (current < target) {

                    counter.innerText =
                        Math.floor(current);

                    requestAnimationFrame(
                        increase
                    );

                } else {

                    counter.innerText =
                        target.toLocaleString();

                }


            };


            increase();


            counterObserver.unobserve(counter);


        });


    });


counters.forEach(counter => {

    counterObserver.observe(counter);

});



/* =====================================
    DARK MODE
===================================== */


function loadDarkMode() {

    const mode =
        localStorage.getItem(
            "darkMode"
        );


    if (mode === "on") {

        document.body.classList.add(
            "dark"
        );

    }

}



loadDarkMode();



if (darkBtn) {


    darkBtn.addEventListener(
        "click",
        () => {


            document.body
                .classList
                .toggle("dark");



            localStorage.setItem(

                "darkMode",

                document.body
                    .classList
                    .contains("dark")
                    ?
                    "on"
                    :
                    "off"

            );


        }
    );


}





/* =====================================
    MODAL
===================================== */


function openModal() {

    modal.classList.add(
        "active"
    );


    createGameMenu();

}



function closeModal() {

    modal.classList.remove(
        "active"
    );


    resetGame();

}



openGameBtn.addEventListener(
    "click",
    openModal
);



closeBtn.addEventListener(
    "click",
    closeModal
);



modal.addEventListener(
    "click",
    e => {


        if (e.target === modal) {

            closeModal();

        }


    }
);



window.addEventListener(
    "keydown",
    e => {


        if (e.key === "Escape") {

            closeModal();

        }


    }
);






/* =====================================
    BASEBALL GAME
===================================== */


let answer = [];

let gameMode = 3;

let tryCount = 0;

let bestScoreKey =
    "baseballBest";





function createGameMenu() {


    gameArea.innerHTML = `

    <div class="game-menu">


        <h3>
        ⚾ 숫자야구
        </h3>


        <p>
        자리수를 선택하세요.
        </p>


        <div class="mode-buttons">


            <button id="mode3">
            3자리
            </button>


            <button id="mode4">
            4자리
            </button>


        </div>


        <div id="bestScore"></div>


    </div>


    `;



    document
        .getElementById("mode3")
        .onclick = () => startGame(3);



    document
        .getElementById("mode4")
        .onclick = () => startGame(4);



    showBestScore();


}





function createAnswer(length) {


    let result = [];


    while (result.length < length) {


        let num =
            Math.floor(
                Math.random() * 10
            );



        if (
            result.length === 0 &&
            num === 0
        )
            continue;



        if (
            !result.includes(num)
        ) {

            result.push(num);

        }


    }


    return result;


}






function startGame(mode) {


    gameMode = mode;


    answer =
        createAnswer(mode);


    tryCount = 0;



    console.log(
        "정답:",
        answer.join("")
    );



    gameArea.innerHTML = `


    <div class="baseball-game">


        <div class="game-header">


            <h3>
            ⚾ ${mode}자리 게임
            </h3>


            <span>

            시도 :
            <b id="tryCount">
            0
            </b>

            </span>


        </div>



        <div class="input-area">


            <input
            id="userInput"
            maxlength="${mode}"
            placeholder="${mode}자리 입력"
            >


            <button id="submitGuess">
            확인
            </button>


        </div>



        <div id="historyArea"></div>



        <button id="restart">
        새 게임
        </button>



    </div>


    `;



    const input =
        document.getElementById(
            "userInput"
        );


    document
        .getElementById("submitGuess")
        .onclick = checkAnswer;



    input.addEventListener(
        "keydown",
        e => {

            if (e.key === "Enter")
                checkAnswer();

        }
    );



    document
        .getElementById("restart")
        .onclick = createGameMenu;


}






function checkAnswer() {


    const input =
        document
            .getElementById(
                "userInput"
            )
            .value;



    if (!validateInput(input))
        return;




    const result =
        checkScore(input);



    tryCount++;



    document
        .getElementById(
            "tryCount"
        )
        .innerText =
        tryCount;



    addHistory(
        input,
        result
    );



    if (
        result.strike === gameMode
    ) {


        saveBestScore(
            tryCount
        );


        setTimeout(() => {

            alert(
                `🎉 성공!\n${tryCount}회 만에 정답`
            );


            showBestScore();


        }, 200);


    }



}







function validateInput(value) {


    if (
        value.length !== gameMode
    ) {

        alert(
            `${gameMode}자리 입력`
        );

        return false;

    }



    if (
        isNaN(value)
    ) {

        alert(
            "숫자만 입력"
        );

        return false;

    }



    if (
        new Set(value).size
        !== gameMode
    ) {

        alert(
            "중복 숫자 불가"
        );

        return false;

    }



    return true;


}







function checkScore(input) {


    const numbers =
        input
            .split("")
            .map(Number);



    let strike = 0;

    let ball = 0;



    numbers.forEach(
        (num, index) => {


            if (answer[index] === num)

                strike++;


            else if (
                answer.includes(num)
            )

                ball++;


        }
    );



    return {
        strike,
        ball
    };


}







function addHistory(
    input,
    result
) {


    const area =
        document.getElementById(
            "historyArea"
        );



    let text;



    if (
        result.strike === 0 &&
        result.ball === 0
    ) {

        text = "OUT";

    } else {

        text =
            `${result.strike} Strike ${result.ball} Ball`;

    }



    const p =
        document.createElement(
            "p"
        );



    p.innerHTML =
        `
    ${tryCount}회 :
    <b>${input}</b>
    →
    ${text}
    `;



    area.prepend(p);


}





/* =====================================
    SCORE
===================================== */


function saveBestScore(score) {


    const best =
        localStorage.getItem(
            bestScoreKey
        );



    if (
        !best ||
        score < Number(best)
    ) {

        localStorage.setItem(
            bestScoreKey,
            score
        );


        alert(
            "🏆 새로운 최고 기록!"
        );

    }


}




function showBestScore() {


    const area =
        document.getElementById(
            "bestScore"
        );


    if (!area)
        return;



    const best =
        localStorage.getItem(
            bestScoreKey
        );



    area.innerHTML =
        best
            ?
            `🏆 최고 기록 : ${best}회`
            :
            "최고 기록 없음";


}




function resetGame() {

    answer = [];

    tryCount = 0;

}





/* =====================================
    SCROLL ANIMATION
===================================== */


const sections =
    document.querySelectorAll(
        "section"
    );


sections.forEach(section => {

    section.classList.add(
        "fade-up"
    );

});



const observer =
    new IntersectionObserver(
        entries => {


            entries.forEach(entry => {


                if (
                    entry.isIntersecting
                ) {

                    entry.target.classList.add(
                        "show"
                    );

                }


            });


        });



sections.forEach(section => {

    observer.observe(section);

});