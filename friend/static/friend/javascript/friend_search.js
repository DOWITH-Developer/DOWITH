const friendContainer = document.querySelector(".friend__list__container ");
const searchFriend = async () => {
    const url = "/friend/search/";
    const value = document.querySelector(".friend__list__search");
    const { data } = await axios.post(url, {
        value: value.value,
    });
    // // serialized로 전체를 넘겨주는 경우
    // let friend = JSON.parse(data.friend);
    // let friendList = JSON.parse(data.friend_list);
    // printFriendList(friendList);

    // 필요한 값만 넘겨주는 경우
    let friendList = data.friend_list;
    printFriendList(friendList);
};


// 필요한 값만 넘겨주는 경우
const printFriendList = (friendListDic) => {
    friendContainer.innerHTML = "";

    for(let key in friendListDic){
        freindInfo = friendListDic[key];
        // console.log(freindInfo);
        let { pk, username, nickname, image } = freindInfo;

        // console.log(pk, username, nickname, image)
        let friends = document.createElement("div");
        friends.className = "friends";
        let profileContainer = document.createElement("div");
        profileContainer.className = `friends__profile ${pk}`;

        let infoContainer = document.createElement("div");
        infoContainer.className = "friends__profile__info";
        infoContainer.innerHTML = `
            <a href="detail/${pk}">
            <img class="friends__profile__image" src="${image}" alt="logo">
            <p class="friends__profile__name"> ${nickname} </p></a>
        `;

        let btnContainer = document.createElement("div");
        btnContainer.className = "friends__btn";
        btnContainer.innerHTML = `<button class="friends__btn__cheer" onclick="giveMotivation()">응원하기</button>`;
        
        let firstModal = document.createElement("div");
        firstModal.className = "firstModal"
        firstModal.innerHTML = `<!-- First Modal content -->
                                <div class="first-modal-content first-modal">
                                    <div class="modal-first-content">
                                        <p class="firstContent">콕 찌르시겠습니까?</p>
                                        <div class="button__container">
                                            <button class="confirm motivationbtn" onclick="makeConfirm({{fd.me.id}})">확인</button>
                                            <button class="motivationbtn" onclick="cancelFirst()">취소</button>
                                        </div>
                                    </div>
                                </div>`
        
        btnContainer.appendChild(firstModal)
        profileContainer.appendChild(infoContainer);
        profileContainer.appendChild(btnContainer);
        friends.appendChild(profileContainer);
        friendContainer.append(friends);
    }
}
