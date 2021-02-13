// 랜덤링크 생성


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
      const url = "/result_ajax/";
  
      const {data} = await axios.post(url, {
          id
      })
      console.log(data);
  
      modify(data.id, data.result);
  }
  
  const modify = (id, result => {
      const resultBtn = document.querySelector(`.result-${id} button`);
  
      if (result === false) {
          resultBtn.className = "result";
      }
      else {
          resultBtn.className = 'result-clicked';
      }
  }
  
  
  // 매일 12시 업데이트
  function getTime() {
      const now = new Date();
      const hours = now.getHours();
      const minutes = now.getMinutes();
      const seconds = now.getSeconds();
      if (hours == 00){
           resultBtn.classList.remove('result-clicked');
      }
      //if (seconds == 00){
      //    resultBtn.classList.remove('result-clicked')
      //}
  }
  
  function init(){
      getTime();
      setInterval(getTime, 1000);
      return;
  }
  
  init()