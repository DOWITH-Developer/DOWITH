const onClickResult = async (id) => {
    const url = "/result_ajax/";

    const { data } = await axios.post(url, {
        id,
    });
    console.log(data);

    modify(data.id, data.result);
};

const modify = (id, result) => {
    const heart = document.querySelector(`.result-${id} i`);
    const like_con = document.querySelector(`.result-${id} .result__content`);

    if (result === false) {
        heart.className = "far fa-check-circle";
        like_con.innerHTML = "챌린지가 성공되면 체크박스를 눌러주세요!";
    } else {
        heart.className = "fas fa-check-circle";
        like_con.innerHTML = "챌린지를 성공처리하셨습니다!";
    }
};
