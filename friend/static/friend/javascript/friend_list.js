const firstModal = document.querySelector(".firstModal");
const firstContent = document.querySelector(".firstContent");
const no = document.querySelector(".no");
const yes = document.querySelector(".confirm")
const secondModal = document.querySelector(".secondModal");
const secondContent = document.querySelector(".secondContent");
const ok = document.querySelector(".ok");

const giveMotivation = async(id) => {
    console.log(firstModal)
    console.log(firstContent)
    firstContent.innerHTML = `콕 찌르시겠습니까?`

    firstModal.style.display = "block";

    no.addEventListener("click", (id) => {
        firstModal.style.display = "none";
    })


    // yes.addEventListener("click", async()=> {
    //     firstModal.style.display = "none";

    //     const url = "/friend/motivate/";
    //     const { data } = await axios.post(url, {
    //         "id":id,
    //     });
    //     secondModal.style.display = "block";
    //     secondContent.textContent = `${data.user} 를 콕 찔렀습니다`; 
    // })
    

    // ok.addEventListener("click", () => {
    //     secondModal.style.display = "none";
    // })

    // -----------------------
    async function motivate() {
        firstModal.style.display = "none";

        const url = "/friend/motivate/";
        const { data } = await axios.post(url, {
            "id":id,
        });
        secondModal.style.display = "block";
        secondContent.textContent = `${data.user}님을 콕 찔렀습니다`; 
        
        yes.removeEventListener("click", motivate, false)
    }

    function cancel() {
        secondModal.style.display = "none";
    }

    yes.addEventListener("click", motivate, false)

    ok.addEventListener("click", cancel);
}







// --------------------------------------------

const thirdModal = document.querySelector(".thirdModal");
const thirdContent = document.querySelector(".thirdContent");
const thirdModalContent = document.querySelector(".third-modal-content");
// let thirdModalText = thirdContent.textContent;

const alertModal = document.querySelector(".alert__modal");
const alertModalContainer = document.querySelector(".alert__modal__container");
const alertModalContent = document.querySelector(".alert__modal__content");

const deleteOneMotivModal = document.querySelector(".Delete__Onemotiv__Modal");
const deleteOneModalContent = document.querySelector("delete-one-modal-content");
const deleteOneContent = document.querySelector(".delete-one-content");

function alertConfirm() {
    alertModal.style.display = "none";
}

function cancelAllDelete() {
    thirdModal.style.display = "none";
}

function cancelDelete() {
    deleteOneMotivModal.style.display = "none";
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


const makeOneRemove = async (id) => {
    deleteOneMotivModal.style.display = "none";
    const url = "/friend/motivate/remove/";
    const motivationTarget = document.querySelector(`.motivation-${id}`)
        .parentNode.parentNode;


    motivationTarget.remove();

    openAlertModal("지웠습니다.");
    const { data } = await axios.post(url, {
        id,
    });
};

const makeRemove = async (id = null) => {
    thirdModal.style.display = "none";
    const url = "/friend/motivate/remove/";
    // const deleteAllSelector = document.querySelector('.moti_delete_all');
    
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
        // deleteAllSelector.remove()
    } else {
        openAlertModal("다시 실행해 주세요.");
    }
};

const removeMotivation = (id = null) => {
    if (id === null) {
        openRemoveModal("모든 콕 찌르기를 지우시겠습니까? ");
    } else {
        openRemoveOneModal("해당 콕 찌르기를 지우시겠습니까? ");
    }
};