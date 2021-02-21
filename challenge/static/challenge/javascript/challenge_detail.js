// 클립보드에 복사하기
function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
  }
  
  
  // 챌린지 성공 버튼
  const onClickResult = async (id) => {
      const url = "/challenge/result_ajax/";
  
      const {data} = await axios.post(url, {
          id
      })

      console.log(data)
      result_modify(data.id, data.result);
  }
  
  const result_modify = (id, result) => {
          const resultBtn = document.querySelector(`.result`);
  
          if (result === false) {
              resultBtn.className = `result ch-result`;
              resultBtn.innerText = "챌린지 실패"
          }
          else {
              resultBtn.classList.add('result-clicked');
              resultBtn.innerText = "챌린지 성공"
          }
      }
  

const urlGet = async (id) => {
    const url = "/challenge/send/invitation/";
    //이미 challengeUrl이 존재한다면 axios 실행을 안해도 됨. 그 조건을 따지기 위한 코드
    const urlStatus = document.querySelector('#urlMaker') === null;
    
    if (urlStatus) {

        const {data} = await axios.post(url, {
            id
        })
        urlGetModify(data.id, data.invitation_key)

    } else {

        const target = document.querySelector('#urlMaker')
        target.remove()

    }
}

const urlGetModify = (id, invitation_key) => {

    const target = document.querySelector('#url-link')

    const urlMaker = document.createElement('div')
    const currentUrl = document.createElement('div')
    const copyBtn = document.createElement('button')

    urlMaker.id = "urlMaker"
    currentUrl.id = "challengeUrl"
    currentUrl.innerText = invitation_key
    copyBtn.id = "copyBtn"

    copyBtn.innerText = '복사하기'
    copyBtn.setAttribute('onclick', "copyToClipboard('#challengeUrl')")

    urlMaker.appendChild(currentUrl)
    urlMaker.appendChild(copyBtn)
    target.appendChild(urlMaker)     
}
  
  
  // 매일 12시 업데이트
  //function getTime() {
  //    const now = new Date();
  //    const hours = now.getHours();
  //    const minutes = now.getMinutes();
  //    const seconds = now.getSeconds();
  //    if (hours == 00){
  //         resultBtn.classList.remove('result-clicked');
  //    }
      //if (seconds == 00){
      //    resultBtn.classList.remove('result-clicked')
      //}
  //}
  
  //function init(){
  //    getTime();
  //    setInterval(getTime, 1000);
  //    return;
  //}
  
  //init()
  