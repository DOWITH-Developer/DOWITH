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