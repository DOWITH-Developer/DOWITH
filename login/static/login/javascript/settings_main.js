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

    const settings_list = [userInfo, userChallenge, ToS];
    // 설정 삭제
    // const settings_list = [userInfo, userChallenge, setting, ToS];
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
// 설정 삭제
// setting.addEventListener("click", checkAddCss)
ToS.addEventListener("click", checkAddCss)




// userChallenge
const onClickUserChallenge = async () => {
    const url = "/login/settings/user_challenge/";

    const {data} = await axios.get(url)
    // printUserChallenge(data.enrollment_list, data.challenge_list);
    printUserChallenge(data.challenge_list);
}

// // challenge 자체의 모든 내용들을 받는 방식
// const printUserChallenge = (enrollmentList, challengeList) => {
//     contentBox.innerHTML = ''

//     const enrollmentListParsed = JSON.parse(enrollmentList)
//     const challengeListParsed = JSON.parse(challengeList)
//     console.log(enrollmentListParsed);
//     console.log(challengeListParsed)
//     console.log(challengeListParsed[0].pk)

//     const userChallengeTemplate = `
//         <div class="userChallenge__content">
//             <div class="status_0__container">   
//                 <div class="status_0__title">
//                     대기 중
//                 </div>
//                 <div class="status_0">
//                 </div>
//             </div>

//             <div class="status_1__container">   
//                 <div class="status_1__title">
//                     진행 중
//                 </div>
//                 <div class="status_1">
//                 </div>
//             </div>

//             <div class="status_2__container">   
//                 <div class="status_2__title">
//                     완료
//                 </div>
//                 <div class="status_2">
//                 </div>
//             </div>
//         </div>
//     `
//     const newUserChallengeDiv = new DOMParser().parseFromString(userChallengeTemplate, "text/html").body.firstElementChild
//     contentBox.appendChild(newUserChallengeDiv)


//     const status0 = document.querySelector(".status_0");
//     const status1 = document.querySelector(".status_1");
//     const status2 = document.querySelector(".status_2");
//     for(let i = 0; i < challengeListParsed.length; i++){
//         // const innerHtmlTemplate = `<div>챌린지 명 : ` + challengeListParsed[i].fields.title +
//         //                             `<br>챌린지 창시일 : ` + challengeListParsed[i].fields.created_date +
//         //                             `<br>챌린지 시작일 : ` + challengeListParsed[i].fields.start_date +
//         //                             `<br>나의 챌린지 신청일 : ` + enrollmentListParsed[i].fields.created_at +
//         //                             `<br><br>
//         //                         </div>`;
//         // const innerHtmlTemplate = `<div><a href="http://127.0.0.1:8000/challenge/3">챌린지 명 : ` + challengeListParsed[i].fields.title + `</a></div>`
//         const innerHtmlTemplate = `<div><a href="http://127.0.0.1:8000/challenge/` + challengeListParsed[i].pk + `">챌린지 명 : `
//                                 + challengeListParsed[i].fields.title + `</a></div>`

//         const newChallengeDiv = new DOMParser().parseFromString(innerHtmlTemplate, "text/html").body.firstElementChild
        
//         if(challengeListParsed[i].fields.status === 0){
//             status0.appendChild(newChallengeDiv);
//         }
//         else if(challengeListParsed[i].fields.status === 1){
//             status1.appendChild(newChallengeDiv);
//         }
//         else if(challengeListParsed[i].fields.status === 2){
//             status2.appendChild(newChallengeDiv);
//         }
//     }
// }

// challenge에서 필요한 내용들만 보내는 방식
const printUserChallenge = (challengeList) => {
    contentBox.innerHTML = ''
    
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
    for(let i = 0; i < challengeList.length; i++){
        // const innerHtmlTemplate = `<div><a href="http://127.0.0.1:8000/challenge/3">챌린지 명 : ` + challengeList[i].title + `</a></div>`
        const innerHtmlTemplate = `<a href="http://127.0.0.1:8000/challenge/invite/` + challengeList[i].invitation_key + `">`
                                + challengeList[i].title + `</a>`

        const newChallengeDiv = new DOMParser().parseFromString(innerHtmlTemplate, "text/html").body.firstElementChild
        
        if(challengeList[i].status === 0){
            status0.appendChild(newChallengeDiv);
        }
        else if(challengeList[i].status === 1){
            status1.appendChild(newChallengeDiv);
        }
        else if(challengeList[i].status === 2){
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

// 설정 삭제
// setting.addEventListener("click", onClickSetting)




// ToS
const printToS = () => {
    contentBox.innerHTML = ''

    const ToSTemplate = `
        <div class="ToS__content">
            <span class="ToS__title">
                    개인정보 수집 및 이용에 대한 안내
                </span>
                <br>
                <br>
                가. 개인정보의 수집 및 이용 목적<br>
                ① DoWith은 다음의 목적을 위하여 개인정보를 처리합니다. 처리하고 있는 개인정보는 다음의 목적 이외의 용도로는 이용되지 않으며, 이용 목적이 변경되는 경우에는 개인정보 보호법 제18조에 따라 별도의 동의를 받는 등 필요한 조치를 이행할 예정입니다. <br>
                <br>
                &nbsp; 1. DoWith 서비스 제공을 위한 회원관리<br>
                &nbsp; 2. 개인정보 다운로드, 오픈API 신청 및 활용 등 포털 서비스 제공과 서비스 부정이용 방지를 목적으로 개인정보를
                처리합니다. <br>
                <br>
                나. 수집하는 개인정보의 항목<br>
                ① DoWith 회원정보(필수): 이름, 이메일(아이디), 비밀번호<br>
                <br>
                다. 개인정보의 보유 및 이용기간<br>
                ① DoWith은 법령에 따른 개인정보 보유ㆍ이용기간 또는 정보주체로부터 개인정보를 수집 시에 동의 받은 개인정보 보유ㆍ이용기간 내에서 개인정보를 처리ㆍ보유합니다. <br>
                <br>
                &nbsp; 1. DoWith 회원정보<br>
                &nbsp; &nbsp; - 수집근거: 정보주체의 동의<br>
                &nbsp; &nbsp; - 보존기간: 회원 탈퇴 요청 전까지(1년 경과 시 재동의) <br>
                &nbsp; &nbsp; - 보존근거: 정보주체의 동의<br>
                <br>
                라. 동의 거부 권리 및 동의 거부에 따른 불이익<br>
                위 개인정보의 수집 및 이용에 대한 동의를 거부할 수 있으나, 동의를 거부할 경우 회원 가입이 제한됩니다. <br>
                <br>
                위의 개인정보 수집 및 이용에 대한 안내에 동의합니다.
        </div>
    `
    const newToSDiv = new DOMParser().parseFromString(ToSTemplate, "text/html").body.firstElementChild
    contentBox.appendChild(newToSDiv)
}

ToS.addEventListener("click", printToS)