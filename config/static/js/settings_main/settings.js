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
        </div>
    `
    const newUserInfoDiv = new DOMParser().parseFromString(userInfoTemplate, "text/html").body.firstElementChild
    contentBox.appendChild(newUserInfoDiv)
}

userInfo.addEventListener("click", onClickUserInfo)




// userChallenge
const onClickUserChallenge = async () => {
    const url = "/login/settings/user_challenge/";

    const {data} = await axios.get(url)
    printUserChallenge();
}

const printUserChallenge = () => {
    contentBox.innerHTML = ''

    const userChallengeTemplate = `
        <div class="userChallenge__content">
            <div>
                user의 challenge 접근하는 문법(쿼리셋?) 공부하기
            </div>
        </div>
    `
    const newUserChallengeDiv = new DOMParser().parseFromString(userChallengeTemplate, "text/html").body.firstElementChild
    contentBox.appendChild(newUserChallengeDiv)
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
            <form action="" method="POST">
                {% csrf_token %}
                <p>디스플레이</p>
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