// make modal 
const x = document.querySelector(".close");
const cancel = document.querySelector(".cancel")
const yes = document.querySelector(".confirm")

const firstModal = document.querySelector('.firstModal');
const firstContent = document.querySelector('firstContent');
const firstModalContent = document.querySelector('.first-modal-content');
let firstModalText = firstModalContent.firstElementChild.textContent;

const secondModal = document.querySelector('.secondModal');
const secondContent = document.querySelector('.secondContent');
const secondModalContent = document.querySelector('.second-modal-content');
let secondModalText = secondModalContent.firstElementChild.textContent;

const finalConfirm = document.querySelector('.finalconfirm');



// const unspecifiedModal = document.querySelector('.unspecified');
// function unspecifiedModal(text){
//     unspecifiedModal.style.display = "block"
// }

// When the user clicks on <span> (x), close the modal
x.onclick = function() {
    firstModal.style.display = "none";
}

cancel.onclick = function() {
    firstModal.style.display = "none";
}

finalConfirm.onclick = function() {
    secondModal.style.display = "none";
}

function openModal(text){
    firstModal.style.display = "block";
    firstModalText = text
}

function openSecondModal(text){
    secondModal.style.display = "block";
    secondModalText = text
}


// 확인해주는 함수를 실행시킨다 (전달할 때 이 유저도 같이 전달) 
const giveMotivation = () => {
    openModal("콕 찌르시겠습니까?")
}

const makeConfirm = async (id) => {
    firstModal.style.display = "none";
    const url = "/friend/motivate/";
    const {data} = await axios.post(url, {
                id
    })
    secondModal.style.display = "block"
    secondContent.textContent = `${data.user} 를 콕 찔렀습니다`;
}

//콕 찌르기의 위치가 정해지면 수정해야 함
// modal 에서 확인 버튼을 누르면 1을 반환 / 취소 버튼을 누르면 0 을 반환
// nested function 에서의 값을 return 하게 

const removeMotivation = async (id=null) => {
    const url = "/friend/motivate/remove/";

    if (id === null) {

        let = message = confirm('모든 콕 찌르기를 지우시겠습니까?')

        if (message) {
            const {data} = await axios.post(url, {
                id
            })

            if (data.status == true) {
                const allMotivations = document.querySelectorAll('.friend__motivation__from__friend')

                allMotivations.forEach(motivation => motivation.remove())

                alert('모든 콕 찌르기를 지우셨습니다.')
            } else {
                alert('다시 실행해 주세요.')
            }
        }

    } else {

        let = message = confirm('해당 콕 찌르기를 지우시겠습니까?')

        if (message) {
            
            const motivationTarget = document.querySelector(`.motivation-${id}`)
            motivationTarget.remove()

            const {data} = await axios.post(url, {
                id
            })

            alert('지웠습니다.')
        }

    }
}