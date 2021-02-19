const searchContainer = document.querySelector('#friend__new__search__container')

const getUserList = async () => {
    const url = "/friend/user/search/";
    const value = document.querySelector('#friend_search');
    const { data } = await axios.post(url, {
        value:value.value,
    })

    let userList = data.user_list;

    makeUserList(userList)
}

const makeUserList = (userList) => {
    searchContainer.innerHTML = "";

    for (var key in userList) {
        userInfo = userList[key]
        
        let { pk, username, nickname } = userInfo;

        console.log(username);

        let newUser = document.createElement("div");
        newUser.className="friends"

        let newUserProfile = document.createElement("div")
        newUserProfile.className="friends__profile"

        let newUserProfileInfo = document.createElement("div")
        newUserProfileInfo.className="friends__profile__info"

        let newUserProfileLink = document.createElement("a")
        newUserProfileLink.setAttribute('href', `../list/detail/${pk}`)

        let newUserProfileImg = document.createElement("img")
        newUserProfileImg.className="friends__profile__imgae"
        newUserProfileImg.setAttribute('src', '#')

        let newUserProfileName = document.createElement("p")
        newUserProfileName.className="friends__profile__name"
        newUserProfileName.innerHTML = `${nickname}`

        newUserProfileLink.appendChild(newUserProfileImg)
        newUserProfileLink.appendChild(newUserProfileName)
        newUserProfileInfo.appendChild(newUserProfileLink)
        newUserProfile.appendChild(newUserProfileInfo)



        let newUserBtnDiv = document.createElement("div")
        newUserBtnDiv.className="friends__btn"

        let newUserBtn = document.createElement("a")
        newUserBtn.className="friends__add__btn"
        newUserBtn.innerHTML="자세히"
        newUserBtn.setAttribute('href', `../list/detail/${pk}`)

        newUserBtnDiv.appendChild(newUserBtn)
        newUserProfile.appendChild(newUserBtnDiv)

        newUser.appendChild(newUserProfile)

        searchContainer.appendChild(newUser);
    };
}