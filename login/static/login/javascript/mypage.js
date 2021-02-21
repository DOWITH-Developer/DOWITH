const x = document.querySelector(".close");
const cancelRemove = document.querySelector(".cancelremove")
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

const thirdModal = document.querySelector('.thirdModal');
const thirdContent = document.querySelector('.thirdContent');
const thirdModalContent = document.querySelector('.third-modal-content');
let thirdModalText = thirdContent.textContent;

const alertModal = document.querySelector('.alert__modal');
const alertModalContainer = document.querySelector('.alert__modal__container');
const alertModalContent = document.querySelector('.alert__modal__content');

const deleteOneMotivModal = document.querySelector('.Delete__Onemotiv__Modal');
const deleteOneModalContent = document.querySelector('.delete-one-modal-content');
const deleteOneContent = document.querySelector('.delete-one-content');
let deleteOneModalText = deleteOneContent.textContent;

cancel.onclick = function() {
    firstModal.style.display = "none";
}

alertConfirm.onclick = function() {
    alertModal.style.display = "none";
}

finalConfirm.onclick = function() {
    secondModal.style.display = "none";
}

x.onclick = function() {
    firstModal.style.display = "none";
}

cancelRemove.onclick = function() {
    thirdModal.style.display = "none";
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

const giveMotivation = () => {
    openModal("콕 찌르시겠습니까?")
}

function openModal(text){
    firstModal.style.display = "block";
    firstModalText = text
}

function openSecondModal(text){
    secondModal.style.display = "block";
    secondModalText = text
}

function openRemoveModal(text){
    thirdModal.style.display = "block";
    thirdModalText = text
}

function openAlertModal(text){
    alertModal.style.display = "block";
    alertModalContent.textContent = text;
}

function openRemoveOneModal(text){
    deleteOneMotivModal.style.display = "block";
}

const makeRemove = async (id=null) => {
    thirdModal.style.display = "none";
    const url = "/friend/motivate/remove/";

    const {data} = await axios.post(url, {
        id
    })
    if (data.status == true) {
        const allMotivations = document.querySelectorAll('.friend__motivation__from__friend')

        allMotivations.forEach(motivation => motivation.remove())
        openAlertModal('모든 콕 찌르기를 지우셨습니다.')
    } else {
        openAlertModal('다시 실행해 주세요.')
    }
}

const makeOneRemove = async (id) => {
    deleteOneMotivModal.style.display = "none";
    const url = "/friend/motivate/remove/";
    const motivationTarget = document.querySelector(`.motivation-${id}`)
    motivationTarget.remove()
    
    openAlertModal('지웠습니다.')
    const {data} = await axios.post(url, {
            id
    })
}

const removeMotivation = (id=null) => {
    if (id === null) {
        openRemoveModal("모든 콕 찌르기를 지우시겠습니까? ")
    } else {
        openRemoveOneModal("해당 콕 찌르기를 지우시겠습니까? ")
    }
}

