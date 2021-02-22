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

//todo 이렇게 하는건 어떻게 하는걸까...
// const deStructure = (friendList) => {
//     // console.log(friendList);
//     friendList.forEach(element => {
//         let {pk, fields} = element;
//         printFriendList(pk, fields)
//     })
// }


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
        btnContainer.innerHTML = `<button class="friends__btn__cheer" onclick="giveMotivation(${pk})">응원하기</button>`;
        
        // let firstModal = document.createElement("div");
        // firstModal.className = "firstModal firstModal1"
        // firstModal.innerHTML = `<!-- First Modal content -->
        //                         <div class="first-modal-content first-modal">
        //                             <div class="modal-first-content">
        //                                 <p class="firstContent">콕 찌르시겠습니까?</p>
        //                                 <div class="button__container">
        //                                     <button class="confirm motivationbtn" onclick="makeConfirm({{fd.me.id}})">확인</button>
        //                                     <button class="motivationbtn" onclick="cancelFirst()">취소</button>
        //                                 </div>
        //                             </div>
        //                         </div>`

        // console.log(firstModal)

        profileContainer.appendChild(infoContainer);
        profileContainer.appendChild(btnContainer);
        // profileContainer.appendChild(firstModal)

        friends.appendChild(profileContainer);
        friendContainer.append(friends);
    }
}

// // serialized로 전체를 넘겨주는 경우
// const printFriendList = (friendList) => {
//     friendContainer.innerHTML = "";

//     friendList.forEach((element) => {
//         let { pk, fields, image } = element;

//         let friends = document.createElement("div");
//         friends.className = "friends";
//         let profileContainer = document.createElement("div");
//         profileContainer.className = `friends__profile ${pk}`;

//         let infoContainer = document.createElement("div");
//         infoContainer.className = "friends__profile__info";
//         infoContainer.innerHTML = `
//             <a href="detail/${pk}">
//             <img class="friends__profile__image" src="${image}" alt="logo">
//             <p class="friends__profile__name"> ${fields.nickname} </p></a>
//         `;

//         let btnContainer = document.createElement("div");
//         btnContainer.className = "friends__btn";
//         btnContainer.innerHTML = `<button class="friends__btn__cheer" onclick="giveMotivation ({{${pk}}})">응원하기</button>`;

//         profileContainer.appendChild(infoContainer);
//         profileContainer.appendChild(btnContainer);
//         friends.appendChild(profileContainer);
//         friendContainer.append(friends);
//     });
//     //todo
//     // 1. 여러개를 domparser로 보이게 하는 방법
//     // 2. img 를 보이게 하는
//     // let friendListTemplate = `
//     //         <div class="friends__profile">
//     //             <div class="friends__profile__info">
//     //                 <a href="{% url 'friend:fd_detail' ${pk} %}">
//     //                 <img class="friends__profile__image" src="{% static ` + 'img/DOWITH.png' + `%}" alt="logo">
//     //                 <p class="friends__profile__name"> ${fields.nickname} </p>
//     //             </a>s
//     //             </div>
//     //             <div class="friends__btn">
//     //                 <button class="friends__btn__cheer" onclick="giveMotivation ({{${pk}}})">응원하기</button>
//     //             </div>
//     //         </div>
//     // `
//     // array 형성
//     // let friendListDiv = new Array();
//     // friendListDiv = new DOMParser().parseFromString(friendListTemplate, "text/html").body.firstChild;
//     // friendContainer.insertAdjacentHTML('beforeend', friend);
//     // console.log(friendListDiv);
// };
