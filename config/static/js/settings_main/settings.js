const userInfo = document.querySelector(".userInfo")
const userChallenge = document.querySelector(".userChallenge")
const setting = document.querySelector(".setting")
const ToS = document.querySelector(".ToS")
const contentBox = document.querySelector(".content")

 // userInfo
 const onClickUserInfo = async () => {
    const url = "/login/settings/user_info/";
    
    const {data} = await axios.get(url)
    printUserInfo(data.name, data.nickname, data.email);
}


const printUserInfo = (name, nickname, email) => {
    contentBox.innerHTML = ''

    const userInfoTemplate = `
        <div class="userInfo__content">
            <div>
                Username : ` + name +
            `</div>
            <div>
                Nickname : ` + nickname +
            `</div>
            <div>
                Email : ` + email +
            `</div>
            <input class="userInfo__modification" type="submit" value="수정하기"/>
        </div>
    `
    const newUserInfoDiv = new DOMParser().parseFromString(userInfoTemplate, "text/html").body.firstElementChild
    contentBox.appendChild(newUserInfoDiv)


    // userInfo__modification
    const userInfoModify = document.querySelector(".userInfo__modification");
    userInfoModify.addEventListener("click", () => {
        document.location.href = url;
    })
}

userInfo.addEventListener("click", onClickUserInfo)




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

    const userChallengeTemplate = `
        <div class="userChallenge__content">
            <div class="status_0">
                대기 중
                <br>
            </div>
            <br>
            <div class="status_1">
                진행 중
                <br>
            </div>
            <br>
            <div class="status_2">
                완료
                <br>
            </div>
        </div>
    `
    const newUserChallengeDiv = new DOMParser().parseFromString(userChallengeTemplate, "text/html").body.firstElementChild
    contentBox.appendChild(newUserChallengeDiv)


    const status0 = document.querySelector(".status_0");
    const status1 = document.querySelector(".status_1");
    const status2 = document.querySelector(".status_2");
    for(let i = 0; i < challengeListParsed.length; i++){
        const innerHtmlTemplate = `<div>챌린지 명 : ` + challengeListParsed[i].fields.title +
                                    `<br>챌린지 창시일 : ` + challengeListParsed[i].fields.created_date +
                                    `<br>챌린지 시작일 : ` + challengeListParsed[i].fields.start_date +
                                    `<br>나의 챌린지 신청일 : ` + enrollmentListParsed[i].fields.created_at +
                                    `<br><br>
                                </div>`;
        
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