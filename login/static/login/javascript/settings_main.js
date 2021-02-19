const userInfo = document.querySelector(".userInfo")
const userChallenge = document.querySelector(".userChallenge")
const setting = document.querySelector(".setting")
const ToS = document.querySelector(".ToS")
const contentBox = document.querySelector(".content")


 // userInfo
 const onClickUserInfo = async () => {
    const url = "/login/settings/user_info/" ; 

    const {data} = await axios.get(url)
    printUserInfo(data.name, data.nickname, data.email, data.is_social, data.image);
}

const printUserInfo = (name, nickname, email, is_social, image) => {
    contentBox.innerHTML = ''

    let userInfoTemplate = `
        <div class="userInfo__content">
            <div class="profile_photo">
                <img src="` + image + `" alt="profile_photo">` +
            `</div>
            <div class="username">
                Username : ` + name +
            `</div>
            <div class="nickname">
                Nickname : ` + nickname +
            `</div>
            <div class="email">
                Email : ` + email
    //         + `</div>
    //         <input class="userInfo__modification" type="submit" value="수정하기"/>
    //         <input class="userInfo_password__modification" type="submit" value="비밀번호 변경하기"/>
    //     </div>
    // `

    if (!(is_social)){
        userInfoTemplate += `</div>
            <input class="userInfo__modification" type="submit" value="수정하기"/>
            <input class="userInfo_password__modification" type="submit" value="비밀번호 변경하기"/>
        </div>
        `
    }
    else if (is_social){
        userInfoTemplate +=`</div>
            <input class="userInfo__modification" type="submit" value="수정하기"/>
        </div>
        `
    }

    let newUserInfoDiv = new DOMParser().parseFromString(userInfoTemplate, "text/html").body.firstElementChild
    contentBox.appendChild(newUserInfoDiv)


    // userInfo__modification
    const userInfoModify = document.querySelector(".userInfo__modification");
    userInfoModify.addEventListener("click", () => {
        document.location.href = userInfoModifyUrl;
    })

    // userInfo_password__modification
    const userInfoPasswordModify = document.querySelector(".userInfo_password__modification");
    userInfoPasswordModify.addEventListener("click", () => {
        document.location.href = passwordModifyUrl;
    })
}

const checkAddCss = (event) => {
    let target = event.currentTarget;
    target.classList.add("check");

    const settings_list = [userInfo, userChallenge, setting, ToS];
    settings_list.forEach((i) => {
        if (i == target){
            i.classList.add("check");
        }
        else{
            i.classList.remove("check");
        }
    })
}

userInfo.addEventListener("click", onClickUserInfo)

userInfo.addEventListener("click", checkAddCss)
userChallenge.addEventListener("click", checkAddCss)
setting.addEventListener("click", checkAddCss)
ToS.addEventListener("click", checkAddCss)




// userChallenge
const onClickUserChallenge = async () => {
    const url = "/login/settings/user_challenge/";

    const {data} = await axios.get(url)
    printUserChallenge(data.enrollment_list, data.challenge_list);
}

const printUserChallenge = (enrollmentList, challengeList) => {
    contentBox.innerHTML = ''

    const enrollmentListParsed = JSON.parse(enrollmentList)
    const challengeListParsed = JSON.parse(challengeList)
    console.log(enrollmentListParsed);
    console.log(challengeListParsed)
    console.log(challengeListParsed[0].pk)

    const userChallengeTemplate = `
        <div class="userChallenge__content">
            <div class="status_0__container">   
                <div class="status_0__title">
                    대기 중
                </div>
                <div class="status_0">
                </div>
            </div>

            <div class="status_1__container">   
                <div class="status_1__title">
                    진행 중
                </div>
                <div class="status_1">
                </div>
            </div>

            <div class="status_2__container">   
                <div class="status_2__title">
                    완료
                </div>
                <div class="status_2">
                </div>
            </div>
        </div>
    `
    const newUserChallengeDiv = new DOMParser().parseFromString(userChallengeTemplate, "text/html").body.firstElementChild
    contentBox.appendChild(newUserChallengeDiv)


    const status0 = document.querySelector(".status_0");
    const status1 = document.querySelector(".status_1");
    const status2 = document.querySelector(".status_2");
    for(let i = 0; i < challengeListParsed.length; i++){
        // const innerHtmlTemplate = `<div>챌린지 명 : ` + challengeListParsed[i].fields.title +
        //                             `<br>챌린지 창시일 : ` + challengeListParsed[i].fields.created_date +
        //                             `<br>챌린지 시작일 : ` + challengeListParsed[i].fields.start_date +
        //                             `<br>나의 챌린지 신청일 : ` + enrollmentListParsed[i].fields.created_at +
        //                             `<br><br>
        //                         </div>`;
        // const innerHtmlTemplate = `<div><a href="http://127.0.0.1:8000/challenge/3">챌린지 명 : ` + challengeListParsed[i].fields.title + `</a></div>`
        const innerHtmlTemplate = `<div><a href="http://127.0.0.1:8000/challenge/` + challengeListParsed[i].pk + `">챌린지 명 : `
                                    + challengeListParsed[i].fields.title + `</a></div>`

        const newChallengeDiv = new DOMParser().parseFromString(innerHtmlTemplate, "text/html").body.firstElementChild
        
        if(challengeListParsed[i].fields.status === 0){
            status0.appendChild(newChallengeDiv);
        }
        else if(challengeListParsed[i].fields.status === 1){
            status1.appendChild(newChallengeDiv);
        }
        else if(challengeListParsed[i].fields.status === 2){
            status2.appendChild(newChallengeDiv);
        }
    }
}

userChallenge.addEventListener("click", onClickUserChallenge)




// settings
const onClickSetting = async () => {
    const url = "/login/settings/setting/";

    const {data} = await axios.get(url)
    printSetting();
}

const printSetting = () => {
    contentBox.innerHTML = ''

    const settingTemplate = `
        <div class="setting__content">
            <form action="" method="POST">` + ``
                // {% csrf_token %}
                + `<p>디스플레이</p>
                <label><input type="radio" name="display_mode" checked> 라이트 모드</label>
                <label><input type="radio" name="display_mode"> 다크 모드</label>
                <button type="submit">저장</button>
                <button type="reset">초기화</button>
            </form>
        </div>
    `
    const newSettingDiv = new DOMParser().parseFromString(settingTemplate, "text/html").body.firstElementChild
    contentBox.appendChild(newSettingDiv)
}

setting.addEventListener("click", onClickSetting)




// ToS
const printToS = () => {
    contentBox.innerHTML = ''

    const ToSTemplate = `
        <div class="ToS__content">
            <div>
                약관 1
                뭐가 있을까
            </div>
            <div>
                약관 2
                흠
            </div>
        </div>
    `
    const newToSDiv = new DOMParser().parseFromString(ToSTemplate, "text/html").body.firstElementChild
    contentBox.appendChild(newToSDiv)
}

ToS.addEventListener("click", printToS)