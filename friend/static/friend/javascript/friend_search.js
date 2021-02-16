const friendContainer = document.querySelector('.friend__list__container')


const searchFriend = async () => {
    const url = "/friend/search/";
    const value = document.querySelector('#id_search_word');    
    const {data} = await axios.post(url, {
        value : value.value
    })
    let friend = JSON.parse(data.friend)
    let friendList = JSON.parse(data.friend_list)
    console.log(friend);
    console.log(friendList);
    printFriendList(friendList)
    // let a = JSON.parse(data);
    // console.log(a);
}

const printFriendList = (friendList) => {
    friendContainer.innerHTML = ''
    console.log(friendList)
    // let friendListTemplate = `
    //     <div class="friends">
    //         <div class="friends__profile">
    //             <div class="friends__profile__info">
    //             <a href="{% url 'friend:fd_detail' fd.me.pk %}">
    //                 <img class="friends__profile__image" src="{% static 'img/DOWITH.png' %}" alt="logo">
    //                 <p class="friends__profile__name">{{fd.me}}</p>
    //             </a>
    //             </div>

    //             <div class="friends__btn">
    //                 <button class="friends__btn__cheer" onclick="giveMotivation({{fd.me.id}})">응원하기</button>
    //             </div>
    //         </div>
    //     </div>
    // `
    // let friendListDiv = new DOMParser().parseFromString(friendListTemplate, "text/html").body.firstElementChild
    // friendContainer.appendChild(friendListDiv)
}
