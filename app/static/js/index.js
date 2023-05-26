const quizQuestion = document.querySelector(".question");
const quizOptions = document.querySelector(".options");
const quizNumber = document.querySelector(".quiz-number");
const quizScore = document.querySelector(".quiz-score");
const submitBtn = document.querySelector(".submit");
const quizResult = document.querySelector(".result");

let quizCount = 1;
let quizLength = 0;
let answers = [];

const loadQuestion = () => {
  fetch(`/get/query=${quizCount}`)
    .then((res) => res.json())
    .then((data) => {
      quizLength = data.quiz_length;
      quizNumber.innerText = quizCount;
      quizOptions.innerHTML = " ";
      quizQuestion.innerText = data.question;
      data.options.forEach((choice, index) => {
        const option = document.createElement("button");
        option.addEventListener("click", () => {
          checkAnswer(choice, data.answer);
        });
        option.setAttribute(
          "class",
          "btn btn-light btn-sm d-block mb-2 shadow rounded-0"
        );
        option.innerText = `${index+1}) ${choice}`;
        quizOptions.appendChild(option);
      });
    });
};

const checkAnswer = (choice, answer) => {
    answers[quizCount] = choice
    if (quizCount === quizLength) {
      finalResult();
    }
};

const finalResult = () => {
  fetch("/get/").then(res=>res.json()).then((data)=> {
    for(let x in data){
      const box = document.createElement('div');
      box.setAttribute('class', 'mb-3')
      const question = document.createElement('div');
      question.setAttribute('class','mb-1 d-flex');
      question.innerHTML = `<b class='text-success me-2'>Question ${x}: </b> <span>${data[x].question}</span>`;
      box.appendChild(question);
      let option = '';
      for(let y in data[x].options){
        option = document.createElement("button");
        option.innerText = data[x].options[y];
        option.setAttribute(
          "class",
          "btn btn-sm d-block mb-2 shadow rounded-0"
        );
        if(answers[x] == data[x].answer && answers[x] == data[x].options[y] || data[x].answer==data[x].options[y] ){
          option.classList.add('btn-success');
        }else if(answers[x]==data[x].options[y]){
          option.classList.add('btn-danger')
        };
        box.appendChild(option);
      };
      quizResult.appendChild(box);
    };
  });
};

submitBtn.addEventListener("click", () => {
  if (quizLength > quizCount) {
    quizCount++;
    loadQuestion();
  };
});

loadQuestion();
