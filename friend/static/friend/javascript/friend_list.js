const firstModal = document.querySelector(".firstModal");
const firstContent = document.querySelector("firstContent");
const firstModalContent = document.querySelector(".first-modal-content");
let firstModalText = firstModalContent.firstElementChild.textContent;

const secondModal = document.querySelector(".secondModal");
const secondContent = document.querySelector(".secondContent");
const secondModalContent = document.querySelector(".second-modal-content");
let secondModalText = secondModalContent.firstElementChild.textContent;

const thirdModal = document.querySelector(".thirdModal");
const thirdContent = document.querySelector(".thirdContent");
const thirdModalContent = document.querySelector(".third-modal-content");
let thirdModalText = thirdContent.textContent;

const alertModal = document.querySelector(".alert__modal");
const alertModalContainer = document.querySelector(".alert__modal__container");
const alertModalContent = document.querySelector(".alert__modal__content");

const deleteOneMotivModal = document.querySelector(".Delete__Onemotiv__Modal");
const deleteOneModalContent = document.querySelector(
    "delete-one-modal-content"
);
const deleteOneContent = document.querySelector(".delete-one-content");
const yes = document.querySelector(".confirm");

function cancelFirst() {
    firstModal.style.display = "none";
}

function alertConfirm() {
    alertModal.style.display = "none";
}

function cancelSecond() {
    secondModal.style.display = "none";
}

function cancelAllDelete() {
    thirdModal.style.display = "none";
}

function cancelDelete() {
    deleteOneMotivModal.style.display = "none";
}

function openModal(text) {
    firstModal.style.display = "block";
    firstModalText = text;
}

function openSecondModal(text) {
    secondModal.style.display = "block";
    secondModalText = text;
}

function openRemoveModal(text) {
    thirdModal.style.display = "block";
    thirdModalText = text;
}

function openAlertModal(text) {
    alertModal.style.display = "block";
    alertModalContent.textContent = text;
}

function openRemoveOneModal(text) {
    deleteOneMotivModal.style.display = "block";
}

const makeConfirm = async (id) => {
    firstModal.style.display = "none";
    const url = "/friend/motivate/";
    const { data } = await axios.post(url, {
        id,
    });
    secondModal.style.display = "block";
    secondContent.textContent = `${data.user} 를 콕 찔렀습니다`;
};

const makeOneRemove = async (id) => {
    deleteOneMotivModal.style.display = "none";
    const url = "/friend/motivate/remove/";
    const motivationTarget = document.querySelector(`.motivation-${id}`)
        .parentNode.parentNode;
    console.log(motivationTarget);

    motivationTarget.remove();

    openAlertModal("지웠습니다.");
    const { data } = await axios.post(url, {
        id,
    });
};

const makeRemove = async (id = null) => {
    thirdModal.style.display = "none";
    const url = "/friend/motivate/remove/";

    const { data } = await axios.post(url, {
        id,
    });
    if (data.status == true) {
        const allMotivations = document.querySelectorAll(
            ".friend__motivation__from__friend"
        );
        allMotivations.forEach((motivation) =>
            motivation.parentNode.parentNode.remove()
        );
        openAlertModal("모든 콕 찌르기를 지우셨습니다.");
    } else {
        openAlertModal("다시 실행해 주세요.");
    }
};

const giveMotivation = () => {
    openModal("콕 찌르시겠습니까?");
};

const removeMotivation = (id = null) => {
    if (id === null) {
        openRemoveModal("모든 콕 찌르기를 지우시겠습니까? ");
    } else {
        openRemoveOneModal("해당 콕 찌르기를 지우시겠습니까? ");
    }
};
