const challengeContainer = document.querySelector(".friend__list__container ");

const searchChallenge = async () => {
    const url = "/challenge/search/";
    const value = document.querySelector(".challenge__list__search");
    const { data } = await axios.post(url, {
        value: value.value,
    });
    let challengeList = JSON.parse(data.challenge_list);
    printFriendList(challengeList);
};

const printFriendList = (challengeList) => {
    challengeContainer.innerHTML = "";
    challengeList.forEach((element) => {
        let { pk, fields } = element;

        let friends = document.createElement("div");
        friends.className = "friends";
        let profileContainer = document.createElement("div");
        profileContainer.className = `friends__profile ${pk}`;

        let infoContainer = document.createElement("div");
        infoContainer.className = "friends__profile__info";
        infoContainer.innerHTML = `
            <a href="detail/${field.invitation_key}">
            <img class="friends__profile__image" src="img/DOWITH.png" alt="logo">
            <p class="friends__profile__name"> ${fields.invitation_key} </p></a>
        `;

        let btnContainer = document.createElement("div");
        btnContainer.className = "friends__btn";
        btnContainer.innerHTML = `<button class="friends__btn__cheer" onclick="giveMotivation ({{${pk}}})">응원하기</button>`;

        profileContainer.appendChild(infoContainer);
        profileContainer.appendChild(btnContainer);
        friends.appendChild(profileContainer);
        friendContainer.append(friends);
    });
    //todo
    // 1. 여러개를 domparser로 보이게 하는 방법
    // 2. img 를 보이게 하는
    // let friendListTemplate = `
    //         <div class="friends__profile">
    //             <div class="friends__profile__info">
    //                 <a href="{% url 'friend:fd_detail' ${pk} %}">
    //                 <img class="friends__profile__image" src="{% static ` + 'img/DOWITH.png' + `%}" alt="logo">
    //                 <p class="friends__profile__name"> ${fields.nickname} </p>
    //             </a>
    //             </div>
    //             <div class="friends__btn">
    //                 <button class="friends__btn__cheer" onclick="giveMotivation ({{${pk}}})">응원하기</button>
    //             </div>
    //         </div>
    // `
    // array 형성
    // let friendListDiv = new Array();
    // friendListDiv = new DOMParser().parseFromString(friendListTemplate, "text/html").body.firstChild;
    // friendContainer.insertAdjacentHTML('beforeend', friend);
    // console.log(friendListDiv);
};
