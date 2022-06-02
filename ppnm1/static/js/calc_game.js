function randInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}


function exRandomNumber(summands, sign, rightAnswer, limit) {
    let r = Math.random();
    switch (true) {
        case (r < .4 && sign == '+' && summands[0] - summands[1] >= 0):
            return summands[0] - summands[1];
        case (r < .4 && sign == '-' && summands[0] + summands[1] <= limit):
            return summands[0] + summands[1];
        case (r < .55 && rightAnswer - 10 >= 0):
            return rightAnswer - 10;
        case (r < .7 && rightAnswer + 10 <= limit):
            return rightAnswer + 10
        default:
            return randInt(0, limit + 1);
    }
}


function generateAnswers(count, summands, sign, rightAnswer, limit) {
    let answers = [];
    for (let i = 0; i < count; i++) {
        while (true) {
            let sample = exRandomNumber(summands, sign, rightAnswer, limit);
            if (sample != rightAnswer && !answers.includes(sample)) {
                answers.push(sample);
                break;
            }
        }
    }
    return answers;
}


class GameIteration {

    constructor(limit, answersCount) {
        this.rightAnswerButtonPk = randInt(0, answersCount);

        this.summand1 = Math.floor(randInt(0, limit + 1));
        switch (randInt(0, 2)) {
            case 0:
                this.sign = '+';
                this.summand2 = Math.floor(randInt(0, limit + 1 - this.summand1));
                break;
            case 1:
                this.sign = '-';
                this.summand2 = Math.floor(randInt(0, this.summand1 + 1));
                break;
        }
        this.answers = generateAnswers(
            answersCount - 1,
            [this.summand1, this.summand2],
            this.sign,
            this.rightAnswer,
            limit
        );
        this.answers.splice(this.rightAnswerButtonPk, 0, this.rightAnswer);
    }

    get leftSideOfEquasionString() {
        return this.summand1 + ' ' + this.sign + ' ' + this.summand2;
    }

    get rightAnswer () {
        return eval(this.leftSideOfEquasionString)
    }

}


class GameModel {

    constructor(
        winCountSpanID, loseCountSpanID,
        questionSpanID,
        buttonIDs,
        winButtonID, loseButtonID
    ) {
        this.wins = 0;
        this.loses = 0;
        this.winCountSpan = document.getElementById(winCountSpanID);
        this.loseCountSpan = document.getElementById(loseCountSpanID);
        this.questionSpan = document.getElementById(questionSpanID);
        this.buttons = []
        buttonIDs.forEach((el) =>
            this.buttons.push(document.getElementById(el))
        );
        this.winButton = document.getElementById(winButtonID);
        this.loseButton = document.getElementById(loseButtonID);
        this.gameIteration = null;
    }

    compareAnswerOfButtonIndex(pk) {
        if (this.gameIteration == null)
            return;
        if (this.buttons[pk].innerHTML == this.gameIteration.rightAnswer) {
            this.wins += 1;
            this.winButton.style.display = 'block';
            this.winCountSpan.innerHTML = this.wins;
        }
        else {
            this.loses += 1;
            this.loseButton.style.display = 'block';
            this.loseCountSpan.innerHTML = this.loses;
            this.buttons[pk].className = 'btn btn-danger col mx-1';
        }
        this.buttons[this.gameIteration.rightAnswerButtonPk].className
            = 'btn btn-success col mx-1';
        this.buttons.forEach((el) => el.disabled = true);
        document.getElementById('result').innerHTML
            = eval(this.gameIteration.leftSideOfEquasionString);
    }

    awake() {
        this.winButton.onclick = () => { this.reset(); };
        this.loseButton.onclick = () => { this.reset(); };
        for (let i = 0; i < this.buttons.length; i++) {
            this.buttons[i].onclick = () => { this.compareAnswerOfButtonIndex(i); };
        }
    }

    reset() {
        delete this.gameIteration;
        this.gameIteration = new GameIteration(100, 3);
        this.questionSpan.innerHTML
            = this.gameIteration.leftSideOfEquasionString
            + ' = <span id="result">?</span>';
        this.winButton.style.display = 'none';
        this.loseButton.style.display = 'none';
        let answers = this.gameIteration.answers;
        for (let i = 0; i < answers.length; i++) {
            this.buttons[i].disabled = false;
            this.buttons[i].className = 'btn btn-primary col mx-1';
            this.buttons[i].innerHTML = answers[i];
        }
    }

}


class Timer {

    constructor(timerSpanID) {
        this.timerSpan = document.getElementById(timerSpanID);
        if (this.timerSpan == null) 
            return;
        this.start = Date.now();
        setInterval(() => {
            let delta = Date.now() - this.start;
            this.timerSpan.innerHTML = new Date(delta).toISOString().substring(14, 19);
        }, 1000);
    }

}


window.onload = () => {
    
    let gameModel = new GameModel(
        'winCount', 'loseCount', 'question', ['answer1', 'answer2', 'answer3'], 'correct', 'incorrect'
    );
    gameModel.awake();
    gameModel.reset();
    
    let timer = new Timer('timePassed');
    
}
