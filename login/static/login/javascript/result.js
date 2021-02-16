const onClickResult = async (id) => {
    const url = "/result_ajax/";

    const { data } = await axios.post(url, {
        id,
    });
    console.log(data);

    modify(data.id, data.result);
};

const modify = (id, result) => {
    const result_word = document.querySelector(`.result-${id} .result_word`);

    if (result === false) {
        result_word.value = "성공시 클릭";
        result_word.classList.remove("success");
        result_word.classList.add("fail");
    } else {
        result_word.value = "챌린지 성공!";
        result_word.classList.remove("fail");
        result_word.classList.add("success");
    }
};
