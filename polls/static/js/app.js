class Polls {

    constructor() {
        this.pollBox = document.querySelectorAll('.question-box');
        [...this.pollBox].forEach( el => {
            el.addEventListener('click', () => window.location.assign(el.dataset.url));
        });
    }
}

myPolls = new Polls();